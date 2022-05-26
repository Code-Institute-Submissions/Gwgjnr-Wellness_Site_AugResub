# [Health Hub](https://wellness-site.herokuapp.com/)

![Mockup of live site on different devices](media/readme/project_5.JPG)

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
        - [**Data Model**](#data-model)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Future Features**](#future-features)

3. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Responsive Testing**](#responsive-testing)
    
4. [**Deployment**](#deployment)
    - [**Heroku Deployment steps**](#heroku-deployment-steps)
    - [**Forking the GitHub Repository**](#forking-the-github-repository)

---

## UX

For this project, I decided to build a web application that allows users to join weekly virtual seminars to improve their health and wellbeing.

### User Stories

"**_As a user, I would like to_** _____________________________"

- Navigate the site using a navbar and footer.
- Sign into an account.
- View seminars.
- Comment and review seminars.
- Register for an event.
- Search for relevant events.

### Design

#### Framework

- [Bootstrap 5.1.3](https://www.djangoproject.com/)

- [Django 3.2](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
  
#### Color Scheme

![Colour Palette](media/readme/.JPG)

#### Typography 

#### Data Model

### Wireframes

## Features

### Existing Features

**Navbar**

![Navbar](media/readme/navbar.JPG)

Navbar set at top of each page to allow the user to easily navigate the site. Made collapsible with Bootstrap to allow a better format for mobile users.

**Seminar Search Page**

### Future Features

A search bar to allow the user to narrow down the seminar list.

## Testing

### Validators

I have thoroughly tested the features of Hobby Hub web application against all user stories.

## Deployment 

### Heroku Deployment steps
 
 1. Ensure all dependencies are listed on requirements.txt. 
 
 Write on python terminal ` pip3 freeze > requirements.txt`, and a list with all requirements will be created to be read by Heroku. 
 
 2. Setting up your Heroku

    2.1 Go to Heroku website (https://www.heroku.com/). 
    
    2.2 Login to Heroku and go to Create App.
    
    2.3 Click in New and Create a new app.
    
    2.4 Choose a name and set your location.

    2.5. Navigate to the Resources tab.

    2.6. Click on Resources and Seach for Heroku Postgres and select it on the list.
    
    2.7. Navigate to the deploy tab.
    
    2.8. Click in Connect to Github and search for 'Gwgjnr' GitHub account and 'Wellness_Site' repository.
    
    2.9.  Navigate to the settings tab.
    
    2.10.  Click on Config Vars, and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.

 3. Deployment on Heroku

    3.1.  Navigate to the Deploy tab.
        
    3.2.  Choose the main branch to deploy and enable automatic deployment to build Heroku every time any changes are pushed on the repository.
        
    3.3 Click on manual deploy to build the App.  When complete, click on View to redirect to the live site. 
    
### Forking the GitHub Repository

* By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account, allowing you to view and/or make changes without affecting the original repository by using the following steps:

    Log in to GitHub and locate the GitHub Repository
    At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
    You should now have a copy of the original repository in your GitHub account.

* Making a Local Clone

    Log in to GitHub and locate the GitHub Repository
    Under the repository name, click "Clone or download".
    To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    Open Git Bash
    Change the current working directory to the location where you want the cloned directory to be made.
    Type git clone, and then paste the URL you copied in Step 3.

$ git clone https://github.com/Gwgjnr/Wellness_Site

Press Enter. Your local clone will be created.

