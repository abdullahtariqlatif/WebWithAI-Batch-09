# PHASE 10 — Frontend ↔ Backend Integration

Goal: stop treating frontend & backend separately and build them as one application.

```text
React → API Client → HTTP → Express → Middleware → Auth → Controller → Service
      → Mongoose / Prisma → MongoDB / PostgreSQL → HTTP Response → React
```

## 10.1 Request Flow & API Contract

* [ ] Request & response lifecycle; where frontend logic ends & backend logic begins (client vs server responsibilities)
* [ ] Trace a request from React to the database and back, and know where validation, auth, authorization, business logic, DB logic & error handling each happen
* [ ] API contract: request, response, error, status-code, pagination, auth & validation-error formats
* [ ] Don't leak database-specific structures; API versioning basics

```json
{ "data": { "id": 1, "title": "Example Article" } }
{ "error": { "code": "VALIDATION_ERROR", "message": "Invalid request", "fields": { "title": "Title is required" } } }
```

## 10.2 API Client & Configuration

* [ ] Centralized API client (`fetch`/Axios): base URL, shared config, auth headers & common error handling, with no request logic duplicated in components
* [ ] Backend URL per environment through frontend env vars; no hard-coded URLs; public vs secret variables (→ 8.4)
* [ ] CORS for your frontend origin & credentials; debugging CORS errors in DevTools (setup → 6.7)

## 10.3 Forms → API

```text
React Form → Client Validation → HTTP → Express → Server Validation → Controller → Database → Response → React UI
```

* [ ] Registration & login forms submitting to Express
* [ ] Show server validation errors; handle success, failure, disabled-while-submitting & form reset
* [ ] Client validation never replaces server validation; keep the two responsibilities clear

## 10.4 Authentication Integration

* [ ] Registration, login, logout & current-user flows
* [ ] Credentialed (HTTP-only cookie) vs bearer-token requests & their security trade-offs
* [ ] Persist auth state; handle expired auth & `401` responses; redirect unauthenticated users; show the logged-in user
* [ ] Protected features: protected routes, `403` handling, role-based UI, admin-only pages & owner-only actions (hide/disable what users can't do)
* [ ] Frontend authorization never replaces backend authorization

## 10.5 CRUD & UI State

* [ ] Create, read (list & single item), update & delete end to end, with server validation & delete confirmation
* [ ] Request states: loading, success, error, empty, submitting, refetching & disabled
* [ ] Avoid stale UI after mutations: refetching vs optimistic updates; server state vs local UI state

## 10.6 Pagination, Search & Filtering

* [ ] Pagination: page & page-size params, total results, next/previous UI & loading on page change
* [ ] Search: query params, debounced input, loading state & empty results
* [ ] Filters & sorting combined with search & pagination, synced to URL params

## 10.7 File Uploads

```text
React File Input → FormData → Express → Multer → Storage Service → S3 / Cloudinary / Local
```

* [ ] File input, `FormData` & `multipart/form-data`
* [ ] Upload progress, file validation & size limits, image previews & upload errors
* [ ] Displaying & deleting uploaded files

## 10.8 Errors, Debugging & Testing Across the Stack

* [ ] Database error → service → controller → HTTP error → API client → React error state: handle HTTP, validation, auth, authorization, not-found & network errors with useful messages that don't expose backend internals
* [ ] DevTools Network: request/response headers & bodies, status codes, cookies & failed requests
* [ ] DevTools Console/Application: frontend errors, auth state, cookies, local & session storage
* [ ] Test React & the API independently, then integration: auth flow, CRUD workflows & errors across both

## Practice

* [ ] Todo app (React → Express → MongoDB): CRUD with loading, error & empty states
* [ ] Auth app: register, login, logout, current user, protected frontend & API routes, auth errors & basic authorization
* [ ] CRUD admin dashboard: forms, validation, search, filtering, sorting, pagination & auth
* [ ] File manager: upload, validate, list & delete files; handle errors
* [ ] Final integration project: React + Express + MongoDB with everything above, plus email, background jobs, API & React tests, API docs & production env config
* [ ] Rebuild the final project on PostgreSQL + Prisma, keeping the frontend unchanged (→ 7.11)
