# Architecture - Kiến trúc module và triển khai

Tài liệu này mở rộng từ [BRD](./1-brd.md) và [Detailed Design](./2-detailed-design.md), tập trung vào cách chia module, luồng gọi, và ranh giới trách nhiệm.

## 1. Mục tiêu
- Tách rõ phần nạp tài liệu, truy xuất, sinh câu trả lời và quản trị.
- Giữ kiến trúc đủ đơn giản để triển khai nhanh nhưng vẫn dễ mở rộng.

## 2. Các module chính

### 2.1 API Gateway / Backend API
- Nhận request từ UI.
- Xác thực người dùng.
- Áp quyền theo nhóm `public / premium / admin`.
- Gọi các service phía sau.

### 2.2 AuthZ Service
- Kiểm tra quyền truy cập tài liệu theo nhóm người dùng.
- Áp rule trước khi retrieval và trước khi đưa context vào LLM.

### 2.3 Ingestion Service
- Nhận tài liệu mới hoặc tài liệu cập nhật.
- Gọi OCR nếu là PDF scan.
- Làm sạch, chunking, gắn metadata, tạo embedding.
- Ghi dữ liệu vào PostgreSQL và Qdrant.

### 2.4 Retrieval Service
- Thực hiện hybrid retrieval:
  - semantic search trên Qdrant
  - keyword search trên PostgreSQL
- Lọc theo `trust tier` và quyền truy cập.

### 2.5 Rerank Service
- Xếp lại các chunk được retrieve.
- Chọn context tốt nhất trước khi gọi LLM.

### 2.6 Answer Service
- Tạo prompt theo format đã chốt trong BRD.
- Sinh câu trả lời:
  - ngắn gọn
  - giải thích
  - bước hành động
  - cảnh báo/rủi ro
  - citation ngắn nếu có
- Nếu thiếu bằng chứng thì từ chối và gợi ý hướng bổ sung.

### 2.7 Admin / Ops Module
- Quản lý tài liệu, version, trust tier, permission group.
- Xem log, feedback, và hiệu năng.

## 3. Luồng xử lý online
1. User gửi câu hỏi.
2. Backend xác thực và xác định nhóm người dùng.
3. AuthZ lọc phạm vi tài liệu.
4. Retrieval Service lấy candidate chunks.
5. Rerank Service chọn context tốt nhất.
6. Answer Service gọi LLM.
7. Backend trả kết quả về UI.

## 4. Luồng xử lý offline
1. Admin nạp tài liệu mới.
2. Ingestion Service xử lý PDF scan/PDF text.
3. PostgreSQL lưu raw data, metadata, version, log.
4. Qdrant lưu vector.
5. Index được cập nhật incremental.

## 5. Nguyên tắc thiết kế
- Tách ingestion và serving để dễ kiểm soát.
- Không để LLM thấy dữ liệu ngoài quyền.
- Ưu tiên retrieval chính xác hơn là nhồi nhiều context.
- Có cơ chế từ chối rõ ràng khi evidence yếu.

## 6. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)

