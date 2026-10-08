# PHASE 08 — Deployment & Production

**Goal:** Learn how to take a full-stack application from local development to a working production application. Understand builds, production configuration, domains, HTTPS, databases, deployment platforms, logs, and basic production troubleshooting.

---

## Production Fundamentals

* [ ] Understand development vs production environments
* [ ] Understand the production deployment lifecycle
* [ ] Understand build vs runtime
* [ ] Understand frontend build process
* [ ] Understand backend production startup
* [ ] Understand production dependencies
* [ ] Understand production configuration
* [ ] Understand environment variables
* [ ] Understand secrets and sensitive configuration
* [ ] Understand production ports
* [ ] Understand processes and services
* [ ] Understand server/container hosting
* [ ] Understand public vs private services

## Frontend Deployment

* [ ] Understand how React applications are built for production
* [ ] Run a production build locally
* [ ] Understand static assets
* [ ] Understand build output
* [ ] Configure production API URLs
* [ ] Configure frontend environment variables
* [ ] Understand public frontend variables vs backend secrets
* [ ] Deploy a React application
* [ ] Verify production assets
* [ ] Configure SPA routing
* [ ] Handle client-side routes on refresh
* [ ] Understand frontend caching basics

## Backend Deployment

* [ ] Prepare an Express application for production
* [ ] Configure production environment variables
* [ ] Configure production database connection
* [ ] Configure production CORS
* [ ] Configure production port
* [ ] Start Express in production mode
* [ ] Understand host binding
* [ ] Configure production logging
* [ ] Handle application errors
* [ ] Handle graceful shutdown
* [ ] Verify API endpoints after deployment
* [ ] Test the production API independently

## Database Deployment

* [ ] Understand local vs production databases
* [ ] Understand managed databases
* [ ] Create a production MongoDB database
* [ ] Configure MongoDB Atlas
* [ ] Configure database users and permissions
* [ ] Configure database connection strings
* [ ] Store database credentials securely
* [ ] Configure network access
* [ ] Understand database backups
* [ ] Understand indexes in production
* [ ] Understand production database security
* [ ] Test backend → production database connectivity

## Environment Variables & Secrets

* [ ] Understand environment-specific configuration
* [ ] Configure development variables
* [ ] Configure production variables
* [ ] Configure database URLs
* [ ] Configure API URLs
* [ ] Configure authentication secrets
* [ ] Configure third-party API keys
* [ ] Configure storage credentials
* [ ] Understand `.env` vs platform environment variables
* [ ] Keep `.env` files and secrets out of Git
* [ ] Understand secret rotation basics
* [ ] Verify that secrets are not exposed to the frontend

## Domains & DNS

* [ ] Understand domains and subdomains
* [ ] Understand DNS
* [ ] Understand DNS records
* [ ] Understand A records
* [ ] Understand CNAME records
* [ ] Understand nameservers
* [ ] Connect a custom domain to a frontend
* [ ] Connect a custom domain/subdomain to an API
* [ ] Understand frontend/API domain separation
* [ ] Configure production URLs
* [ ] Verify DNS propagation
* [ ] Understand basic DNS troubleshooting

Example:

```text
example.com
     │
     ▼
React Frontend

api.example.com
     │
     ▼
Express API
     │
     ├── MongoDB Atlas
     └── Redis
```

## HTTPS & TLS

* [ ] Understand HTTP vs HTTPS
* [ ] Understand TLS at a high level
* [ ] Understand SSL certificates
* [ ] Configure HTTPS on a deployed application
* [ ] Understand automatic certificate management
* [ ] Verify HTTPS
* [ ] Understand secure cookies
* [ ] Understand mixed-content problems
* [ ] Understand HTTP → HTTPS redirects
* [ ] Understand why HTTPS is required for production authentication/security

## CORS in Production

* [ ] Understand development CORS vs production CORS
* [ ] Configure allowed frontend origins
* [ ] Configure allowed methods
* [ ] Configure allowed headers
* [ ] Configure credentials
* [ ] Understand preflight requests
* [ ] Debug production CORS errors
* [ ] Verify frontend → production API communication
* [ ] Avoid allowing unrestricted origins unnecessarily

## Production Authentication

* [ ] Configure production authentication
* [ ] Configure secure cookies
* [ ] Configure HTTP-only cookies
* [ ] Understand `Secure` and `SameSite`
* [ ] Configure production JWT secrets when using JWT
* [ ] Understand frontend/API domain considerations
* [ ] Verify login in production
* [ ] Verify logout in production
* [ ] Verify protected API requests
* [ ] Test expired/invalid authentication

## File Storage in Production

* [ ] Understand local filesystem vs production storage
* [ ] Understand why local container/server storage may not be persistent
* [ ] Configure cloud/object storage
* [ ] Understand S3-style storage
* [ ] Configure file upload credentials
* [ ] Configure public/private files
* [ ] Understand signed URLs at a high level
* [ ] Test production file uploads

## Logging & Monitoring

* [ ] Understand application logs
* [ ] View deployment logs
* [ ] View backend logs
* [ ] View build logs
* [ ] Understand request/error logging
* [ ] Debug failed deployments from logs
* [ ] Debug production API errors from logs
* [ ] Understand health checks
* [ ] Understand uptime monitoring
* [ ] Understand basic application monitoring
* [ ] Understand error tracking
* [ ] Avoid logging passwords, tokens, and sensitive information

## Deployment Platforms

Practice deploying the same application to different hosting platforms.

### Render

* [ ] Deploy React frontend
* [ ] Deploy Express backend
* [ ] Configure environment variables
* [ ] Configure build/start commands
* [ ] Configure database connection
* [ ] Configure CORS
* [ ] Inspect deployment/build logs

### Railway

* [ ] Deploy Express backend
* [ ] Configure environment variables
* [ ] Configure build/start commands
* [ ] Connect production database
* [ ] Inspect logs
* [ ] Understand service configuration

### Vercel

* [ ] Deploy a React frontend
* [ ] Configure production environment variables
* [ ] Configure custom domain
* [ ] Understand frontend build/deployment workflow
* [ ] Understand SPA routing configuration
* [ ] Connect the frontend to an external Express API

### Replit

* [ ] Deploy a full-stack application
* [ ] Configure environment variables
* [ ] Understand application runtime
* [ ] Configure networking/public access
* [ ] Inspect logs
* [ ] Understand the platform's deployment model

### Lovable

* [ ] Understand Lovable's deployment workflow
* [ ] Deploy a frontend application
* [ ] Understand generated application configuration
* [ ] Understand how external APIs/backend services are connected
* [ ] Compare its workflow with traditional deployment platforms

### Another Deployment Platform

* [ ] Choose another free/low-cost deployment platform
* [ ] Deploy the Express API
* [ ] Deploy the React frontend
* [ ] Configure environment variables
* [ ] Configure the production database
* [ ] Compare the deployment workflow with the other platforms

---

## Docker + Deployment

Connect the previous Docker phase with production deployment.

* [ ] Understand deploying Dockerized applications
* [ ] Understand image-based deployment
* [ ] Build a production Docker image
* [ ] Configure production environment variables
* [ ] Push an image to a container registry
* [ ] Deploy a containerized Express application
* [ ] Deploy a containerized full-stack application
* [ ] Understand platform-managed containers vs self-managed containers
* [ ] Understand when Docker is useful in deployment
* [ ] Understand when a platform can deploy directly from source code

## CI/CD Basics

* [ ] Understand continuous integration
* [ ] Understand continuous deployment
* [ ] Understand deployment pipelines
* [ ] Understand build → test → deploy
* [ ] Understand automatic deployment from Git
* [ ] Understand deployment triggers
* [ ] Run tests before deployment
* [ ] Understand failed deployment rollback
* [ ] Understand basic deployment branches/workflows
* [ ] Understand GitHub-based deployment workflows

---

# Actual Production Deployment

Deploy a complete application from start to finish.

## Application

```text
React
   ↓
HTTPS
   ↓
Express API
   ↓
MongoDB Atlas
   +
Redis
```

## Frontend

* [ ] Build the React application
* [ ] Configure production API URL
* [ ] Configure production environment variables
* [ ] Deploy React frontend
* [ ] Configure frontend domain
* [ ] Enable HTTPS
* [ ] Verify frontend production build

## Backend

* [ ] Prepare Express for production
* [ ] Configure production environment variables
* [ ] Configure production port
* [ ] Configure production CORS
* [ ] Configure production authentication
* [ ] Deploy Express API
* [ ] Configure API domain/subdomain
* [ ] Enable HTTPS
* [ ] Verify API endpoints

## Database

* [ ] Create MongoDB Atlas production database
* [ ] Create database user
* [ ] Configure network access
* [ ] Configure connection string
* [ ] Add database URL to backend environment
* [ ] Verify Express → MongoDB Atlas connection

## Final Integration

* [ ] React frontend deployed
* [ ] Express API deployed
* [ ] MongoDB Atlas configured
* [ ] Environment variables configured
* [ ] CORS configured
* [ ] HTTPS working
* [ ] Production authentication working
* [ ] Production API working
* [ ] Production frontend working
* [ ] CRUD functionality working
* [ ] Search/filter/pagination working
* [ ] File uploads working if implemented
* [ ] Logs accessible
* [ ] Production errors can be diagnosed

---

# Production Troubleshooting

* [ ] Debug failed builds
* [ ] Debug failed deployments
* [ ] Debug incorrect environment variables
* [ ] Debug production CORS
* [ ] Debug DNS problems
* [ ] Debug HTTPS/certificate problems
* [ ] Debug frontend → API connection problems
* [ ] Debug API → database connection problems
* [ ] Debug authentication/cookie problems
* [ ] Debug missing production assets
* [ ] Debug SPA routing problems
* [ ] Read deployment and application logs
* [ ] Reproduce production problems locally
* [ ] Understand rollback/redeploy workflows

---

# Deployment Comparison

Compare deployment models rather than memorizing individual platforms.

* [ ] Compare source-based deployment
* [ ] Compare Docker/container deployment
* [ ] Compare static frontend hosting
* [ ] Compare managed backend hosting
* [ ] Compare managed databases
* [ ] Compare serverless deployment
* [ ] Compare platform-managed vs self-managed infrastructure
* [ ] Understand platform limitations
* [ ] Understand free-tier limitations
* [ ] Understand cold starts at a high level
* [ ] Understand scaling basics
* [ ] Understand when to move beyond a free platform

---

# Practice Projects

## Project 1 — Deploy a React Application

* [ ] Build React application
* [ ] Configure production environment
* [ ] Deploy frontend
* [ ] Configure domain
* [ ] Enable HTTPS
* [ ] Verify production routing

## Project 2 — Deploy an Express API

* [ ] Configure production Express server
* [ ] Configure environment variables
* [ ] Deploy API
* [ ] Configure domain/subdomain
* [ ] Enable HTTPS
* [ ] Inspect logs
* [ ] Test API endpoints

## Project 3 — Deploy MERN Application

* [ ] React frontend
* [ ] Express backend
* [ ] MongoDB Atlas
* [ ] Production environment variables
* [ ] Production CORS
* [ ] Authentication
* [ ] HTTPS
* [ ] Custom domains
* [ ] Logs
* [ ] Full production testing

## Project 4 — Dockerized Production Application

* [ ] Build production Docker images
* [ ] Push images to a registry
* [ ] Deploy containerized backend
* [ ] Configure production environment
* [ ] Connect production database
* [ ] Verify application
* [ ] Compare source-based and Docker-based deployment

---

# Completion Goal

By the end of this phase, be able to take an application from:

```text
Local Development
       ↓
Git Repository
       ↓
Production Build
       ↓
Environment Configuration
       ↓
Deployment Platform
       ↓
Domain + DNS
       ↓
HTTPS
       ↓
Production Database
       ↓
Production API
       ↓
Production Frontend
       ↓
Logs + Monitoring
```

You should be able to **deploy, configure, connect, verify, troubleshoot, and maintain a real full-stack application in production**.

The important goal is not memorizing Render, Railway, Vercel, or any other platform. The goal is understanding the **deployment concepts that transfer between platforms**.
