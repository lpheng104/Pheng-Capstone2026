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


### FR-ACCT-01 — Account Username Creation

**Priority:** Must 
**Requirement:** All new users of Acountabilibuddy will be able to create a unique username in order to log into and utilize Acountabilibuddy.
**Rationale:** All users of Acountabilibuddy will require a unique account so that the program can designate rank, role, and permissions to set account
**Acceptance criteria:**
- Given a new user wants to create an account, the user will be prompted to input a unique unused username into the system, then given the username is not already taken, the username will create a new account within the MongoDB database.
- Given the username is already in use (by checking already existing accounts and usernames within the MongoDB database), when a new user inputs the username they want to use, then an error code will push back that the "username already is in use" and will not create the account within the database, it will then prompt the new user to create a new username.

**Source:** your own decision — I believe that creating an account and logging into the system will be the best and easiest way to assign privileges to users as well as assign rank and role.


### FR-ACCT-02 — Account Password Creation

**Priority:** Must 
**Requirement:** All new users of Acountabilibuddy will be able to create a unique user account with a password in order to log into and utilize Acountabilibuddy.
**Rationale:** All users of Acountabilibuddy will require a secure password so that the program can finish setting the account
**Acceptance criteria:**
- Given a new user wants to create an account, the user will be prompted to input a secure password (at least 8 characters, 1 lowercase, 1 uppercase, special character (!,@,#,$,%)) into the system, then given the password and already created username, the system will assign the password to the account created under the username in MongoDB.
- Given the user input password is not secure (does not meet the password criteria), when inputting the newly created password for the account, then the system will spit out "Password does not meet the secure requirements" and then prompt the user to create a new password. The system will not store the invalid password to the account created in MongoDB.

**Source:** your own decision — I believe that creating an account and logging into the system will be the best and easiest way to assign privileges to users as well as assign rank and role.


### FR-ACCT-03 — Account Password Change

**Priority:** Should
**Requirement:** All users of Acountabilibuddy will be able to change their unique user account password.
**Rationale:** All users of Acountabilibuddy will have the ability to change their password in the event of forgetting password or the account is compromised. 
**Acceptance criteria:**
- Given an already existing user wants to change their already existing password, when they click the "change password option" they will be taken to a screen asking for input of new password. The user will then input a newly generated password that meets the security criteria (at least 8 characters, 1 lowercase, 1 uppercase, special character (!,@,#,$,%)) and input it into the system. The new password will then overwrite the already existing password within the MongoDB database assigned to their account. 
- Given the user input newly generated password is not secure (does not meet the password criteria), when inputting the newly created password for the account, then the system will spit out "Password does not meet the secure requirements" and then prompt the user to create a new password. The system will not store the invalid password to the account created in MongoDB.

**Source:** your own decision — I believe that the ability to change a password will be a quality of life feature that will greatly help the users feel secure in their ability to recover their accounts in the event of forgetting or losing password.

### FR-ACCT-04 — User Login

**Priority:** Must  
**Requirement:** A registered user will be able to log in using their username and password and in order to access the features authorized for their assigned role/rank.
**Rationale:** Account login authentication is required to prevent unauthorized users from accessing unit communication, events, and accountability information.
**Acceptance criteria:**
- Given a user has already created an account with a valid username and password, and the account was saved in the account database in MongoDB, The user will input their username and password into the respective fields at the login screen. Upon validation with the database that the account username matches with an existing account, the system will cross examine if the password assigned to the account is valid. If the username and password are both correct the System will allow the user into their account and give them access to the services provided by Acountabilibuddy. The system will then create an authenticated session within the program which allows the user to utilize Acountabilibuddy features.  
- Given the user has not created an account and inputs a random username and password which are not found within the account database, the system will reject the login request and kick the user back to the login screen
- Given the user inputs an invalid username that is not found within the database, the login request will be rejected and the user will be kicked back to the login screen.
- Given the user has a valid username found in the account database, but the password input does not validate with the password assigned to the account within the database, the login request will be rejected and the styem will kick the user back to the login screen.

**Source:** your own decision — Requiring an account and login credentials is essential in maintaining security within Acountabilibuddy and protecting private information stored within user accounts, chat history, and privileges 

### FR-ACCT-05 — User Logout

**Priority:** Must  
**Requirement:** A registered user will be able to log out from the system which will end the authenticated session started at login
**Rationale:** Users should be able to logout of their authenticated sessions when they are finished with the tasks in Acountabilibuddy. This is to promote security and reduce active sessions within Acountabilibuddy
**Acceptance criteria:**
- Given a user no longer wants to utilize the authenticated session in Acountabilibuddy, they will hit the "logout" button to end the session with the server. This will prevent them from accessing authenticated pages without logging back into the program with the validated user credentials.
- Given a user attempts to access authenticated pages after logging out, the read or write request will be rejected and they will be kicked back to the login screen, in order to access the data. 
  
**Source:** your own decision — Allowing users to logout will reduce strain on the program servers and promote better security due to closing inactive user authenticated sessions. 

### FR-ACCT-06 — Unique Username

**Priority:** Must  
**Requirement:**The system will prevent multiple accounts to be created with the same username
**Rationale:** Not allowing the creation of multiple accounts with the same username will prevent technical errors and the risk of data or personal information being accessible to unauthorized users
**Acceptance criteria:**
- Given a new user is attempting to create an account. They will input a unique username to the system to create an account within the database. If the system reads that there are no accounts in the database with that exact username, the account with the username will be created in the MongoDB database and the account creation will continue.  
- Given a user attempts to input a username that already exists within the MongoDB database, the system will push back that the "username already is in use" and will not create the account within the database, it will then prompt the new user to create a new username. 
  
**Source:** your own decision — preventing the creation of multiple accounts using the same username will prevent technical errors and data loss issues 


### FR-UNIT-01 — Unit Creation

**Priority:** Must
**Requirement:** Administrative users shall be able to create large groups based on the unit utilizing the system
**Rationale:** The creation of Unit groups within Acountabilibuddy will allow the transffering of information and data between large groups of users that require access to it (requested by Lionel Carapia, and Jack Malenock)
**Acceptance criteria:**
- Given an administrative user needs to create a unit group to send out information, when the administrative user initiates a create group request, then the program will create an entity within the Database housing the unit and its data.
- Given the unit creation request has been initiated and the unit entity has been created in the database, the administrative user will be asked to input the unit name, and the users that will be in the unit
- Given the user does not have administrative privileges to create a unit, the program will reject the creation request and will not create the entity within the database. The system will tell the user "Invalid Permissions".
- Given the Administrative user does not input a name for the unit, the program will cancel the creation request and delete the entity within the database. it will then tell the user "No unit name entered creation request cancelled" 

**Source:** Interviews with Lionel Carapia 09-04-2026 and Jack Malenock 09-09-2026.


### FR-UNIT-02 — Add User to Unit

**Priority:** Must
**Requirement:** Administrative users shall be able to add existing Acountabilibuddy users to already existing units.
**Rationale:** If new soldiers are added to military unit, the ability to add the soldier's Acountabilibuddy account to the Acountabilibuddy unit group will be required for effective communication.
**Acceptance criteria:**
- Given a user is required to be in a unit group and is not, when an administrative/leadership user initiates an add user request. The system will ask what the username of the added user is, then the administrative user will input the soldiers password to continue the request.
- Given the username input by the administrative user is a valid username found within the database, the user's account will be added to the unit group and they will have access to the unit calendar, chat, and information within the unit.
- Given the username input by the administrative user is invalid and not found within the database, the add user request will be cancelled and the system will spit out "Invalid user, add user request cancelled"

**Source:** your own decision — The ability to add users to already existing unit groups will be required because in the military new soldiers are always being transferred in and out of existing units.


### FR-UNIT-03 — Remove User from Unit

**Priority:** Must
**Requirement:** Administrative users shall be able to remove existing Acountabilibuddy users from already existing units.
**Rationale:** If soldiers are transferred out of a military unit, the ability to remove the soldier's Acountabilibuddy account from the Acountabilibuddy unit group will be required to prevent former members from continuing to access unit communication, calendar events, and information.
**Acceptance criteria:**
- Given a user is currently a member of a unit, when an administrative/leadership user initiates a remove user request. The system will ask what the username of the removed user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected unit, the user's account will be removed from the unit group and they will no longer have access to the unit calendar, chat, and information.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the remove user request will be cancelled and the system will spit out "User is not a member of this unit, remove user request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the remove user request will be cancelled and the system will spit out "Invalid user, remove user request cancelled."
- Given a non-administrative user attempts to remove another user from a unit, the system will deny the request.

**Source:** your own decision — The ability to remove users from existing unit groups will be required because military personnel are frequently transferred in and out of existing units, and former members should no longer have access to that unit's communication, calendar, or information.


### FR-UNIT-04 — Make User Admin of Unit

**Priority:** Could
**Requirement:** Administrative users shall be able to make existing Acountabilibuddy users administrators of already existing units.
**Rationale:** Military units may have multiple leaders who require administrative access to manage unit members, communication, calendar events, and accountability information.
**Acceptance criteria:**
- Given a user is currently a member of a unit, when an administrative/leadership user initiates a make admin request. The system will ask what the username of the user being made an administrator is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected unit, the user's account will be given administrator permissions for the unit.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the make admin request will be cancelled and the system will spit out "User is not a member of this unit, make admin request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the make admin request will be cancelled and the system will spit out "Invalid user, make admin request cancelled."
- Given a non-administrative user attempts to make another user an administrator, the system will deny the request.

**Source:** your own decision — The ability to make users administrators of existing unit groups will be required because multiple leaders within a military unit may need administrative permissions to manage unit members, communication, calendar events, and accountability.


### FR-UNIT-05 — Remove User Admin

**Priority:** Could
**Requirement:** Administrative users shall be able to remove administrator permissions from existing Acountabilibuddy users within already existing units.
**Rationale:** Military units may have leaders transfer out of leadership positions or units, requiring their administrator permissions to be removed while allowing them to remain members of the unit.
**Acceptance criteria:**
- Given a user is currently an administrator of a unit, when an administrative/leadership user initiates a remove admin request. The system will ask what the username of the user having their administrator permissions removed is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is an administrator of the selected unit, the user's administrator permissions will be removed while they remain a member of the unit.
- Given the username input by the administrative user is a valid username found within the database but is not an administrator of the selected unit, the remove admin request will be cancelled and the system will spit out "User is not an admin of this unit, remove admin request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the remove admin request will be cancelled and the system will spit out "Invalid user, remove admin request cancelled."
- Given a non-administrative user attempts to remove another user's administrator permissions, the system will deny the request.

**Source:** your own decision — The ability to remove administrator permissions from existing unit members will be required because military personnel may transfer out of leadership positions or responsibilities while remaining members of the unit.


### FR-CHAT-01 — Create Group Chat

**Priority:** Must
**Requirement:** Administrative users shall be able to create group chats for existing Acountabilibuddy units.
**Rationale:** Military units may need separate communication channels for different groups of users, such as squads, platoons, or leadership groups, to allow information to be communicated to the appropriate personnel.
**Acceptance criteria:**
- Given an administrative/leadership user is viewing an existing unit, when they initiate a create group chat request. The system will ask for the name of the group chat and which users should be included.
- Given the administrative user provides a valid group chat name and selects valid users within the unit, the system will create the group chat and add the selected users to the group chat.
- Given the administrative user provides a group chat name that is already being used within the selected unit, the create group chat request will be cancelled and the system will spit out "Group chat name already exists, create group chat request cancelled."
- Given the administrative user attempts to add a user who is not a member of the selected unit, the user will not be added to the group chat and the system will spit out "User is not a member of this unit."
- Given a non-administrative user attempts to create a group chat, the system will deny the request.

**Source:** your own decision — The ability to create group chats will be required because military units may need separate communication channels for different groups of personnel within the same unit.


### FR-CHAT-02 — Add User to Group Chat

**Priority:** Should
**Requirement:** Administrative users shall be able to add existing Acountabilibuddy users who are members of the unit to already existing group chats.
**Rationale:** Military units may need to add new personnel to existing group chats when soldiers are transferred into a unit or when additional personnel need access to a specific communication group.
**Acceptance criteria:**
- Given a group chat already exists, when an administrative/leadership user initiates an add user request. The system will ask what the username of the added user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and the user is a member of the selected unit, the user's account will be added to the group chat and they will have access to the group's messages.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the add user request will be cancelled and the system will spit out "User is not a member of this unit, add user request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the add user request will be cancelled and the system will spit out "Invalid user, add user request cancelled."
- Given the username input by the administrative user is already a member of the group chat, the add user request will be cancelled and the system will spit out "User is already a member of this group chat, add user request cancelled."
- Given a non-administrative user attempts to add another user to a group chat, the system will deny the request.

**Source:** your own decision — The ability to add users to existing group chats will be required because military personnel may be transferred into existing units and need to be added to established communication groups.


### FR-CHAT-03 — Remove User from Group Chat

**Priority:** Should
**Requirement:** Administrative users shall be able to remove existing Acountabilibuddy users from already existing group chats.
**Rationale:** Military personnel may be transferred out of a unit or no longer require access to a specific communication group, requiring their access to the group chat to be removed.
**Acceptance criteria:**
- Given a user is currently a member of a group chat, when an administrative/leadership user initiates a remove user request. The system will ask what the username of the removed user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected group chat, the user's account will be removed from the group chat and they will no longer have access to the group's messages.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected group chat, the remove user request will be cancelled and the system will spit out "User is not a member of this group chat, remove user request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the remove user request will be cancelled and the system will spit out "Invalid user, remove user request cancelled."
- Given a non-administrative user attempts to remove another user from a group chat, the system will deny the request.

**Source:** your own decision — The ability to remove users from existing group chats will be required because military personnel may be transferred out of units or no longer require access to specific communication groups.


### FR-CHAT-04 — Send Message in Group Chat

**Priority:** Must
**Requirement:** Users shall be able to send messages in group chats that they are members of.
**Rationale:** Group chat communication is a core feature of Acountabilibuddy and will allow authorized members of military units to communicate information within their assigned communication groups.
**Acceptance criteria:**
- Given a user is a member of a group chat, when they enter a message and submit it, the system will send the message to the group chat.
- Given a message is successfully sent, the message will be displayed in the group chat and will be visible to all authorized members of the group chat.
- Given a user attempts to send an empty message, the system will not send the message and will display "Message cannot be empty."
- Given a user is not a member of the group chat, the system will deny the user from sending messages in the group chat.
- Given a message is sent, the system will associate the message with the username of the user who sent it and the time the message was sent.

**Source:** Interviews with Thomas Yang and Jack Malenock on 09-09-2026 — The ability to send messages in group chats will be required because communication between authorized members is a core purpose of Acountabilibuddy.


### FR-CHAT-05 — Maintain Chat History

**Priority:** Must
**Requirement:** The system shall maintain a history of messages sent within group chats and allow authorized members to view previous messages.
**Rationale:** Maintaining chat history will allow users to review previously communicated information and prevent important unit communication from being lost when users leave and return to the application.
**Acceptance criteria:**
- Given a user is a member of a group chat, when they open the group chat, the system will display previously sent messages that the user is authorized to view.
- Given a message has been successfully sent, the system will store the message in the database as part of the group's chat history.
- Given a user leaves or is removed from a group chat, the user will no longer have access to the group's chat history.
- Given a user is added to an existing group chat, the user will be able to view the available chat history for that group.
- Given a user attempts to access the chat history of a group chat they are not authorized to access, the system will deny access.

**Source:** your own decision — The ability to maintain chat history will be required so authorized users can review previously communicated information and important unit communication is not lost.


### FR-CHAT-06 — Create Backbrief Assignment

**Priority:** Could
**Requirement:** Administrative/leadership users shall be able to create and assign a backbrief task within a group chat to one or more members of the group chat.
**Rationale:** Military leaders may need subordinate personnel to review information and provide a backbrief confirming their understanding of the information provided.
**Acceptance criteria:**
- Given a user has administrative/leadership permissions in a group chat, when the user creates a backbrief task, the system will allow the user to enter the backbrief instructions.
- Given a user has administrative/leadership permissions in a group chat, when the user creates a backbrief task, the system will allow the user to select one or more members of the group chat as recipients.
- Given a backbrief task is created, the system will display the backbrief task within the group chat.
- Given a user is assigned a backbrief task, the user will be able to view the backbrief instructions and submission requirements.
- Given a non-administrative user attempts to create a backbrief task, the system will deny the request.
- Given a backbrief task is assigned, the system will associate the task with the group chat and assigned recipient(s).
  
**Source:** Interview with XO Estella Hageman 09-04-2026 — A backbrief feature was identified as a potential extension of the group communication functionality to allow leaders to verify that subordinate personnel understand information distributed through the group chat.


### FR-CLNDR-01 — Add Calendar to Unit

**Priority:** Must
**Requirement:** Administrative users shall be able to add a calendar to an existing Acountabilibuddy unit.
**Rationale:** Each military unit will require a centralized calendar to organize and communicate upcoming unit events, training, meetings, and other scheduled activities.
**Acceptance criteria:**
- Given an existing unit does not have a calendar, when an administrative/leadership user initiates an add calendar request, the system will create a calendar for the selected unit.
- Given a calendar is successfully created, the calendar will be associated with the selected unit and accessible to authorized members of that unit.
- Given the selected unit already has a calendar, the add calendar request will be cancelled and the system will spit out "This unit already has a calendar, add calendar request cancelled."
- Given an administrative/leadership user attempts to create a calendar for a unit they are not authorized to manage, the system will deny the request.
- Given a non-administrative user attempts to add a calendar to a unit, the system will deny the request.

**Source:** Interview with XO Estella Hageman 09-04-2026 — The ability to add a calendar to an existing unit will be required because military units need a centralized location to organize and communicate upcoming events and activities.


### FR-CLNDR-02 — Add Calendar Event

**Priority:** Must
**Requirement:** Administrative users shall be able to add events to an existing Acountabilibuddy unit calendar.
**Rationale:** Military units need a centralized location to schedule and communicate upcoming training, meetings, and other unit activities to authorized members.
**Acceptance criteria:**
- Given an existing unit has a calendar, when an administrative/leadership user initiates an add calendar event request, the system will ask for the event name, date, time, and event information.
- Given the administrative user provides valid event information, the system will create the event and add it to the selected unit's calendar.
- Given an administrative user attempts to add an event to a unit calendar they are not authorized to manage, the system will deny the request.
- Given the administrative user does not provide all required event information, the system will cancel the add calendar event request and display "Required event information missing, add calendar event request cancelled."
- Given a non-administrative user attempts to add an event to a unit calendar, the system will deny the request.

**Source:** Interview with S3 Hunter Szymborski 09-04-2026 — The ability to add calendar events will be required because military units need to schedule and communicate upcoming training, meetings, and other unit activities in a centralized location.


### FR-CLNDR-03 — Delete Calendar Event

**Priority:** Could
**Requirement:** Administrative users shall be able to delete existing events from an Acountabilibuddy unit calendar.
**Rationale:** Military units may need to remove cancelled, outdated, or incorrectly created events from the unit calendar to prevent users from relying on incorrect scheduling information.
**Acceptance criteria:**
- Given an existing event is on a unit calendar, when an administrative/leadership user initiates a delete calendar event request, the system will ask which event they want to delete.
- Given the administrative user selects a valid event from the unit calendar, the system will delete the event from the selected unit's calendar.
- Given the selected event does not exist on the unit calendar, the delete calendar event request will be cancelled and the system will spit out "Invalid event, delete calendar event request cancelled."
- Given an administrative user attempts to delete an event from a unit calendar they are not authorized to manage, the system will deny the request.
- Given a non-administrative user attempts to delete a calendar event, the system will deny the request.

**Source:** your own decision — The ability to delete calendar events will be required because military units may need to remove cancelled, outdated, or incorrectly created events from their calendar.


### FR-CLNDR-04 — Accountability Tracker Event

**Priority:** Should
**Requirement:** Administrative users shall be able to enable accountability tracking for an existing Acountabilibuddy calendar event.
**Rationale:** Military units require the ability to track which personnel have acknowledged or confirmed their attendance for scheduled events.
**Acceptance criteria:**
- Given an existing calendar event, when an administrative/leadership user initiates an accountability tracker event request, the system will allow the administrative user to enable accountability tracking for the selected event.
- Given accountability tracking is enabled for an event, the system will create an accountability list containing the authorized members of the selected unit.
- Given a user is included in the accountability list, the user will be able to acknowledge the event through Acountabilibuddy.
- Given a user acknowledges the event, the system will record the user's acknowledgement and the time the acknowledgement was submitted.
- Given an administrative/leadership user views the accountability tracker for an event, the system will display which users have and have not acknowledged the event.
- Given a non-administrative user attempts to enable accountability tracking for an event, the system will deny the request.

**Source:** Interview with S3 Hunter Szymborski 09-04-2026 — The ability to enable an accountability tracker for calendar events will be required because military units need to track which personnel have acknowledged or confirmed their attendance for scheduled events.


### FR-RANK-01 — Assign User Role

**Priority:** Must
**Requirement:** Administrative users shall be able to assign an existing Acountabilibuddy user a role within an already existing unit.
**Rationale:** Assigning users specific roles will be required to establish the unit's chain of command and determine which features and information each user is authorized to access.
**Acceptance criteria:**
- Given a user is a member of a unit, when an administrative/leadership user initiates an assign user role request. The system will ask what the username of the user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected unit, the system will display the available roles and allow the administrative user to assign a role to the selected user.
- Given a valid role is selected, the system will assign the selected role to the user's account within the selected unit.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the assign user role request will be cancelled and the system will spit out "User is not a member of this unit, assign user role request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the assign user role request will be cancelled and the system will spit out "Invalid user, assign user role request cancelled."
- Given a non-administrative user attempts to assign a role to another user, the system will deny the request.

**Source:** Interview with Lionel Carapia 09-04-2026 and Jack Malenock 09-09-2026 — The ability to assign users roles within existing unit groups will be required because user roles will determine the user's position within the chain of command and what features and information they are authorized to access.


### FR-RANK-02 — Assign User Rank

**Priority:** Must
**Requirement:** Administrative users shall be able to assign an existing Acountabilibuddy user a military rank within an already existing unit.
**Rationale:** Assigning users military ranks will be required to accurately represent the unit's chain of command and provide users with identifiable rank information within Acountabilibuddy.
**Acceptance criteria:**
- Given a user is a member of a unit, when an administrative/leadership user initiates an assign user rank request. The system will ask what the username of the user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected unit, the system will display the available military ranks and allow the administrative user to assign a rank to the selected user.
- Given a valid military rank is selected, the system will assign the selected rank to the user's account within the selected unit.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the assign user rank request will be cancelled and the system will spit out "User is not a member of this unit, assign user rank request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the assign user rank request will be cancelled and the system will spit out "Invalid user, assign user rank request cancelled."
- Given a non-administrative user attempts to assign a rank to another user, the system will deny the request.

**Source:** Interview with Lionel Carapia 09-04-2026 and Jack Malenock 09-09-2026 — The ability to assign users military ranks within existing unit groups will be required because rank information is necessary to represent the unit's chain of command and identify users within the military organization.


### FR-RANK-03 — Change User Rank

**Priority:** Should
**Requirement:** Administrative users shall be able to change the military rank of an existing Acountabilibuddy user within an already existing unit.
**Rationale:** Military personnel may be promoted, demoted, or otherwise have their rank changed while remaining members of the same unit. The ability to update a user's rank will ensure that the unit's chain of command and user information remain accurate.
**Acceptance criteria:**
- Given a user is a member of a unit, when an administrative/leadership user initiates a change user rank request. The system will ask what the username of the user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected unit, the system will display the user's current rank and the available military ranks.
- Given a valid military rank is selected, the system will change the user's current rank to the newly selected rank within the selected unit.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the change user rank request will be cancelled and the system will spit out "User is not a member of this unit, change user rank request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the change user rank request will be cancelled and the system will spit out "Invalid user, change user rank request cancelled."
- Given a non-administrative user attempts to change another user's rank, the system will deny the request.

**Source:** your own decision — The ability to change users' military ranks within existing unit groups will be required because military personnel may be promoted, demoted, or otherwise have their rank changed while remaining members of the unit.


### FR-RANK-04 — Change User Role

**Priority:** Should
**Requirement:** Administrative users shall be able to change the role of an existing Acountabilibuddy user within an already existing unit.
**Rationale:** Military personnel may change positions or responsibilities while remaining members of the same unit. The ability to update a user's role will ensure that the unit's chain of command and the user's authorized permissions remain accurate.
**Acceptance criteria:**
- Given a user is a member of a unit, when an administrative/leadership user initiates a change user role request. The system will ask what the username of the user is, then the administrative user will input the username to continue the request.
- Given the username input by the administrative user is a valid username found within the database and is a member of the selected unit, the system will display the user's current role and the available roles.
- Given a valid role is selected, the system will change the user's current role to the newly selected role within the selected unit.
- Given the username input by the administrative user is a valid username found within the database but is not a member of the selected unit, the change user role request will be cancelled and the system will spit out "User is not a member of this unit, change user role request cancelled."
- Given the username input by the administrative user is invalid and not found within the database, the change user role request will be cancelled and the system will spit out "Invalid user, change user role request cancelled."
- Given a non-administrative user attempts to change another user's role, the system will deny the request.

**Source:** your own decision — The ability to change users' roles within existing unit groups will be required because military personnel may change positions or responsibilities while remaining members of the unit.


### FR-RANK-05 — Chain of Command Enforcement

**Priority:** Must
**Requirement:** The system shall enforce the established chain of command by restricting users' access to unit information, group chats, assignments, and administrative functions based on their assigned role and rank within the unit.
**Rationale:** Military units operate through a defined chain of command. Enforcing the chain of command helps ensure that users only access information and perform actions appropriate to their position within the unit.
**Acceptance criteria:**
- Given a user has an assigned rank and role, when the user accesses the system, the system will determine their permissions based on their position within the chain of command.
- Given a user attempts to access information outside of their authorized level of the chain of command, the system will deny access.
- Given a user attempts to perform an administrative function outside of their authorized level of the chain of command, the system will deny the request.
- Given a leader creates an assignment or accountability event, the system will restrict the assignment to users within the leader's authorized chain of command.
- Given a user's rank or role changes, the system will update the user's permissions to reflect their new position within the chain of command.
- Given a user attempts to bypass the established chain of command, the system will prevent the unauthorized action.

**Source:**  Interview with Jack Malenock 09-09-2026 — Chain of command enforcement was identified as a core requirement for ensuring that Acountabilibuddy reflects military organizational structure and restricts access and responsibilities according to a user's assigned rank and role.


## 6. Non-functional requirements

Each target is intentionally small enough to reproduce on a student laptop or the selected free/low-cost services. Raw results belong in [measurements.md](measurements.md); a requirement passes only when its stated method produces its threshold under its condition.

### 6.1 Performance

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-PERF-01 | Must | p95 server response time | ≤ 1.5 s | 20 sequential authenticated GETs of a unit page containing 50 members, 100 messages, and 25 events from the deployed service after one warm-up | Seed the stated dataset; run `python code/measure_http.py --url URL --requests 20`; save its p95 output. |
| NFR-PERF-02 | Should | HTML response size | ≤ 500 KiB | Same seeded unit-page request, excluding separately loaded CSS | Save the response with `curl`; record `Length`/byte count and confirm the threshold. |

### 6.2 Reliability

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-REL-01 | Must | Successful test runs | 10 of 10 consecutive runs | Clean test environment using pinned development requirements | Run the pytest command ten times; record each exit code, all of which must be zero. |
| NFR-REL-02 | Must | Recovery result after database interruption | No data loss among acknowledged writes; `/health` returns 200 within 5 minutes | Restart an Atlas test cluster or disconnect/reconnect a local MongoDB after creating a uniquely named event | Record event ID, outage responses, recovery time, and confirm the same event after reconnection. |

### 6.3 Security

These are prohibitions: a single successful prohibited action fails the requirement.

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-SEC-01 | Must | Unauthorized unit reads/writes | 0 successful requests | Anonymous, authenticated non-member, member, leader, and owner exercise every unit-scoped route | Run the role-permission pytest cases; every disallowed request must be 302, 403, or 404 and create no record. |
| NFR-SEC-02 | Must | Accepted state-changing requests lacking a valid CSRF token | 0 | Every POST route is called once with no token and once with a modified token | Parameterized Flask-client test must return 400 for every request and show no database change. |
| NFR-SEC-03 | Must | Committed secrets or plaintext passwords | 0 findings | Git-tracked files plus one newly registered test user | Run `git grep` for configured secret patterns and inspect the user document; run `pip-audit -r implementation/requirements.txt`; record zero secrets/plaintext credentials and resolve any known high/critical vulnerability before release. |
| NFR-SEC-04 | Must | Executable markup from user-controlled message/name fields | 0 executions | Submit `<script>alert(1)</script>` in every displayed text field | Automated response assertions require escaped markup; manually open each affected view and confirm no alert or injected element. |

### 6.4 Privacy

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-PRIV-01 | Must | Data fields collected outside the inventory below | 0 | Registration and normal member/leader workflows | Compare MongoDB document keys from a seeded end-to-end run with the inventory; document and approve any difference before merge. |
| NFR-PRIV-02 | Should | Time to complete a verified deletion request | ≤ 7 calendar days, with 0 matching application records afterward | Prototype user makes a written request and proves control of the username | Admin runs the documented deletion procedure, searches all collections by user ID/name, and records date, query results, and any provider-backup limitation. |

#### Data inventory

| Data element | Purpose | Location | Retention | User deletion |
|---|---|---|---|---|
| Username and display name | Authentication and attribution | Atlas `users`; duplicated display name in `messages` | While account exists; message attribution remains until messages are deleted | Written request to prototype administrator; delete/anonymize user, membership, session, response, and attributed message records within 7 days. |
| Password hash | Authenticate without retaining the password | Atlas `users.password_hash` | While account exists | Deleted with account; plaintext must never be stored. |
| Unit name, echelon, role, and rank label | Organize access and roster display | Atlas `units` and `memberships` | Until unit/account deletion | Owner requests unit deletion; user request removes membership/rank. |
| Message author, body, and timestamp | Unit chat | Atlas `messages` | Prototype duration or until unit deletion; a production retention policy must be verified before real use | Administrator deletes the requested message or unit; no self-service UI yet. |
| Event title, time, location, uniform, details | Scheduling | Atlas `events` | Prototype duration or until unit deletion | Unit owner requests event/unit deletion; no self-service UI yet. |
| Attendance intention and linked user/event IDs | Accountability view | Atlas `responses` | Until event, unit, or account deletion | Removed with the associated account/event/unit. |
| Random session token, user ID, expiration | Maintain login | Atlas `sessions`; signed session cookie carries the token | 8 hours, logout, or TTL cleanup | Logout revokes the database token; browser cookie expires/clears. |
| Username, failed-login count, expiration | Rate-limit sign-in attempts | Atlas `login_attempts` | 15 minutes via TTL | Automatic expiry; successful login deletes it immediately. |
| Atlas operational logs/backups | Hosting, recovery, and security | MongoDB Atlas/provider systems | **VERIFY before production:** depends on chosen Atlas tier/settings | **VERIFY:** follow the Atlas project deletion/support process and current Cloud Terms. Primary source: https://www.mongodb.com/legal/terms-and-conditions/cloud (checked 2026-09-20). |
| Render request/platform logs | Operate hosted service | Render systems | **VERIFY before production:** selected plan and log settings | **VERIFY:** use Render account/service deletion and support process. Primary source: https://render.com/privacy (checked 2026-09-20). |

### 6.5 Accessibility

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-A11Y-01 | Must | Critical/serious automated accessibility findings | 0 | Register, login, dashboard, and populated unit pages at desktop and 390 px viewport | Run axe DevTools on each page; save dated results and resolve every critical/serious finding. |
| NFR-A11Y-02 | Must | Core tasks completable using keyboard only | 5 of 5: register, sign in, post message, respond to event, sign out | Chrome at 100% zoom with mouse/touch unused | Start at address bar; use Tab/Shift+Tab/Enter/Space, record pass/fail, and confirm visible focus and logical order. |

### 6.6 Usability

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-USE-01 | Should | First-attempt task completion | ≥ 4 of 5 representative users complete ≥ 4 of 5 core tasks without coaching, each task in ≤ 2 minutes | Fresh accounts and a seeded unit on a phone or laptop | Give the five task prompts without procedural hints; time attempts and record completion/errors, not participant names. |
| NFR-USE-02 | Must | Invalid-input responses that explain a corrective action | 100% of the 8 documented invalid-input cases | Weak password, duplicate username, bad administrator token, unknown member, missing field, overlong field, naive event time, invalid attendance value | Execute the checklist; response must reject the write and supply an actionable message or documented HTTP error. |

### 6.7 Maintainability

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-MAINT-01 | Must | Automated regression status and runtime | 100% pass in ≤ 60 s | Fresh virtual environment on the course-development laptop | Install pinned files and run `python -m pytest implementation/tests -q`; record count, time, and exit code. |
| NFR-MAINT-02 | Should | Traceability validation findings | 0 | Every requirements change before merge | Run `python code/check-traceability.py`; it must exit 0 with no missing IDs, blanks, duplicates, or unknown requirement references. |

### 6.8 Portability

| ID | Priority | Metric | Threshold | Condition | Method |
|---|---|---|---|---|---|
| NFR-PORT-01 | Should | Successful supported-environment smoke tests | 2 of 2 environments | Windows 11 local Python 3.12 and Render Linux using the same dependency pins | In each environment register/login, create a unit/event, and record attendance |

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
| <2026-09-20> | 1.0 | NonFunctional Requirements, Constraits, and Definition of Done | Milestone 4 |


## 10. Constraints

| ID | Constraint | What it rules out |
|---|---|---|
| CON-01 | Course work must be submitted through this Git repository and remain reproducible by the reviewer. | Untracked-only configuration, manual server changes, and undocumented build steps. |
| CON-02 | Development/deployment spending is limited to free payment plans or open use software | Paid software, APIs, monitoring, database, and notification products. |
| CON-03 | Secrets and real passwords may not be committed; deployment configuration must use environment variables. | Hard-coded Atlas URIs, Flask keys, administrator tokens, or credentials in examples/tests. |
| CON-04 | Acountabilibuddy can't store sensitive personal information like Social Security numbers, medical data, or deep personal information. | Official military use and demonstrations with sensitive real-world soldier data. |
| CON-05 | The supported server stack is Python 3.12+, Flask, Gunicorn, and MongoDB for this milestone. | A rewrite to a native mobile application or incompatible relational-only architecture before design review. |

## 11. Assumptions

| ID | Assumption | Owner | Verify by | Consequence if false |
|---|---|---|---|---|
| ASM-01 | The instructor accepts fictional unit/member data for all demonstrations. | Liam Pheng | 2026-09-27 | Pause real-user testing and use a fully synthetic seed dataset; escalate OQ-01. |
| ASM-02 | Render and Atlas free/low-cost tiers can keep the demo reachable through Week 16. | Liam Pheng | 2026-09-27 | Run locally for the live demo and create a Week-15 fallback recording; reconsider CON-02. |
| ASM-03 | Target users have a current browser, cookies, JavaScript-independent HTML form support, and internet access. | Liam Pheng | 2026-10-04 | Narrow the supported environment explicitly or add an alternate client/offline design. |
| ASM-04 | A unit in Acountabilibuddy has no more than 50 members, 100 displayed messages, and 25 upcoming events. | Liam Pheng / stakeholder | 2026-10-04 | Repeat performance/design analysis at the confirmed scale and add pagination before pilot use. |
| ASM-05 | Attendance acountability is good enough for the course workflow and will not be treated as physical accountability. | Liam Pheng | 2026-09-27 | Rename/remove the feature or design verified check-in and audit controls before further use. |

## 12. Dependencies

| ID | Dependency and pinned plan/version | Failure mode | Fallback |
|---|---|---|---|
| DEP-01 | Python 3.12+ and Flask 3.1.3 | Runtime/package incompatibility or security advisory | Stay on the last tested Python 3.12 patch and upgrade the pin on a branch after the regression suite passes. |
| DEP-02 | MongoDB Atlas compatible with PyMongo 4.18.1 | Cluster unreachable, quota exhausted, terms/tier changes, or data loss | Use local MongoDB for development/demo, export a sanitized backup, and show a recorded fallback demo. |
| DEP-03 | Render Python service using Gunicorn 23.0.0 | Deploy/build failure, sleeping service, outage, or free-tier removal | Run Gunicorn locally, retain documented build commands, and use the fallback recording. |
| DEP-04 | python-dotenv 1.2.3 | Local environment variables fail to load | Set environment variables directly in PowerShell/hosting dashboard; never commit `.env`. |
| DEP-05 | pytest 9.1.1 and mongomock 4.3.0 for automated tests | Mock behavior diverges from Atlas or packages become incompatible | Run critical tests against a disposable real MongoDB database and pin the last compatible test versions. |

## 13. Obligations

### 13.1 Project license position

The project is licensed under **MIT**. The complete license is present at  Main/LICENSE. 

### 13.2 Third-party obligations verified 2026-09-20

| Component/service | Current obligation or license | Primary source checked | Project action |
|---|---|---|---|
| Flask 3.1.3 | BSD-3-Clause | https://github.com/pallets/flask/blob/main/LICENSE.txt | Retain copyright/license notices in redistributed copies. |
| PyMongo 4.18.1 | Apache-2.0 | https://github.com/mongodb/mongo-python-driver/blob/master/LICENSE | Retain license/notice terms if redistributed; do not imply MongoDB endorsement. |
| python-dotenv 1.2.3 | BSD-3-Clause | https://github.com/theskumar/python-dotenv/blob/main/LICENSE | Retain the license notice in source/binary redistributions. |
| Gunicorn 23.0.0 | MIT | https://github.com/benoitc/gunicorn/blob/master/LICENSE | Retain copyright and permission notice in redistributed copies. |
| pytest 9.1.1 | MIT | https://github.com/pytest-dev/pytest/blob/main/LICENSE | Development-only; retain notice if redistributed. |
| mongomock 4.3.0 | ISC | https://github.com/mongomock/mongomock/blob/develop/LICENSE | Development-only; retain notice if redistributed. |
| MongoDB Atlas | Cloud Terms govern use and state that stored data need not be retained after termination. | https://www.mongodb.com/legal/terms-and-conditions/cloud | Accept only through an authorized account; keep sanitized backups; verify tier and deletion behavior before a pilot. |
| Render | Terms and Acceptable Use Policy govern hosted content, credentials, usage, and suspension. | https://render.com/terms and https://render.com/acceptable-use | Keep credentials private, use lawful/non-sensitive test content, monitor terms, and maintain the local fallback. |
