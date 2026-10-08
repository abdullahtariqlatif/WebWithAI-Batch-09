# PHASE 9 — Backend Features: Email, Jobs, Files, Real-time & Testing

Each section starts from the Rails feature you already know. These mappings are conceptual equivalents, not exact technical replacements.

## 9.1 Email (Rails: ActionMailer)

* [ ] Nodemailer, SMTP & transactional email providers
* [ ] Email templates: HTML & plain-text emails
* [ ] Verification, password-reset & notification emails
* [ ] Architecture: email logic in an email service (not controllers), sent from background jobs, with failure handling, never blocking HTTP requests

## 9.2 Background Jobs (Rails: ActiveJob → Sidekiq → Redis)

```text
Node: Application → BullMQ → Redis → Worker
```

* [ ] Queues, Redis & BullMQ; jobs, workers, producers & consumers
* [ ] Retries, delayed jobs, scheduled/repeatable jobs & failed jobs
* [ ] Concurrency, job priorities & job monitoring (queue dashboard)
* [ ] Rails mapping: ActiveJob → job abstraction, Sidekiq → BullMQ + Redis, job classes → job modules, ActiveJob retries → queue retry config, scheduled jobs → repeatable jobs
* [ ] Redis caching basics & cache invalidation

## 9.3 File Uploads & Storage (Rails: ActiveStorage)

* [ ] `multipart/form-data` & Multer
* [ ] Local storage vs object storage: Amazon S3 & Cloudinary
* [ ] Image uploads; file type & size validation; secure file handling
* [ ] Architecture: a storage service separate from controllers, direct-to-storage uploads, signed upload/download URLs

## 9.4 Real-time (Rails: ActionCable)

* [ ] WebSockets & Socket.IO: connections, disconnects, reconnection, connection state & events
* [ ] Broadcasting, rooms & private rooms
* [ ] Socket authentication & authorization

## 9.5 Backend Testing (Rails: RSpec + FactoryBot)

| Rails | Node |
|---|---|
| RSpec | Jest / Vitest |
| Request specs | Supertest |
| FactoryBot | Test factories |
| Fixtures | Fixtures / seed test data |
| Mocks | Jest / Vitest mocks |
| Model / service specs | Data-layer / service tests |

* [ ] Jest vs Vitest; Supertest for API tests
* [ ] Unit, integration & API tests
* [ ] Mocking, test doubles, fixtures, factories & a test database strategy
* [ ] Test models, services, controllers, API endpoints, validation & error responses
* [ ] Test authentication & authorization

## Practice: Rails Rebuild Exercises

Rebuild the Rails feature in Node, on top of the Phase 8 API.

* [ ] ActionMailer → Nodemailer, email template & email provider
* [ ] ActiveJob + Sidekiq → Redis, BullMQ & a worker: email job, scheduled job, retryable job, failed-job handling & queue dashboard
* [ ] ActiveStorage → Multer, S3/Cloudinary & file URLs
* [ ] ActionCable → chat app: rooms, broadcast, authentication, online/offline status, typing indicator, real-time notifications & a real-time dashboard
* [ ] RSpec + FactoryBot → test suite with Jest/Vitest, Supertest, factories & mocks
* [ ] User / Article / Comments → the whole thing in Express, MongoDB & Mongoose (React frontend in Phase 10)
