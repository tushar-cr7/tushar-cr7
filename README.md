<!--
  This profile is a drawing set. Every sheet is an SVG drawn by tools/draw.py
  from live GitHub + LeetCode data, re-issued daily by .github/workflows/reissue.yml.
-->

<a name="top"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/g-001-cover.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/g-001-cover.svg">
  <img width="100%" alt="Sheet G-001, cover. Tushar Joshi, engineer under construction. B.Tech CSE at SRM Institute of Science and Technology, class of 2028. Currently on site: REVORA, revenue recovery infrastructure where AI proposes and deterministic rules decide." src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/g-001-cover.svg">
</picture>

<p align="center">
  <b>Tushar Joshi</b> · B.Tech CSE, SRM IST · class of 2028 · open to backend / SWE internships, summer 2027 → <a href="#x-900">X-900</a><br>
  Building <a href="https://github.com/tushar-cr7/REVORA"><b>REVORA</b></a> — revenue recovery infrastructure where AI proposes and rules decide. <b>Under construction.</b><br>
  <sub>Every sheet below is drawn by code in this repo from live GitHub and LeetCode data — <a href="#how">how</a>.</sub>
</p>

<a name="g-000"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/g-000-index.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/g-000-index.svg">
  <img width="100%" alt="Sheet G-000: drawing index" src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/g-000-index.svg">
</picture>

| SHEET | TITLE | STATUS |
|:--|:--|:--|
| [`G‑002`](#g-002) | General notes — how I build | Issued |
| [`A‑101`](#a-101) | **REVORA** — section through the whole stack | **Under construction** |
| [`A‑102`](#a-102) | **REVORA** — one decision, end to end | **Under construction** |
| [`A‑103`](#a-103) | **REVORA** — punch list | 8 open items |
| [`S‑201`](#s-201) | Foundation plan — DSA, redrawn from LeetCode daily | Live |
| [`R‑301`](#r-301) | Stair section — how I got here | As-built |
| [`R‑302`](#r-302) | As-built register — every public project | As-built |
| [`X‑900`](#x-900) | Requests for information | Open |

<a name="g-002"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/g-002-notes.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/g-002-notes.svg">
  <img width="100%" alt="Sheet G-002: general notes" src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/g-002-notes.svg">
</picture>

| NO. | NOTE |
|:-:|:--|
| **1** | **AI MAY PROPOSE. ONLY RULES MAY APPROVE.**<br><sub>In REVORA a model ranks the options and one 113-line, ML-free file decides. It can downgrade what the AI asked for. It cannot expand it.</sub> |
| **2** | **A BLOCKED ACTION IS A RESULT. SHOW IT.**<br><sub>Blocked, escalated and suppressed outcomes get the same screen time as successes. Nothing is hardcoded to look like it worked.</sub> |
| **3** | **DOING NOTHING IS A DECISION. LOG IT.**<br><sub><code>suppress</code> is a first-class action with its own audit event. Sometimes the highest-value move is not messaging the customer at all.</sub> |
| **4** | **IF IT CAN'T BE COMPUTED, IT DOESN'T GET DRAWN.**<br><sub>Every number on these sheets comes from a repo, an API or a test run. The ones that can change redraw themselves.</sub> |
| **5** | **SHIP THE BORING PARTS.**<br><sub>Idempotency keys. Audit trails. Test suites. Installers. That's where software earns trust.</sub> |
| **6** | **READ THE FIELD. TAKE THE HIGHEST-VALUE OPTION. COMMIT.**<br><sub>I play striker / right winger. It's also, roughly, what a decision engine does.</sub> |

<a name="a-101"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/a-101-revora-section.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/a-101-revora-section.svg">
  <img width="100%" alt="Sheet A-101: REVORA drawn as a building section under construction. Built floors: product surfaces (Next.js 14, 12 app routes, 5 site pages), API (FastAPI, 17 endpoints), services, intelligence (XGBoost and an expected-value engine), on a foundation of six deterministic policy rules. Scaffolding: AI copilot. Not built: database, authentication, live payment connection. 22 backend tests passing." src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/a-101-revora-section.svg">
</picture>

<p align="center">
  <kbd>DETECT</kbd> → <kbd>DIAGNOSE</kbd> → <kbd>PREDICT</kbd> → <kbd>DECIDE</kbd> → <kbd>ACT</kbd> → <kbd>MEASURE</kbd> → <kbd>LEARN</kbd>
</p>

<p align="center">
  <b>REVORA</b> watches a merchant's payments for revenue that quietly leaks — a failed card, an abandoned checkout,<br>
  a failed renewal, an overdue invoice. It predicts what's recoverable, proposes the highest-value action,<br>
  and lets a deterministic policy layer have the final word. Every decision is audited.<br>
  <sub>Not launched: execution is simulated and every transaction is synthetic demo data.</sub><br><br>
  <a href="https://github.com/tushar-cr7/REVORA"><b>→ tushar-cr7/REVORA</b></a>
</p>

<a name="a-102"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/a-102-decision-path.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/a-102-decision-path.svg">
  <img width="100%" alt="Sheet A-102: one REVORA decision end to end. Detect the leak type, take a fixed subset of five candidate actions, score each by expected value using an XGBoost recovery probability, propose the highest. A deterministic policy gate with six rules either allows execution or downgrades to escalate or suppress. Every step is written to the audit log." src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/a-102-decision-path.svg">
</picture>

<p align="center"><sub>Violet is the model's proposal. The gate is <code>policy.py</code> — no ML, six rules, and the only code in the system allowed to say yes.</sub></p>

<a name="a-103"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/a-103-punch.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/a-103-punch.svg">
  <img width="100%" alt="Sheet A-103: REVORA punch list, eight open items" src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/a-103-punch.svg">
</picture>

| ITEM | OPEN ITEM | WHERE |
|:--|:--|:--|
| `P01` | **No database.** `InMemoryRepository` is the only store; every restart wipes state. A `PostgresRepository` behind the same interface isn't built yet. | `repositories/` |
| `P02` | **Payments are simulated.** `SimulationProvider` draws each outcome weighted by the action's scored probability. No live provider is connected. | `integrations/` |
| `P03` | **No authentication.** Single-tenant demo mode. | — |
| `P04` | **The copilot isn't an LLM.** Keyword routing and templates over pipeline data. | `recovery_service.py` |
| `P05` | **No server-side execution queue.** "Executing" only exists in the browser. | `interventionSignals.ts` |
| `P06` | `/api/opportunities` still returns already-executed transactions; the frontend dedupes them. | `routes.py` |
| `P07` | **Frontend has no automated tests.** The backend has 22. | `frontend/` |
| `P08` | The Revenue Command hero logs a console warning — an SVG `r` animated without an initial value. One-line fix, never in scope. | `RevenueFlowSystem.tsx` |

<p align="right"><sub><i>Renders hide their punch lists. Drawings don't.</i></sub></p>

<a name="s-201"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/s-201-foundation.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/s-201-foundation.svg">
  <img width="100%" alt="Sheet S-201: DSA foundation plan. One pile per accepted LeetCode problem, pile depth by difficulty, with a 90-day log of submissions per day. Redrawn daily from LeetCode's public API." src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/s-201-foundation.svg">
</picture>

<p align="center"><sub>Redrawn every day from LeetCode's public API. The count isn't the point — the pour log is.</sub></p>

<a name="r-301"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/r-301-stair.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/r-301-stair.svg">
  <img width="100%" alt="Sheet R-301: stair section of public work. Fundamentals, October to December 2025. Visualizers, February to May 2026. Shipped product DailyFlow, August 2026. Infrastructure: REVORA, September 2026 to now." src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/r-301-stair.svg">
</picture>

<a name="r-302"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/r-302-register.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/r-302-register.svg">
  <img width="100%" alt="Sheet R-302: as-built register" src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/r-302-register.svg">
</picture>

<details>
<summary><b>DailyFlow</b> &nbsp;<code>IN SERVICE</code>&nbsp; local-first desktop workspace, shipped with a Windows installer</summary>
<br>

```text
PURPOSE   plan · focus · finish · reflect — one workspace for the day
STACK     Electron 37 · React 19 · TypeScript · Vite · Tailwind · better-sqlite3
EVIDENCE  17 Vitest files · v.1.0.0 Windows installer (NSIS) · live site

renderer (React) ──► preload bridge ──► IPC handlers ×8 ──► repositories ×6 ──► SQLite
                                               └─► services: notification scheduler · data management
```

[repository](https://github.com/tushar-cr7/DailyFlow) · [live site](https://dailyflow-planner.vercel.app/) · [release](https://github.com/tushar-cr7/DailyFlow/releases)

</details>

<details>
<summary><b>A* Search Visualizer</b> &nbsp;<code>AS-BUILT</code>&nbsp; heuristic search you can watch</summary>
<br>

```text
PURPOSE   make f(n) = g(n) + h(n) visible, one node expansion at a time
BUILT     interactive grid · wall placement · step-by-step expansion · shortest path
REPO      README + an A3 explainer poster generated in Python (reportlab)
```

[live demo](https://a-star-algo-aii.netlify.app/) · [repository](https://github.com/tushar-cr7/A_star)

</details>

<details>
<summary><b>3D-Shearing</b> &nbsp;<code>AS-BUILT</code>&nbsp; computer graphics coursework as a website</summary>
<br>

```text
PURPOSE   Computer Graphics & Animation, taught as a site instead of a PDF
BUILT     interactive 3D shearing demo · syllabus organised by unit
REPO      documentation only — the site's source isn't in the repository
```

[live site](https://3d-shearing.netlify.app/) · [repository](https://github.com/tushar-cr7/3D-Shearing)

</details>

<details>
<summary><b>DSA-in-Cpp</b> &nbsp;<code>AS-BUILT</code>&nbsp; 21 data structures and algorithms, from scratch</summary>
<br>

```text
CONTENTS  arrays · singly / doubly / circular linked lists · stacks & queues (array + list)
          BST search / delete / traversals · BFS · DFS · bubble & selection sort
```

[repository](https://github.com/tushar-cr7/DSA-in-Cpp)

</details>

<details>
<summary><b>campus-apex</b> &nbsp;<code>AS-BUILT</code>&nbsp; Java student-records manager</summary>
<br>

```text
SYSTEM    console CRUD — add · view · search · update · delete, with GPA
DESIGN    Student · StudentManager · Main — an in-memory ArrayList as the store
```

[repository](https://github.com/tushar-cr7/campus-apex)

</details>

<sub><b>PRACTICE PIECES</b> &nbsp;·&nbsp; [Java-Finance-Tracker](https://github.com/tushar-cr7/Java-Finance-Tracker) · [PalindromeCheckerApp](https://github.com/tushar-cr7/PalindromeCheckerApp) · [Password-Manager-PY-](https://github.com/tushar-cr7/Password-Manager-PY-) · [DBMS-SQL-Practice](https://github.com/tushar-cr7/DBMS-SQL-Practice)</sub><br>
<sub><b>OFF THE PUBLIC RECORD</b> &nbsp;·&nbsp; FootballIQ (match analytics & prediction) and StadiumPro (stadium-management database) aren't public yet, so they don't get drawings. This set only draws what you can inspect.</sub>

<a name="x-900"></a><picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/x-900-rfi.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/x-900-rfi.svg">
  <img width="100%" alt="Sheet X-900: requests for information" src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/x-900-rfi.svg">
</picture>

| RFI | SUBJECT | ROUTE |
|:--|:--|:--|
| `001` | Backend / SWE internship — Summer 2027 | [tusharrjoshi2007@gmail.com](mailto:tusharrjoshi2007@gmail.com) |
| `002` | Work, collaboration, REVORA | [linkedin.com/in/tushar-joshi007](https://www.linkedin.com/in/tushar-joshi007/) |
| `003` | Problem solving | [leetcode.com/u/Tusharr_07](https://leetcode.com/u/Tusharr_07/) |
| `004` | Code — issues, ideas, review | [github.com/tushar-cr7](https://github.com/tushar-cr7) |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/zz-end-of-set.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/light/zz-end-of-set.svg">
  <img width="100%" alt="End of set. This revision is superseded by REVORA's next commit." src="https://raw.githubusercontent.com/tushar-cr7/tushar-cr7/main/drawings/dark/zz-end-of-set.svg">
</picture>

<a name="how"></a>
<details>
<summary><sub>how this set is drawn</sub></summary>
<br>

- Every sheet is an SVG drawn by [`tools/draw.py`](https://github.com/tushar-cr7/tushar-cr7/blob/main/tools/draw.py) — standard-library Python, no templates, no image services.
- [`reissue.yml`](https://github.com/tushar-cr7/tushar-cr7/blob/main/.github/workflows/reissue.yml) redraws the set daily from the GitHub REST API and LeetCode's public GraphQL endpoint, and commits only when the data changed.
- The **REV** in every title block is REVORA's public commit count. The profile revs when the product does.
- Dark theme prints blueprint. Light theme prints whiteprint. Switch your GitHub appearance.
- If a source is unreachable, the last verified data stays on the sheet. Nothing is estimated.

<p align="right"><a href="#top"><sub>↑ back to cover</sub></a></p>
</details>
