<!DOCTYPE md>
<md>
#OpenTable (placeholder)

##Concept
This app is designed to support traditional board game play in an online setting with multiple players jumping in and out of games. It will be something like a Roll20 clone. It will have multiple die-rolling functions through Python, profile pages for players and game organizers, options for uploading rules to the site, wish lists for players looking for groups and organizers looking for players. A chatroom-style interface accessible to players and organizers will be the means through which actual games are played. If there is time, I will add a game/player search function.

###Functions
* Die rolling system
* Personalized profile pages
  - Bio
  - Blog
  - Playgroup Records
  - Game Wish List
* Game/Die/Record keeping customizability (Ties into Playgroup Records)
* Scheduling system (Ties into Bio)
* Forum-style playgroup page.

###Problems Solved
- [] Determine which Frameworks to use
- [] Determine the models for game sessions
- [] Create database for game sessions
- [] Determine the models for profiles
- [] Create database for profiles
- [] Determine the models for social function
- [] Create database for social function
- [] Figure out how to tie interface to each database API style
- [] Front End and formatting

###Libraries/Frameworks
TBD

##Functionality

###Interface
* User login
* Profile page
  - Play Records pages
  - Simple blog posts
  - Wish List page
* Game Organizer page
  - Play Records pages
  - Rule customization page
  - Piece image uploading
  - Rulebook
* Campaign page for actual play
  - Roll field
  - Board field
  - Chat room
* Forum page
  - Campaign organizing rooms
  - Player search
  - Campaign search

###Data Input
* Profile data
  - Bio (Personal info, schedule, etc.)
  - Play records (History of recent sessions)
  - Wish List (What systems you want to play; searchable)
  - Blog posts (Twitter-style comments on your page)
* Playgroup data
  - Players involved
  - Game data for each player
  - Rolls
  - History
  - Chat
* Game organization data
  - Basic description
  - Select ruleset
  - Add players
  - Add custom rules
  - Update history
* Forum data
  - Make page for campaign
  - Search players
  - Search organizers

###Back-End/Data
* Profile database
  - Bio info
  - Games invitations
  - Games run
  - Wishlist data
  - History of posts
  - Activity record/dates
* Game database
  - Dice info
  - Rulesets
* Session database
  - Players invited
  - Rulesets used
  - Player game records
  - Session records
  - Access permissions
* Forum database
  - Game data
  - Timezone data
  - Profile data
  - Tags data

##Schedule

###Week 1 Goals

###Week 2 Goals

###Week 3 Goals
</md>
