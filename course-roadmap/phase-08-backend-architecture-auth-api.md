# PHASE 8 — Backend Architecture, Auth & API Design (Rails → Node)

Goal: build a Node/Express app with the organization and maintainability you expect from Rails. The point is **not** to make Express behave like Rails. Learn Node on its own terms, then settle on a consistent architecture that gives you a familiar separation of concerns.

## 8.1 Rails → Node Mental Model

| Rails | Node / Express |
|---|---|
| `app/models`, Model, ActiveRecord | `models/`, Mongoose / Prisma model |
| Migration | Mongoose migration scripts / Prisma migrations |
| Routes, Controller | Express Router, Express controller |
| Service Object | Service module / class |
| Rack middleware, `before_action` | Express middleware |
| Devise | JWT/session auth library or custom auth |
| Pundit, CanCanCan | Authorization middleware / policies / CASL |
| ActionMailer | Nodemailer / email provider |
| ActiveJob, Sidekiq | BullMQ + Redis |
| ActiveStorage | Multer + S3 / Cloudinary |
| ActionCable | Socket.IO / WebSockets |
| RSpec, FactoryBot | Jest / Vitest, test factories |
| `Rails.env`, credentials, `config/` | `NODE_ENV`, env vars / secret management, config modules |
| ActiveSupport | Utility libraries / custom helpers |
| `bin/rails` | npm scripts / CLI tools |

* [ ] These mappings are conceptual, not 1:1: ActiveRecord vs Mongoose vs Prisma, Rails conventions vs Express flexibility, Rack vs Express middleware
* [ ] What Rails gives you automatically that Express doesn't, and what you have to choose & configure yourself in Node

## 8.2 Project Structure

Layer-based (a good default for Rails developers):

```text
server/
├── config/        database.js, env.js, cors.js
├── models/        User.js, Article.js
├── controllers/   usersController.js, articlesController.js
├── routes/        usersRoutes.js, articlesRoutes.js
├── services/      authService.js, emailService.js
├── middleware/    auth.js, authorization.js, errorHandler.js
├── validators/    userValidator.js, articleValidator.js
├── utils/
├── jobs/
├── tests/
├── app.js
├── server.js
├── package.json
└── .env
```

Feature-based (for larger apps):

```text
server/
├── config/
├── modules/
│   ├── users/      user.model.js, user.controller.js, user.routes.js, user.service.js, user.validator.js
│   └── articles/   article.model.js, article.controller.js, ...
├── middleware/  jobs/  utils/  tests/
├── app.js
└── server.js
```

* [ ] Purpose of each layer: config, models/data access, routes, controllers, services, middleware, validators, utils, jobs, tests, app & server entry points
* [ ] Layer responsibilities: routes route, controllers handle HTTP, services hold business logic, the data layer persists, middleware handles cross-cutting concerns, validators validate
* [ ] Express is unopinionated, so this structure is a project convention, not a framework requirement; why consistent conventions matter
* [ ] Layer-based vs feature-based: when each fits & how apps evolve as they grow
* [ ] Avoid unnecessary/premature abstraction, oversized controllers & oversized service classes

## 8.3 Request Lifecycle & Startup

```text
HTTP Request → Route → Middleware → Validation → Authentication → Authorization
            → Controller → Service → Data Access → Database
            → Service → Controller → HTTP Response
```

* [ ] Trace the full request lifecycle & middleware execution order
* [ ] Keep controllers on HTTP concerns, business logic in services, database access separate from HTTP
* [ ] Centralize validation, authentication, authorization & error handling
* [ ] `app.js` (configure Express → middleware → routes → error handling) vs `server.js` (load config → connect DB → start HTTP server)
* [ ] Graceful startup & shutdown; npm scripts as application commands

## 8.4 Environment Configuration

Basics (`.env`, `.env.example`, environments) → Phase 3.

* [ ] `NODE_ENV`; development, test & production configuration
* [ ] Secrets: API keys, database URLs & JWT secrets; secret management; never commit secrets
* [ ] Backend vs frontend (public) environment variables

## 8.5 Authentication

* [ ] Authentication vs authorization; sessions vs token-based authentication
* [ ] JWT: access & refresh tokens, expiration, signing, verification, storage & bearer tokens
* [ ] Cookies: HTTP-only & secure cookies; password hashing with `bcrypt`
* [ ] Build: signup, login, logout, current-user endpoint, protected routes & authentication middleware
* [ ] Build: refresh-token flow, password reset, email verification & auth error handling
* [ ] Rails comparison: Devise, `current_user`, `before_action`, Rails sessions & cookies vs JWT & HTTP-only cookies

## 8.6 Authorization

* [ ] Roles, permissions, admin vs regular users & resource ownership
* [ ] Route-, controller- & service-level authorization, kept separate from authentication
* [ ] Patterns: policy pattern, Pundit-style architecture, CASL & authorization middleware
* [ ] Build: admin-only & user-only routes, owner-only resources, role-based & resource-level permissions

## 8.7 Validation

* [ ] Validating body, query & route params: schema & type validation, required fields & custom rules
* [ ] Sanitizing user input; consistent validation errors; validation middleware
* [ ] Zod vs Joi vs `express-validator`, and when to use schema-based validation

## 8.8 Error Handling

* [ ] HTTP errors & status codes; custom `Error` classes
* [ ] Error types: validation, authentication, authorization, not-found, conflict & database errors
* [ ] Centralized error middleware & a consistent error response format
* [ ] Production: detailed errors in development vs safe responses in production, never leaking sensitive info, handling unexpected errors
* [ ] Error logging & structured logging (monitoring → Phase 12)

## 8.9 REST API Design

```text
GET    /api/articles
GET    /api/articles/:id
POST   /api/articles
PATCH  /api/articles/:id
DELETE /api/articles/:id
```

* [ ] REST principles: resources, resource naming, URL structure & nested resources
* [ ] Methods, status codes, request/response bodies & headers used consistently
* [ ] Consistent response & error formats
* [ ] Pagination, filtering, sorting & searching through query params
* [ ] API versioning
* [ ] Postman collections, API documentation & Swagger/OpenAPI
* [ ] REST vs GraphQL; build one small GraphQL endpoint

## 8.10 Security

* [ ] Input validation & sanitization; CSRF & XSS basics
* [ ] Secure password storage, HTTP-only cookies & CORS configuration
* [ ] Rate limiting & security headers
* [ ] Secrets management; dependency auditing with `npm audit`

## Practice

* [ ] Structured Express API: the 8.2 structure, env config, DB connection, routes/controllers/services/models, validation & centralized errors
* [ ] Rails rebuild: Devise → JWT, bcrypt, auth middleware & refresh tokens
* [ ] Rails rebuild: Pundit → roles, permissions, policies & resource ownership
* [ ] Document the API with Postman or OpenAPI
