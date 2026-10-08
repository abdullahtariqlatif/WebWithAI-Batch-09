# 05 · Node.js, Express, API design

| Rails | Express |
|---|---|
| `routes.rb` | `express.Router()` |
| controller | controller module |
| `before_action` / Rack middleware | middleware |
| service object | service module |
| Devise | JWT + bcrypt (or Passport) |
| Pundit / CanCanCan | policy middleware / CASL |
| ActionMailer | Nodemailer |
| ActiveJob + Sidekiq | BullMQ + Redis |
| ActiveStorage | Multer + S3/Cloudinary |
| RSpec request specs | Jest/Vitest + Supertest |

## Checklist
- [ ] Node basics: runtime vs browser, modules, `package.json`, npm scripts, semver
- [ ] Node APIs: `fs`, `path`, `process`, events, streams
- [ ] Express: app, routes, params/query/body, status codes, JSON
- [ ] MVC layout: routes → controllers → services → models (+ middleware, validators, config)
- [ ] Middleware: logging, auth, error handler
- [ ] CORS: origins, credentials, methods
- [ ] Validation: Zod / Joi / express-validator
- [ ] Errors: custom error classes, central error middleware, consistent error format
- [ ] Auth: bcrypt, JWT access + refresh, HTTP-only cookies, `current_user` equivalent
- [ ] Authorization: roles, ownership, policy pattern
- [ ] Email (Nodemailer), background jobs (BullMQ/Redis), uploads (Multer + S3)
- [ ] Testing: Jest/Vitest + Supertest, mocks, factories
- [ ] API design: REST conventions, pagination/filtering/sorting, versioning
- [ ] Docs: Postman collection, Swagger/OpenAPI
- [ ] REST vs GraphQL (build one small GraphQL endpoint)
- [ ] Security: rate limiting, sanitization, XSS/CSRF, `npm audit`

## Practice
- [ ] Express REST API with MVC + auth + validation + tests
- [ ] Rebuild Devise (signup/login/logout/refresh/reset)
- [ ] Rebuild Pundit (roles, policies, owner-only)
- [ ] Rebuild ActiveJob/Sidekiq + ActionMailer (queued email with retries)

## Work
