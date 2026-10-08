# PHASE 7 — Databases: MongoDB, Mongoose, Prisma & PostgreSQL

This is the only place MERN vs PERN is covered. Later phases refer back here.

## 7.1 MongoDB Fundamentals

* [ ] NoSQL vs relational databases; MongoDB architecture
* [ ] Databases, collections & documents; BSON, `_id` & ObjectId
* [ ] Fields, nested documents & arrays

## 7.2 MongoDB CRUD & Queries

* [ ] Insert, `find` & `findOne`
* [ ] `updateOne` & `updateMany`; `deleteOne` & `deleteMany`
* [ ] Filtering, sorting, pagination & projections
* [ ] Query operators: `$in`, `$or`, `$and`, `$gt`, `$gte`, `$lt` & `$lte`; regex queries

## 7.3 MongoDB Data Modeling

* [ ] Document-oriented modeling: embedding vs referencing & choosing between them
* [ ] One-to-one, one-to-many & many-to-many relationships
* [ ] Denormalization, data-duplication trade-offs & schema flexibility
* [ ] Index design

## 7.4 MongoDB Setup & Operations

* [ ] MongoDB locally, MongoDB Atlas & Compass
* [ ] Connection strings, database credentials & environment variables
* [ ] Backups & basic production database configuration

## 7.5 Mongoose

* [ ] Installation, connection, schemas, models, documents & schema types
* [ ] Validation: required, defaults, enums, custom validation & timestamps
* [ ] Relationships: `ObjectId` references, `populate`, one-to-one/one-to-many/many-to-many, embedding vs referencing
* [ ] Middleware/hooks & virtuals
* [ ] Instance methods, static methods & query methods
* [ ] Pagination, indexes & transactions

## 7.6 Prisma Fundamentals

* [ ] What an ORM is; Prisma architecture & configuration
* [ ] Prisma schema as the data contract: models, fields, primary keys & relations
* [ ] Prisma Client: typed data access & type-safe queries
* [ ] Database connection

## 7.7 PostgreSQL with Prisma

* [ ] Relational models: tables, columns, primary keys & foreign keys
* [ ] One-to-one, one-to-many & many-to-many (join tables)
* [ ] Constraints, unique constraints & indexes
* [ ] Migrations & seed data
* [ ] Queries & transactions

## 7.8 MongoDB with Prisma

* [ ] MongoDB models, ObjectId fields, embedded documents & references
* [ ] MongoDB-specific schema considerations, queries, indexes & schema changes
* [ ] Limitations & feature differences compared to Mongoose

## 7.9 Firebase

* [ ] Firestore: collections, documents & queries
* [ ] Firebase Auth basics

## 7.10 MongoDB vs PostgreSQL

* [ ] Modeling: document vs relational, collections vs tables, documents vs rows, embedded documents vs related tables, references vs foreign keys
* [ ] Schemas: flexible vs structured, denormalization vs normalization, modeling one-to-many & many-to-many
* [ ] Querying: document vs SQL queries, joins vs embedding, aggregation pipelines vs SQL aggregation, pagination & indexing strategies
* [ ] Integrity: app-level validation vs database constraints, foreign keys, unique constraints, referential integrity, transactions & atomic operations
* [ ] Architecture: designing APIs for each, the data access layer, ORM/ODM responsibilities, keeping database-specific logic in the data layer
* [ ] Choosing a database based on application requirements

## 7.11 MERN vs PERN

```text
MERN: React → Express → Mongoose / Prisma → MongoDB     (documents, flexible schemas)
PERN: React → Express → Prisma → PostgreSQL              (normalized tables, foreign keys, SQL, transactions)
```

* [ ] Data: collections → tables, documents → rows, normalize schemas, embedded documents → related tables, references → foreign keys, many-to-many → join tables
* [ ] Code: Mongoose → Prisma; rewrite queries, pagination, filtering, validation, constraints, migrations, transactions & data-access logic
* [ ] Keep the React/API contract unchanged where possible; know which parts of the app shouldn't change

## Practice

* [ ] MongoDB CRUD API with related Mongoose models (User, Post): validation, search, filtering & pagination
* [ ] Rebuild it with Prisma + PostgreSQL (relations, foreign keys, constraints & transactions), then compare both implementations
* [ ] Small Firebase app
