# Detailed Design - Hệ thống Q&A chatbot chuyên môn sâu

## 1. Mục đích
Thiết kế kiến trúc RAG cho chatbot chuyên môn sâu, ưu tiên `y học cổ truyền` và `dinh dưỡng chuyên sâu`, chạy trên `Qdrant + PostgreSQL`, hỗ trợ `song ngữ`, có phân quyền theo nhóm người dùng và cơ chế từ chối khi thiếu bằng chứng.

## 2. Tóm tắt kiến trúc

```text
Tài liệu nguồn -> OCR/chuẩn hóa -> Chunking -> Embedding -> Qdrant
                         \-> PostgreSQL lưu raw docs, metadata, quyền, version, log

User query -> kiểm tra quyền -> retrieval hybrid -> rerank -> gom context -> LLM -> trả lời + citation ngắn
```

Kiến trúc tách làm 2 luồng:
- `Ingestion pipeline`: nạp và lập chỉ mục tài liệu.
- `Online query pipeline`: trả lời câu hỏi theo thời gian thực.

## 3. Thành phần chính

### 3.1 PostgreSQL
Lưu dữ liệu chuẩn và dễ truy vết:
- tài liệu gốc
- chunk text
- metadata: domain, ngôn ngữ, version, độ tin cậy, nhóm truy cập
- log truy vấn và phản hồi
- feedback người dùng

### 3.2 Qdrant
Lưu vector embedding của chunk để tìm đoạn văn bản liên quan nhanh.
- hỗ trợ lọc theo metadata
- phù hợp truy xuất semantic search

### 3.3 OCR service
Dùng cho `PDF scan`.
- trích chữ từ ảnh scan
- sau đó đưa qua bước làm sạch và chunking

### 3.4 Embedding service
Chuyển text thành vector số để so sánh ngữ nghĩa.
- nên dùng embedding đa ngôn ngữ vì hệ thống song ngữ

### 3.5 Reranker
Nhận danh sách chunk đã truy xuất và xếp lại theo độ liên quan.
- giảm nhiễu
- tăng độ chính xác
- giảm số token đưa vào LLM

### 3.6 LLM
Sinh câu trả lời cuối cùng dựa trên context đã được lọc.
- chỉ trả lời theo bằng chứng
- nếu thiếu bằng chứng thì từ chối và gợi ý hướng bổ sung

## 4. Luồng nạp tài liệu
1. Nhận tài liệu từ `PDF scan` hoặc `PDF text`.
2. OCR nếu là scan.
3. Làm sạch nội dung, bỏ header/footer, chuẩn hóa đoạn văn.
4. Chia chunk theo cấu trúc tài liệu.
5. Gán metadata và `trust tier`.
6. Tạo embedding.
7. Ghi metadata/chunk vào PostgreSQL.
8. Ghi vector vào Qdrant.

## 5. Luồng hỏi đáp
1. User gửi câu hỏi.
2. Hệ thống xác định nhóm người dùng: `public`, `premium`, `admin`.
3. Lọc tài liệu theo quyền truy cập.
4. Tìm kiếm hybrid:
   - semantic search trên Qdrant
   - keyword search trên PostgreSQL
5. Rerank top kết quả.
6. Chọn context tốt nhất theo ngưỡng tin cậy.
7. Nếu bằng chứng chưa đủ, từ chối và gợi ý câu hỏi hoặc nguồn bổ sung.
8. Nếu đủ bằng chứng, đưa context vào LLM.
9. Trả về:
   - trả lời ngắn gọn
   - giải thích
   - bước hành động
   - cảnh báo/rủi ro
   - trích nguồn ngắn gọn nếu có

## 6. Chiến lược truy xuất
- Ưu tiên nguồn có `trust tier` cao hơn.
- Hybrid retrieval để cân bằng:
  - `vector search` cho ý nghĩa
  - `keyword search` cho thuật ngữ chính xác
- Chỉ đưa vào LLM các chunk đã qua lọc quyền và rerank.
- Có ngưỡng từ chối khi không đủ bằng chứng.

## 7. Phân quyền và độ tin cậy
- `public` truy cập `Tier 1`, `Tier 2`
- `premium` truy cập `Tier 1`, `Tier 2`, `Tier 3`
- `admin` truy cập tất cả, gồm `Tier 4`
- Quyền được áp dụng trước khi retrieval và trước khi tạo context cho LLM.

## 8. Yêu cầu hiệu năng
- Mục tiêu `p95 < 10 giây`.
- Tối ưu bằng cách:
  - giới hạn số chunk đưa vào LLM
  - cache câu hỏi lặp lại
  - dùng reranker nhẹ, không quá tốn thời gian
  - cập nhật index theo kiểu incremental

## 9. Yêu cầu chất lượng
- Giảm hallucination là ưu tiên số 1.
- Khi thiếu bằng chứng, hệ thống phải từ chối thay vì đoán.
- Câu trả lời dành cho người dùng phổ thông, nên ngắn gọn và dễ hiểu.
- Citation không bắt buộc nhưng nên có ở dạng ngắn.

## 10. Thuật ngữ nhanh

| Thuật ngữ | Giải thích ngắn |
|---|---|
| AI | Trí tuệ nhân tạo, hệ thống thực hiện các nhiệm vụ cần “thông minh” như hiểu câu hỏi, sinh câu trả lời |
| ML | Machine Learning, một nhánh của AI cho phép hệ thống học từ dữ liệu thay vì viết luật thủ công |
| LLM | Large Language Model, mô hình ngôn ngữ lớn dùng để đọc hiểu và sinh văn bản |
| Embedding | Cách biến văn bản thành vector số để máy tính so sánh độ giống nhau |
| Vector DB | Cơ sở dữ liệu tối ưu để tìm kiếm theo vector, ví dụ Qdrant |
| RAG | Retrieval-Augmented Generation, kiểu kiến trúc “tìm tài liệu liên quan trước, rồi mới để LLM trả lời” |
| Chunk | Một đoạn nhỏ của tài liệu sau khi chia tách để truy xuất hiệu quả hơn |
| Rerank | Bước xếp lại kết quả tìm kiếm để chọn đoạn liên quan nhất |

## 11. Kết quả mong đợi
- Hệ thống trả lời an toàn, có kiểm soát theo quyền truy cập.
- Tài liệu được cập nhật theo lịch và có versioning.
- Kiến trúc đủ rõ để triển khai tiếp sang schema DB, API, và implementation.

## 12. Từ vựng chuẩn

| Thuật ngữ | Cách dùng trong bộ tài liệu |
|---|---|
| `RAG` | Kiến trúc truy xuất tài liệu trước rồi mới sinh câu trả lời |
| `retrieval` | Bước truy xuất tài liệu liên quan |
| `generation` | Bước sinh câu trả lời bằng LLM |
| `chunk` | Đoạn tài liệu nhỏ dùng để truy xuất |
| `embedding` | Vector biểu diễn nội dung văn bản |
| `rerank` | Xếp lại kết quả truy xuất để chọn chunk tốt hơn |
| `citation` | Trích nguồn ngắn từ tài liệu |
| `trust tier` | Mức độ tin cậy của nguồn tài liệu |
| `access group` | Nhóm người dùng được phép truy cập |
| `bám bằng chứng` | Cách diễn đạt chuẩn cho câu trả lời grounded |
