# PHASE 13 — Capstone Projects

Goal: turn everything from the earlier phases into **1–3 serious, complete applications**. Don't build every idea, and don't rebuild small tutorial apps.

## 13.1 How to Approach Capstones

**Project ladder.** Don't build 20 tiny projects. About 5, each harder than the last:

1. Frontend: React admin dashboard (Tailwind, routing, forms, API), from the Phase 4 practice
2. Backend: Express REST API (MongoDB, Mongoose, MVC, auth, validation, tests), from the Phase 8–9 practice
3. Full MERN: blog/CMS → Capstone 2
4. Real-time: chat app (Socket.IO, auth, notifications), from the Phase 9 practice
5. Full production: SaaS → Capstone 1

**A good capstone:** solves a realistic problem; has several related resources with non-trivial relationships; needs auth, meaningful authorization, CRUD, search/filtering/pagination, real frontend state, a real API & database design; benefits from background jobs; shows production concerns; is big enough to expose architectural gaps but small enough to finish.

**Not a capstone:** todo lists, calculators, basic weather apps, simple CRUD demos, API-fetching exercises, small UI demos. Those belong to earlier phases.

**Other candidate ideas:** community/social app, booking/reservation platform, learning management system, help desk, analytics dashboard, multi-tenant SaaS. When an earlier phase's project has real full-stack potential, mark it **Capstone Candidate** and decide here.

**Pick 1–3 based on:** learning value, portfolio value, technical complexity, real-world relevance, how well it shows full-stack & production skills, and whether you can actually finish it.

**Workflow** (plan it Agile-style: small backlog items, short iterations, SDLC in mind):

```text
Idea → Requirements → Data Model → API Design → Backend Foundation → Auth → Core CRUD → React UI
     → Integration → Search/Filter/Pagination → Advanced Features → Testing → Docker → Deploy → Verify
```

1. **Foundation:** requirements, entities, database design, API resources, project structure, dev environment
2. **Core:** authentication, authorization, core models, CRUD, validation, API errors
3. **Frontend:** layout, routing, auth UI, core screens, API connection, loading/error/empty states
4. **Advanced:** search, filtering, pagination, uploads, email, background jobs, Redis, real-time
5. **Quality:** backend, API, React, auth, authz & critical user-flow tests; debug & refactor
6. **Production:** Dockerize, configure env, deploy, domain, HTTPS, database, storage, Redis, logs, verify

**Engineering review**, applied to every capstone:
- **Architecture:** clear structure; routes, controllers, services, data access, models, middleware, validators, config, utils, jobs, tests
- **API:** RESTful resources; consistent status codes, responses & errors; validation, auth, authz, pagination/filtering/search & docs
- **Frontend:** component architecture, routing, auth & server state, forms & validation, loading/error/empty states, responsive, accessible & performant
- **Quality:** unit, API, React & critical-flow tests; error handling, logging, debugging, code organization & documentation
- **Production:** env config, secrets, database deployment, file storage, Redis, Docker, HTTPS, domain, deployment, logs, monitoring & backups

## 13.2 Capstone 1: Mini SaaS / Project Management System

* [ ] Users: registration, login, logout, current user/session, profile, password management, roles & authorization
* [ ] Domain: projects, project members, tasks, task assignment, status & priorities with full CRUD
* [ ] Data: search, filtering, sorting & pagination via URL query params; user/project/task relationships; validation; consistent responses & errors
* [ ] Collaboration: comments, activity history, notifications, user mentions, real-time notifications & online/offline state
* [ ] Auth: JWT or sessions, protected routes, role-based authorization, resource ownership, admin/project-owner permissions, `401`/`403` handling, auth persistence & expiry
* [ ] Files & email: attachments on projects/tasks/comments; email notifications, verification & password reset through background jobs
* [ ] Infrastructure: Redis, background jobs with retries & scheduling, Socket.IO real-time events, centralized error handling & structured logging
* [ ] Frontend: responsive dashboard, auth UI, project & task screens, search/filter UI, pagination, forms & validation, loading/error/empty states, optimistic & real-time updates
* [ ] Testing: unit, service, API/integration, auth & authorization tests; React component & interaction tests; key end-to-end flows
* [ ] Production: Docker; deploy frontend & backend; production database, Redis & file storage; HTTPS, domains, CORS, secrets & logging; verify

## 13.3 Capstone 2: Content / Publishing Platform

A production-style publishing platform (news site, knowledge base, documentation platform, magazine or community publishing), not a basic blog.

* [ ] Core: auth, profiles, roles & permissions, authors, articles, categories, tags, draft/published states, CRUD, search, filtering, pagination, comments & moderation
* [ ] Content: rich text/Markdown, featured images, uploads & image management, slugs/public URLs, related content, publishing workflow & scheduled publishing
* [ ] Communication: email notifications, newsletter/subscriptions, background & scheduled jobs, notifications
* [ ] Production: API architecture, auth, authorization, validation, error handling, tests, Docker, deployment & logging

## 13.4 Capstone 3: E-Commerce / Marketplace

* [ ] Core: auth, customer profiles, admin roles, products, categories, product images & variants, inventory, cart, orders, order items & status; CRUD, search, filtering, sorting & pagination
* [ ] Customer: product browsing, cart management, checkout flow, order history, profile, reviews/ratings & wishlist
* [ ] Admin: product, inventory, order & user management; role-based authorization; dashboard with search/filtering
* [ ] Backend: validation, transactions, background jobs, email notifications, Redis caching, file storage, API tests & error handling
* [ ] Production: Docker, production database, file/object storage, HTTPS, deployment, logging & production testing

## 13.5 Capstone 4: Rebuild Using PERN

Goal: prove your architecture isn't tied to one database (see 7.11).

* [ ] Convert a finished MERN capstone: MongoDB → PostgreSQL, Mongoose → Prisma; normalize document models; foreign keys, indexes, unique constraints & many-to-many join tables
* [ ] Migrations & dev/test seed data; rewrite queries, pagination, filtering/search; transactions where appropriate
* [ ] Keep the frontend API contract; compare the two implementations & document the architectural differences

## Completion Goal

At least **one serious, production-style application** showing: React + Node/Express + MongoDB or PostgreSQL, authentication, authorization, a REST API, database design, validation, search/filtering/pagination, file storage, email, background jobs, Redis, real-time features, testing, Docker & deployment. Optionally add an AI feature (Phase 16).

The goal isn't to cram every technology into one app. It's to show you can **design, build, test, containerize, deploy & maintain a real full-stack application**.
