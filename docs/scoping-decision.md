# Scoping Decision — Acountabilibuddy

**Author:** Liam Pheng  ·  **Date:** <2026-09-06>  ·  **Course week:** 2

---

## 1. Problem

2LT Joe Snuffy, a new Infantry Platoon Leader, needs to push information to his subordinate leaders, such as squad and team leaders. 2LT Joe Snuffy needs to distribute a Platoon OPORD, but his unit is using several communication channels, including Microsoft Teams, Signal, GroupMe, and text messaging. Joe Snuffy and his PSG, SFC John Smith, must determine which platform should be used to distribute the information. 2LT Joe Snuffy says that not having a set standardized application, specifically built with a focus on inter military communication causes confusion and missed messages across 2LT Snuffy's platoon, leading to soldiers missing events or not bringing the correct equipment. Also not having a singular method of communication leads to missed information in some apps and a non consolidated location of information and accountability tracking. Joe Snuffy may spend approximately one hour per week rewriting or resending information and checking whether personnel received it. Using several communication applications can also result in outdated or conflicting information, which creates additional time costs when leaders have to clarify or correct information. 2LT Joe Snuffy's unit: Alpha Company, 2nd Platoon, may decide to use GroupMe as its primary platform for distributing information to platoon leaders and members. 2LT Joe Snuffy may use GroupMe to communicate with his platoon, while his Company Commander uses Microsoft Teams to communicate with the company, and 2LT Snuffy's squad leaders use Signal Chat for their squads. As a result, information, tasks, and accountability data can become distributed across multiple applications, increasing the possibility of missed, outdated, or conflicting information.

## 2. Evidence a user exists

Interviewed LC HS EH / BN Commander, BN S3, BN XO on <2026-09-04>, <N> 30 minutes     past-tense questions only.
Full write-up in `docs/interviews/<YYYY-MM-DD>-<initials>.md`.

1. "<The non uniformity of communication in units is a prevalent issue I've seen throughout all units I've been a part of (c/LTC Lionel Carapia)>"
  2. "<Not having a standard app has made pushing out information from the S3 (operations) shop a lot more difficult because we are unaware if lower leadership has given out the correct information because we can't see those channels (c/MAJ Hunter Szymorski)>"
  3. "<The biggest issue I'm seeing with it (Microsoft Teams) is that it wasn't built specifically for military use so it lacks some features and abilities that would make pushing out information and sending orders up and down the chain of command way more convenient (c/MAJ Estella Hageman)>"
- **The workaround they already use:** <Unit communication app is designated (i.e Microsoft Teams)>

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

Plan: 60 hours. Hard ceiling: 75. My number: 65 . <My project is a total of 65 hours which leaves around 10 before I hit the hard ceiling. This means that I have about 10 hours of wiggle room incase things take longer than expected or I want to add the additional features listed below. >

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

<One big tradeoff that I have chosen for this project is to utilize a web based application rather than a mobile app due to my unfimilarity with both Android and IOS app development. This will help reduce the development time but might hurt the user experience a little bit because I wasn't comfortable having to learn IOS and/or Android app development during the 240 hour project window. This tradeoff is acceptable however, because both chat features and calendar/event accountability can be performed through a web based application.     

Another big trade off that the users will have to endure is the role based permission system I want to integrate. Not all users will have administrative permissions to create or add events to the unit calendar and some users will only have the privileges to read events and write in their own squad chats. The trade off of denying the majority of users these privileges and permissions stem from the need of a military based organizational command chain.>

## 7. Rejected candidates

**Rejected: Pricey.** <It failed the Get gate because it isn't plausible to get access to all the online retailer APIs as it would cost me a small fortune. Although very useful and has a much wider audience than Acountabilibuddy, I don't believe that it would be possible to make>

**Rejected: Group Project Management.** <It failed the build gate because of the amount of novelty technology I would have to learn in order to complete the project. I don't think I would be able to accurately manage both learning the new technology required as well as spending time putting together the group management software within the allocated 240 hours. While I think that the application has a much broader range of use as it can be applied in all levels of education, I just think that the project is too ambitious for 240 hours.>

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

<My plan and set hours work, but I do have an additional 20 hours of features that I potentially want to add. I was very generous and allocated a lot of extra hours to developing the core features. I am hoping that I will complete those objectives a lot quicker than I anticipate leaving me time to add additional features.>

## 9. The one hard part

<The biggest challenge that I forsee in the developing of this project will undoubtedly be developing and managing the roles and permissions of different users. I want to ensure that only administrative/leadership positions are able to create and track accountability data for calendar events. I don't exactly know how I am going to implement non privileged users to access, view, and acknowledge the calendar events while not allowing them to read or write. It is definitely a system I am going to have to develop overtime and put an additional amount of hours into. I am anticipating putting at least 10 hours into developing the role/rank system to develop the chain of command features of the web application. >

## 10. Risks and the scope-cut trigger

| # | Risk | Likelihood (L/M/H) | Impact (L/M/H) | Early warning sign | What I will do |
|---|---|---|---|---|---|
| R1 | Procrastination | L | H | Putting Less than 15 hours a week and starting Milestones late | Dedicate more hours from the following weeks to make up and catch up to the 24o hour milestones. (i.e if I procrastinate on week 7 and only put in 9 hours, Week 8 will have 6 additional hours to make up for the lost time. I will find more time by cutting non-essential/mandatory extracurricular activities, (i.e going out with friends, playing video games, or going to the Gym |
| R2 | Project Becomes too Big for 16 Weeks | L | M | Towards weeks 10 - 12 I have not developed the calendar based system for accountability tracking or I am not completed all the functions and features of the Interpersonal communication/text focus of inter-echelon communication | Put an emphasis on finishing and refining the communication/chain of command systems by cutting features listed in the Section 7 "When I fall behind" segment. (i.e I will cut the advanced calendar features first to give me more time to focus on the communication system) |
| R3 | Computer Failure or Data Loss | L | L | Updated Project files are only on my computer and have not been uploaded to the GitHub Repository | Always upload my files to the repository after every project work session |


**Scope-cut trigger.** If I don't have the chat and rank/role features completed by October 30th, 2026, I will cut
Profile Customization first, then The public document access feature, followed by FRAGO system, and Backbrief assignments and submissions. Decided now, in advance, so I do not have to decide
it while panicking.

---

**Signed:** Liam Pheng, <2026-09-06>
**AI use for this document:** None
