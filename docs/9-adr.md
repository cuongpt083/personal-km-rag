# ADR - Architecture Decision Records

Tài liệu này bám theo [BRD](./1-brd.md) và [Detailed Design](./2-detailed-design.md). Dùng để ghi lại các quyết định kiến trúc quan trọng và lý do chọn.

## 1. Mục đích
- Ghi lại quyết định đã chốt.
- Giải thích lý do chọn phương án đó.
- Giúp team hiểu lịch sử kiến trúc sau này.

## 2. Quyết định đã chốt

### ADR-001: Chọn mô hình RAG
- **Decision**: Dùng RAG với retrieval trước, generation sau.
- **Reason**: Giảm hallucination, phù hợp tài liệu chuyên môn, dễ kiểm soát bằng chứng.
- **Status**: Accepted

### ADR-002: Chọn Qdrant + PostgreSQL
- **Decision**: Dùng Qdrant cho vector search, PostgreSQL cho metadata và dữ liệu quan hệ.
- **Reason**: Tách rõ trách nhiệm, dễ filter theo quyền, dễ audit và versioning.
- **Status**: Accepted

### ADR-003: Dùng hybrid retrieval
- **Decision**: Kết hợp semantic search và keyword search.
- **Reason**: Tăng khả năng bắt đúng tài liệu trong domain chuyên sâu, nhất là với thuật ngữ đặc thù.
- **Status**: Accepted

### ADR-004: Áp quyền trước khi đưa context vào LLM
- **Decision**: Lọc theo `public / premium / admin` trước retrieval và trước generation.
- **Reason**: Tránh lộ tài liệu ngoài quyền truy cập.
- **Status**: Accepted

### ADR-005: Từ chối khi thiếu bằng chứng
- **Decision**: Nếu evidence yếu, hệ thống phải từ chối và gợi ý hướng bổ sung.
- **Reason**: Ưu tiên an toàn và giảm hallucination.
- **Status**: Accepted

## 3. Mẫu ADR mới

### ADR-XXX: <Tên quyết định>
- **Status**: Proposed | Accepted | Rejected | Superseded
- **Context**: Bối cảnh và vấn đề cần giải quyết
- **Decision**: Quyết định cuối cùng
- **Reason**: Lý do chọn
- **Consequences**: Hệ quả kỹ thuật và vận hành

## 4. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)
- Architecture: [docs/3-architecture.md](./3-architecture.md)
- Schema: [docs/4-schema.md](./4-schema.md)
- Evaluation Plan: [docs/5-evaluation-plan.md](./5-evaluation-plan.md)
- API Spec: [docs/6-api-spec.md](./6-api-spec.md)
- Implementation Plan: [docs/7-implementation-plan.md](./7-implementation-plan.md)

