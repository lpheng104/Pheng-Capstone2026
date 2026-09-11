# Software Requirements Specification — Acountabilibuddy

<!--
COPY THIS FILE into your repository as docs/requirements.md and delete every
comment block as you fill it in. Keep the section numbering; the Week-16 rubric
and the Week-4 traceability matrix both key off it.
Requirement IDs are FR-<AREA>-<nn>. Assign an ID once and never reuse it.
Retire an ID by marking it Withdrawn; do not renumber.
-->

**Author:** Liam Pheng  **Version:** 1.0  **Date:** <2026-09-09>
**Status:** Draft <!--| In review | Baselined -->

---

## 1. Purpose and Scope

**One paragraph:** Acountabilibuddy is a communication web application with a focus in military accountability and chain of command communication. The idea is to create an application where information will be pushed out to military members via a structured and enforced chain of command system. Additionally, Accountabilibuddy will feature a calendar event system where all members of a military unit can see what events are upcoming and the accountability information for the events. Accountabilibuddy was designed specifically for military service members to address the problems of non standardization communication across the military. The biggest problem Acountabilibuddy will resolve is the military's lack of a consolidated app for information and regulatory orders.       

**One paragraph:** Although Acountabilibuddy at release will be a web application with many different features included (the ability create an account, log in, create group chats, text, and calendar functions), Acountabilibuddy version 1.0 will not be a mobile app and will not have a variety of features simply due to the strict 240 hour limit confining the scope of the project. Some major features that will be outside the 240 hour scope are; Single Sign-on verification systems, synchronization with email and text notifications, User location/GPS tracking, social networking or social media features (i.e will not be an instagram or facebook), video and voice calling, or synchronization or integration with other well known communication apps (i.e Microsoft Teams, Signal, GroupMe, etc.). While features like video calling and voice chatting would be convenient and fit within the application, the 240 hour scope deem them unecessary additional addons for future Accountabilibuddy releases/versions. 

## 2. Stakeholders and Personas

| Persona | Who they are | What they need from the system | Evidence they exist |
|---|---|---|---|
| Liam Pheng, 21, Maintainer/develoepr> | Creator and developer of Acountabilibuddy | Accountabilibuddy to be a functional project to integrate for Military use | n/a |
| <Lionel Carapia, 21, Administrative/leadership user/Primary user> | c/Battalion Commander GEB 3BDE USACC | The ability to consolidate orders and information in one place | <09-04-2026 / "Definitely, right now the spreadsheets are all over the place and if we could put them in the same place and have the ability to check off as we go would be huge" / /docs/interviews/<09-04-2026>-<LC HS EH>.md> |
| <Jack Malenock, 20, Administrative/leadership user/Primary user> | c/Squad Leader 1SQD 2PLT A CO GEB 3BDE USACC | Chain of Command restrictions on who users are allowed to contact based off of rank and status | <09-09-2026 / "I would like to see a feature where chain of command is enforced and joe's (regular soldiers/privates) are unable to skip myself in the chain of command and directly talk to the PL or PSG."  / /docs/interviews/<09-09-2026>-<JM>.md> |
| <Moucheng (Thomas) Yang, 20, Non leadership user/ recipient of information/ end user > | GRN 1SQD 1PLT B CO GEB 3BDE USACC | The ability to communicate with squad leader and track upcoming squad events | <09-09-2026 / "Develop something with chat communication and event tracking" / /docs/interviews/<09-09-2026>-<TY>.md> |
| <name, age, role> | <one sentence> | <one sentence> | <interview date / observation / artifact> |
| <name, age, role> | <one sentence> | <one sentence> | <interview date / observation / artifact> |
| <name, age, role> | <one sentence> | <one sentence> | <interview date / observation / artifact> |

Include the maintainer who inherits this repository. They are a stakeholder.

## 3. Definitions

Define every term your requirements use in a project-specific sense. If a reader
could interpret a word two ways, it belongs here.

| Term | Definition in this document |
|---|---|

## 4. Assumptions and Dependencies

- **Assumption:** <something you are taking as true without proof> — *If false:* <consequence>
- **Dependency:** <an external service, dataset, device, or person you rely on> — *If unavailable:* <fallback>

## 5. Functional Requirements

<!-- Repeat this block for every requirement. Group by area. -->

### FR-<AREA>-<nn> — <short imperative name>

**Priority:** Must | Should | Could | Won't (this release)
**Requirement:** <Actor> shall be able to <action> <object> <under what condition>.
**Rationale:** Why this exists, and which persona asked for it.
**Acceptance criteria:**
- Given <starting state>, when <the actor does this>, then <this observable thing is true>.
- Given <edge or failure case>, when <trigger>, then <defined behavior>.

**Source:** <interview, observation, regulation, your own decision — name it>

## 6. Non-Functional Requirements

Placeholder for Week 4. Do not write vague quality words here now; write nothing
and fill it in when you can make each one measurable.

## 7. Out of Scope (the Won't-Have List)

Things a reasonable reader might expect and will not get in this release, each
with one line of reasoning. A short list here means you have not thought hard enough.

| Not building | Why not | Revisit when |
|---|---|---|

## 8. Open Questions

| # | Question | Who can answer it | Needed by |
|---|---|---|---|

## 9. Document Change Log

| Date | Version | Change | Reason |
|---|---|---|---|
| <YYYY-MM-DD> | 1.0 | Initial specification | Milestone 3 |
