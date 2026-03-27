# Evaluation Plan - Đánh giá chất lượng và hiệu năng

Tài liệu này bám theo [BRD](./1-brd.md) và [Detailed Design](./2-detailed-design.md), dùng để kiểm tra hệ thống trước khi mở rộng.

## 1. Mục tiêu đánh giá
- Kiểm tra chatbot trả lời đúng, an toàn, có kiểm soát quyền truy cập.
- Đo khả năng truy xuất, mức độ bám bằng chứng, và hiệu năng `p95 < 10 giây`.

## 2. Bộ test cần có

### 2.1 Retrieval set
- Câu hỏi có đáp án rõ trong tài liệu.
- Câu hỏi gần nghĩa nhưng khác ý để test precision.
- Câu hỏi chỉ có trong `Tier 3` hoặc `Tier 4` để test quyền.

### 2.2 Rejection set
- Câu hỏi thiếu dữ liệu.
- Câu hỏi ngoài phạm vi tài liệu.
- Câu hỏi mơ hồ hoặc yêu cầu suy đoán.

### 2.3 Multi-language set
- Câu hỏi tiếng Việt.
- Câu hỏi tiếng Anh.
- Câu hỏi pha trộn hai ngôn ngữ.

## 3. Metrics chính
- `Recall@k`: tài liệu đúng có được retrieve hay không.
- `Precision@k`: kết quả top-k có liên quan không.
- `Groundedness`: câu trả lời có bám bằng chứng từ tài liệu không.
- `Rejection accuracy`: khi nào nên từ chối thì hệ thống có từ chối đúng không.
- `p95 latency`: thời gian phản hồi 95th percentile.
- `Citation quality`: citation ngắn có khớp nguồn không.

## 4. Ngưỡng đề xuất
- `p95 latency < 10 giây`
- `Groundedness` phải cao để hạn chế hallucination
- `Rejection accuracy` phải đủ tốt để ưu tiên an toàn

## 5. Quy trình đánh giá
1. Nạp bộ test chuẩn.
2. Chạy retrieval và ghi log candidate chunks.
3. Chạy answer generation.
4. So sánh kết quả với expected outcome.
5. Phân tích lỗi:
   - retrieve sai
   - rerank sai
   - context quá dài
   - LLM trả lời vượt evidence

## 6. Tiêu chí đạt MVP
- Truy xuất đúng phần lớn câu hỏi chuẩn.
- Từ chối đúng khi thiếu bằng chứng.
- Phân quyền không bị vượt.
- Hiệu năng đạt mục tiêu `p95 < 10 giây`.

## 7. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)
- Architecture: [docs/3-architecture.md](./3-architecture.md)
- Schema: [docs/4-schema.md](./4-schema.md)
