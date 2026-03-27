# Open Questions - Các câu hỏi cần chốt

Tài liệu này bám theo [BRD](./1-brd.md) và [Detailed Design](./2-detailed-design.md), dùng để khóa các điểm còn mơ hồ trước khi triển khai.

## 1. Mục đích
- Liệt kê các câu hỏi còn mở.
- Giảm rủi ro đổi hướng trong lúc code.

## 2. Câu hỏi còn mở

### 2.1 Dữ liệu và chất lượng
- Bộ tài liệu ban đầu sẽ có bao nhiêu nguồn?
- Có cần loại bỏ hoặc ưu tiên tài liệu theo độ mới không?
- Có quy tắc nào cho việc gắn `trust tier` khi tài liệu không rõ nguồn không?

### 2.2 Trả lời và an toàn
- Khi nào hệ thống phải từ chối thay vì trả lời?
- Có cần ngưỡng confidence cố định cho retrieval/rerank không?
- Citation ngắn sẽ hiển thị ở mức nào trong UI?

### 2.3 Vận hành
- Có cần re-index toàn bộ hay chỉ incremental update?
- Cần lưu trữ log bao lâu?
- Có cần cơ chế xóa dữ liệu theo yêu cầu không?

### 2.4 UI/UX
- Câu trả lời sẽ hiển thị một khối hay nhiều khối tách biệt?
- Có cần nút feedback nhanh như `hữu ích / không hữu ích` không?
- Có cần hiển thị nguồn gốc chunk cho admin không?

### 2.5 Kỹ thuật
- Chọn embedding model nào cho song ngữ?
- Reranker chạy bằng API hay model nội bộ?
- Có dùng cache ở tầng API hay tầng retrieval?

## 3. Cách dùng tài liệu này
- Khi câu hỏi được chốt, cập nhật lại BRD hoặc Detailed Design nếu cần.
- Nếu câu hỏi ảnh hưởng kiến trúc, ghi quyết định vào [ADR](./9-adr.md).

## 4. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)
- Architecture: [docs/3-architecture.md](./3-architecture.md)
- Schema: [docs/4-schema.md](./4-schema.md)
- API Spec: [docs/6-api-spec.md](./6-api-spec.md)

