# Scoping Decision — <Acountabilibuddy>

**Author:** Liam Pheng  ·  **Date:** <2026-09-06>  ·  **Course week:** 2

---

## 1. Problem

2LT Joe Snuffy, a new Infantry Platoon Leader, needs to push information to his subordinate leaders, such as squad and team leaders. 2LT Joe Snuffy needs to distribute a Platoon OPORD, but his unit is using several communication channels, including Microsoft Teams, Signal, GroupMe, and text messaging. Joe Snuffy and his PSG, SFC John Smith, must determine which platform should be used to distribute the information. 2LT Joe Snuffy says that not having a set standardized application, specifically built with a focus on inter military communication causes confusion and missed messages across 2LT Snuffy's platoon, leading to soldiers missing events or not bringing the correct equipment. Also not having a singular method of communication leads to missed information in some apps and a non consolidated location of information and accountability tracking. Joe Snuffy may spend approximately one hour per week rewriting or resending information and checking whether personnel received it. Using several communication applications can also result in outdated or conflicting information, which creates additional time costs when leaders have to clarify or correct information. 2LT Joe Snuffy's unit: Alpha Company, 2nd Platoon, may decide to use GroupMe as its primary platform for distributing information to platoon leaders and members. 2LT Joe Snuffy may use GroupMe to communicate with his platoon, while his Company Commander uses Microsoft Teams to communicate with the company, and 2LT Snuffy's squad leaders use Signal Chat for their squads. As a result, information, tasks, and accountability data can become distributed across multiple applications, increasing the possibility of missed, outdated, or conflicting information.

## 2. Evidence a user exists

Interviewed LC HS EH / BN Commander, BN S3, BN XO on <2026-09-04>, <N> 30, past-tense questions only.
Full write-up in `docs/interviews/<YYYY-MM-DD>-<initials>.md`.

1. "<The non uniformity of communication in units is a prevalent issue I've seen throughout all units I've been a part of (c/LTC Lionel Carapia)>"
  2. "<Not having a standard app has made pushing out information from the S3 (operations) shop a lot more difficult because we are unaware if lower leadership has given out the correct information because we can't see those channels (c/MAJ Hunter Szymorski)>"
  3. "<The biggest issue I'm seeing with it (Microsoft Teams) is that it wasn't built specifically for military use so it lacks some features and abilities that would make pushing out information and sending orders up and down the chain of command way more convenient (c/MAJ Estella Hageman)>"
- **The workaround they already use:** <Unit communication app is designated (i.e Microsoft Teams)>

<If your project has no user but you, say so here in one sentence and substitute a
competitive scan of at least three existing tools. Do not invent a user.>

## 3. Chosen scope — Must features

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

Plan: 60 hours. Hard ceiling: 75. My number: <N>. <One sentence saying whether that
leaves slack, and what happens if it does not.>

## 4. Should features — built only if there is room
| # | Feature (one vertical slice each) | Hours |
|---|---|---:|
| First to be cut | Profile Customization | 5 |
| Second to be cut | Public document access | 5 |
| Third to be cut | Unit Wide FRAGO System | 5 |
| Fourth to be cut | Backbrief assignment and submission | 5 |

## 5. Out of scope — will not be built

1. Mobile App       
2. Single Sign-on verification     
3. Email or text notifications     
4. User location tracking     
5. Social Networking platform    
6. Social Media platform     
7. Voice Calling   
8. Video Calling    
9. Integration with other apps (i.e Microsoft Teams, Signal, GroupMe, etc.    

## 6. Accepted tradeoffs

<Any place you deliberately chose a cheaper design that costs the user something.
Name the cost. Name why you accepted it. Name what would make you revisit.>

## 7. Rejected candidates

**Rejected: Pricey.** <It failed the Get gate because it isn't plausible to get access to all the online retailer APIs as it would cost me a small fortune. Although very useful and has a much wider audience than Acountabilibuddy, I don't believe that it would be possible to make>

**Rejected: <name>.** <Same.>

## 8. Hour budget, reconciled

| Weeks | Phase | Hours |
|---|---|---:|
| 1–2 | Inception | 30 |
| 3–4 | Requirements | 30 |
| 5–6 | Design | 30 |
| 7 | Planning | 15 |
| 8 | Design review + midterm | 15 |
| 9–12 | Construction + verification | 60 |
| 13 | Documentation | 15 |
| 14 | Deployment + handoff | 15 |
| 15–16 | Presentation + delivery | 30 |
| | **Total** | **240** |

<One sentence: does your construction total fit inside the 60/75 line, and what did
you cut to make it fit?>

## 9. The one hard part

<Name exactly one. Two sentences on what makes it hard. This is what you will talk
about for ten minutes in Week 16.>

## 10. Risks and the scope-cut trigger

| Risk | Likelihood | What it costs me | Early warning sign |
|---|---|---|---|
| | | | |
| | | | |

**Scope-cut trigger.** If <a checkable condition> by <a real date>, I will cut
<feature> first, then <feature>. Decided now, in advance, so I do not have to decide
it while panicking.

---

**Signed:** Liam Pheng, <2026-09-06>
**AI use for this document:** None
