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


### FR-<ACCT>-<01> — <Account Username Creation>

**Priority:** Must 
**Requirement:** All new users of Acountabilibuddy will be able to create a unique username in order to log into and utilize Acountabilibuddy.
**Rationale:** All users of Acountabilibuddy will require a unique account so that the program can designate rank, role, and permissions to set account
**Acceptance criteria:**
- Given a new user wants to create an account, the user will be prompted to input a unique unused username into the system, then given the username is not already taken, the username will create a new account within the MongoDB database.
- Given the username is already in use (by checking already existing accounts and usernames within the MongoDB database), when a new user inputs the username they want to use, then an error code will push back that the "username already is in use" and will not create the account within the database, it will then prompt the new user to create a new username.

**Source:** your own decision — I believe that creating an account and logging into the system will be the best and easiest way to assign privileges to users as well as assign rank and role.


### FR-<ACCT>-<02> — <Account Password Creation>

**Priority:** Must 
**Requirement:** All new users of Acountabilibuddy will be able to create a unique user account with a password in order to log into and utilize Acountabilibuddy.
**Rationale:** All users of Acountabilibuddy will require a secure password so that the program can finish setting the account
**Acceptance criteria:**
- Given a new user wants to create an account, the user will be prompted to input a secure password (at least 8 characters, 1 lowercase, 1 uppercase, special character (!,@,#,$,%)) into the system, then given the password and already created username, the system will assign the password to the account created under the username in MongoDB.
- Given the user input password is not secure (does not meet the password criteria), when inputting the newly created password for the account, then the system will spit out "Password does not meet the secure requirements" and then prompt the user to create a new password. The system will not store the invalid password to the account created in MongoDB.

**Source:** your own decision — I believe that creating an account and logging into the system will be the best and easiest way to assign privileges to users as well as assign rank and role.


### FR-<ACCT>-<03> — <Account Password Change>

**Priority:** Should
**Requirement:** All users of Acountabilibuddy will be able to change their unique user account password.
**Rationale:** All users of Acountabilibuddy will have the ability to change their password in the event of forgetting password or the account is compromised. 
**Acceptance criteria:**
- Given an already existing user wants to change their already existing password, when they click the "change password option" they will be taken to a screen asking for input of new password. The user will then input a newly generated password that meets the security criteria (at least 8 characters, 1 lowercase, 1 uppercase, special character (!,@,#,$,%)) and input it into the system. The new password will then overwrite the already existing password within the MongoDB database assigned to their account. 
- Given the user input newly generated password is not secure (does not meet the password criteria), when inputting the newly created password for the account, then the system will spit out "Password does not meet the secure requirements" and then prompt the user to create a new password. The system will not store the invalid password to the account created in MongoDB.

**Source:** your own decision — I believe that the ability to change a password will be a quality of life feature that will greatly help the users feel secure in their ability to recover their accounts in the event of forgetting or losing password.

### FR-<ACCT>-<04> — <User Login>

**Priority:** Must  
**Requirement:** A registered user will be able to log in using their username and password and in order to access the features authorized for their assigned role/rank.
**Rationale:** Account login authentication is required to prevent unauthorized users from accessing unit communication, events, and accountability information.
**Acceptance criteria:**
- Given a user has already created an account with a valid username and password, and the account was saved in the account database in MongoDB, The user will input their username and password into the respective fields at the login screen. Upon validation with the database that the account username matches with an existing account, the system will cross examine if the password assigned to the account is valid. If the username and password are both correct the System will allow the user into their account and give them access to the services provided by Acountabilibuddy. The system will then create an authenticated session within the program which allows the user to utilize Acountabilibuddy features.  
- Given the user has not created an account and inputs a random username and password which are not found within the account database, the system will reject the login request and kick the user back to the login screen
- Given the user inputs an invalid username that is not found within the database, the login request will be rejected and the user will be kicked back to the login screen.
- Given the user has a valid username found in the account database, but the password input does not validate with the password assigned to the account within the database, the login request will be rejected and the styem will kick the user back to the login screen.

**Source:** your own decision — Requiring an account and login credentials is essential in maintaining security within Acountabilibuddy and protecting private information stored within user accounts, chat history, and privileges 

### FR-<ACCT>-<05> — <User Logout>

**Priority:** Must  
**Requirement:** A registered user will be able to log out from the system which will end the authenticated session started at login
**Rationale:** Users should be able to logout of their authenticated sessions when they are finished with the tasks in Acountabilibuddy. This is to promote security and reduce active sessions within Acountabilibuddy
**Acceptance criteria:**
- Given a user no longer wants to utilize the authenticated session in Acountabilibuddy, they will hit the "logout" button to end the session with the server. This will prevent them from accessing authenticated pages without logging back into the program with the validated user credentials.
- Given a user attempts to access authenticated pages after logging out, the read or write request will be rejected and they will be kicked back to the login screen, in order to access the data. 
  
**Source:** your own decision — Allowing users to logout will reduce strain on the program servers and promote better security due to closing inactive user authenticated sessions. 

### FR-<ACCT>-<06> — <Unique Username>

**Priority:** Must  
**Requirement:**The system will prevent multiple accounts to be created with the same username
**Rationale:** Not allowing the creation of multiple accounts with the same username will prevent technical errors and the risk of data or personal information being accessible to unauthorized users
**Acceptance criteria:**
- Given a new user is attempting to create an account. They will input a unique username to the system to create an account within the database. If the system reads that there are no accounts in the database with that exact username, the account with the username will be created in the MongoDB database and the account creation will continue.  
- Given a user attempts to input a username that already exists within the MongoDB database, the system will push back that the "username already is in use" and will not create the account within the database, it will then prompt the new user to create a new username. 
  
**Source:** your own decision — preventing the creation of multiple accounts using the same username will prevent technical errors and data loss issues 


### FR-<UNIT>-<01> — <Unit Creation>

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
