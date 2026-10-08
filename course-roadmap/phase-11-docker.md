# PHASE 11 — Docker & Containerized Full-Stack Apps

Goal: build, run, connect, persist, debug & package a React + Express + MongoDB + Redis app with Docker.

```text
Source Code → Dockerfile → Image → Container → Network → Volumes → Env Config → Compose → Full Stack
```

## 11.1 Fundamentals

* [ ] Containers, images, and the difference between them
* [ ] Docker client, daemon, container runtime & registries
* [ ] Container lifecycle: pull, run, stop, start, restart, remove & inspect
* [ ] Logs, running processes & executing commands inside containers
* [ ] Container isolation: what it does & doesn't isolate

## 11.2 Images

* [ ] Layers & caching, tags & versions
* [ ] Pull from Docker Hub; build, tag, inspect & remove images
* [ ] Image size & why smaller images matter

## 11.3 Dockerfile

* [ ] Base & official images; `WORKDIR`, `COPY`, `RUN`, `ENV` & `EXPOSE`
* [ ] `CMD` vs `ENTRYPOINT`
* [ ] Build context & `.dockerignore`; instruction order & layer caching; not copying unnecessary files
* [ ] Node/Express image: install deps, copy source, expose the port, listen on the right host/interface, configure through env vars
* [ ] React image: dev vs production containers; build the bundle & serve it; multi-stage builds separating build & runtime dependencies

## 11.4 Volumes

* [ ] Why container data disappears; named volumes vs bind mounts
* [ ] Persist MongoDB (and Redis when needed); bind-mount source code for development
* [ ] Volume ownership & permissions

## 11.5 Networking

* [ ] Custom networks, container-to-container communication & Docker's internal DNS (service names, not IPs)
* [ ] Host vs container ports, `localhost` inside a container & when to publish ports
* [ ] Connect Express → MongoDB & Express → Redis over the Docker network

## 11.6 Environment Configuration

* [ ] Passing env vars, `.env` files & Compose environment config
* [ ] Dev vs production config; database, Redis & API URLs; frontend public variables
* [ ] Build-time vs runtime variables; keeping secrets out of Dockerfiles & Git

## 11.7 Docker Compose

* [ ] Why Compose; `compose.yaml` / `docker-compose.yml`: services, images, builds, ports, volumes, networks & env (incl. `.env`)
* [ ] Start/stop the whole stack, rebuild one service, per-service logs & exec
* [ ] Service dependencies, health checks & restart policies
* [ ] Full stack: React, Express, MongoDB & Redis services, connected & persisted, running with one command

## 11.8 Development Workflow

* [ ] Docker-based vs local development; source mounts & hot reload; handling `node_modules`
* [ ] Avoiding unnecessary rebuilds, using layer caching, rebuilding when dependencies change
* [ ] Debugging app errors, networking, env-var & volume/permission problems inside containers

## 11.9 Production Images & Security

* [ ] Multi-stage builds, production-only dependencies & minimal image size
* [ ] Non-root user, signal handling & graceful shutdown, health checks & restart policies
* [ ] Container logs & resource limits; secrets outside images; proper production tags
* [ ] Security: updated base images, fewer packages, exposed vs published ports, limited privileges, vulnerability scanning & why Docker isn't a complete security boundary

## 11.10 Registries

* [ ] Tag, push & pull images; public vs private repositories
* [ ] Image versioning: immutable version tags vs floating tags

## 11.11 Docker + Rails

* [ ] Docker as an environment/runtime layer, not an application framework
* [ ] Containerize a Rails app; run Rails + PostgreSQL and Express + MongoDB/PostgreSQL with Compose
* [ ] Compare persistence, env config & dev workflows across the two stacks

## Practice

* [ ] Dockerized Express API: Dockerfile, build, run, env vars, ports, logs & debugging
* [ ] Dockerized MERN + Redis with Compose: internal networking, persistent DB volume, env config & full-stack communication
* [ ] Dev + production setup: dev Compose with mounts & hot reload; production multi-stage Dockerfiles; run the production-like stack locally
* [ ] Final: the whole stack with health checks, production images pushed to a registry & a README for running it on a clean machine
