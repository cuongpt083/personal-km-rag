# Implementation Plan - Kế hoạch triển khai

Tài liệu này bám theo [BRD](./1-brd.md), [Detailed Design](./2-detailed-design.md), [Architecture](./3-architecture.md), [Schema](./4-schema.md), [API Spec](./6-api-spec.md) và [Evaluation Plan](./5-evaluation-plan.md).

## 1. Mục tiêu
- Triển khai MVP trong 1 tuần.
- Ưu tiên đúng kiến trúc, an toàn, và đo được chất lượng.

## 2. Kế hoạch theo giai đoạn

### Ngày 1 - Khởi tạo nền tảng
- Chốt cấu trúc repo.
- Dựng PostgreSQL và Qdrant.
- Tạo skeleton backend.
- Chuẩn hóa cấu hình môi trường.

### Ngày 2 - Ingestion pipeline
- Làm OCR cho PDF scan.
- Chuẩn hóa text.
- Chunking theo cấu trúc.
- Ghi document, version, chunk vào PostgreSQL.
- Upsert vector vào Qdrant.

### Ngày 3 - Retrieval pipeline
- Xây hybrid retrieval.
- Thêm filter theo `trust tier` và `access_group`.
- Gắn metadata phục vụ truy xuất và citation.

### Ngày 4 - Rerank và trả lời
- Thêm rerank.
- Xây prompt theo format chuẩn.
- Thêm logic từ chối khi thiếu bằng chứng.

### Ngày 5 - API và phân quyền
- Hoàn thiện các API chính.
- Áp quyền theo `public / premium / admin`.
- Ghi log query, answer, feedback.

### Ngày 6 - Evaluation
- Tạo bộ câu hỏi test.
- Đo `Recall@k`, `Groundedness`, `Rejection accuracy`, `p95 latency`.
- Sửa các điểm yếu lớn nhất.

### Ngày 7 - Hardening
- Tối ưu cache.
- Tối ưu context length.
- Kiểm tra lỗi quyền truy cập.
- Chuẩn bị bản chạy thử nội bộ.

## 3. Ưu tiên kỹ thuật
- Không để LLM trả lời ngoài bằng chứng.
- Không cho context vượt quyền truy cập.
- Ưu tiên retrieval chất lượng hơn mở rộng tính năng sớm.
- Tối ưu để đạt `p95 < 10 giây`.

## 4. Đầu ra mong đợi sau MVP
- Chatbot hỏi đáp được theo nhóm người dùng.
- Có cập nhật tài liệu.
- Có citation ngắn khi có thể.
- Có cơ chế từ chối an toàn.
- Có dashboard/log cơ bản để theo dõi lỗi và latency.

## 5. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)
- Architecture: [docs/3-architecture.md](./3-architecture.md)
- Schema: [docs/4-schema.md](./4-schema.md)
- Evaluation Plan: [docs/5-evaluation-plan.md](./5-evaluation-plan.md)
- API Spec: [docs/6-api-spec.md](./6-api-spec.md)

