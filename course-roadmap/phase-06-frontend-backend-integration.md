# PHASE 6 — Frontend ↔ Backend Integration

Connect the React frontend to the Node.js / Express backend and build complete full-stack features.

The goal of this phase is to move from learning frontend and backend technologies separately to understanding how they work together as one application.

---

# Full-Stack Request Flow

Understand the complete flow:

```text
React
   ↓
HTTP Request
   ↓
Express
   ↓
Middleware
   ↓
Controller
   ↓
Service
   ↓
Mongoose / Prisma
   ↓
MongoDB / PostgreSQL
   ↓
HTTP Response
   ↓
React
```

* [ ] Understand the complete frontend → backend → database request lifecycle
* [ ] Understand the response lifecycle
* [ ] Understand where frontend logic ends and backend logic begins
* [ ] Understand client-side vs server-side responsibilities
* [ ] Understand API contracts between frontend and backend

---

# React API Integration

## HTTP Requests

* [ ] Connect React to an Express API
* [ ] Make GET requests from React
* [ ] Make POST requests from React
* [ ] Make PATCH requests from React
* [ ] Make DELETE requests from React
* [ ] Send request bodies
* [ ] Send request headers
* [ ] Handle JSON responses
* [ ] Handle HTTP status codes
* [ ] Handle API errors
* [ ] Handle network errors

## API Client

* [ ] Create a centralized API client
* [ ] Understand `fetch`
* [ ] Understand Axios
* [ ] Configure a base API URL
* [ ] Centralize request configuration
* [ ] Centralize authentication headers
* [ ] Handle common API errors
* [ ] Avoid duplicating API request logic across components

Example:

```text id="4z1q8c"
React Component
      ↓
API Client
      ↓
Express API
```

---

# Environment Configuration

Connect the frontend and backend using environment-specific configuration.

* [ ] Configure backend API URL
* [ ] Frontend environment variables
* [ ] Development API configuration
* [ ] Production API configuration
* [ ] `.env` files
* [ ] `.env.example`
* [ ] Avoid hard-coding API URLs
* [ ] Understand public vs secret environment variables

---

# CORS & Cross-Origin Requests

* [ ] Understand same-origin policy
* [ ] Understand CORS
* [ ] Configure CORS in Express
* [ ] Configure allowed frontend origins
* [ ] Configure allowed methods
* [ ] Configure allowed headers
* [ ] Understand credentials
* [ ] Understand preflight requests
* [ ] Debug CORS errors using DevTools

---

# Forms → API

Connect React forms to backend endpoints.

* [ ] Build registration form
* [ ] Build login form
* [ ] Submit form data to Express
* [ ] Handle server-side validation errors
* [ ] Display validation errors in React
* [ ] Handle successful submissions
* [ ] Disable forms while submitting
* [ ] Handle failed requests
* [ ] Reset forms after successful submission

Request flow:

```text id="g7w2ye"
React Form
    ↓
Client Validation
    ↓
HTTP Request
    ↓
Express
    ↓
Server Validation
    ↓
Controller
    ↓
Database
    ↓
Response
    ↓
React UI
```

* [ ] Understand why client-side validation does not replace server-side validation
* [ ] Handle different validation errors from the API
* [ ] Keep frontend and backend validation responsibilities clear

---

# Authentication Integration

Connect the React authentication UI to the Express authentication system.

## Authentication Flow

* [ ] Registration flow
* [ ] Login flow
* [ ] Logout flow
* [ ] Current-user request
* [ ] Authentication state
* [ ] Persist authentication state appropriately
* [ ] Handle expired authentication
* [ ] Handle unauthorized API responses

## Cookies / Tokens

* [ ] Understand JWT authentication from the frontend perspective
* [ ] Understand HTTP-only cookies
* [ ] Understand credentialed requests
* [ ] Understand bearer-token requests
* [ ] Understand the security trade-offs of different approaches
* [ ] Configure frontend requests for authentication
* [ ] Protect frontend routes
* [ ] Redirect unauthenticated users
* [ ] Display authenticated user information

> JWT internals, token architecture, refresh-token design and authentication security belong primarily in the later Architecture & Rails Translation phase.

---

# CRUD Integration

Build complete CRUD features from React through Express to the database.

## Create

* [ ] React form
* [ ] POST request
* [ ] Server validation
* [ ] Database creation
* [ ] Success response
* [ ] Update React state

## Read

* [ ] Fetch collection
* [ ] Fetch individual resource
* [ ] Display loading state
* [ ] Display empty state
* [ ] Display error state

## Update

* [ ] Edit form
* [ ] PATCH request
* [ ] Server validation
* [ ] Update database
* [ ] Update React UI

## Delete

* [ ] Delete action
* [ ] Confirmation
* [ ] DELETE request
* [ ] Handle successful deletion
* [ ] Handle failed deletion
* [ ] Update React UI

---

# UI State & API State

Learn how frontend state changes when dealing with asynchronous APIs.

## Request States

* [ ] Loading state
* [ ] Success state
* [ ] Error state
* [ ] Empty state
* [ ] Submitting state
* [ ] Refetching state
* [ ] Disabled states

## State Flow

```text id="8qzq0a"
User Action
    ↓
API Request
    ↓
Loading
    ↓
Success ──→ Update UI
    │
    └──→ Error ──→ Display Error
```

* [ ] Avoid stale UI after mutations
* [ ] Understand when to refetch data
* [ ] Understand optimistic UI basics
* [ ] Understand server state vs local UI state

---

# Pagination, Search & Filtering

Connect backend query features to React UI.

## Pagination

* [ ] API pagination
* [ ] Page parameters
* [ ] Page size
* [ ] Total results
* [ ] Next/previous navigation
* [ ] Pagination UI
* [ ] Loading during page changes

## Search

* [ ] Search input
* [ ] Query parameters
* [ ] Search API
* [ ] Debouncing search input
* [ ] Search loading state
* [ ] Empty search results

## Filtering & Sorting

* [ ] Filter controls
* [ ] Query parameters
* [ ] Multiple filters
* [ ] Sorting
* [ ] Combining search, filtering and pagination
* [ ] Synchronizing filters with URL parameters

---

# File Upload Integration

Connect React file inputs to the Express backend.

* [ ] File input
* [ ] `FormData`
* [ ] `multipart/form-data`
* [ ] Upload progress basics
* [ ] File validation
* [ ] File size limits
* [ ] Image preview
* [ ] Upload error handling
* [ ] Display uploaded files
* [ ] Delete uploaded files

Understand the complete flow:

```text id="av5j6w"
React File Input
      ↓
FormData
      ↓
Express
      ↓
Multer
      ↓
Storage Service
      ↓
S3 / Cloudinary / Local Storage
```

> Storage architecture and signed URLs are covered in greater depth in the Architecture & Rails Translation phase.

---

# Protected Features

Build frontend features that depend on authentication and authorization.

* [ ] Protected React routes
* [ ] Authenticated API requests
* [ ] Unauthorized responses
* [ ] Forbidden responses
* [ ] Role-based UI
* [ ] Admin-only pages
* [ ] Owner-only actions
* [ ] Hide or disable unauthorized actions
* [ ] Understand that frontend authorization does not replace backend authorization

Example:

```text id="5d6z2w"
React
  ↓
Protected Route
  ↓
API Request
  ↓
Authentication
  ↓
Authorization
  ↓
Controller
  ↓
Database
```

---

# Error Handling Across the Stack

Understand errors at each layer.

```text id="lq7q5r"
Database Error
      ↓
Service
      ↓
Controller
      ↓
HTTP Error Response
      ↓
API Client
      ↓
React Error State
      ↓
User
```

* [ ] Handle HTTP errors
* [ ] Handle validation errors
* [ ] Handle authentication errors
* [ ] Handle authorization errors
* [ ] Handle not-found responses
* [ ] Handle network errors
* [ ] Display useful user-facing errors
* [ ] Avoid exposing backend internals to users
* [ ] Debug frontend/backend errors using DevTools

---

# Browser DevTools for Full-Stack Debugging

Use browser DevTools to debug the complete application.

## Network

* [ ] Inspect API requests
* [ ] Inspect request headers
* [ ] Inspect request body
* [ ] Inspect response headers
* [ ] Inspect response body
* [ ] Inspect status codes
* [ ] Inspect cookies
* [ ] Identify failed requests
* [ ] Debug CORS errors

## Console & Application

* [ ] Debug frontend errors
* [ ] Inspect authentication state
* [ ] Inspect cookies
* [ ] Inspect local storage
* [ ] Inspect session storage
* [ ] Trace frontend API errors

---

# API Contract

Keep the frontend and backend aligned around a predictable API contract.

* [ ] Define request formats
* [ ] Define response formats
* [ ] Define error formats
* [ ] Define status-code conventions
* [ ] Define pagination responses
* [ ] Define authentication responses
* [ ] Define validation error responses
* [ ] Avoid leaking database-specific structures unnecessarily
* [ ] Understand API versioning basics

Example:

```json
{
  "data": {
    "id": 1,
    "title": "Example Article"
  }
}
```

Error example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request",
    "fields": {
      "title": "Title is required"
    }
  }
}
```

---

# Full-Stack Practice

## Demo 1 — Todo Application

Build:

```text id="4j0k4q"
React
  ↓
Express
  ↓
MongoDB
```

* [ ] Create todos
* [ ] List todos
* [ ] Update todos
* [ ] Delete todos
* [ ] Loading states
* [ ] Error states
* [ ] Empty states

## Demo 2 — Authentication Application

* [ ] Registration
* [ ] Login
* [ ] Logout
* [ ] Current user
* [ ] Protected frontend routes
* [ ] Protected API routes
* [ ] Authentication errors
* [ ] Authorization basics

## Demo 3 — CRUD Dashboard

Build a small admin-style application.

* [ ] CRUD
* [ ] Forms
* [ ] Validation
* [ ] Search
* [ ] Filtering
* [ ] Sorting
* [ ] Pagination
* [ ] Loading states
* [ ] Error states
* [ ] Authentication
* [ ] Authorization

## Demo 4 — File Management

* [ ] Upload files
* [ ] Validate files
* [ ] Display uploaded files
* [ ] Delete files
* [ ] Handle upload errors

## Final Integration Project

Build a complete React + Express application.

* [ ] React frontend
* [ ] Express backend
* [ ] MongoDB / PostgreSQL database
* [ ] Authentication
* [ ] Authorization
* [ ] CRUD
* [ ] Forms
* [ ] Validation
* [ ] Search
* [ ] Filtering
* [ ] Pagination
* [ ] File uploads
* [ ] Loading states
* [ ] Error handling
* [ ] Protected routes
* [ ] API documentation
* [ ] Production environment configuration

---

# MERN → PERN Integration

Repeat the application using PostgreSQL.

```text id="7c2d6f"
React
   ↓
HTTP
   ↓
Express
   ↓
Controller
   ↓
Service
   ↓
Prisma
   ↓
PostgreSQL
```

* [ ] Rebuild the API using PostgreSQL
* [ ] Replace Mongoose with Prisma
* [ ] Adapt database queries
* [ ] Adapt relationships
* [ ] Adapt pagination
* [ ] Adapt filtering
* [ ] Adapt validation
* [ ] Preserve the frontend where possible
* [ ] Compare the MERN and PERN implementations

---

# Completion Goal

By the end of this phase, you should be able to independently build:

```text id="zj9g7v"
React Frontend
      ↓
API Client
      ↓
Express API
      ↓
Authentication / Authorization
      ↓
Controllers
      ↓
Services
      ↓
Mongoose / Prisma
      ↓
MongoDB / PostgreSQL
```
