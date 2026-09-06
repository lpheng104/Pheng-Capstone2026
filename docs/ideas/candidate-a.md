# Idea Canvas — Candidate <A>

Copy this file once per candidate into your repository as `docs/ideas/candidate-a.md`
(then `-b`, `-c`). Fill every field. A blank field is an answer: it means you do not
know yet, and that is exactly what this page is for. Delete the bracketed guidance
as you go.

**Candidate name:** <Acountabilibuddy>
**Date started:** <2026-08-31>   **Well it came from:** <Military Experience working under Army Reserves, USACC, and Army ROTC>

---

## 1. Problem statement

Concept Summary: A military communication web app that will be used to push out important information, track upcoming events, and allow leaders and soldiers to communicate through a standardized military unit application. 
| Category | Description | Specific Example |
|---|---|---|
| **Software Type** | Web Application | |
| **For** | Leaders within military units, including Team Leaders, Squad Leaders, Platoon Leaders, Company Commanders, and Battalion Commanders. | 2LT Joe Snuffy, a new Infantry Platoon Leader, needs to push information to his subordinate leaders, such as squad and team leaders. |
| **Who** | Information and orders are not always distributed through the same platform while soldiers are in garrison, and there is no single standardized communication application. | 2LT Joe Snuffy needs to distribute a Platoon OPORD, but his unit is using several communication channels, including Microsoft Teams, Signal, GroupMe, and text messaging. Joe Snuffy and his PSG, SFC John Smith, must determine which platform should be used to distribute the information. |
| **The Problem Is** | There is no standardized communication application specifically designed around military unit communication and accountability. This can cause confusion and missed messages, potentially resulting in soldiers missing events, arriving at the wrong time, wearing the wrong uniform, or failing to bring the required equipment. Information and accountability data can also become scattered across multiple applications rather than being maintained in one centralized location. | 2LT Joe Snuffy would say that not having a set standardized application, specifically built with a focus on inter military communication. This issue causes confusion and missed messages across 2LT Snuffy's platoon, leading to soldiers missing events or not bringing the correct equipment. Also not having a singular method of communication leads to missed information in some apps and a non consolidated location of information and accountability tracking |
| **Which Costs** | 1-2 additional hours of repeating information across different applications and providing verbal reminders takes additional time. | Joe Snuffy may spend approximately one hour per week rewriting or resending information and checking whether personnel received it. Using several communication applications can also result in outdated or conflicting information, which creates additional time costs when leaders have to clarify or correct information. |
| **Today They** | Military units typically designate one or more existing communication applications for distributing information while in garrison. | 2LT Joe Snuffy's unit: Alpha Company, 2nd Platoon, may decide to use GroupMe as its primary platform for distributing information to platoon leaders and members. |
| **Which Falls Short Because** | Standardization can differ between units and organizational levels, causing information to exist across multiple applications and group chats. | 2LT Joe Snuffy may use GroupMe to communicate with his platoon, while his Company Commander uses Microsoft Teams to communicate with the company, and 2LT Snuffy's squad leaders use Signal Chat for their squads. As a result, information, tasks, and accountability data can become distributed across multiple applications, increasing the possibility of missed, outdated, or conflicting information. |

## 2. Evidence a user exists

- **Person spoken to:** <c/LTC Lionel Carapia, c/MAJ Hunter Szymorsi, c/MAJ Estella Hageman>
- **Date and length:** <2026-09-04, 30 minutes>
- **Three verbatim quotes:**
  1. "<The non uniformity of communication in units is a prevalent issue I've seen throughout all units I've been a part of (c/LTC Lionel Carapia)>"
  2. "<Not having a standard app has made pushing out information from the S3 (operations) shop a lot more difficult because we are unaware if lower leadership has given out the correct information because we can't see those channels (c/MAJ Hunter Szymorski)>"
  3. "<The biggest issue I'm seeing with it (Microsoft Teams) is that it wasn't built specifically for military use so it lacks some features and abilities that would make pushing out information and sending orders up and down the chain of command way more convenient (c/MAJ Estella Hageman)>"
- **The workaround they already use:** <Unit communication app is designated (i.e Microsoft Teams)>
- **Full write-up:** `docs/interviews/<YYYY-MM-DD>-<initials>.md`

## 3. Candidate scope (Must features only)

| # | Feature (one vertical slice each) | Hours |
|---|---|---:|
| 1 | Profile Creation and password security system | 5 |
| 2 | Unit Chats with roster information | 15 |
| 3 | Military Rank and status role-based access system | 10 |
| 4 | Calendar events with accountability tracking features | 10 |
| 5 | Additional Calendar event information attachments | 5 |
| | Walking skeleton + CI | 10 |
| | Deployment + clean-machine test | 10 |
| | **Construction total** | 65 |

Budget: plan on **60 hours**, hard ceiling **75**. Above 75 you are borrowing from
testing and documentation, which are graded.

## 4. Out of scope — will NOT be built

<1. Mobile App       
2. Single Sign-on verification     
3. Email or text notifications     
4. User location tracking     
5. Social Networking platform    
6. Social Media platform     
7. Voice Calling   
8. Video Calling    
9. Integration with other apps (i.e Microsoft Teams, Signal, GroupMe, etc.    >

## 5. Feasibility screen

| Gate | Verdict | Evidence (dated) |
|---|---|---|
| **Build** — novelty load 2 | pass | <Python (known), HTML (known), MongoDB (unkown), Render (unknown) |
| **Get** — every dependency exercised for real | pass | <MongoDB Capstone Cluster created, 2026-09-06> |
| **Ship** — Render has been selected as my deployment method, terms read | pass | <Render + pricing page read on 2026-09-06> |
| **Show** — a stranger sees it work in 10 minutes | pass | <1. Create User Account 2. Log in and view your unit chats 3. Click on calendar to open up future events 4. View events coming up 5. click on event manager to determine additional information about events 6. Open unit chat to communicate with echelon 7. respond to messages, orders, and information 8. log out> |

**Technologies:** <Python> (known) · <MongoDB> (new) · <Render> (new)
**Novelty load:** <2>

## 6. The one hard part

<The hardest part for me is going to be creating and implementing the role-based rank system for communication. I don't really know how I want to implement the system at this time and I have general idea of having a echelon by echelon group with set permissions but I haven't thought of the best way to do it yet.>

## 7. Scorecard (1–5 each; weight in parentheses)

| Criterion | (w) | Score | Weighted |
|---|---:|---:|---:|
| Evidence a user exists | 3 | | |
| Fits ~45 hours of features | 3 | | |
| Novelty load | 2 | | |
| Dependencies verified | 2 | | |
| Demonstrable in ten minutes | 1 | | |
| **Total (max 55)** | | | |

## 8. If this candidate is rejected

<Write the rejection paragraph NOW, while you still like the idea. Name the gate it
failed, the number that killed it, and the condition under which you would revisit
it — or say plainly that it is closed, not deferred.>
