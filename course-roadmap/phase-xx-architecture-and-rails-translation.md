# PHASE — Full-Stack Architecture & Rails Translation

The goal of this phase is to take the Node.js, Express.js, React, MongoDB, Mongoose, Prisma and PostgreSQL knowledge learned in the previous phases and organize it into a maintainable full-stack application.

This phase is especially useful for a Rails developer because it answers:

> **How do I build a Node/Express application with the same level of organization, conventions and maintainability that I expect from a Rails application?**

The goal is **not** to make Express behave exactly like Rails.

Instead, learn the Node ecosystem on its own terms, then establish a consistent architecture that provides familiar separation of concerns.

---

# Application Architecture

## Recommended Backend Structure

A good starting convention for a Rails developer is:

```text
server/
├── config/
│   ├── database.js
│   ├── env.js
│   └── cors.js
│
├── models/
│   ├── User.js
│   └── Article.js
│
├── controllers/
│   ├── usersController.js
│   └── articlesController.js
│
├── routes/
│   ├── usersRoutes.js
│   └── articlesRoutes.js
│
├── services/
│   ├── authService.js
│   └── emailService.js
│
├── middleware/
│   ├── auth.js
│   ├── authorization.js
│   └── errorHandler.js
│
├── validators/
│   ├── userValidator.js
│   └── articleValidator.js
│
├── utils/
│
├── jobs/
│
├── tests/
│
├── app.js
├── server.js
├── package.json
└── .env
```

* [ ] Understand the purpose of each application layer
* [ ] Configuration layer
* [ ] Models / data layer
* [ ] Controllers
* [ ] Routes
* [ ] Services / business logic
* [ ] Middleware
* [ ] Validators
* [ ] Utilities
* [ ] Background jobs
* [ ] Tests
* [ ] Application entry point
* [ ] HTTP server entry point

### Important Architecture Principle

Express does not require this structure.

* [ ] Understand that Express is intentionally unopinionated
* [ ] Treat the structure as a project convention rather than a framework requirement
* [ ] Understand why consistent conventions are valuable
* [ ] Avoid unnecessary abstraction
* [ ] Keep responsibilities separated without creating excessive layers

---

# Request Lifecycle

## Application Flow

```text
HTTP Request
     ↓
Route
     ↓
Middleware
     ↓
Validation
     ↓
Authentication
     ↓
Authorization
     ↓
Controller
     ↓
Service
     ↓
Data Access
     ↓
Database
     ↓
Service
     ↓
Controller
     ↓
HTTP Response
```

* [ ] Understand the complete request lifecycle
* [ ] Understand Express middleware execution order
* [ ] Keep controllers focused on HTTP concerns
* [ ] Keep business logic inside services
* [ ] Keep database access separate from HTTP concerns
* [ ] Centralize validation
* [ ] Centralize authentication
* [ ] Centralize authorization
* [ ] Centralize error handling

---

# Application Startup & Configuration

## Application vs Server

Separate Express application configuration from HTTP server startup.

```text
app.js
  ↓
Configure Express
  ↓
Middleware
  ↓
Routes
  ↓
Error Handling
```

```text
server.js
  ↓
Load configuration
  ↓
Connect database
  ↓
Start HTTP server
```

* [ ] Understand `app.js`
* [ ] Understand `server.js`
* [ ] Separate application configuration from server startup
* [ ] Understand graceful server startup
* [ ] Understand graceful shutdown
* [ ] Understand npm scripts as application commands

---

# Environment Configuration

Learn the Node equivalents of the Rails environment model.

```text
Rails

development
test
production
```

Node applications commonly use:

```text
NODE_ENV
.env
```

* [ ] `NODE_ENV`
* [ ] `.env`
* [ ] `.env.example`
* [ ] Development configuration
* [ ] Test configuration
* [ ] Production configuration
* [ ] Secrets
* [ ] API keys
* [ ] Database URLs
* [ ] JWT secrets
* [ ] Backend environment variables
* [ ] Frontend environment variables
* [ ] Environment-specific configuration
* [ ] Secret management
* [ ] Keeping secrets out of Git

> Never commit secrets to source control.

---

# Authentication

## Authentication Fundamentals

* [ ] Authentication vs authorization
* [ ] Sessions vs token-based authentication
* [ ] JWT authentication
* [ ] Access tokens
* [ ] Refresh tokens
* [ ] Token expiration
* [ ] Token signing
* [ ] Token verification
* [ ] Token storage
* [ ] Bearer tokens
* [ ] HTTP-only cookies
* [ ] Secure cookies
* [ ] Password hashing
* [ ] `bcrypt`

## Authentication Implementation

* [ ] Build signup
* [ ] Build login
* [ ] Build logout
* [ ] Build current-user endpoint
* [ ] Build protected routes
* [ ] Authentication middleware
* [ ] Refresh-token flow
* [ ] Password reset
* [ ] Email verification
* [ ] Authentication error handling

## Rails Translation

* [ ] Devise authentication model
* [ ] `current_user`
* [ ] `before_action`
* [ ] Authentication middleware
* [ ] Rails sessions vs JWT
* [ ] Rails cookies vs HTTP-only cookies

---

# Authorization

## Access Control

* [ ] Roles
* [ ] Permissions
* [ ] Admin users
* [ ] Regular users
* [ ] Resource ownership
* [ ] Role-based authorization
* [ ] Route authorization
* [ ] Controller authorization
* [ ] Service-level authorization

## Authorization Patterns

* [ ] Policy pattern
* [ ] Pundit-style architecture
* [ ] Access-control patterns
* [ ] CASL
* [ ] Authorization middleware
* [ ] Keeping authorization separate from authentication

## Build

* [ ] Admin-only route
* [ ] User-only route
* [ ] Owner-only resource
* [ ] Role-based permissions
* [ ] Resource-level authorization

---

# Validation & Input Handling

## Request Validation

* [ ] Request validation
* [ ] Request body validation
* [ ] Query parameter validation
* [ ] Route parameter validation
* [ ] Schema validation
* [ ] Type validation
* [ ] Required fields
* [ ] Custom validation rules
* [ ] Sanitizing user input
* [ ] Consistent validation errors

## Validation Libraries

* [ ] Zod
* [ ] Joi
* [ ] `express-validator`
* [ ] Understand when to use schema-based validation
* [ ] Compare validation approaches

## Request Pipeline

```text
Request
   ↓
Validation
   ↓
Authentication
   ↓
Authorization
   ↓
Controller
   ↓
Service
   ↓
Data Access
   ↓
Database
```

---

# Backend Error Handling

## Errors

* [ ] HTTP errors
* [ ] HTTP status codes
* [ ] Custom `Error` classes
* [ ] Validation errors
* [ ] Authentication errors
* [ ] Authorization errors
* [ ] Database errors
* [ ] Not-found errors
* [ ] Conflict errors
* [ ] Centralized error middleware
* [ ] Consistent error response format

## Production Error Handling

* [ ] Development error details
* [ ] Production-safe error responses
* [ ] Error logging
* [ ] Structured logging
* [ ] Avoid leaking sensitive information
* [ ] Error monitoring
* [ ] Unexpected error handling

---

# API Design

## REST API

* [ ] REST principles
* [ ] Resources
* [ ] Endpoints
* [ ] HTTP methods
* [ ] Status codes
* [ ] Request bodies
* [ ] Response bodies
* [ ] Request headers
* [ ] Response headers
* [ ] Resource naming
* [ ] Nested resources
* [ ] API versioning

Example:

```text
GET    /api/articles
GET    /api/articles/:id
POST   /api/articles
PATCH  /api/articles/:id
DELETE /api/articles/:id
```

## API Features

* [ ] Pagination
* [ ] Filtering
* [ ] Sorting
* [ ] Searching
* [ ] Query parameters
* [ ] Consistent response format
* [ ] Consistent error responses
* [ ] Authentication
* [ ] Authorization
* [ ] API versioning

## API Tools

* [ ] Postman collections
* [ ] API documentation
* [ ] Swagger/OpenAPI basics

---

# Email

## Rails → Node Translation

Rails:

```text
ActionMailer
```

Node ecosystem:

* [ ] Nodemailer
* [ ] SMTP
* [ ] Transactional email providers
* [ ] Email service abstraction
* [ ] Email templates
* [ ] HTML emails
* [ ] Plain-text emails
* [ ] Verification emails
* [ ] Password-reset emails
* [ ] Notification emails

## Architecture

* [ ] Keep email logic outside controllers
* [ ] Create an email service
* [ ] Integrate email with background jobs
* [ ] Handle email failures
* [ ] Avoid blocking HTTP requests with slow email operations

---

# Background Jobs

## Rails → Node Translation

Rails:

```text
ActiveJob
    ↓
Sidekiq
    ↓
Redis
```

Node ecosystem:

```text
Application
    ↓
BullMQ
    ↓
Redis
    ↓
Worker
```

## Job Concepts

* [ ] Understand queues
* [ ] Redis
* [ ] BullMQ
* [ ] Jobs
* [ ] Workers
* [ ] Job producers
* [ ] Job consumers
* [ ] Retries
* [ ] Delayed jobs
* [ ] Scheduled / repeatable jobs
* [ ] Failed jobs
* [ ] Concurrency
* [ ] Job priorities
* [ ] Job monitoring

## Build

* [ ] Email background job
* [ ] Scheduled job
* [ ] Retryable job
* [ ] Failed-job handling
* [ ] Queue dashboard
* [ ] Worker process

## Rails Translation

* [ ] ActiveJob → job abstraction
* [ ] Sidekiq → BullMQ + Redis
* [ ] Rails job classes → Node job modules/classes
* [ ] ActiveJob retries → queue retry configuration
* [ ] Scheduled jobs → repeatable/scheduled jobs

> These are conceptual equivalents, not exact technical replacements.

---

# File Uploads & Storage

## Rails → Node Translation

Rails:

```text
ActiveStorage
```

Node ecosystem:

* [ ] `multipart/form-data`
* [ ] Multer
* [ ] Local file storage
* [ ] Object storage
* [ ] Amazon S3
* [ ] Cloudinary
* [ ] Signed URLs
* [ ] Image uploads
* [ ] File validation
* [ ] File size limits
* [ ] File type validation
* [ ] Secure file handling

## Architecture

* [ ] Separate upload handling from controllers
* [ ] Create a storage service
* [ ] Understand local vs cloud storage
* [ ] Understand direct-to-storage uploads
* [ ] Understand signed upload/download URLs

---

# Real-Time Features

## Rails → Node Translation

Rails:

```text
ActionCable
```

Node ecosystem:

```text
WebSockets
Socket.IO
```

## WebSocket Concepts

* [ ] WebSockets
* [ ] Socket.IO
* [ ] Connections
* [ ] Disconnects
* [ ] Events
* [ ] Broadcasting
* [ ] Rooms
* [ ] Private rooms
* [ ] Authentication
* [ ] Authorization
* [ ] Reconnection
* [ ] Connection state

## Build

* [ ] Chat application
* [ ] Online/offline status
* [ ] Typing indicator
* [ ] Real-time notifications
* [ ] Real-time dashboard

---

# Testing

## Backend Testing

* [ ] Jest
* [ ] Vitest
* [ ] Supertest
* [ ] Unit tests
* [ ] Integration tests
* [ ] API tests
* [ ] Mocking
* [ ] Test doubles
* [ ] Fixtures
* [ ] Factories
* [ ] Test database strategy
* [ ] Authentication tests
* [ ] Authorization tests

## Test

* [ ] Model behavior
* [ ] Services
* [ ] Controllers
* [ ] Authentication
* [ ] Authorization
* [ ] API endpoints
* [ ] Validation
* [ ] Error responses

## Rails Translation

| Rails         | Node Ecosystem            |
| ------------- | ------------------------- |
| RSpec         | Jest / Vitest             |
| Request specs | Supertest                 |
| FactoryBot    | Test factories            |
| Fixtures      | Fixtures / seed test data |
| Mocks         | Jest / Vitest mocks       |
| Model specs   | Model/data-layer tests    |
| Service specs | Service tests             |

---

# React Testing

## Component Testing

* [ ] React Testing Library
* [ ] Component tests
* [ ] User interaction tests
* [ ] Form tests
* [ ] API mocking
* [ ] Async component testing
* [ ] Integration testing
* [ ] Loading-state testing
* [ ] Error-state testing
* [ ] Authentication-state testing

## Full-Stack Testing

* [ ] Test React frontend independently
* [ ] Test Express API independently
* [ ] Test frontend/API integration
* [ ] Test authentication flow
* [ ] Test CRUD workflows
* [ ] Test error handling across frontend and backend

---

# Database Architecture

## MERN

```text
React
  ↓
Express API
  ↓
Controllers
  ↓
Services
  ↓
Mongoose
  ↓
MongoDB
```

* [ ] Understand document-oriented persistence
* [ ] Understand Mongoose as the data-access layer
* [ ] Keep MongoDB-specific logic in the data layer
* [ ] Keep controllers independent of database implementation where practical

## PERN

```text
React
  ↓
Express API
  ↓
Controllers
  ↓
Services
  ↓
Prisma
  ↓
PostgreSQL
```

* [ ] Understand relational persistence
* [ ] Understand Prisma as the data-access layer
* [ ] Understand relational constraints
* [ ] Understand foreign keys
* [ ] Understand transactions
* [ ] Keep database-specific concerns inside the data layer

## Switching MERN → PERN

* [ ] Replace MongoDB collections with PostgreSQL tables
* [ ] Replace documents with relational rows
* [ ] Replace embedded documents with related tables where appropriate
* [ ] Replace document references with foreign keys
* [ ] Replace many-to-many document relationships with join tables
* [ ] Replace Mongoose with Prisma
* [ ] Redesign validation and constraints
* [ ] Redesign pagination and filtering queries
* [ ] Update transaction handling
* [ ] Keep the API contract consistent where possible
* [ ] Understand which parts of the application should remain unchanged

---

# Rails → Node / Express Translation

The following mappings are useful for building a mental bridge between Rails and the Node ecosystem.

| Rails           | Node / Express Ecosystem                        |
| --------------- | ----------------------------------------------- |
| `app/models`    | `models/`                                       |
| ActiveRecord    | Mongoose / Prisma                               |
| Model           | Mongoose Model / Prisma Model                   |
| Migration       | Mongoose migration strategy / Prisma migrations |
| Controller      | Express Controller                              |
| Routes          | Express Router                                  |
| Service Object  | Service Module / Class                          |
| ActiveJob       | BullMQ / other job queue                        |
| Sidekiq         | BullMQ + Redis                                  |
| ActionMailer    | Nodemailer / email provider                     |
| Devise          | Authentication library / custom authentication  |
| Pundit          | Authorization middleware / CASL                 |
| CanCanCan       | CASL / authorization middleware                 |
| ActiveStorage   | S3 / Cloudinary / Multer                        |
| ActionCable     | Socket.IO / WebSockets                          |
| RSpec           | Jest / Vitest                                   |
| FactoryBot      | Test factories                                  |
| `Rails.env`     | `NODE_ENV`                                      |
| Credentials     | Environment variables / secret management       |
| `config/`       | Configuration modules                           |
| Rack middleware | Express middleware                              |
| `bin/rails`     | npm scripts / CLI tools                         |

## Important Differences

* [ ] Understand that these mappings are conceptual rather than 1:1
* [ ] Understand ActiveRecord vs Mongoose vs Prisma
* [ ] Understand Rails conventions vs Express flexibility
* [ ] Understand Rails middleware vs Express middleware
* [ ] Understand ActiveJob/Sidekiq vs Node queues
* [ ] Understand Devise vs Node authentication approaches
* [ ] Understand Pundit/Cancancan vs Node authorization approaches
* [ ] Understand ActiveStorage vs object-storage libraries
* [ ] Understand ActionCable vs WebSockets/Socket.IO
* [ ] Understand what Rails provides automatically that Express does not

---

# Rails-Like Project Conventions

The purpose of this section is to establish your own consistent conventions for Node projects.

## Layer-Based Architecture

```text
routes/
   ↓
controllers/
   ↓
services/
   ↓
data access/
   ↓
database
```

* [ ] Keep routes focused on routing
* [ ] Keep controllers focused on HTTP concerns
* [ ] Keep services focused on business logic
* [ ] Keep data access focused on persistence
* [ ] Keep middleware focused on cross-cutting request concerns
* [ ] Keep validators focused on input validation

## Feature-Based Architecture

For larger applications, understand an alternative organization:

```text
server/
├── config/
│
├── modules/
│   ├── users/
│   │   ├── user.model.js
│   │   ├── user.controller.js
│   │   ├── user.routes.js
│   │   ├── user.service.js
│   │   └── user.validator.js
│   │
│   └── articles/
│       ├── article.model.js
│       ├── article.controller.js
│       ├── article.routes.js
│       ├── article.service.js
│       └── article.validator.js
│
├── middleware/
├── jobs/
├── utils/
├── tests/
├── app.js
└── server.js
```

* [ ] Understand layer-based architecture
* [ ] Understand feature-based architecture
* [ ] Understand when each structure is appropriate
* [ ] Understand how applications evolve as they grow
* [ ] Avoid premature abstraction
* [ ] Avoid excessively large controllers
* [ ] Avoid excessively large service classes

---

# Production Backend Practices

## Reliability

* [ ] Graceful shutdown
* [ ] Database connection management
* [ ] Connection pooling
* [ ] Health checks
* [ ] Error monitoring
* [ ] Structured logging
* [ ] Background worker management

## Security

* [ ] Secure password storage
* [ ] HTTP-only cookies
* [ ] CORS configuration
* [ ] CSRF basics
* [ ] Rate limiting
* [ ] Security headers
* [ ] Input validation
* [ ] Input sanitization
* [ ] Secrets management
* [ ] Authentication
* [ ] Authorization

## Database

* [ ] Database indexes
* [ ] Query performance
* [ ] Transactions
* [ ] Database backups
* [ ] Production database configuration
* [ ] Database connection security

---

# Full-Stack Integration

## React + Express

* [ ] React frontend → Express API architecture
* [ ] API request lifecycle
* [ ] Loading states
* [ ] Success states
* [ ] Error states
* [ ] CRUD operations
* [ ] Pagination
* [ ] Search
* [ ] Filtering
* [ ] Authentication
* [ ] Authorization
* [ ] Cookies and credentials
* [ ] CORS
* [ ] File uploads
* [ ] API error handling

## Complete Application Flow

```text
React
  ↓
HTTP / REST API
  ↓
Express Router
  ↓
Middleware
  ↓
Validation
  ↓
Authentication
  ↓
Authorization
  ↓
Controller
  ↓
Service
  ↓
Mongoose / Prisma
  ↓
MongoDB / PostgreSQL
```

* [ ] Trace a complete request from React to the database
* [ ] Trace a response from the database back to React
* [ ] Understand where validation occurs
* [ ] Understand where authentication occurs
* [ ] Understand where authorization occurs
* [ ] Understand where business logic occurs
* [ ] Understand where database logic occurs
* [ ] Understand where errors are handled

---

# Practice Projects

## Project 1 — Structured Express API

* [ ] Create the recommended project structure
* [ ] Configure environment variables
* [ ] Configure database connection
* [ ] Create routes
* [ ] Create controllers
* [ ] Create services
* [ ] Create models
* [ ] Add validation
* [ ] Add centralized error handling
* [ ] Add authentication
* [ ] Add authorization
* [ ] Add API tests

## Project 2 — MERN Application

* [ ] Build a React + Express + MongoDB application
* [ ] Implement authentication
* [ ] Implement authorization
* [ ] Implement CRUD
* [ ] Implement search
* [ ] Implement filtering
* [ ] Implement pagination
* [ ] Implement file uploads
* [ ] Implement email
* [ ] Implement background jobs
* [ ] Implement API tests
* [ ] Implement React tests

## Project 3 — PERN Conversion

Take the MERN application and rebuild its persistence layer using PostgreSQL.

* [ ] Replace MongoDB with PostgreSQL
* [ ] Replace Mongoose with Prisma
* [ ] Redesign database models
* [ ] Add relational constraints
* [ ] Add foreign keys
* [ ] Add transactions
* [ ] Update database queries
* [ ] Update pagination and filtering
* [ ] Preserve the React/API contract where possible
* [ ] Compare MERN and PERN implementations

## Final Architecture Project

Build a production-style full-stack application using the architecture learned in this phase.

* [ ] Design the application architecture
* [ ] Create the project structure
* [ ] Configure environments
* [ ] Implement authentication
* [ ] Implement authorization
* [ ] Implement validation
* [ ] Implement centralized errors
* [ ] Implement REST API
* [ ] Implement database layer
* [ ] Implement email
* [ ] Implement background jobs
* [ ] Implement file storage
* [ ] Implement real-time functionality
* [ ] Implement backend tests
* [ ] Implement React tests
* [ ] Implement logging
* [ ] Implement security controls
* [ ] Implement production configuration
* [ ] Document the API
* [ ] Deploy the application

---

# Final Rails Comparison

At the end of this phase, be able to look at the same application from both perspectives:

```text
Rails

Routes
  ↓
Controller
  ↓
Service
  ↓
ActiveRecord
  ↓
Database

        ≈

Node / Express

Routes
  ↓
Middleware
  ↓
Controller
  ↓
Service
  ↓
Mongoose / Prisma
  ↓
Database
```

The goal is not to memorize a translation table.

The goal is to understand:

* [ ] How Rails organizes an application
* [ ] How Express applications are commonly organized
* [ ] What Rails provides automatically
* [ ] What must be chosen/configured in Node
* [ ] Which concepts transfer directly
* [ ] Which concepts only have approximate equivalents
* [ ] How to design maintainable Node applications independently of Rails
* [ ] How to move comfortably between Rails and Node ecosystems
* [ ] How to choose MERN or PERN based on application requirements
* [ ] How to build a consistent project architecture without relying on a framework to make every architectural decision
