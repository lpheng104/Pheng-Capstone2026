# Idea Canvas — Candidate C

**Candidate name:** Group Project Management
**Date started:** <2026-08-31>   **Well it came from:** Online Shopping Experience

---

## 1. Problem statement

Summary: A Web Application that is used for school group projects to track contributions, commits, and progress of the group
| Category | Description | Specific Example |
|---|---|---|
| **Software Type** | Webb Application | |
| **For** | Groups of Students working on a collaborative project | Four Business students have been given a group project to work on |
| **Who** | When individual group members don't contribute and the others have to pick up the slack | One of the four students decides they don't want to contribute to the group project and decides to not do their part |
| **The Problem Is** | Individuals not contributing or not putting in work forces others to have to do the work for them | The other three students have to do more work to compensate and get the project completed |
| **Which Costs** | Extra time and effort is required to make up for the slackers lack of contributions | The other three students have to put in an additional three hours of work to make up for their partner's slack |
| **Today They** | Students have to put in extra work and have to inform professors and teachers about the slackers | The three good working students complete the project after putting in extra work and inform their teacher about the slacker |
| **Which Falls Short Because** | There is no documentation of contributions and professors do not always grade slackers differently | The students are not able to get more credit than the slacker because there is no documentation of group contributions or work distribution |

*** 

## 2. Evidence a user exists

- **Person spoken to:** <Brayden Gregor>
- **Date and length:** <2026-09-05, 10 minutes>
- **Three verbatim quotes:**
  1. "<Group Project work has always been super annoying to deal with>"
  2. "<Why do I have to do more work for slackers when they get the same grade as me?>"
  3. "<If we could track what people are doing and how much they are (contributing) it would be helpful to show teachers and potentially get better grades then them (slackers) >"
- **The workaround they already use:** <Report slackers to professor/teacher which doesn't always work)>     
  
## 3. Candidate scope (Must features only)

| # | Feature (one vertical slice each) | Hours |
|---|---|---:|
| 1 | User Creation and profile management | 10 |
| 2 | Create and join groups function | 15 |
| 3 | Shared document upload and work progress tracker | 15 |
| 4 | Task creation and assigning | 5 |
| 5 | Progress Tracker | 5 |
| | Walking skeleton + CI | 10 |
| | Deployment + clean-machine test | 10 |
| | **Construction total** | 70 |

Budget: plan on **60 hours**, hard ceiling **75**. Above 75 you are borrowing from
testing and documentation, which are graded.

## 4. Out of scope — will NOT be built

1. Mobile App       
2. Single Sign-on verification     
3. Email or text notifications     
4. User location tracking     
5. Social Networking platform    
6. Social Media platform
7. Chat features
8. Video Calling
9. Voice Calling

## 5. Feasibility screen

| Gate | Verdict | Evidence (dated) |
|---|---|---|
| **Build** — novelty load 2 | pass | <Python (known), HTML (known), MongoDB (unkown), Render (unknown) |
| **Get** — every dependency exercised for real | pass | <MongoDB Capstone Cluster created, 2026-09-06> |
| **Ship** — Render has been selected as my deployment method, terms read | pass | <Render + pricing page read on 2026-09-06> |
| **Show** — a stranger sees it work in 10 minutes | pass | <1. Create an account with user name and password 2. log in using new login credentials 3. access your group projects page 4. if empty click "create new group project" 5. share project with other users/classmates 6. assign tasks for others and yourself to do 7. click commits tab and track what work is being done and who has contributed 8. hit contributions tab and see the percentage of work each contributor has provided 9. look at the project to do list and start working on your tasks 9. check your commits page to see what you've been doing has been documented 10. log out for the day > |

**Technologies:** <Python> (known) · <MongoDB> (new) · <Render> (new)
**Novelty load:** <2>

## 6. The one hard part

< I think that the most difficult part of this project would be combining or attaching word documents or spread sheets and having the application track how much work is being done between all group members. Having the application be able to see who is contributing what and when is going to be very difficult across different file formats like .pptx and .doc >

## 7. Scorecard (1–5 each; weight in parentheses)

| Criterion | (w) | Score | Weighted |
|---|---:|---:|---:|
| Evidence a user exists | 3 | 5 | 15 |
| Fits ~45 hours of features | 3 | 3 | 9 |
| Novelty load | 2 | 2 | 4 |
| Dependencies verified | 2 | 3 | 6 |
| Demonstrable in ten minutes | 1 | 5 | 5 |
| **Total (max 55)** | | | 39 |

## 8. If this candidate is rejected

<The biggest reason why this project would be or is rejected is the difficulty of tracking user edits and contributions to different types of files from an outside web application. It will be very difficult to have the application track who is contributing when and where. I don't believe it would be very easy to carry those features over to a GitHub like application that can determine the work of each group member in different shared documents or powerpoints. >
