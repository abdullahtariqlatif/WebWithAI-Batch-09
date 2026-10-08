# PHASE 12 — Deployment & Production

Goal: understand the deployment concepts that carry over between platforms, not memorize Render, Railway or Vercel.

```text
Local Dev → Git → Production Build → Env Config → Platform → Domain + DNS → HTTPS
          → Production DB → Production API → Production Frontend → Logs + Monitoring
```

## 12.1 Production Fundamentals

* [ ] Dev vs production environments; the deployment lifecycle; build vs runtime
* [ ] Production dependencies, configuration, ports, processes & services
* [ ] Server vs container hosting; public vs private services

## 12.2 Frontend Deployment

* [ ] React production build: build output & static assets; run it locally first
* [ ] Production API URL & public env vars (never backend secrets)
* [ ] Deploy & verify assets; SPA routing & client-side routes on refresh; frontend caching basics

## 12.3 Backend Deployment

* [ ] Prepare Express for production: env vars, DB connection, CORS, port & host binding, production mode
* [ ] Production logging, error handling & graceful shutdown
* [ ] Verify & test the production API independently

## 12.4 Database Deployment

* [ ] Local vs managed databases
* [ ] MongoDB Atlas: database users & permissions, connection strings, secure credentials & network access
* [ ] Backups, production indexes & database security; verify backend → database connectivity

## 12.5 Secrets

* [ ] Database & API URLs, auth secrets, third-party API keys & storage credentials per environment
* [ ] `.env` vs platform environment variables; keeping `.env` out of Git
* [ ] Secret rotation basics; verifying no secrets reach the frontend

## 12.6 Domains, DNS & HTTPS

```text
example.com      → React frontend
api.example.com  → Express API → MongoDB Atlas + Redis
```

* [ ] Domains & subdomains; DNS, A & CNAME records, nameservers
* [ ] Custom domains for frontend & API; frontend/API domain separation; production URLs
* [ ] DNS propagation & basic DNS troubleshooting
* [ ] HTTP vs HTTPS, TLS, SSL certificates & automatic certificate management
* [ ] HTTP → HTTPS redirects, mixed content, secure cookies & why HTTPS is required for production auth

## 12.7 Production CORS & Auth

* [ ] Dev vs production CORS: restricted origins (never unrestricted without reason), methods, headers, credentials & preflight; debugging production CORS
* [ ] Production cookies: `Secure`, `HttpOnly` & `SameSite`; production JWT secrets; frontend/API domain considerations
* [ ] Verify login, logout, protected requests & expired/invalid auth in production

## 12.8 File Storage in Production

* [ ] Why local server/container storage may not persist
* [ ] Cloud/object storage (S3-style), credentials, public vs private files & signed URLs
* [ ] Test production uploads

## 12.9 Logging, Monitoring & Reliability

* [ ] Build, deployment & application logs; request & error logging; debugging failed deploys & API errors from logs
* [ ] Never log passwords, tokens or sensitive data
* [ ] Health checks, uptime monitoring, application monitoring & error tracking
* [ ] Database connection management & pooling; background worker management

## 12.10 Deployment Platforms

Deploy the same app to several platforms and compare them.

* [ ] Render: React frontend & Express backend, build/start commands, env vars, database, CORS & logs
* [ ] Railway: Express backend, env vars, build/start commands, production database, logs & service config
* [ ] Vercel: React frontend, env vars, custom domain, SPA routing & connecting to an external API
* [ ] Replit: full-stack app, env vars, runtime, public networking, logs & its deployment model
* [ ] Lovable: deployment workflow, generated app config, connecting external APIs/backends; compare with traditional platforms
* [ ] One more free/low-cost platform: deploy API & frontend, env vars & database; compare

## 12.11 Docker Deployment

* [ ] Image-based deployment: build a production image, push it to a registry & configure its env
* [ ] Deploy a containerized Express app & a containerized full-stack app
* [ ] Platform-managed vs self-managed containers; when Docker helps vs deploying straight from source

## 12.12 CI/CD

* [ ] Continuous integration vs continuous deployment; build → test → deploy pipelines
* [ ] Auto-deploy from Git, deployment triggers, branches & workflows (GitHub Actions)
* [ ] Running tests before deploy; rollback after a failed deployment

## 12.13 Troubleshooting

* [ ] Failed builds & deployments, wrong env vars, missing assets & SPA routing
* [ ] CORS, DNS, HTTPS/certificate & auth/cookie problems
* [ ] Frontend → API and API → database connection problems
* [ ] Reading logs, reproducing production problems locally, rollback & redeploy

## 12.14 Deployment Models & System Design

* [ ] Source vs container deployment; static frontend hosting; managed backends & databases; serverless functions (Vercel, Netlify, Firebase)
* [ ] Platform-managed vs self-managed infrastructure; platform & free-tier limits; cold starts
* [ ] Scaling, caching & performance basics; when to move beyond a free platform
* [ ] System design case studies: Facebook, Uber, YouTube, Instagram & Messenger

## Practice

* [ ] Deploy a React app: production env, domain, HTTPS & verified routing
* [ ] Deploy an Express API: env vars, subdomain, HTTPS, logs & endpoint tests
* [ ] Deploy a full MERN app end to end: frontend & API live on HTTPS with domains, Atlas connected, env & CORS configured; auth, CRUD, search/filter/pagination & uploads working; logs readable & errors diagnosable
* [ ] Dockerized deployment: push images, deploy the containerized backend, compare source-based vs Docker-based deployment
* [ ] GitHub Actions pipeline that runs tests, then deploys
