# BRD - Hệ thống Q&A chatbot chuyên môn sâu

## 1. Mục tiêu
- Xây dựng chatbot Q&A cho các lĩnh vực chuyên môn sâu, ưu tiên `y học cổ truyền` và `dinh dưỡng chuyên sâu`.
- Hỗ trợ người dùng phổ thông bằng câu trả lời ngắn gọn, dễ hiểu, có giải thích, bước hành động và cảnh báo/rủi ro.
- Giảm tối đa hallucination, ưu tiên trả lời bám bằng chứng từ tài liệu đã nạp.

## 2. Phạm vi
- Nguồn dữ liệu chính: `PDF scan` và `PDF text`.
- Hệ thống hỗ trợ `song ngữ`.
- Kiến trúc lưu trữ và truy xuất dự kiến:
  - `Qdrant` cho vector retrieval
  - `PostgreSQL` cho metadata, quyền truy cập, phiên bản tài liệu, log và feedback
- Hệ thống có cơ chế từ chối trả lời khi không đủ bằng chứng.

## 3. Người dùng và phân quyền
- Nhóm người dùng:
  - `public`
  - `premium`
  - `admin`
- Ma trận truy cập tài liệu:
  - `public`: `Tier 1`, `Tier 2`
  - `premium`: `Tier 1`, `Tier 2`, `Tier 3`
  - `admin`: `Tier 1`, `Tier 2`, `Tier 3`, `Tier 4`

## 4. Độ tin cậy nguồn tài liệu
- `Tier 1`: guideline chính thống
- `Tier 2`: sách chuyên khảo
- `Tier 3`: bài nghiên cứu
- `Tier 4`: tài liệu nội bộ
- Truy xuất và trả lời phải ưu tiên nguồn có độ tin cậy cao hơn.

## 5. Yêu cầu chức năng
1. Nạp và xử lý tài liệu từ PDF scan và PDF text.
2. OCR cho tài liệu scan.
3. Chuẩn hóa tài liệu, tách đoạn và chia chunk theo cấu trúc.
4. Gắn metadata: domain, nguồn, phiên bản, độ tin cậy, ngôn ngữ, quyền truy cập.
5. Lưu và truy xuất vector bằng Qdrant.
6. Lưu metadata, tài liệu gốc, chunk text, log và feedback bằng PostgreSQL.
7. Hỗ trợ hybrid retrieval kết hợp semantic search và keyword search.
8. Hỗ trợ rerank trước khi đưa context vào LLM.
9. Sinh câu trả lời theo format cố định:
   - trả lời ngắn gọn
   - giải thích
   - bước hành động
   - cảnh báo/rủi ro
   - trích nguồn ngắn gọn nếu có
10. Từ chối trả lời khi thiếu bằng chứng và gợi ý câu hỏi hoặc nguồn bổ sung.

## 6. Yêu cầu phi chức năng
- Hiệu năng:
  - mục tiêu `p95 < 10 giây`
  - tối ưu số lượng chunk đưa vào LLM
  - ưu tiên cache cho câu hỏi lặp lại
- Chất lượng:
  - giảm hallucination
  - ưu tiên trả lời bám bằng chứng
  - có thể từ chối thay vì trả lời suy đoán
- Bảo mật và phân quyền:
  - lọc tài liệu theo nhóm người dùng trước khi đưa vào context
  - không để LLM thấy dữ liệu ngoài quyền truy cập
- Vận hành:
  - cập nhật tài liệu hàng ngày trong 1 tháng đầu
  - sau đó cập nhật hàng tháng
  - hỗ trợ versioning và incremental indexing

## 7. Tone và trải nghiệm trả lời
- Giọng điệu: tư vấn gần gũi nhưng vẫn thận trọng.
- Văn phong cho người dùng phổ thông, hạn chế thuật ngữ khó nếu không giải thích.
- Citation không bắt buộc nhưng nên hiển thị ngắn gọn khi có thể.

## 8. Tiêu chí hoàn thành
- Người dùng có thể hỏi và nhận câu trả lời an toàn, có kiểm soát theo quyền truy cập.
- Hệ thống trả lời đúng format đã chốt.
- Khi thiếu bằng chứng, hệ thống từ chối và gợi ý hướng bổ sung.
- Đáp ứng mục tiêu hiệu năng `p95 < 10 giây` trong môi trường triển khai thực tế.
