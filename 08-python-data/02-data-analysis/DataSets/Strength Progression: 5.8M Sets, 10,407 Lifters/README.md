# Hardy Strength Progression Report 2026: aggregate data

Aggregated, anonymised statistics from workouts logged in the Hardy strength training app between 2021-03-06 and 2026-09-02. The report built on this data is at https://hardy.app/strength-report; this file documents the CSV so the numbers can be reused without the page.

- **Report:** https://hardy.app/strength-report (per-lift chapters linked from the hub)
- **Data file:** `strength-report-2026.csv` (long format, 5,176 rows), also served at https://hardy.app/strength-report-data.csv
- **Edition:** 2026 (data generated 2026-09-02, report published 2026-09-03)
- **License:** CC BY 4.0 (see `LICENSE`)
- **Citation:** see `CITATION.cff`. Plain text: Hardy (2026). *Hardy Strength Progression Report 2026: aggregate data*. https://hardy.app/strength-report
- **Contact:** https://hardy.app

## Abstract

Every published strength-standards table is built from one-off, self-reported best lifts. Hardy users log every set as they train, which makes it possible to measure strength *over time*: how long plate milestones (135/225/315/405 lb, or 60/100/140/180 kg) take from a lifter's first logged session, how much estimated one-rep max changes after 1, 3, 6, 12 and 24 months by starting strength, and what people who track their training actually log. The dataset covers 5,843,507 finished sets across 368,505 workouts by 10,407 lifters, and reports per-lift percentiles of best estimated 1RM, exercise and muscle-group volume shares, workout length and frequency, rest, RPE and rep-range distributions, and training-time histograms. Every group with fewer than 50 lifters is suppressed.

## Sample

| | |
|---|---|
| Accounts in the app over the period (`users_total`) | 49,139 |
| Lifters with at least one qualifying workout (`users_selected`) | 10,407 |
| Lifters with 3 or more qualifying workouts, used for progression (`users_qualified_3plus_sessions`) | 7,667 |
| Qualifying workouts | 368,505 |
| Finished sets | 5,843,507 |
| Date range | 2021-03-06 to 2026-09-02 |
| Unit preference | 5,184 metric, 5,223 imperial |
| Lifters per lift (3+ workouts) | bench press 6,500; squat 5,931; deadlift 5,247; overhead press 4,582 |

The 10,407 are the subset of all accounts that logged at least one qualifying workout; the rest never finished a workout that met the filters below. Hardy users are people who chose a strength-tracking app and kept logging, so they are stronger and more consistent than the general gym population. **The app never collected bodyweight, age or sex**, so nothing here is a bodyweight-relative strength standard.

## Method and filters

- A workout counts if it lasted between 5 minutes and 6 hours.
- A set counts as finished if it has 1 to 50 logged reps. Weight is the precise logged weight in kilograms (imperial entries converted).
- Admin and official-content accounts are excluded.
- Progression analyses use lifters with at least 3 qualifying workouts and the built-in barbell bench press, squat, deadlift and overhead press exercises.
- Estimated 1RM (e1RM) is Epley, weight × (1 + reps / 30), on the best set of a session, using sets of 10 reps or fewer; sets implying more than 500 kg are dropped as entry errors.
- Plate milestones are 60/100/140/180 kg for metric users and 135/225/315/405 lb for imperial users. A milestone counts on the first session where that weight was lifted for at least one rep (an actual set, not an estimate).
- Time-to-milestone curves include only lifters who started below the milestone (best set in their first two weeks) and were still logging in the month shown, so stopping the app is not counted as failing. The long end of every curve is therefore survivor-biased.
- Starting tiers for milestones: `from_previous_plate` = best set in the first two weeks was at or above the previous plate; `from_below_previous_plate` = below it; `all` = both.
- Starting tiers for e1RM gain are the lifter's best e1RM in their first month of logging that lift, bucketed in kilograms.
- RPE is stored as 0 when not entered; RPE distributions use only sets where it was recorded (10.7% of finished sets, see `rpe_coverage`).
- Workout timestamps are UTC, so weekday and hour-of-day histograms are not local time.
- Any group with fewer than 50 lifters is suppressed at the source.

## File format

`strength-report-2026.csv` is a long-format table with six columns:

| Column | Meaning |
|---|---|
| `dataset` | Which table the row belongs to (values below) |
| `key1`, `key2`, `key3` | Dimension keys for that table; unused keys are empty |
| `metric` | Name of the measure |
| `value` | Number (shares are fractions 0 to 1, weights are kilograms) or text |

### `totals` (no keys)

`users_total`, `users_selected`, `users_qualified_3plus_sessions`, `sessions`, `sessions_qualified_users`, `finished_sets`, `finished_sets_weighted`, `total_tonnage_kg`, `first_session`, `last_session`, `distinct_exercises_logged`, `users_selected_metric`, `users_selected_imperial`, `lift_users_<lift>`.

Lift slugs used throughout: `bench-press`, `squat`, `deadlift`, `overhead-press`.

### `milestones`

Month-by-month time-to-milestone curves.

- `key1` lift slug
- `key2` `<plates>-plates/<startTier>`, plates 1 to 4, startTier `all`, `from_previous_plate` or `from_below_previous_plate` (1 plate has `all` only)
- `key3` months since the lifter's first logged session of that lift (1 up to 36, while at least 50 lifters were still observed)
- metrics: `observedUsers` (lifters started below the milestone and still logging that month), `reachedUsers`, `reachedShare` (= reachedUsers / observedUsers)

### `milestone-summary`

One row set per lift × milestone.

- `key1` lift slug, `key2` `<plates>-plates`
- metrics: `startedBelow`, `observed12m`, `reachedWithin12m`, `observed24m`, `reachedWithin24m`, `reachedEver`, `medianMonthsAmongReached`, `p25MonthsAmongReached`, `p75MonthsAmongReached`, `medianSessionsAmongReached`. The "among reached" medians are survivor statistics; the report only quotes them where `reachedEver` ≥ 50.

### `monthly-gain`

Change in best e1RM relative to the lifter's first month.

- `key1` lift slug
- `key2` starting tier in kg of e1RM: `0-40kg`, `40-60kg`, `60-100kg`, `100-140kg`, `140-180kg`, `180kg+`, or `all`
- `key3` month: 1, 3, 6, 12 or 24 (lifter must have a session in a window around that month)
- metrics: `n`, `medianGainKg`, `p25GainKg`, `p75GainKg`, `medianGainPct` (fraction), `meanGainKg`, `shareNoGain` (fraction with gain ≤ 0)

### `percentiles`

Best e1RM per lifter, across lifters with the lift in 3+ workouts.

- `key1` lift slug, `key2` units group: `all`, `metric`, `imperial`
- metrics: `users`, `e1rmP10Kg`, `e1rmP25Kg`, `e1rmP50Kg`, `e1rmP75Kg`, `e1rmP90Kg`, `e1rmP99Kg`, `bestSetP50Kg`, `bestSetP90Kg` (heaviest actual set), `shareSet60kgPlus`, `shareSet100kgPlus`, `shareSet140kgPlus`, `shareSet180kgPlus` (share of lifters who have lifted that weight for at least one rep; for imperial users the thresholds are 135/225/315/405 lb)

### `top-exercises`

Most logged built-in exercises.

- `key1` exercise name, `key2` exercise type (barbell, dumbbell, machine, bodyweight, ...)
- metrics: `sets`, `sessions`, `users`, `shareOfSets`, `medianKg`, `medianReps`

### `muscle-groups`

Sets by primary muscle group.

- `key1` muscle group
- metrics: `primarySets`, `shareOfPrimarySets`, `users`, `sessionsWithLowerBodyShare`, `lowerOnlySessionsShare`, `upperOnlySessionsShare`

### `session-stats` (no keys)

`sessions`, `duration_median_min` and `duration_p10/p25/p75/p90_min`, `sets_per_session_median/p25/p75`, `exercises_per_session_median`, `tonnage_per_session_median_kg`, `tonnage_per_session_p90_kg`, `sessions_per_active_week_median/mean`, `active_weeks_share_1` … `active_weeks_share_5plus` (share of a lifter's active weeks with that many workouts).

### `set-distributions`

- `key1` dimension: `reps` (buckets `1-3`, `4-5`, `6-8`, `9-12`, `13-20`, `21+`), `rest_time` (seconds buckets, where a rest timer was used), `rpe` (recorded RPE value), `rpe_coverage` (`has_rpe` / `no_rpe`)
- `key2` bucket
- metrics: `count` (sets), `share`

### `when`

- `key1` dimension: `weekday` (1 = Monday … 7 = Sunday, UTC), `hour` (0 to 23, UTC), `month` (calendar month 1 to 12), `year`
- `key2` bucket
- metrics: `sessions`, `share`

## Known limitations

1. Self-selected sample of app users; not a population estimate.
2. No bodyweight, age or sex.
3. Survivorship in every over-time curve: only lifters still logging are counted at each month.
4. e1RM is an estimate; the same estimator is applied to everyone, so comparisons hold better than absolute values.
5. UTC timestamps make hour-of-day uninformative.
6. Small groups (< 50 lifters) are suppressed, so some lift × milestone × tier combinations are absent.

## Changelog

- **2026 edition** (2026-09-03): first release. Queries in the Hardy repository under `server/scripts/strength-report/`.
