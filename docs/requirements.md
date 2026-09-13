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
| Liam Pheng, 21, developer> | Creator and developer of Acountabilibuddy | Accountabilibuddy to be a functional project to integrate for Military use | n/a |
| <Lionel Carapia, 21, Administrative/leadership user/Primary user> | c/Battalion Commander GEB 3BDE USACC "Leader in charge of all operations conducted at the battalion level and disseminating information and enforcing standards pushed out by Brigade level" | The ability to consolidate orders and information in one place | <09-04-2026 / "Definitely, right now the spreadsheets are all over the place and if we could put them in the same place and have the ability to check off as we go would be huge" / /docs/interviews/<09-04-2026>-<LC HS EH>.md> |
| <Jack Malenock, 20, Administrative/leadership user/Primary user> | c/Squad Leader 1SQD 2PLT A CO GEB 3BDE USACC "In command of a squad and responsible for deseminating information pushed down from higher echelons of command" | Chain of Command restrictions on who users are allowed to contact based off of rank and status | <09-09-2026 / "I would like to see a feature where chain of command is enforced and joe's (regular soldiers/privates) are unable to skip myself in the chain of command and directly talk to the PL or PSG."  / /docs/interviews/<09-09-2026-JM.pdf> |
| <Moucheng (Thomas) Yang, 20, Non leadership user/ recipient of information/ end user > | GRN 1SQD 1PLT B CO GEB 3BDE USACC "Standard line infantry soldier responsible for carrying out the orders pushed down to him" | The ability to communicate with squad leader and track upcoming squad events | <09-09-2026 / "Develop something with chat communication and event tracking" / /docs/interviews/<09-09-2026-TY.pdf> |
| <Hunter Szymborski, 21, Administrative User/Primary user> | c/Battalion S3 Operations Support Officer GEB 3BDE USACC "In charge of pushing out weekly and monthly Operations Orders to maintain unit productivity" | Have accountability trackers integrated with calendar function | <09-04-2026 / "That would definitely be a huge bonus, being able to have an accountability tracker in the same place" / /docs/interviews/<09-04-2026>-<LC HS EH>.md> |
| <Estella Hageman, 21, Administrative User/Primary user> | c/Battalion Executive Officer GEB 3BDE USACC "In charge of training and coordinating battalion events" | Ability to create calendar events viewable to the entire battalion | <09-04-2026 / "I think that would be very helpful especially because we have a million different trackers and accountability lists all over the sharepoint. If we could consolidate PT accountability trackers and Lab accountability we would be much more organized." / /docs/interviews/<09-04-2026>-<LC HS EH>.md> |
| Next Maintainer, N/A , Maintainer> | Clones the repository in Week 17 knowing nothing | To understand what every feature was for, from the document alone | Chapter 3 Capstone Textbook Section 3.2 Figure |
| <Dr. Litman, IDK, Capstone Grader> | Evaluator of Capstone Project | Acountabilibuddy to be a functional project for grading at the end of the 16 hour course. | <n/a / Project needs to be completed in 16 weeks and 240 hours / Course Syllabus> |

## 3. Definitions

Define every term your requirements use in a project-specific sense. If a reader
could interpret a word two ways, it belongs here.

| **Term** | **Definition in this document** |
|---|---
| User | Someone who uses Acountabilibuddy and has created an account |
| Unit | A military group of soldiers ranging from the smallest team (4 people) to a battalion Brigade (3,000-5,000 people) |
| Echelon | another fancy word for unit |
| Team | 4 person unit |
| Squad | Unit Made up of 2 Teams and is 9 people total (2 teams plus a squad leader) |
| Platoon | Unit Made up of 4 Squads and is around 40 Personnel |
| Company | Unit Made up of 3-4 Platoons and is around 200 Personnel (platoons plus staff) |
| Battalion | Unit Made up of 3-5 Companies and is around 1,000 Personnel |
| Brigade | Unit Made up of 3-6 Battalions and is around 3,000-5,000 Personnel |
| Privilege | The ability to make changes within the application |
| Leadership User | a user with set permissions to send out information, create calendar events, and manage unit communication groups within Accountabilibuddy |
| Standard User | a user without administrative/leadership privileges to send out public information, create calendar events, or manage unit comms |
| Role & Rank | The position a user has within the unit hierarchy. Role is a position someone holds while rank is the status they require to hold that position |
| Chain of Command | The system that the Military uses to pass information up and down the different units. Uses leaders at each unit level to send information from their bosses/leaders to their subordinates |
| Accountability | The ability to track if users are required to be at certain events and have an attendance tracker for those said events |
| FRAGO | Short for "Fragmentary Order which basically means an announcement of change to orders pushed out |
| OPORD | Short for "Operations Order" which is the information and orders for events happening throughout a period of time. Gives information and specifics on what a unit will be doing throughout a time period. Can be published daily, weekly, or monthly depending on need |
| Unit Chat | A group chat that a military unit will utilize to communicate between itself |
| Event | Any significant operation or procedure a unit will be doing on a specific day at a specific time |
| Backbrief | A question or quiz that a unit leader will give to his subordinates to ensure that they are understanding the information given to them |


## 4. Assumptions and Dependencies

- **Assumption:** Accountabilibuddy can be completed as a web application — *If false:* a lot of additionall time will be required to switch project over to mobile app development
- **Assumption:** Users will have access and connection to the internet to access the Web app of Acountabilibuddy — *If false:* Users will not have the ability to load the database, messages, or any accountability information
- **Assumption:** Each user will have unique login credentials — *If false:* Acountabilibuddy will have a hard time differentiating between users with the same credentials and cause database synchronization and privacy issues
- **Dependency:** MongoDB — *If unavailable:* Use a local MongoDB instance or another compatible database solution
- **Dependency:** Render — *If unavailable:* Deploy the application to another supported hosting service or run it locally for development and testing
- **Dependency:** GitHub — *If unavailable:* Use another Git hosting service or maintain a local Git repository

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
| **Native Android application** | The capstone is limited to a web application to control development time | A future project has sufficient time for mobile development |
| **Native iOS application** | Developing a second native platform would increase development and testing requirements | A future project has sufficient time and resources |
| **Emergency communications** | Emergency communication requires reliability and availability beyond the scope of this capstone | A future system specifically designed and tested for emergency use |
| **Microsoft Teams integration** | External integrations would increase development and dependency risk | If a future version requires integration and an accessible API is available |
| **Signal integration** | The project does not require external messaging-platform integration | If a future version establishes a supported integration method |
| **GroupMe integration** | External platform integration is outside the current project scope | If a future version requires it and an appropriate API is available |
| **SMS/text notifications** | External messaging adds additional dependencies and costs | If user testing demonstrates that notifications are necessary |
| **Voice calling** | Voice communication is not required to demonstrate the core problem or solution | If communication requirements expand in a future release |
| **Video calling** | Video communication is not required for the core accountability workflow | If required by future users |
| **GPS/location tracking** | Location tracking is unrelated to the core communication and accountability problem | Only if a future project establishes a legitimate requirement for it |
| **Social networking features** | Social features do not contribute directly to the project's core communication and accountability goals | If a future release identifies a specific requirement for them |
| **Single Sign-On** | Implementing SSO would add additional authentication and integration requirements | If the application is later integrated with an approved organizational identity provider |


## 8. Open Questions

| # | Question | Who can answer it | Needed by |
|---|---|---|---|
| 1 | What specific leadership roles should be able to create and manage events? | Interviewed military leadership users | Week 4 |
| 2 | What information should be required when creating a unit event? | Leadership users | Week 4 |
| 3 | Should event accountability require a simple acknowledgement, or should users select a response such as attending/not attending? | Leadership and end users | Week 4 |
| 4 | What file types should be supported as event attachments? | Leadership users | Week 4 |
| 5 | What minimum information should appear on the leadership accountability dashboard? | Leadership users | Week 4 |


## 9. Document Change Log

| Date | Version | Change | Reason |
|---|---|---|---|
| <YYYY-MM-DD> | 1.0 | Initial specification | Milestone 3 |
