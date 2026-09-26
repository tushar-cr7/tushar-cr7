<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=Tushar%20Joshi&fontSize=64&fontColor=fff&animation=twinkling&fontAlignY=36&desc=CS%20Undergraduate%20%E2%80%A2%20Software%20Developer%20%E2%80%A2%20Product%20Builder&descAlignY=58&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=900&color=58A6FF&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=60&lines=Building+REVORA+%E2%80%94+revenue+recovery+infrastructure;Building+software%2C+solving+problems%2C+shipping+products." />

<p>
  <a href="https://github.com/tushar-cr7">
    <img src="https://komarev.com/ghpvc/?username=tushar-cr7&label=Profile%20Views&color=58A6FF&style=for-the-badge" alt="Profile Views"/>
  </a>
  <a href="https://leetcode.com/u/Tusharr_07/">
    <img src="https://img.shields.io/badge/LeetCode-125%2B%20Solved-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"/>
  </a>
  <img src="https://img.shields.io/badge/Open%20To-SWE%20Internships%20Summer%202027-brightgreen?style=for-the-badge" alt="open to work"/>
</p>

</div>

---

### About Me

- 🎓 B.Tech CSE undergraduate at **SRM Institute of Science and Technology**, Chennai, India — expected graduation **2028**
- 🛠️ Focused on backend engineering, systems architecture, and turning ideas into shippable products — not just finishing tutorials
- 📈 Currently deep in DSA (C++) and building **REVORA**, a revenue-recovery infrastructure product, from the ground up
- 🎯 Targeting a **Software Engineering internship for Summer 2027**
- ⚽ Off the keyboard: plays Striker / Right Winger — *read the field, make the decision, execute* applies to both football and engineering

---

### 🚀 REVORA — Major Product

**Under Construction**

`ACTIVE DEVELOPMENT` · `BUILDING IN PUBLIC` · `MORE COMING SOON`

REVORA is my primary product build right now — revenue recovery infrastructure for merchants losing money to failed payments, abandoned checkouts, failed subscription renewals, and overdue invoices. It's not a finished product; it's the one I'm spending the most engineering effort on.

> **AI FOR INTELLIGENCE. RULES FOR CONTROL.**
>
> The core idea: AI can detect patterns, predict recovery probability, and recommend an action — but it can never authorize money movement on its own. A separate, deterministic policy layer is the only thing allowed to approve, downgrade, or block an action. That split between "AI recommends" and "rules decide" is the whole point of the project.

**The loop it runs on every at-risk transaction:**

\`\`\`
DETECT → DIAGNOSE → PREDICT → DECIDE → ACT → MEASURE → LEARN
\`\`\`

**What's actually built so far:**

- A FastAPI backend implementing the full pipeline above, with a real test suite (22 passing tests) covering the decision engine, policy engine, and API
- A trained **XGBoost** model producing an actual recovery-probability score per transaction — not a stub
- A deterministic policy engine that independently blocks, downgrades, or reroutes proposed actions based on merchant-defined limits (retry limits, cooldowns, contact limits, a value ceiling for autonomous recovery, escalation age thresholds)
- A full **Next.js** dashboard — Revenue Command, Revenue Scanner, Recovery Brain, Transactions, Interventions, Recovery Controls, Escalations, Audit Trail, Analytics, Integrations, Settings, and an AI Copilot panel — each wired to real API data, not mocked screens
- A structured, independently queryable audit trail for every decision and executed action

**Honestly, what's still simulated / in progress** (because "no fake functionality" matters to me even in my own README):

- Payment execution currently runs through a simulation provider, not a live payment gateway
- The AI Copilot is currently deterministic template logic over real pipeline data — no live LLM call wired in yet
- Storage is in-memory only — no persistent database yet
- No auth layer yet — single-tenant demo mode

**Stack:** FastAPI · Python · XGBoost · Next.js · React · TypeScript · Tailwind CSS

**Repository:** [github.com/tushar-cr7/REVORA](https://github.com/tushar-cr7/REVORA)

---

### 🔧 Current Builds

Projects I'm actively working on right now, in order of where my time goes.

| Project | What it is | Status |
|---|---|---|
| **[REVORA](https://github.com/tushar-cr7/REVORA)** | Revenue recovery infrastructure — AI-scored decisions gated by a deterministic policy engine | 🟡 Active development |
| **[DailyFlow](https://github.com/tushar-cr7/DailyFlow)** | Local-first Windows productivity desktop app — task planning, focus mode, streaks, analytics | 🟢 Shipping ([live site](https://dailyflow-planner.vercel.app/)) |

---

### 🧠 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

**🌊 DailyFlow**

Local-first Windows desktop productivity app for daily task planning, scheduling, focus sessions, and progress tracking, with Windows-startup integration.

`Electron` `React` `TypeScript` `SQLite` `Vite` `Tailwind CSS`

🔗 [Repository](https://github.com/tushar-cr7/DailyFlow) · 🌐 [Live Site](https://dailyflow-planner.vercel.app/)

</td>
<td width="50%" valign="top">

**🧭 A\* Pathfinding**

An AI search tool that finds the shortest path between two points at minimal cost using the A* heuristic search algorithm.

`Python`

🔗 [Repository](https://github.com/tushar-cr7/A_star)

</td>
</tr>
<tr>
<td width="50%" valign="top">

**🎓 Campus-Apex**

Java-based student database management system with CRUD operations, GPA tracking, and persistent record storage.

`Java`

🔗 [Repository](https://github.com/tushar-cr7/campus-apex)

</td>
<td width="50%" valign="top">

**📐 3D-Shearing**

A computer graphics and animation project implementing 3D shearing transformations interactively in the browser.

`HTML` `CSS` `JavaScript`

🔗 [Repository](https://github.com/tushar-cr7/3D-Shearing)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

**📚 DSA-in-Cpp**

My working set of data structures and algorithms implementations in C++ — the same practice that backs my LeetCode progress below.

`C++`

🔗 [Repository](https://github.com/tushar-cr7/DSA-in-Cpp)

</td>
</tr>
</table>

---

### 🛠️ Tech Stack

Technologies I've actually shipped code with, not an aspirational list.

**Languages**

![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**Frontend / Desktop**

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Electron](https://img.shields.io/badge/Electron-191970?style=for-the-badge&logo=electron&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)

**Backend / ML**

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-0E7C7B?style=for-the-badge)

**Data & Tools**

![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

---

### 📊 DSA / LeetCode

Building consistency through daily problem-solving, primarily in C++.

- **125+** problems solved
- **50+** day active streak
- Current focus: arrays & strings, hashing, two pointers, binary search, trees & graphs, dynamic programming

🔗 [LeetCode Profile →](https://leetcode.com/u/Tusharr_07/)

---

### 🧩 Engineering Interests

Data Structures & Algorithms · Backend Engineering · Database Design · Full-Stack & Desktop Development · System Design Fundamentals

What I care about right now isn't collecting more small projects — it's understanding architecture well enough to build something like REVORA end-to-end: real ML-driven decisions, a real safety layer, and a real audit trail, not just a UI on top of a database.

---

### 📈 GitHub Activity

<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=tushar-cr7&show_icons=true&theme=github_dark&hide_border=true&count_private=true" width="48%"/>
<img src="https://github-readme-streak-stats.herokuapp.com/?user=tushar-cr7&theme=github-dark&hide_border=true" width="48%"/>
</div>

<div align="center">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=tushar-cr7&layout=compact&theme=github_dark&hide_border=true" width="60%"/>
</div>

---

### 🤝 Connect With Me

<div align="center">

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tusharrjoshi2007@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tushar-cr7)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Tusharr_07/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tushar-joshi007/)

</div>

<p align="center"><sub>Building software that solves real problems — one commit at a time.</sub></p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=90&section=footer" width="100%"/>
