# Title: Nursery Communicator

## 1. Overview
### Major web application features:
  - An administrative page where features can be added or removed.
  - Major features of this application will be a user-login/logout.
  - A 2D visual display of the property with shapes representing actual structures.
    * The structures can be interacted with.
    * Employees have the ability to change colors.
    * The admin can move, insert and remove structures, as well as adjust values pertaining to certain structures.
  - A system to produce, review, and update “todo” lists
### Problem to be solved
  Nurseries and agriculture are largely staffed by ESL or non-English speaking employees, making communication a challenge.  Using a technology which they are comfortable with, management and the workforce can more effectively communicate using visual references.

### Libraries and frameworks:
  - This app will be created using Django.
  - Canvas will be used to create objects.
  - js.interact will be used to create the drag and drop feature of objects

## 2. Functionality:

### What will the user see on each page

  - There will be four pages:

    - An index page requesting a user sign-on.
    - A homepage that can be have announcements and a nav bar that will bring up todo lists for a user and a link to the nursery page.
    - A todo list page.  
    - The nursery will display the layout with the structures highlights and when you click on the structure of interest, a modal will pop up with a specific instructions.

### What can they input, click, see

  - Users should be able to see announcements.
  - Users should be able to see a list of to-do items and locations where the items will be completed.
  - Users should be able to review the nursery map and see where work can be conducted.  

### how will their actions correspond to events on the back-end

  - Initially, the nursery display will be blank.  
  - The todo list is also empty.
  - The admin has the ability to fill out information related to model attributes that are built in Django.  A model will be created for each type of greenhouse.  For this project, I will create 3 greenhouse models.  

    - Gutter connected
    - Free standing
    - Even span

  - I will also create a model for Color coding.

  An example of how a user’s action, the “Grower”, will relate to back-end.  A grower wants to water a greenhouse.  They select the greenhouse and then select a list color coded options.  After changing the color, this is then rendered on the other user’s screen and everyone knows there is water.  If they decide the next greenhouse is close to needing to be watered, they can select a color and this is also made visible to everyone.  The structure will also be added to a todo list that is meant for the growers.  The grower once the “watch color” == “the water color” the todo item is removed form the list!

  At any point, the admin can review what crops in a nursery need to be watered or any staff that may be working in the near area or taking over that crop the next day.

### What data will need to be stored as apart of your application?

  - User - first name, last name, email, password
  - Greenhouse location -  x and y coordinate, size.
  - greenhouse type - graphic
    - color-code
    - container capacity
    - a picture
  - Todo - datetime, task, needs to be linked to  greenhouse type (a one to one relationship)
  - NRCS plant list - API plant list.org  

## 3. Schedule
### Milestone 1
  - 04/26 - Project proposal is submitted
  - 05/03 - Website layout will be sketched out with the purpose of each page defined.
    - Django development.
    - Color code model will be complete.  
    - Plant list api will be accessible.  
    - Greenhouse designs and property canvas will be complete.

  - 05/10 Django in development
    - Greenhouse models will be complete with Path to nursery template laid out.  
    - make test ability to add information to the greenhouse structure and polish up the admin interface.

  - 05/14 - Django development
    - make it so the admin can create, copy, drag, scale and rotate greenhouse structures on the template and then save the whole layout with the amended data.

### Milestone 2

  - 05/17
    - onClick listeners for changing the color of structures.
    - save changes so different users will see changes to the nursery template.
    - Integrate the todo system, so that if a user changes a color that color corresponds to a value which is then added to the todo.

### Milestone 3
   - 05/22
    - Have a sign in system for multiple users.  
    - Have permissions set up for the users
    - Finish the todo, so that as colors are changed, the todo item is removed.

### Milestone 4
  - 06/05
    - Complete everything up to Milestone 3.
    - Create more models/structures for the user to generate. - outdoor compounds, field grown trees.
    - create a hierarchy of communication for different teams, or different views for different teams.  Head grower can use the admins display to generate a todo list specifically for the grow team.  The maintenence crew can highlight specific items and record what was replaced and when.
    - utilities and other site infrastructure should be included
    - running inventories for materials
    - include pesticide information for easily displaying pertinent information
    - include a homepage with announcements and randomly selected safety talk ideas(probably need to scrape the internet for this.)
