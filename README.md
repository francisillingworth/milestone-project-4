[![Build Status](https://travis-ci.org/francisillingworth/milestone-project-4.svg?branch=master)](https://travis-ci.org/francisillingworth/milestone-project-4)


# Unicorn Attractor Issues and New Features Tracker

This project is designed as a platform on which to demonstrate skill across the full stack, from backend MySQL database management to frontend user centric development. 


## Demo

A live demo of the website can be found [here](https://milestone-project-three.herokuapp.com/)


## UX

The Unicorn Attractor Issues and New Features Tracker is a web application that allows a user log issues they are having with a fictional new app called 'Unicorn Attractor' as well as contribute new feature ideas
for the app. The business plan behind the web app is that issues and features can be logged for free, the features and issues that gain the most upvotes will then be worked on first. To make money from this, to 
upvote a feature there is a static cost of £10/upvote, in return for this money 50% of all development time will be spent working on the highest voted feature. This concept is clearly defined on the web app in the
how it works section but also as a modal pop-up on the features page that launches on the first page load of the session explaining the costs involved and the logic behind upvotinf features. 

The design was delibrately chosen to be easy to navigate and easy to understand while also conveying to the user that its purpose is actually quite technical. This technical aspect is made by using the faded image
of the circuit board in the background while keeping the navigation bars a fairly sterile blue. Meanwhile any aspect of the page that has an effect (such as the submit comment and like buttons) all use bright
colours to make them stand out and also provide insight into their purpose.

Issues and Features are listed in order of the number of likes they have. This gives the user and immediate impression of the most common issues and most sought after features but also is a useful way of showing 
the issues and features being worked on at that specific time as they will be the first to load. 

Users are all encouraged to create their own profile, visually this is not something that is forced down their throat but it is made clear throughout the site that to have any interation with the website and comminuty of users they
must make a profile and log in as otherwise the website is read-only. Aspects of the page design were  isnpired by various social media outlets, an example of this would be the originally hidden comments being made visible
by clicking the show comments button.

### User Stories

##### Registering a profile

From the home page you can chose to click either the register button on the nav bar or click the link below the login form that says register here. From here the user then just needs to enter an email address, username and password (has to be entered twice to get match) before clicking the register button. The account will then be created and the user will be logged in. This is confirmed by the message bar 'You have successfully registered' and also the nav bar will now say 'Logged in as (Username)'

##### Logging in

From the home page you can chose to click either the login button on the nav bar or just fill in the login form that loads on index.html . Enter Username and password and click login, if successful the user will be met with the message 'You have successfull logged in'. If a mistake has been made the user will get the message 'username or password is incorrect'.


##### Logging an issue/feature

To log an issue or feature the user must be logged in. Once logged in the user can navigate to the issues or feature page which are layed out the same. At the top of these pages there is a box that says 'Can't find the issue you're having? Add your issue to the list here!'. By clicking 'here' the user will be redirected to a form that requests the name of the issue/feature and then a description. Once these are completed click the 'submit new issue/feature' buttons. The user will be notified once this is done buy a massage apperaing across the top of the screen saying 'Your issue/feature has been posted!'.


##### Liking an issue

To Like an issue the user must first be logged in. Once logged in click then like button on the corresponding issue card. This will refresh the screen and will be confirmed by a message saying 'Thank you for liking this issue, the issues with the most likes will be worked on first!' as well as the issue you liked now having an extra like on its like counter.

##### Liking a feature

To Like a feature the user must first be logged in. Once logged in click then like button on the corresponding feature card. This will redirect  to a checkout preloaded for a payment of £10, enter card details and click 'Submit payment to confirm like'. The user will then either be shown an incorrect card detial message or if successful be redirected  back to features html.

##### Leaving a comment

To leave a comment on an issue or feature the user must first be logged in. Each issue and feature has its own comment form to complete. once filled in click the 'Submit new comment' button. The will be confirmed by a message saying 'your comment has been posted'.

## Features

#### Existing Features

Reister profile - Allows users to create a profile which they can then log into.

Login - Allows users to log into their profile and gain access to the interactive elements of the website

Like issues/features - Allows users to have thier say over which issues and features are acted upon first.

Comment on issues/features - Allows users to get involved as a community, share thier user stories etc. 

Pay to like a feature - Allows users to upvote a feature. This is how the website makes money.

Pagination - Makes it easier to navigate the issues and features pages as they are limited to 3 per page. This prevents information overload messy pages.


#### Features Left to Implement

I would like to add charts to show live numbers of likes in relation to each feature/issue. 

I would like to link the like button with the payment button so a like is only registered if a payment is made as opposed to how it is now where a website admin would need to monitor payments and likes.

## Technologies Used

HTML - Used for basic structure of webpage as was so structuring lists and forms on the webpage.

CSS - Used for basic styling of HTML elements

JQuery - Used to add meat to the HTML elements e.g show comments feature

Python - Used for all functionality - CRUD

Django - Framework used to run application

.
## Testing



## Deployment


The website is hosted by Heroku and is deployed from the master branch. A live demo of the website can be found [here](https://milestone-project-four.herokuapp.com/)

You can also git clone the code to run it locally on your machine via this link [Milestone Project 4 Git Hub Link](https://github.com/francisillingworth/milestone-project-4) .



## Credits


