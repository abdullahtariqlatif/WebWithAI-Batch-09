# PHASE 4 — React

HTTP & `fetch` basics → Phase 3. TypeScript with React → Phase 5. Wiring React to your own Express API → Phase 10.

## 4.1 Fundamentals

* [ ] Setup: Vite, project structure, importing & exporting components
* [ ] JSX, components, component trees & fragments
* [ ] Props & `children`
* [ ] Conditional rendering, rendering lists & keys
* [ ] Event handling & basic forms

## 4.2 Components & Composition

* [ ] Functional components, component responsibilities & boundaries (separation of concerns)
* [ ] Reusable components & props composition
* [ ] Patterns: presentational/container, render props, compound components, higher-order components, headless components
* [ ] Controlled vs uncontrolled components
* [ ] Avoiding prop drilling

## 4.3 State

* [ ] `useState`: initialization, updates & functional updates
* [ ] Immutability: updating objects & arrays in state
* [ ] Derived state, lifting state up, local vs shared state & state colocation
* [ ] `useReducer`, reducer patterns & state-machine basics

## 4.4 Hooks & Effects

* [ ] Rules of Hooks
* [ ] `useEffect`, `useContext`, `useRef`, `useMemo`, `useCallback`, `useId`, `useLayoutEffect`, `useImperativeHandle` & `useDebugValue`
* [ ] Custom hooks & hook composition
* [ ] Effects: lifecycle & synchronization, dependency arrays & cleanup
* [ ] Effect uses: API requests, subscriptions, timers, event listeners & external systems
* [ ] When *not* to use an effect; stale closures & effect dependencies

## 4.5 Context, Refs & the DOM

* [ ] Context: `createContext`, providers, consumers, `useContext` & context composition
* [ ] Context for app config & auth/user state; context performance; not using Context for every kind of state
* [ ] Refs: DOM refs, mutable refs, forwarding refs, `useImperativeHandle` & imperative APIs
* [ ] Measuring DOM elements, focus management & portals

## 4.6 Routing

* [ ] React Router: `BrowserRouter`, route configuration, `Route`, `Link` & `NavLink`
* [ ] Nested & dynamic routes, route params & query/search params
* [ ] Programmatic navigation, route layouts & 404/catch-all routes
* [ ] Protected routes; authentication- & authorization-aware routing
* [ ] Route-level loading & error states; URL state & navigation patterns

## 4.7 Data Fetching & Server State

* [ ] `fetch` vs Axios: methods, headers, JSON, auth headers, cookies & credentials
* [ ] API service layer & API error handling
* [ ] Loading, error & empty states; retries & request cancellation
* [ ] Pagination, filtering, sorting & debounced search
* [ ] Optimistic UI
* [ ] Client state vs server state & the server-state lifecycle
* [ ] TanStack Query: queries, mutations, query keys, caching, cache invalidation, refetching & stale data
* [ ] TanStack Query advanced: pagination & infinite queries, optimistic updates, prefetching, dependent queries & request deduplication

## 4.8 Forms

* [ ] Controlled vs uncontrolled forms, form state, submission & error handling
* [ ] Validation: client-side, showing server-side errors & schema validation with Zod
* [ ] React Hook Form & reusable form components
* [ ] File inputs, multi-step forms & dynamic forms

## 4.9 Global State

* [ ] Redux concepts: store, state, actions, reducers, selectors, dispatch & middleware
* [ ] Redux Toolkit: `configureStore`, `createSlice`, `createAsyncThunk` & async state
* [ ] Redux DevTools, normalized state & global state architecture
* [ ] RTK Query: caching & mutations
* [ ] Zustand
* [ ] Choosing between local state, Context, Redux, Zustand, URL state & server state; avoiding unnecessary global state

## 4.10 Authentication UI

* [ ] Login, logout & registration flows; current-user/session request
* [ ] Persisting auth state & protected routes
* [ ] Role-based & permission-based UI

Sessions vs tokens, JWT, refresh tokens, cookies & CSRF → Phase 8.5. Connecting to Express → Phase 10.4.

## 4.11 Architecture

* [ ] Component-based & feature-based folder structure; feature modules
* [ ] Folders: components, pages, layouts, hooks, services/API layer, state, utils, constants, config, types & shared UI
* [ ] Separating UI, state & API logic; dependency boundaries; scalable project structure

## 4.12 Performance & Modern React

* [ ] Rendering model, reconciliation, re-renders & referential equality
* [ ] `React.memo`, `useMemo` & `useCallback`; memoization trade-offs; state placement to avoid re-renders
* [ ] Code splitting & lazy loading (incl. route-level), `Suspense` & Suspense boundaries
* [ ] Bundle analysis, image/asset optimization, virtualized lists, debouncing & throttling
* [ ] Concurrent features: transitions, `useTransition`, `useDeferredValue` & streaming concepts, and when they're useful
* [ ] React 19: actions & form actions, `useActionState`, `useFormStatus` & `useOptimistic`
* [ ] Component identity: keys & state preservation, state reset patterns
* [ ] Error boundaries & recovery

## 4.13 Server-Side React & Next.js

* [ ] Client vs server components, React Server Components, server/client & serialization boundaries, server actions
* [ ] CSR, SSR & SSG, hydration & streaming server rendering
* [ ] Next.js fundamentals & framework-based architecture; plain React/Vite vs Next.js

## 4.14 Accessibility

* [ ] Semantic HTML, accessible forms, labels & descriptions
* [ ] Keyboard navigation, focus management & ARIA basics
* [ ] Accessible dialogs/modals & navigation; screen-reader considerations; accessibility-aware component design
* [ ] Accessibility testing

## 4.15 Testing & Debugging

* [ ] Unit, component & integration testing concepts; Vitest + React Testing Library
* [ ] Testing user interactions, forms, async UI, loading/error states & auth state
* [ ] Mocking API requests with MSW
* [ ] End-to-end testing with Playwright or Cypress; testing auth flows
* [ ] React DevTools: component, props & state inspection; Profiler; debugging unnecessary renders
* [ ] Browser DevTools: network & console debugging, source maps & debugging async code

## 4.16 Production React

* [ ] Environment variables, per-environment API config, dev vs production config
* [ ] Build process, production builds, bundle optimization & source maps
* [ ] Error monitoring & logging
* [ ] Static hosting & CDN basics (deploying → Phase 12); security basics & dependency management

## 4.17 React + Rails API

* [ ] Rails API-only app + React frontend architecture; REST integration & API versioning
* [ ] CORS, cookie-based vs token-based auth & CSRF with Rails
* [ ] Rails serializers/JSON responses, validation errors & pagination in React; error handling between the two
* [ ] Active Storage & direct uploads from React
* [ ] Action Cable & WebSocket concepts
* [ ] Deploying React & Rails separately

## Practice

* [ ] Todo app, grown into a CRUD app with search & filtering (4.1–4.7)
* [ ] Multi-page app with auth UI and a protected, role-based admin dashboard (4.6, 4.10)
* [ ] API dashboard using TanStack Query (4.7)
* [ ] Forms app with React Hook Form + Zod (4.8)
* [ ] Redux Toolkit application (4.9)
* [ ] React frontend for a Rails API (4.17)
