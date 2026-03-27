# API Spec - Hợp đồng API cho chatbot RAG

Tài liệu này bám theo [BRD](./1-brd.md), [Detailed Design](./2-detailed-design.md), [Architecture](./3-architecture.md) và [Schema](./4-schema.md).

## 1. Mục tiêu
- Định nghĩa các API tối thiểu cho MVP.
- Tách rõ API cho hỏi đáp, ingestion, quản trị và kiểm tra hệ thống.

## 2. API chính

### 2.1 `POST /api/v1/chat`
Hỏi đáp chatbot.

Request:
```json
{
  "user_id": "u123",
  "user_group": "public",
  "language": "vi",
  "question": "..."
}
```

Response:
```json
{
  "decision": "answer",
  "answer_short": "...",
  "explanation": "...",
  "action_steps": ["..."],
  "warnings": ["..."],
  "citations": [
    {
      "document_id": "d1",
      "chunk_id": "c10",
      "title": "..."
    }
  ],
  "latency_ms": 1234
}
```

Nếu thiếu bằng chứng:
```json
{
  "decision": "reject",
  "message": "Không đủ bằng chứng để trả lời an toàn.",
  "suggestions": ["...", "..."]
}
```

### 2.2 `POST /api/v1/documents`
Nạp tài liệu mới.

### 2.3 `POST /api/v1/documents/{id}/versions`
Thêm version mới cho tài liệu đã có.

### 2.4 `GET /api/v1/documents`
Danh sách tài liệu theo quyền truy cập, domain, trust tier, status.

### 2.5 `GET /api/v1/queries/{id}`
Xem log một truy vấn và kết quả trả lời.

### 2.6 `POST /api/v1/feedback`
Gửi đánh giá từ người dùng.

### 2.7 `GET /api/v1/health`
Kiểm tra trạng thái service.

## 3. Quy tắc API
- Tất cả request phải kèm thông tin xác thực.
- Quyền truy cập tài liệu phải được áp dụng trước khi retrieval.
- Response cho user phổ thông phải ngắn gọn, dễ hiểu, thận trọng.
- Citation ngắn là tùy chọn nhưng nên trả về khi có nguồn phù hợp.

## 4. Gợi ý trạng thái lỗi
- `400`: request không hợp lệ
- `401`: chưa xác thực
- `403`: không có quyền truy cập
- `404`: tài nguyên không tồn tại
- `422`: câu hỏi không đủ điều kiện xử lý
- `500`: lỗi hệ thống

## 5. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)
- Architecture: [docs/3-architecture.md](./3-architecture.md)
- Schema: [docs/4-schema.md](./4-schema.md)
- Evaluation Plan: [docs/5-evaluation-plan.md](./5-evaluation-plan.md)

