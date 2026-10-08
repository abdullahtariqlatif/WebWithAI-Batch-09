# PHASE 10 — Practice Applications & MERN Capstones

**Goal:** Turn the concepts from the previous phases into a small number of serious, complete applications. Do not build every practice exercise as a full application. Use the earlier phases to identify promising projects, then select the strongest ideas here for complete implementation.

---

## How to Use This Phase

* [ ] Review the practice projects mentioned throughout the previous phases
* [ ] Identify projects marked as **capstone candidates**
* [ ] Select only the strongest and most useful applications
* [ ] Avoid rebuilding small tutorial/demo applications from earlier phases
* [ ] Prefer applications that combine multiple technologies and concepts
* [ ] Build applications incrementally rather than trying to implement everything at once
* [ ] Reuse architecture and patterns learned in previous phases
* [ ] Document important technical decisions
* [ ] Test applications properly
* [ ] Dockerize appropriate applications
* [ ] Deploy appropriate applications
* [ ] Use completed applications as portfolio projects

---

## Capstone Selection Criteria

A project is a good capstone candidate if it:

* [ ] Solves a realistic problem
* [ ] Has multiple related entities/resources
* [ ] Requires authentication
* [ ] Has meaningful authorization
* [ ] Requires CRUD operations
* [ ] Has non-trivial data relationships
* [ ] Requires search/filtering/pagination
* [ ] Has meaningful frontend state
* [ ] Uses a real backend API
* [ ] Requires database design
* [ ] Can benefit from background jobs or asynchronous processing
* [ ] Can demonstrate production concerns
* [ ] Is large enough to expose architectural gaps
* [ ] Is small enough to realistically finish

Avoid selecting projects that are essentially:

* [ ] Todo lists
* [ ] Simple calculators
* [ ] Basic weather apps
* [ ] Simple CRUD demos
* [ ] API-fetching exercises
* [ ] Small UI component demos

Those belong in the earlier learning phases.

---

# Capstone 1 — Mini SaaS / Project Management System

Build one serious full-stack application around project and task management.

## Core Application

* [ ] User registration
* [ ] Login
* [ ] Logout
* [ ] Current-user/session handling
* [ ] User profile
* [ ] Password management
* [ ] Roles
* [ ] Authorization
* [ ] Projects
* [ ] Project members
* [ ] Tasks
* [ ] Task assignment
* [ ] Task status
* [ ] Task priorities
* [ ] CRUD operations

## Search & Data Features

* [ ] Search
* [ ] Filtering
* [ ] Sorting
* [ ] Pagination
* [ ] URL query parameters
* [ ] Relationships between users/projects/tasks
* [ ] Validation
* [ ] Consistent API responses
* [ ] Consistent API errors

## Collaboration Features

* [ ] Comments
* [ ] Activity/history
* [ ] Notifications
* [ ] User mentions
* [ ] Real-time notifications
* [ ] Online/offline state where appropriate

## Authentication & Authorization

* [ ] JWT authentication or session-based authentication
* [ ] Protected routes
* [ ] Role-based authorization
* [ ] Resource ownership
* [ ] Admin/project-owner permissions
* [ ] Unauthorized/forbidden handling
* [ ] Authentication persistence
* [ ] Expired authentication handling

## Files & Communication

* [ ] File uploads
* [ ] Attachments on projects/tasks/comments
* [ ] Email notifications
* [ ] Email verification
* [ ] Password reset
* [ ] Background email jobs

## Backend Infrastructure

* [ ] Redis
* [ ] Background jobs
* [ ] Job retries
* [ ] Scheduled jobs where appropriate
* [ ] Socket.IO/WebSockets
* [ ] Real-time events
* [ ] Centralized error handling
* [ ] Structured logging

## Frontend

* [ ] Responsive dashboard
* [ ] Authentication UI
* [ ] Project dashboard
* [ ] Task management UI
* [ ] Search/filter UI
* [ ] Pagination
* [ ] Forms and validation
* [ ] Loading states
* [ ] Error states
* [ ] Empty states
* [ ] Optimistic updates where appropriate
* [ ] Real-time UI updates

## Testing

* [ ] Backend unit tests
* [ ] Service tests
* [ ] API/integration tests
* [ ] Authentication tests
* [ ] Authorization tests
* [ ] React component tests
* [ ] User interaction tests
* [ ] Important end-to-end flows

## Production

* [ ] Dockerize application
* [ ] Configure production environment
* [ ] Deploy frontend
* [ ] Deploy backend
* [ ] Configure production database
* [ ] Configure Redis
* [ ] Configure file storage
* [ ] Configure HTTPS
* [ ] Configure domains
* [ ] Configure CORS
* [ ] Configure production secrets
* [ ] Configure logging
* [ ] Verify production application

---

# Capstone 2 — Real-World Content / Publishing Platform

Build a production-style publishing platform rather than a simple blog.

Possible examples:

```text
News Platform
Knowledge Base
Documentation Platform
Magazine
Community Publishing Platform
```

## Core Features

* [ ] User registration/login
* [ ] User profiles
* [ ] Roles and permissions
* [ ] Authors
* [ ] Articles/posts
* [ ] Categories
* [ ] Tags
* [ ] Draft/published states
* [ ] CRUD
* [ ] Search
* [ ] Filtering
* [ ] Pagination
* [ ] Comments
* [ ] Moderation

## Content Features

* [ ] Rich text/Markdown content
* [ ] Featured images
* [ ] File uploads
* [ ] Image management
* [ ] Slugs/public URLs
* [ ] Related content
* [ ] Publishing workflow
* [ ] Scheduled publishing

## Communication

* [ ] Email notifications
* [ ] Newsletter/subscription system
* [ ] Background jobs
* [ ] Scheduled jobs
* [ ] Notifications

## Production Features

* [ ] API architecture
* [ ] Authentication
* [ ] Authorization
* [ ] Validation
* [ ] Error handling
* [ ] Tests
* [ ] Docker
* [ ] Deployment
* [ ] Logging

---

# Capstone 3 — E-Commerce / Marketplace Application

Build a realistic commerce system with multiple users and related resources.

## Core Features

* [ ] User registration/login
* [ ] Customer profiles
* [ ] Admin roles
* [ ] Products
* [ ] Categories
* [ ] Product images
* [ ] Product variants
* [ ] Inventory
* [ ] Cart
* [ ] Orders
* [ ] Order items
* [ ] Order status
* [ ] CRUD
* [ ] Search
* [ ] Filtering
* [ ] Pagination
* [ ] Sorting

## User Features

* [ ] Product browsing
* [ ] Cart management
* [ ] Checkout flow
* [ ] Order history
* [ ] Profile management
* [ ] Reviews/ratings
* [ ] Wishlist

## Admin Features

* [ ] Product management
* [ ] Inventory management
* [ ] Order management
* [ ] User management
* [ ] Role-based authorization
* [ ] Dashboard
* [ ] Search/filtering

## Backend Features

* [ ] Validation
* [ ] Transactions where appropriate
* [ ] Background jobs
* [ ] Email notifications
* [ ] Redis caching where appropriate
* [ ] File storage
* [ ] API tests
* [ ] Error handling

## Production

* [ ] Docker
* [ ] Production database
* [ ] File/object storage
* [ ] HTTPS
* [ ] Deployment
* [ ] Logging
* [ ] Production testing

---

# Capstone 4 — Rebuild Using PERN

Take one completed MERN application and rebuild its backend using PostgreSQL and Prisma.

* [ ] Replace MongoDB with PostgreSQL
* [ ] Replace Mongoose with Prisma
* [ ] Convert document models to relational models
* [ ] Normalize appropriate data
* [ ] Create foreign keys
* [ ] Create indexes
* [ ] Create unique constraints
* [ ] Create many-to-many relationships
* [ ] Create migrations
* [ ] Seed development/test data
* [ ] Rewrite database queries
* [ ] Rewrite pagination
* [ ] Rewrite filtering/search
* [ ] Implement transactions where appropriate
* [ ] Preserve the frontend API contract where practical
* [ ] Compare MongoDB and PostgreSQL implementations
* [ ] Document the architectural differences

**Goal:** Demonstrate that the application architecture is not tightly coupled to one database.

---

# Capstone Engineering Checklist

Apply these to the serious applications selected above.

## Architecture

* [ ] Clear project structure
* [ ] Routes
* [ ] Controllers
* [ ] Services
* [ ] Data access layer
* [ ] Models/schema
* [ ] Middleware
* [ ] Validators
* [ ] Configuration
* [ ] Utilities
* [ ] Background jobs
* [ ] Tests

## API

* [ ] RESTful resources
* [ ] Consistent HTTP status codes
* [ ] Consistent response format
* [ ] Consistent error format
* [ ] Validation
* [ ] Authentication
* [ ] Authorization
* [ ] Pagination
* [ ] Filtering
* [ ] Search
* [ ] API documentation

## Frontend

* [ ] Component architecture
* [ ] Routing
* [ ] Authentication state
* [ ] Server state
* [ ] Forms
* [ ] Validation
* [ ] Loading states
* [ ] Error states
* [ ] Empty states
* [ ] Responsive UI
* [ ] Accessibility
* [ ] Performance considerations

## Quality

* [ ] Unit tests
* [ ] Integration/API tests
* [ ] React tests
* [ ] Critical user-flow tests
* [ ] Error handling
* [ ] Logging
* [ ] Debugging
* [ ] Code organization
* [ ] Documentation

## Production

* [ ] Environment configuration
* [ ] Secrets management
* [ ] Database deployment
* [ ] File storage
* [ ] Redis
* [ ] Docker
* [ ] HTTPS
* [ ] Domain
* [ ] Deployment
* [ ] Logs
* [ ] Monitoring
* [ ] Backup considerations

---

# Capstone Workflow

Do not attempt to build every feature at once.

Use an incremental development process:

```text
Idea
 ↓
Requirements
 ↓
Data Model
 ↓
API Design
 ↓
Backend Foundation
 ↓
Authentication
 ↓
Core CRUD
 ↓
React UI
 ↓
Frontend ↔ Backend Integration
 ↓
Search / Filtering / Pagination
 ↓
Advanced Features
 ↓
Testing
 ↓
Docker
 ↓
Deployment
 ↓
Production Verification
```

## Development Stages

### Stage 1 — Foundation

* [ ] Define requirements
* [ ] Define entities
* [ ] Design database
* [ ] Define API resources
* [ ] Create project structure
* [ ] Configure development environment

### Stage 2 — Core Application

* [ ] Implement authentication
* [ ] Implement authorization
* [ ] Implement core models
* [ ] Implement CRUD
* [ ] Implement validation
* [ ] Implement API errors

### Stage 3 — Frontend

* [ ] Build application layout
* [ ] Add routing
* [ ] Add authentication UI
* [ ] Build core screens
* [ ] Connect frontend to API
* [ ] Add loading/error/empty states

### Stage 4 — Advanced Features

* [ ] Search
* [ ] Filtering
* [ ] Pagination
* [ ] File uploads
* [ ] Email
* [ ] Background jobs
* [ ] Redis
* [ ] Real-time functionality

### Stage 5 — Quality

* [ ] Backend tests
* [ ] API tests
* [ ] React tests
* [ ] Authentication tests
* [ ] Authorization tests
* [ ] Critical user-flow tests
* [ ] Debug and refactor

### Stage 6 — Production

* [ ] Dockerize
* [ ] Configure production environment
* [ ] Deploy
* [ ] Configure domain
* [ ] Configure HTTPS
* [ ] Configure database
* [ ] Configure storage
* [ ] Configure Redis
* [ ] Configure logs
* [ ] Verify production functionality

---

# Capstone Candidate References

Earlier phases should **mention serious application ideas here without requiring those applications to be fully built during that phase**.

When an earlier phase introduces a project that could become a substantial application, mark it as:

> **Capstone Candidate:** This project may be selected for full implementation in Phase 10.

Only projects with meaningful architectural or full-stack potential should receive this designation.

Examples of suitable candidates:

* [ ] Project management system
* [ ] Publishing/content platform
* [ ] E-commerce/marketplace
* [ ] Community/social application
* [ ] Booking/reservation platform
* [ ] Learning management system
* [ ] Help desk/support platform
* [ ] Analytics/dashboard platform
* [ ] Multi-tenant SaaS application

Small exercises remain practice exercises and should **not** be promoted to capstones.

---

# Final Capstone Selection

Do not build every candidate.

Select **1–3 serious applications** based on:

* [ ] Learning value
* [ ] Portfolio value
* [ ] Technical complexity
* [ ] Real-world relevance
* [ ] Ability to demonstrate full-stack skills
* [ ] Ability to demonstrate production skills
* [ ] Ability to finish the project

Recommended approach:

```text
Many small exercises
        ↓
Several practice applications
        ↓
Several capstone candidates
        ↓
Select 1–3 serious projects
        ↓
Build completely
        ↓
Test
        ↓
Dockerize
        ↓
Deploy
        ↓
Portfolio
```

---

# Completion Goal

By the end of this phase, you should have at least **one serious, production-style full-stack application** that demonstrates:

```text
React
 +
Node.js / Express
 +
MongoDB or PostgreSQL
 +
Authentication
 +
Authorization
 +
REST API
 +
Database Design
 +
Validation
 +
Search / Filtering / Pagination
 +
File Storage
 +
Email
 +
Background Jobs
 +
Redis
 +
Real-Time Features
 +
Testing
 +
Docker
 +
Deployment
```

The goal is not to prove that every technology can be used in one application.

The goal is to demonstrate that you can **design, build, test, containerize, deploy, and maintain a real full-stack application.**
