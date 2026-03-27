# Schema - PostgreSQL và Qdrant

Tài liệu này là phần mở rộng của [BRD](./1-brd.md) và [Detailed Design](./2-detailed-design.md), mô tả schema tối thiểu cho MVP.

## 1. Mục tiêu
- Lưu tài liệu, chunk, metadata, quyền truy cập, version và feedback.
- Tách rõ dữ liệu quan hệ ở PostgreSQL và dữ liệu vector ở Qdrant.

## 2. PostgreSQL

### 2.1 `documents`
- `id`
- `title`
- `source_type` (`pdf_scan`, `pdf_text`)
- `domain`
- `language`
- `trust_tier`
- `access_group`
- `version`
- `status`
- `created_at`
- `updated_at`

### 2.2 `document_versions`
- `id`
- `document_id`
- `version`
- `file_path`
- `hash`
- `effective_from`
- `effective_to`
- `created_at`

### 2.3 `chunks`
- `id`
- `document_id`
- `chunk_index`
- `chunk_text`
- `chunk_type`
- `section_path`
- `language`
- `trust_tier`
- `access_group`
- `created_at`

### 2.4 `queries`
- `id`
- `user_id`
- `user_group`
- `question`
- `language`
- `created_at`

### 2.5 `answers`
- `id`
- `query_id`
- `answer_text`
- `decision` (`answer`, `reject`)
- `latency_ms`
- `created_at`

### 2.6 `feedback`
- `id`
- `query_id`
- `rating`
- `comment`
- `created_at`

### 2.7 `audit_logs`
- `id`
- `actor`
- `action`
- `target_type`
- `target_id`
- `payload`
- `created_at`

## 3. Index khuyến nghị
- `documents(domain, trust_tier, access_group, status)`
- `chunks(document_id, trust_tier, access_group)`
- `queries(user_group, created_at)`
- full-text index trên `chunks.chunk_text`

## 4. Qdrant collection

### 4.1 Collection: `document_chunks`
Payload đề xuất:
- `chunk_id`
- `document_id`
- `version`
- `domain`
- `language`
- `trust_tier`
- `access_group`
- `section_path`
- `chunk_type`

Vector:
- embedding của `chunk_text`

## 5. Quy ước dữ liệu
- Một document có nhiều version.
- Một version có nhiều chunk.
- Chunk text là nguồn chính cho retrieval và citation.
- Payload trong Qdrant phải đủ để filter quyền truy cập và độ tin cậy.

## 6. Luồng ghi dữ liệu
1. Ghi document và version vào PostgreSQL.
2. Ghi chunk text và metadata vào PostgreSQL.
3. Tạo embedding cho từng chunk.
4. Upsert vector và payload vào Qdrant.

## 7. Liên kết tài liệu
- BRD: [docs/1-brd.md](./1-brd.md)
- Detailed Design: [docs/2-detailed-design.md](./2-detailed-design.md)
- Architecture: [docs/3-architecture.md](./3-architecture.md)

