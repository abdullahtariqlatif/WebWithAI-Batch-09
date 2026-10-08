# PHASE — Node.js, Express.js & Databases

## Node.js

### Node Fundamentals

* [ ] What Node.js is
* [ ] Node.js runtime vs browser runtime
* [ ] V8 JavaScript engine
* [ ] Node.js process
* [ ] Event-driven architecture
* [ ] Non-blocking I/O
* [ ] Node.js modules
* [ ] CommonJS
* [ ] ES modules

### npm Ecosystem

* [ ] npm
* [ ] `package.json`
* [ ] `package-lock.json`
* [ ] Dependencies & `devDependencies`
* [ ] npm scripts
* [ ] `npm install`, `npm uninstall` & `npm update`
* [ ] Semantic versioning
* [ ] Package version ranges
* [ ] `npx`
* [ ] Local vs global packages

### Node APIs

* [ ] `fs`
* [ ] `path`
* [ ] `process`
* [ ] Environment variables
* [ ] Events
* [ ] Streams
* [ ] Buffers
* [ ] File handling
* [ ] Working with JSON files

### Node Application Structure

* [ ] Entry points
* [ ] Module organization
* [ ] Configuration
* [ ] Environment configuration
* [ ] Application vs library code
* [ ] Separating configuration, business logic & infrastructure

---

# Express.js

## Fundamentals

* [ ] Express installation & setup
* [ ] Express application
* [ ] HTTP server
* [ ] Routes
* [ ] Route handlers
* [ ] Controllers
* [ ] Middleware
* [ ] Request object
* [ ] Response object
* [ ] Route parameters
* [ ] Query parameters
* [ ] Request body
* [ ] JSON responses

## HTTP & REST APIs

* [ ] GET, POST, PUT, PATCH & DELETE
* [ ] HTTP status codes
* [ ] Request & response headers
* [ ] JSON APIs
* [ ] REST API principles
* [ ] Resource-oriented API design
* [ ] API URL structure
* [ ] Request validation
* [ ] Response structure
* [ ] Consistent API errors

## Middleware

* [ ] Built-in middleware
* [ ] Custom middleware
* [ ] Middleware execution order
* [ ] Request logging
* [ ] Authentication middleware
* [ ] Authorization middleware
* [ ] Validation middleware
* [ ] Error-handling middleware
* [ ] Middleware composition

## CORS

* [ ] What CORS is
* [ ] Same-origin policy
* [ ] Browser CORS behavior
* [ ] Express CORS configuration
* [ ] Allowed origins
* [ ] Allowed methods
* [ ] Allowed headers
* [ ] Credentials
* [ ] Preflight requests

## Express Architecture

* [ ] Routes → controllers → services → data layer
* [ ] Controllers
* [ ] Services
* [ ] Data access layer
* [ ] Middleware layer
* [ ] Validation layer
* [ ] Error-handling strategy
* [ ] Feature-based project structure
* [ ] Separation of concerns

## API Security Basics

* [ ] Input validation
* [ ] Sanitizing user input
* [ ] Authentication vs authorization
* [ ] Password hashing
* [ ] Cookies
* [ ] HTTP-only cookies
* [ ] CSRF basics
* [ ] Rate limiting
* [ ] Security headers
* [ ] Secrets & environment variables

---

# MongoDB

## MongoDB Fundamentals

* [ ] NoSQL vs relational databases
* [ ] MongoDB architecture
* [ ] Database
* [ ] Collections
* [ ] Documents
* [ ] BSON
* [ ] `_id`
* [ ] ObjectId
* [ ] Fields & nested documents
* [ ] Arrays
* [ ] Indexes

## CRUD

* [ ] Insert documents
* [ ] Find documents
* [ ] `find`
* [ ] `findOne`
* [ ] Update documents
* [ ] `updateOne`
* [ ] `updateMany`
* [ ] Delete documents
* [ ] `deleteOne`
* [ ] `deleteMany`

## Queries

* [ ] Filtering
* [ ] Sorting
* [ ] Pagination
* [ ] Projections
* [ ] Query operators
* [ ] `$in`
* [ ] `$or`
* [ ] `$and`
* [ ] `$gt`
* [ ] `$gte`
* [ ] `$lt`
* [ ] `$lte`
* [ ] Regular-expression queries

## MongoDB Data Modeling

* [ ] Document-oriented data modeling
* [ ] Embedding documents
* [ ] Referencing documents
* [ ] One-to-one relationships
* [ ] One-to-many relationships
* [ ] Many-to-many relationships
* [ ] Choosing embedding vs referencing
* [ ] Denormalization
* [ ] Data duplication trade-offs
* [ ] Schema flexibility
* [ ] Index design

## MongoDB Architecture & Deployment

* [ ] MongoDB locally
* [ ] MongoDB Atlas
* [ ] Connection strings
* [ ] Database credentials
* [ ] Environment variables
* [ ] Indexes
* [ ] Backups
* [ ] Basic production database configuration

---

# Mongoose

## Mongoose Fundamentals

* [ ] Mongoose installation
* [ ] MongoDB connection
* [ ] Schemas
* [ ] Models
* [ ] Documents
* [ ] Schema types
* [ ] Validation
* [ ] Defaults
* [ ] Required fields
* [ ] Enums
* [ ] Timestamps

## Mongoose Relationships

* [ ] References
* [ ] `ObjectId` references
* [ ] `populate`
* [ ] One-to-one relationships
* [ ] One-to-many relationships
* [ ] Many-to-many relationships
* [ ] Embedding vs referencing with Mongoose

## Mongoose Features

* [ ] Middleware / hooks
* [ ] Virtuals
* [ ] Instance methods
* [ ] Static methods
* [ ] Query methods
* [ ] Custom validation
* [ ] Pagination
* [ ] Indexes
* [ ] Transactions

## Mongoose Practice

* [ ] Build User model
* [ ] Build Post model
* [ ] Create relationships between models
* [ ] Implement CRUD through Mongoose
* [ ] Implement validation
* [ ] Implement pagination
* [ ] Implement search & filtering

---

# Prisma ORM

## Prisma Fundamentals

* [ ] What an ORM is
* [ ] Prisma ORM architecture
* [ ] Prisma Client / typed data access
* [ ] Prisma schema / data contract
* [ ] Models
* [ ] Fields
* [ ] Primary keys
* [ ] Relations
* [ ] Type-safe database queries
* [ ] Prisma configuration
* [ ] Database connection

## Prisma with MongoDB

* [ ] Prisma with MongoDB
* [ ] MongoDB models in Prisma
* [ ] ObjectId fields
* [ ] MongoDB embedded documents
* [ ] MongoDB references
* [ ] MongoDB-specific schema considerations
* [ ] Prisma queries against MongoDB
* [ ] MongoDB indexes
* [ ] MongoDB migrations / schema changes
* [ ] Limitations and feature differences when using Prisma with MongoDB

## Prisma with PostgreSQL

* [ ] Prisma with PostgreSQL
* [ ] Relational models
* [ ] Tables & columns
* [ ] Primary keys
* [ ] Foreign keys
* [ ] One-to-one relationships
* [ ] One-to-many relationships
* [ ] Many-to-many relationships
* [ ] Constraints
* [ ] Unique constraints
* [ ] Indexes
* [ ] Prisma migrations
* [ ] Seed data
* [ ] Prisma queries
* [ ] Transactions

---

# MongoDB vs PostgreSQL

## Data Modeling

* [ ] Document model vs relational model
* [ ] Collections vs tables
* [ ] Documents vs rows
* [ ] Embedded documents vs related tables
* [ ] References vs foreign keys
* [ ] Flexible schemas vs structured schemas
* [ ] Denormalization vs normalization
* [ ] Modeling one-to-many relationships
* [ ] Modeling many-to-many relationships
* [ ] Choosing a database based on application requirements

## Querying

* [ ] MongoDB document queries
* [ ] SQL relational queries
* [ ] Filtering & sorting
* [ ] Joins vs document embedding
* [ ] Aggregation pipelines vs SQL aggregation
* [ ] Pagination strategies
* [ ] Indexing strategies

## Data Integrity

* [ ] Application-level validation
* [ ] Database-level constraints
* [ ] Foreign keys
* [ ] Unique constraints
* [ ] Referential integrity
* [ ] Transactions
* [ ] Atomic operations

## Architecture Differences

* [ ] Designing APIs for MongoDB
* [ ] Designing APIs for PostgreSQL
* [ ] Data access layer abstraction
* [ ] ORM / ODM responsibilities
* [ ] Database-specific business logic
* [ ] Avoiding database-specific assumptions in application code

---

# MERN vs PERN

## MERN

* [ ] MongoDB
* [ ] Express.js
* [ ] React
* [ ] Node.js
* [ ] MongoDB data modeling
* [ ] Mongoose or Prisma data layer
* [ ] Document-oriented persistence
* [ ] API design around document-based data

## PERN

* [ ] PostgreSQL
* [ ] Express.js
* [ ] React
* [ ] Node.js
* [ ] PostgreSQL data modeling
* [ ] Prisma data layer
* [ ] Relational persistence
* [ ] Normalized relational schema
* [ ] Foreign keys & constraints
* [ ] SQL-based querying
* [ ] Transactions & relational integrity

## Switching MERN → PERN

* [ ] Replace MongoDB collections with PostgreSQL tables
* [ ] Replace MongoDB documents with relational rows
* [ ] Redesign schemas around normalization
* [ ] Replace embedded documents with related tables where appropriate
* [ ] Replace document references with foreign keys
* [ ] Redesign many-to-many relationships using join tables
* [ ] Replace MongoDB queries with relational queries
* [ ] Replace Mongoose with Prisma
* [ ] Update validation & constraints
* [ ] Update migrations
* [ ] Update pagination & filtering queries
* [ ] Update transaction handling
* [ ] Update API data-access logic
* [ ] Preserve React/API contracts where possible

---

# Full-Stack Backend Integration

## React + Express API

* [ ] React frontend → Express API architecture
* [ ] REST API integration
* [ ] API request lifecycle
* [ ] Loading, success & error states
* [ ] CRUD operations
* [ ] Pagination
* [ ] Search & filtering
* [ ] Authentication
* [ ] Authorization
* [ ] Cookies & credentials
* [ ] CORS
* [ ] File uploads
* [ ] API error handling

## Database Integration

* [ ] Express → Mongoose → MongoDB
* [ ] Express → Prisma → MongoDB
* [ ] Express → Prisma → PostgreSQL
* [ ] Separating API logic from data access
* [ ] Database validation
* [ ] Application validation
* [ ] Transactions
* [ ] Database error handling

## Production Backend

* [ ] Environment configuration
* [ ] Database connection management
* [ ] Connection pooling
* [ ] Logging
* [ ] Error monitoring
* [ ] API security
* [ ] Rate limiting
* [ ] Database indexes
* [ ] Database backups
* [ ] Health checks
* [ ] Graceful shutdown
* [ ] Production configuration

---

# Practice

## Node & Express

* [ ] Build a basic Express API
* [ ] Build REST CRUD endpoints
* [ ] Add middleware
* [ ] Add validation
* [ ] Add centralized error handling
* [ ] Add authentication
* [ ] Add authorization

## MongoDB + Mongoose

* [ ] Build a MongoDB CRUD API
* [ ] Create related Mongoose models
* [ ] Implement search & filtering
* [ ] Implement pagination
* [ ] Implement authentication with MongoDB

## Prisma + PostgreSQL

* [ ] Rebuild the MongoDB API using PostgreSQL
* [ ] Rebuild the data models using Prisma
* [ ] Implement relational relationships
* [ ] Implement foreign keys & constraints
* [ ] Implement transactions
* [ ] Compare the MongoDB and PostgreSQL implementations

## Full-Stack

* [ ] Build a React + Express + MongoDB application
* [ ] Build a React + Express + PostgreSQL application
* [ ] Implement authentication
* [ ] Implement CRUD
* [ ] Implement search & filtering
* [ ] Implement pagination
* [ ] Deploy a production-style full-stack application
