<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:080B12,100:131A26&height=90&section=header" width="100%"/>

</div>

<div align="center">

```
$ whoami
```

**Tushar Joshi** — B.Tech CSE, SRM Institute of Science and Technology · Class of 2028

<sub>Chennai, India — DSA Club & International Student Chapter, leadership roles</sub>

<img src="https://komarev.com/ghpvc/?username=tushar-cr7&label=PROFILE+VIEWS&color=4F6EF7&style=flat-square" alt="profile views"/>
<img src="https://img.shields.io/badge/LEETCODE-125%2B%20SOLVED-4F6EF7?style=flat-square&logo=leetcode&logoColor=white" alt="leetcode"/>
<img src="https://img.shields.io/badge/STREAK-50%2B%20DAYS-4F6EF7?style=flat-square" alt="streak"/>
<img src="https://img.shields.io/badge/OPEN%20TO-SWE%20INTERNSHIPS-10B981?style=flat-square" alt="open to work"/>

</div>

<br/>

> Most people building with AI right now are optimizing for what it can do.
> I spend most of my time on what it should never be allowed to do.

I don't build projects to fill a contribution graph. I build systems, then
spend the second half of the work deciding what the system is **not**
allowed to do on its own. That second half is usually the part nobody
shows — so it's the part this profile leads with.

<br/>

<div align="center">

## 01 — WHAT I'M BUILDING RIGHT NOW

</div>

<div align="center">
<img src="https://img.shields.io/badge/STATUS-UNDER%20CONSTRUCTION-F5A623?style=flat-square" alt="status"/>
<img src="https://img.shields.io/github/last-commit/tushar-cr7/REVORA?style=flat-square&label=LAST%20COMMIT&color=4F6EF7" alt="last commit"/>
<img src="https://img.shields.io/badge/BACKEND-FastAPI%20%2B%20XGBoost-4F6EF7?style=flat-square" alt="backend"/>
<img src="https://img.shields.io/badge/FRONTEND-Next.js%2014-4F6EF7?style=flat-square" alt="frontend"/>
</div>

<h3 align="center">REVORA</h3>
<p align="center"><i>Revenue Recovery Infrastructure</i></p>
<p align="center"><strong>Recover more revenue. Automatically. Safely.</strong></p>

REVORA is the biggest thing I'm building — a system that watches a
merchant's payments for revenue quietly leaking out (a failed card, an
abandoned checkout, a failed subscription renewal, an overdue invoice),
and runs one loop over every leak it finds:

```
  DETECT  →  DIAGNOSE  →  PREDICT  →  DECIDE  →  ACT  →  MEASURE  →  LEARN
```

The interesting engineering problem isn't the recovery actions themselves
— a retry, a payment link, a reminder are not novel. The problem is:
**how much do you let an AI decide on its own before a human has to sign
off?** REVORA's answer is architectural, not a policy document:

```
                 ┌─────────────────────────┐
                 │       TRANSACTION        │
                 │    fails / stalls        │
                 └────────────┬────────────┘
                              │
                 ┌────────────▼────────────┐
                 │         AI LAYER         │   proposes — never executes
                 │  predicts P(recovery),   │
                 │  scores retry / link /   │
                 │  reminder / escalate /   │
                 │  suppress by expected    │
                 │  value                   │
                 └────────────┬────────────┘
                              │ highest-EV candidate
                 ┌────────────▼────────────┐
                 │      POLICY LAYER        │   deterministic — cannot be
                 │  retries ≤ 2              │   overridden by the AI
                 │  cooldown ≥ 6h            │
                 │  contacts ≤ 1 / day       │
                 │  autonomy ceiling ₹25,000 │
                 └──────┬─────────────┬─────┘
                  allow │             │ block / downgrade / escalate
                        ▼             ▼
                  EXECUTE        ROUTE TO HUMAN
                        │             │
                        └──────┬──────┘
                               ▼
                       AUDIT TRAIL — always
```

<div align="center">
<img src="https://img.shields.io/badge/AI-proposes-8B5CF6?style=flat-square" alt="ai proposes"/>
<img src="https://img.shields.io/badge/POLICY-decides-F5484F?style=flat-square" alt="policy decides"/>
<img src="https://img.shields.io/badge/EVERY%20ACTION-audited-10B981?style=flat-square" alt="audited"/>
</div>

That split — AI for intelligence, rules for control — is the entire trust
claim of the product. It shows up in the backend architecture, the API
contract, and every screen of the dashboard.

REVORA also doesn't let its own AI fake a result: a blocked action is
shown as blocked, a failed recovery is shown as failed, and nothing is
hardcoded to look like a success. This README holds itself to the same
rule about the project below.

<details>
<summary><b>▸ expand: what's actually real vs. simulated right now</b></summary>
<br/>

```
REAL AND RUNNING
  [x] FastAPI backend running the full detect → learn pipeline
  [x] XGBoost model scoring real P(recovery) per transaction
  [x] Deterministic policy engine — actually blocks / downgrades / reroutes
  [x] 22 passing tests — decision engine, policy engine, executor,
      full pipeline, API (pytest, 5 suites)
  [x] Full Next.js dashboard wired to live backend data, 12 routes
  [x] Idempotency-key protected execution + structured audit log

SIMULATED — NOT REAL YET
  [ ] Payment execution — SimulationProvider draws a weighted random
      outcome, does not call Razorpay or any live payment API
  [ ] AI Copilot — deterministic string-matching + templating today,
      not an LLM call
  [ ] Persistence — in-memory only, resets on backend restart
  [ ] Auth — none, single-tenant demo mode
```

</details>

<div align="center">

**[→ EXPLORE THE REPOSITORY](https://github.com/tushar-cr7/REVORA)**

</div>

<br/>

<div align="center">

## 02 — BUILD QUEUE

<sub>everything else currently running, shipped, or in the lab</sub>

</div>

```
[ 01 ]  DailyFlow                                          STATE: SHIPPED
         problem  → daily planning fragmented across five different apps
         system   → local-first Windows desktop workspace — planning,
                     focus sessions, streaks/XP, reflection
         stack    → Electron · React · TypeScript · SQLite
         →  github.com/tushar-cr7/DailyFlow
         →  dailyflow-planner.vercel.app

[ 02 ]  A* Pathfinding                                      STATE: COMPLETE
         problem  → search algorithms are easy to describe, hard to see
         system   → interactive grid visualizer for A*, live heuristic
                     exploration, obstacle placement
         stack    → HTML · CSS · JavaScript
         →  github.com/tushar-cr7/A_star

[ 03 ]  Campus-Apex                                         STATE: COMPLETE
         problem  → student records scattered across spreadsheets
         system   → Java CRUD system — GPA tracking, persistent storage
         stack    → Java
         →  github.com/tushar-cr7/campus-apex

[ 04 ]  DSA-in-Cpp                                          STATE: GROWING
         problem  → interview-grade problem solving needs a real log,
                     not a folder of one-off files
         system   → structured DSA implementations, organized by topic
         stack    → C++
         →  github.com/tushar-cr7/DSA-in-Cpp

[ 05 ]  3D-Shearing                                         STATE: COMPLETE
         problem  → geometric transforms are abstract until you can
                     drag them
         system   → in-browser demo of 3D shearing transformations
         stack    → HTML · CSS · JavaScript
         →  github.com/tushar-cr7/3D-Shearing

[ 06 ]  FootballIQ                                          STATE: IN THE LAB
         problem  → match outcomes get predicted on vibes, not validation
         system   → multi-paradigm analytics engine — walk-forward
                     validation, calibration metrics, experiment tracking
         stack    → FastAPI · Next.js · PostgreSQL · XGBoost / LightGBM
         →  not yet public

[ 07 ]  StadiumPro                                          STATE: IN THE LAB
         problem  → stadium operations run on spreadsheets, not systems
         system   → stadium management system — stored procedures,
                     triggers, normalized schema, transactions
         stack    → Java · MySQL · PL/SQL
         →  not yet public
```

<br/>

<div align="center">

## 03 — STACK REGISTRY

</div>

<div align="center">

`languages`
<br/>
<img src="https://img.shields.io/badge/C++-4F6EF7?style=flat-square&logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/Java-4F6EF7?style=flat-square&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-4F6EF7?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/TypeScript-4F6EF7?style=flat-square&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-4F6EF7?style=flat-square&logo=javascript&logoColor=white"/>
<img src="https://img.shields.io/badge/SQL-4F6EF7?style=flat-square&logo=postgresql&logoColor=white"/>

`systems & frameworks`
<br/>
<img src="https://img.shields.io/badge/FastAPI-131A26?style=flat-square&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Next.js-131A26?style=flat-square&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/React-131A26?style=flat-square&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/Electron-131A26?style=flat-square&logo=electron&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-131A26?style=flat-square&logoColor=white"/>
<img src="https://img.shields.io/badge/TailwindCSS-131A26?style=flat-square&logo=tailwindcss&logoColor=white"/>

`data & tools`
<br/>
<img src="https://img.shields.io/badge/PostgreSQL-0F141F?style=flat-square&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-0F141F?style=flat-square&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-0F141F?style=flat-square&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-0F141F?style=flat-square&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/VS%20Code-0F141F?style=flat-square&logo=visualstudiocode&logoColor=white"/>

</div>

<br/>

<div align="center">

## 04 — DSA LEDGER

</div>

```
$ solved --lang cpp
> 125+ problems cleared
> 50+ day active streak
> consistency over sprints
```

<div align="center">

**[→ leetcode.com/u/Tusharr_07](https://leetcode.com/u/Tusharr_07/)**

</div>

<br/>

<div align="center">

## 05 — LIVE TELEMETRY

</div>

<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=tushar-cr7&show_icons=true&theme=github_dark&hide_border=true&bg_color=00000000&title_color=4F6EF7&icon_color=4F6EF7" width="49%"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=tushar-cr7&layout=compact&theme=github_dark&hide_border=true&bg_color=00000000&title_color=4F6EF7" width="38%"/>
</div>

<br/>

<div align="center">

## 06 — OFF THE PITCH

</div>

<p align="center">
I play Striker / Right Winger. The same read applies on the pitch and in
a codebase: <b>see the pattern before it fully forms, commit to a decision,
execute it cleanly</b> — and know when the right move is to not take the
shot.
</p>

<br/>

<div align="center">

## CONNECT

</div>

```
$ tail -f engineering.log
> shipping REVORA — recovery infrastructure, in active development
> open to backend / SWE internships, summer 2027
> the log continues in the commits
```

<div align="center">

[![Email](https://img.shields.io/badge/EMAIL-131A26?style=flat-square&logo=gmail&logoColor=white)](mailto:tusharrjoshi2007@gmail.com)
[![GitHub](https://img.shields.io/badge/GITHUB-131A26?style=flat-square&logo=github&logoColor=white)](https://github.com/tushar-cr7)
[![LeetCode](https://img.shields.io/badge/LEETCODE-131A26?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/u/Tusharr_07/)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-131A26?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tushar-joshi007/)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:131A26,100:080B12&height=90&section=footer" width="100%"/>
