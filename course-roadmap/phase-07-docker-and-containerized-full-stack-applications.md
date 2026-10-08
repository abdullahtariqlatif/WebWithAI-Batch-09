# PHASE — Docker & Containerized Full-Stack Applications

**Goal:** Learn how to containerize and run a complete full-stack application with Docker. Understand how containers, images, networks, volumes, environment variables, and Docker Compose work together.

---

## Docker Fundamentals

* [ ] Understand containers and containerized applications
* [ ] Understand Docker images and containers
* [ ] Understand the difference between an image and a container
* [ ] Understand Docker's client, daemon, and container runtime
* [ ] Understand Docker registries and image repositories
* [ ] Pull, run, stop, start, restart, remove, and inspect containers
* [ ] View container logs and running processes
* [ ] Execute commands inside running containers
* [ ] Understand container lifecycle
* [ ] Understand container isolation and what containers do and do not isolate

## Docker Images

* [ ] Understand image layers
* [ ] Understand image caching
* [ ] Understand image tags and versions
* [ ] Pull images from Docker Hub
* [ ] Build images locally
* [ ] Tag images
* [ ] Remove unused images
* [ ] Inspect image metadata
* [ ] Understand image size and why smaller images matter

## Dockerfile

* [ ] Understand the purpose of a Dockerfile
* [ ] Choose a base image
* [ ] Understand official images
* [ ] Set a working directory with `WORKDIR`
* [ ] Copy files with `COPY`
* [ ] Run build/install commands with `RUN`
* [ ] Set environment variables with `ENV`
* [ ] Document ports with `EXPOSE`
* [ ] Define default commands with `CMD`
* [ ] Understand `ENTRYPOINT`
* [ ] Understand `CMD` vs `ENTRYPOINT`
* [ ] Understand build context
* [ ] Understand `.dockerignore`
* [ ] Understand Dockerfile instruction order and layer caching
* [ ] Optimize Dockerfile layer usage
* [ ] Avoid copying unnecessary files into images

### Node / Express Dockerfile

* [ ] Containerize a Node.js application
* [ ] Install dependencies inside the image
* [ ] Copy application source
* [ ] Expose the Express port
* [ ] Start the Express server from the container
* [ ] Configure the application to listen on the correct host/interface
* [ ] Use environment variables for configuration

### React Dockerfile

* [ ] Containerize a React development environment
* [ ] Understand development vs production containers
* [ ] Build a React production bundle
* [ ] Serve a production React application from a container
* [ ] Understand multi-stage Docker builds
* [ ] Separate build dependencies from runtime dependencies

## Docker Volumes

* [ ] Understand container filesystem persistence
* [ ] Understand why container data disappears when containers are removed
* [ ] Create and use named volumes
* [ ] Mount volumes into containers
* [ ] Understand bind mounts
* [ ] Compare named volumes and bind mounts
* [ ] Persist MongoDB data
* [ ] Persist Redis data when required
* [ ] Use bind mounts for development source code
* [ ] Understand volume ownership and permissions

## Docker Networking

* [ ] Understand Docker networks
* [ ] Create custom Docker networks
* [ ] Connect containers to the same network
* [ ] Understand container-to-container communication
* [ ] Understand Docker's internal DNS
* [ ] Use service/container names instead of hard-coded container IPs
* [ ] Understand host ports vs container ports
* [ ] Understand `localhost` inside a container
* [ ] Connect Express to MongoDB through the Docker network
* [ ] Connect Express to Redis through the Docker network
* [ ] Understand when ports need to be published to the host

## Environment Configuration

* [ ] Understand environment variables in containers
* [ ] Pass environment variables with Docker
* [ ] Use `.env` files
* [ ] Understand Docker Compose environment configuration
* [ ] Separate development and production configuration
* [ ] Configure database URLs
* [ ] Configure Redis URLs
* [ ] Configure API URLs
* [ ] Handle frontend public environment variables correctly
* [ ] Keep secrets out of Dockerfiles and source control
* [ ] Understand build-time vs runtime environment variables

---

## Docker Compose

* [ ] Understand why Docker Compose is useful
* [ ] Understand Compose services
* [ ] Create a `compose.yaml` / `docker-compose.yml`
* [ ] Define services
* [ ] Configure images
* [ ] Build services from Dockerfiles
* [ ] Configure ports
* [ ] Configure volumes
* [ ] Configure networks
* [ ] Configure environment variables
* [ ] Use `.env` with Compose
* [ ] Start and stop the entire application stack
* [ ] Rebuild individual services
* [ ] View logs for individual services
* [ ] Execute commands inside Compose services
* [ ] Understand service dependencies
* [ ] Understand health checks
* [ ] Understand restart policies

## Full-Stack Docker Compose

Build the following application as one Compose project:

```text
React
   ↓
Express
   ↓
MongoDB
   +
Redis
```

* [ ] Create a React service
* [ ] Create an Express service
* [ ] Create a MongoDB service
* [ ] Create a Redis service
* [ ] Connect services through a Docker network
* [ ] Persist MongoDB data with a volume
* [ ] Configure Redis
* [ ] Configure backend environment variables
* [ ] Configure frontend environment variables
* [ ] Connect Express → MongoDB
* [ ] Connect Express → Redis
* [ ] Connect React → Express
* [ ] Verify service-to-service communication
* [ ] Run the complete stack with one Compose command
* [ ] Inspect logs across the entire stack

## Development Workflow

* [ ] Understand Docker-based development vs local development
* [ ] Mount source code into development containers
* [ ] Configure hot reload
* [ ] Handle `node_modules` correctly with containers
* [ ] Avoid unnecessary image rebuilds
* [ ] Use Docker layer caching effectively
* [ ] Rebuild containers when dependencies change
* [ ] Debug application errors inside containers
* [ ] Debug networking problems
* [ ] Debug environment-variable problems
* [ ] Debug volume and permission problems

---

## Production Docker

* [ ] Understand development vs production Docker images
* [ ] Use production dependencies only where appropriate
* [ ] Use multi-stage builds
* [ ] Minimize image size
* [ ] Run containers as a non-root user
* [ ] Handle application signals correctly
* [ ] Configure graceful shutdown
* [ ] Configure health checks
* [ ] Use appropriate restart policies
* [ ] Understand container logs in production
* [ ] Understand container resource limits
* [ ] Keep secrets outside images
* [ ] Tag production images properly

## Docker Security Basics

* [ ] Understand container isolation
* [ ] Avoid running applications as root
* [ ] Keep base images updated
* [ ] Avoid unnecessary packages
* [ ] Avoid embedding secrets in images
* [ ] Use `.dockerignore`
* [ ] Understand exposed vs published ports
* [ ] Limit unnecessary container privileges
* [ ] Scan images for known vulnerabilities
* [ ] Understand why Docker is not a complete security boundary

---

## Docker Registry

* [ ] Understand Docker registries
* [ ] Tag images for a registry
* [ ] Push images to a registry
* [ ] Pull images from a registry
* [ ] Understand public vs private repositories
* [ ] Understand image versioning and tags
* [ ] Understand immutable version tags vs floating tags

---

## Docker + Rails Translation

Relate Docker concepts to familiar Rails development:

* [ ] Understand Docker as an environment/runtime layer rather than an application framework
* [ ] Containerize a Rails application
* [ ] Containerize a Node/Express application
* [ ] Compare Rails development environment vs Dockerized environment
* [ ] Run Rails + PostgreSQL with Docker Compose
* [ ] Run Express + MongoDB/PostgreSQL with Docker Compose
* [ ] Understand database persistence in both stacks
* [ ] Understand environment configuration in both stacks
* [ ] Understand Dockerized development workflows across Rails and Node

---

## Practice Projects

### Project 1 — Dockerized Express API

* [ ] Create an Express API
* [ ] Write a Dockerfile
* [ ] Build the image
* [ ] Run the container
* [ ] Configure environment variables
* [ ] Expose the API port
* [ ] Inspect logs and debug the container

### Project 2 — Dockerized MERN Application

* [ ] React frontend
* [ ] Express backend
* [ ] MongoDB database
* [ ] Redis
* [ ] Dockerfiles
* [ ] Docker Compose
* [ ] Internal networking
* [ ] Persistent database volume
* [ ] Environment configuration
* [ ] Full-stack communication

### Project 3 — Development + Production Setup

* [ ] Create a development Compose configuration
* [ ] Add source-code mounts and hot reload
* [ ] Create production Dockerfiles
* [ ] Use multi-stage builds
* [ ] Separate development and production configuration
* [ ] Build production images
* [ ] Run the production-like stack locally

### Final Docker Project

Build and containerize a complete application:

```text
                    ┌──────────────┐
                    │    React     │
                    └──────┬───────┘
                           │
                         HTTP
                           │
                    ┌──────▼───────┐
                    │   Express    │
                    └───┬──────┬───┘
                        │      │
                   MongoDB    Redis
                        │      │
                    ┌───▼──────▼───┐
                    │   Volumes    │
                    └──────────────┘
```

* [ ] Containerize the frontend
* [ ] Containerize the backend
* [ ] Add MongoDB
* [ ] Add Redis
* [ ] Configure networking
* [ ] Configure persistent storage
* [ ] Configure environment variables
* [ ] Add health checks
* [ ] Add production Dockerfiles
* [ ] Use multi-stage builds
* [ ] Run the entire stack with Docker Compose
* [ ] Debug the complete application from inside the containers
* [ ] Build and tag production images
* [ ] Push images to a container registry
* [ ] Document how to run the project from a clean machine

---

## Completion Goal

By the end of this phase, be able to take a full-stack application and explain:

```text
Source Code
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Container
    ↓
Docker Network
    ↓
Docker Volumes
    ↓
Environment Configuration
    ↓
Docker Compose
    ↓
Complete Application Stack
```

You should be able to **build, run, connect, persist, debug, and package** a React + Express + MongoDB + Redis application using Docker.
