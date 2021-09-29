# Milestone Project 04 

### Spartan Fitness Club E-Commerce Store<br/><br/>

## Table of contents
1. [Introduction](#intro)
2. [Responsive Design](#responsive_design)
3. [My Project Description and Design](#project_description)
    1. [Wire Frames](#wire_frame)
    2. [Pop up Delete Modals](#pop_modal)
    3. [Nav Bar](#nav_bar)
    4. [Hero Image](#hero_image)
    5. [Page Links and Button Navigation](#page_links)
    6. [flash messages](#flash_messages)
    7. [Search Products](#search_products)
    8. [No Image Default](#default_Image)
    9. [Footer](#footer)
4. [Utilising the 5 Planes of UX Design](#ux_design)
    1. [The Strategy Plane](#strategy_plane)
    2. [The Scope Plane](#scope_plane)
    3. [The Structure Plane](#structure_plane)
    4. [The Skeleton Plane](#skeleton_plane)
    5. [The Surface Plane](#surface_plane)
5. [Typography](#typography)
6. [User Stories/Testing](#user_stories_testing)
    1. [TESTING.md document](#external_document)
7. [Bugs and Fixes](#bug_fixes)
8. [References and Credits Section](#references_and_credits)
    1. [Technologies Used In The Project](#technologies_used)
    2. [Media](#media)
9. [Future "Nice to Have" Additions to The Website](#additions)
10. [Deployment of Project](#project_deployment)
    1. [Creating a New Project](#new_project)
    2. [Commands Utilised Throughout The Project After Changes](#commands)
    3. [How to Deploy My Milestone\_Project\_04 on Heroku](#how_to_deploy)
    4. [How to Download, View and Edit and Run this project locally](#how_to_download)
11. [My Data Base Layout and Structure](#db_structure)
12. [Previous Assessment Comments and How I Have Addressed Them](#previous_comments)
13. [Acknowledgements](#acknowledgements)
<br/><br/>

## Introduction <a name="intro"></a>

My Milestone Project 4 was envisioned by me and created based on the knowledge gained so far from this course. 
I have taken the fundamentals that I have learned from the course and applied them to this website with style and format changes. 
I have created Python, Jscript and jQuery functions where required to manipulate data, undertake logic and enable the end result back to the user.
I hope that the outcome of my works has translated into a web application UI, that shows and facilitates my understanding of the Django framework learned throughout this development module.
I feel that additions to the site can be made very easily by adding new models to the postgres database and tailoring the files within the app structure itself to suit. 
My goal was to create an application that visually appears accessible and familiar to sports and gym goers.
I also wanted to make it responsive and easy to navigate by using tailored css and css bootstrap classes.
As well as the course materials, there have been some additional code examples which I have searched for online and utilised.
These additions have been highlighted and referenced later on in this document (references and credits section).
As well as these additions I have received excellent feedback from my mentor Maranatha Ilesanmi throughout this course.
For the previous project, Maranatha has re-capped and explained the reasons for the comments I received. He has given me great advice again on how to improve so that I can attain a higher mark.
I have also added a [section](#previous_comments) in this README file, where I explain what has been implemented in this project to counter act the reasons for falling down in the last project.

## Responsive Design <a name="responsive_design"></a>

As can be seen in the screenshot below, media queries and Bootstrap classes have been used to ensure that the website is completely responsive across Desktop and Mobile devices.

![](media/readme_images/README001.png)

View the deployed project here:[ SFC ](https://ferdia-milestone-project-04.herokuapp.com/)<br/><br/>

## My Project Description and Design <a name="project_description"></a>

The Spartan Fitness Club website is a full-stack responsive website which utilises Python, JQuery & javasript methods and functions to carry out CRUD functionality using the Django framework,
a Heroku postgres database and AWS static and media file storage. 
Please see initial envisioned wireframes for desktop and mobile devices (before project start) and actual screenshots of the finished website in the sections that follow:
<br/><br/>

### Wire Frames <a name="wire_frame"></a>

This time around, I found the wire-frames extremely helpful for planning the structure and navigation throughout the site. 
The main langing page is the centre hub for all users until logged in. From here all non-admin, and non-registered user options are available through the navbar.
There are additional options available if logged in as an admin, or a registered user which will be discussed further in the document.
A number of redirects are used and placed in known locations that users that would be familiar with in keeping with good practise.

Please see below links to individual Mobile & Desktop views:

[Home Page](media/readme_images/Main_Page.png)

[Products](media/readme_images/All_Products_Page.png)

[Product Detail](media/readme_images/Product_Detail.png)

[Add/Edit Product](media/readme_images/Add_Edit_Product.png)

[Blog](media/readme_images/All_Blogs.png)

[Blog Detail](media/readme_images/Blog_Detail.png)

[Add/Edit Blog](media/readme_images/Add_Edit_Blog.png)

[Profile](media/readme_images/Profile.png)
<br/><br/>

### Pop up Delete Modals <a name="pop_modal"></a>

![](media/readme_images/README002.png)

There are 3 pop up modals used on this application. All three modals are used in conjunction with the delete options for products, blog posts, and comments.
It is a way of protecting against accidental deletion of each item by providing the user with a way of opting out if delete was pressed accidentally, 
and a way of giving the user a second chance to re-consider if they had decided to delete the item but now have changed their mind.
<br/><br/>

### Nav Bar <a name="nav_bar"></a>

![](media/readme_images/README003.png)

This project has a Fixed nav-bar and five sub-sections "All Products, Clothing, Gym, Special Offers and Blog". Once the page is scrolled the navbar follows. 
I felt that having the navbar quickly accessible from all locations of the website would benefit a potential shopper and it keeps in-line with professional sites I am familiar with.
Easy acces to the "Log In", "Log Out" and shopping bag pages are possible through the "My Account" Icon's dropdown menu and the "Shopping Bag" Icon link.
The nav-bar can be separated up into desktop (as seen above) and mobile views as seen below. 
Clicking the "Spartan Fitness" logo re-loads the main page and re-directs you back there if clicked from another location on the site.
Clicking the "All Products" link navigates the user to the all products page, displaying all products in the e-commerce store.
Clicking the "Clothing" link allows the user to see products that fall into the clothing section.
Clicking the "Gym" link allows the user to see products that fall into the gym section.
Clicking the "Special Offers" link allows the user to see products that fall into the special offers section.
Clicking the "Blog" link navigates the user to the Blog post section of the website.
The "Free Delivery Threshold" banner is static, unclickable and remains in place throughout the site.

![](media/readme_images/README004.png)
<br/><br/>

### Hero Image <a name="hero_image"></a>

![](media/readme_images/README005.png)

The Hero Image that loads upon display of the main page is of a large gym facility which shows alot of differing fitness equipment.
The image contains all of the primary colours in the centre of the image (weights), and it has a lerge quantity taken up by the colour green.
I added a blue hue to the image in photoshop which has allowed the use of purples,blues and greens which now I feel mix quite well.
The image is responsive accross all sizes of device by utilising css classes.
<br/><br/>

### Page Links and Button Navigation <a name="page_links"></a>

![](media/readme_images/README006.png)

In the image above I have placed all the href, onClick and submit type button navigations used in this project. 
All links have been incorporated with huge consideration to the users overall experience and ease of use.
It is my intention here to have the user feel a sense of familiarity by keeping everything quite similar to UI's, websites and layouts that I am familiar with using myself.
I have tried to make sure that every feature here conforms to modern best practise standards.
All links have been tested and are fully functional. The social media links in the footer open in separate tabs where required.
<br/><br/>

### Flash Messages <a name="flash_messages"></a>

![](media/readme_images/README007.png)

I have kept the Flash messages being presented back with similar styling as the flash messages in the Boutique Ado project as I really liked how they presented.
They definitely fit very well with the theme I have implemented.
The messages appear consistently at the top right of the screen under the shopping bag and convey success, error, info and warning messages.
The alert messages appear with differing colours, linked with the bootstrap classes of colours for severity.
The messages disappear when the user clicks on the "X" located at the top right of the message.
A minified version of the shopping bag appears within the success message when items are added.
<br/><br/>

### Search Products <a name="search_products"></a>

![](media/readme_images/README008.png)

The search products search bar will query the product name and description fields in the Heroku postgres database.
The user just has to type their query and then click or press "Search". The query will return items that match the descriptive search text entered.
For example, in the screenshot above, I have queried the word "shorts" and two products have returned. With the products returned,
you then have the option to sort the returned results by "Price, Rating, Name and Category". Each of those sorting methods can also be reverse ordered.
<br/><br/>

### No Image Default<a name="default_Image"></a>

![](media/readme_images/README010.png)

The default no image file is used for times when the url link may not be available, or when the user has forgotten or chosen not to upload an image.
<br/><br/>

### Footer <a name="footer"></a>

![](media/readme_images/README011.png)

I have kept the footer very simple so not to distract from what is taking place on the rest of the main page.
While being simplistic all its functions work really well. 
Its contains the following:
1. Heading text.
2. Three hover and clickable social media Icons.
3. A contact us link which generates an mailto link with your default email client (as seen below).
4. Copyright text which updates its year with the current year through an inline javascript function.
<br/><br/>

![](media/readme_images/EMAIL.png)
<br/><br/>

## Utilising the 5 Planes of UX Design <a name="ux_design"></a>

**The Strategy Plane** <a name="strategy_plane"></a>

The strategy plane here is concerned with attracting individuals who are into fitness and excercise, or those who are thinking of getting into it and considering membership options.
The main business objectives of SFC are to sell their e-commerce store products online, sell gym memberships, meal plans and promote themselves as as fitness advice and training experts (blog).
As the company grows I envision them selling more and more third party offerings through the store, making it ever more important to have a quick and easy method of adding products.
I believe the use of the blog and interactive commenting to promote upcoming events will generate large interest in the company.

**The Scope Plane** <a name="scope_plane"></a>

The app, I feel, utilises modern techniques to be in line with what is current, and trys to enhance the users experience by keeping everything sports related and familiar. 
The navbar structure will be a very familiar feature to most e-commerce users and incorporates the necessary links for logging in and signing up through the "My Account" icon.
The search bar I have kept centered and familiar looking also, and the text for the dropdown menus, I think, pre-define what is expected when the user presses them.
The displayed all products and all blogs, as well as detailed product and blog views have intuitive buttons associated with each of their views for navigating, submission, editing and deleting.
Upon all user interactions where a submission occurs (Log In, Log Out, CRUD, checkout) the user is presented with [flash messages](#flash_messages) to confirm the status of their request.
The "Add Product"/"Edit Product" and "Add Blog"/"Edit Blog" pages are designed to be very simple and easy to follow and fill out. 
The items are filled out in the order that they are displayed which will lead to better familiarity from repitition by the admin user.
The checkout page keeps in-line with what is common and modern, utilising Strip payments to complete the purchasing of products.

**The Structure Plane** <a name="structure_plane"></a>

This app is a multi-page page layout that extends from the base.html template. I have tried to keep everything simplistic and familiar.
It is navigated from top to bottom with a fixed nav-bar at the top and a footer at the bottom of the main page only. 
The nav-bar turns into a mobile friendly toggler once below a specific resolution. Underneath the nav-bar is where the “Hero-Image” is located.
The hero image is consistently placed accross all pages and has an opacity overlay for every page except the home page.
The hero image and home text are [responsive](#responsive_design) accross desktop and mobile as can be seen in previous screenshots.
The logo text and "Shop Now" button are only visible on the main page. The items common to all pages are the hero image, the navbar and the free delivery threshold banner.

If you are not a registered user, you will have pretty much full access to the site (even to make a purchase) without the option to store and view order related data, or comment on blog posts
If you are an existing user, after logging in you will have access to your profile page to view historical order data and you will be able to comment on the various blog posts that exist. 

The profile page contains historical order details, as well as a saved version of your delivery details which can be updated and saved by the user at any point.
These details are then used to populate the delivery form on the checkout page when making a purchase.

User interactions accross the site will be intuitive, familiar and consistent on all pages to ensure the user has a great UX experience.
Hoverable and clickable links, buttons are used throughout the app to present the user with easy and expected navigation results.
The hover effects will be a change in background colour (darker), and the moise pointer will change to a finger pointer when on top of clickable items.

**The Skeleton Plane** <a name="skeleton_plane"></a>

The app will have a consistently placed background image which will be responsive and appear on all pages (opacity layer, on top, on every page except the main page).
The use of [colours](#colours), [fonts](#typography) and responsive elements were carefully chosen to add user expected functionality.
Careful consideration was given to making the content well placed, clear and well presented. This was achieved by utilising contrasting colours, 
right size, style fonts and adequate spacing. In order to try and create a professional feel I was quite selective with the product images used from Unsplash.com
In this project, the Balsamic [wire frames](#wire_frame) have been a fantastic tool to envision what the end result would be.
There have been some subtle changes to the placement of elements and styles from what was originally envisioned through the wireframes.
The page is scrolled top to bottom with a "Scroll To Top" feature displaying in the bottom right margin when the page is scrolled beyond 100px.
This feature only appears on pages where the content is expected to require it.

**The Surface Plane** <a name="surface_plane"></a>

The colours and imagery used on this website, I feel, are really in line with the sports and fitness theme.
The hero image and a sports jersey that I own were the inspiration for the entire colour theme.
I have kept greens/blues as my main colour with a contrasting purple for highlighting links.
I have used white and black in standard and opaque styles where I think further contrasting is required to allow for element separation.
The remaining colours used throughout the project were picked based on complimenting the existing colours.
The palette picker I used to assist my choices was created at [www.coolers.co](https://coolors.co/) <a name="colours"></a>

![](media/readme_images/Coolors.png)

I have used subtle background shading to highlight certain text elements and the hovering and clicking of items throughout.
Keeping in line with modern UX standards, Hovering over links, buttons and text selectors causes the elements to change colour, alerting the user to the presence of their mouse pointer.
<br/><br/>

## Typography <a name="typography"></a>

The fonts used for the milestone project are: “Aclonica” and “Rubik”.

Both fonts were located and used from Google Fonts:[ Aclonica ](https://fonts.google.com/specimen/Aclonica?query=aclonica), [ Rubik ](https://fonts.google.com/specimen/Rubik?query=rubik)

![](media/readme_images/FONT.png)

I felt the contrast between Aclonica and Rubik works really well. I picked Aclonica based on the name of the website, Spartan Fitness Club. I thought the capitol letter A looked like a Spartan Warriors helmet.
I feel the bold, thick font of Aclonica with subtle shading has really played a part in defining the brand and definitely keeps in line with the warrior/gym fitness theme.
I have made subtle changes to the font colors, shadows, sizes and spacings for contrasting & responsiveness as can be seen on the finished app and in the base.css sheet. 
<br/><br/>

## User Stories/Testing <a name="user_stories_testing"></a>

**Testing Document** <a name="external_document"></a>

For this project I have created a separate testing document which details the user stories and the user testing.
Inside the testing document there are also 2 links to pdf spreadsheets. The first spreadsheet was used to create the user stories and the second 
is an excerpt from the complete manual user testing PASS Sheet which covered all app functionality and expected results.
Please click on this link: ["TESTING"](TESTING.md) to view the testing document and please click on the pdf links inside the document when required.
<br/><br/>

## Bugs and Bug Fixes <a name="bug_fixes"></a>

During the creation of this project I encountered alot of self inflicted bugs due to unfamiliarity with the new additions in this module.
It was all part of the learning process and I have become quite familiar with the django error message structure and fault finding a resolution.

Google Inspect was used to eliminate any styling and format bugs encountered. 
For any other fixes to bugs that were encountered that could not be visualised, 
I used console.log() for JS, print() for Python and displayed django template variables to a div to visualise the results.
Changes were then made from there to fix code or eliminate the bug completely.

Unfortunately during PEP8 correcting I suffered a bug which flagged an error 500 when trying to setup a new user account.
I have carried out research and tried numerous methods to break the lines length so that it meets the PEP8 standard but none have been successful.
I have consulted other students settings.py files and I can see that they have not solved the problem either, so I have left it as is.
In the future, when I am more knowlegeable in the subject area, I will return to fix the error.
Please see a screenshot below of the error with Flake8 lynting.

![](media/readme_images/VALIDATE.png)


## References and Credits Section <a name="references_and_credits"></a>

**Technologies Used In The Project** <a name="technologies_used"></a>

- The application was created utilising the Django, full-stack, framework.
- For each required function of the site a Django app was created with customizable settings.
- Stripe utilised for the payment function of the e-commerce store.
- Heroku was used to deploy the app.
- Amazon AWS was used to place the static and media files.

### Languages Used In The Project

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used to structure the content of each page.

- [CSS](https://en.wikipedia.org/wiki/CSS) was used to ensure the website was styled in accordance with my theme and ensure responsivity accross all devices with media queries.

- [javaScript](https://en.wikipedia.org/wiki/JavaScript) was used to make the site interactive as well as providing some additional functions that could not be achieved in the python code.

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was the scripting language used for the backend logic.
<br/><br/>
### Django and Django extensions used in the project

- [Django](https://www.djangoproject.com/) was used to create the project structure.

- [Django](https://django-allauth.readthedocs.io/en/latest/) allauth was used for user creation and sign-in.

- [Django](https://pypi.org/project/django-countries/) Countries was used for the checkout and profile page country field selector.

- [Django](https://django-crispy-forms.readthedocs.io/en/latest/) Crispy Forms were used to render the input forms.
<br/><br/>
### 3rd Party Additional Requirements for the project functionality and deployment

- [Stripe](https://stripe.com/ie) has been used for tprocessing online payments.

- [Heroku](https://signup.heroku.com/) was used for deployment of the app.

- [Amazon](https://aws.amazon.com/) AWS was used to store the static files and the images for the site.

- [Gunicorn](https://gunicorn.org/) Web Server Gateway used to deploy the project successfully to Heroku.
<br/><br/>

The Contents of My "requirement.txt" file:

asgiref==3.3.4

boto3==1.18.27

botocore==1.21.27

dj-database-url==0.5.0

Django==3.2.4

django-allauth==0.41.0

django-countries==7.2.1

django-crispy-forms==1.12.0

django-storages==1.11.1

gunicorn==20.1.0

jmespath==0.10.0

oauthlib==3.1.1

Pillow==8.3.0

psycopg2==2.9.1

PyJWT==2.1.0

python3-openid==3.2.0

pytz==2021.1

requests-oauthlib==1.3.0

s3transfer==0.5.0

sqlparse==0.4.1

stripe==2.60.0
<br/><br/>

**Media** <a name="media"></a>

The photos used for the hero Image and the individual products were taken from [https://unsplash.com/ ](https://unsplash.com/).

Please see list of credits below for the owner of each photo: 

* tyler-nix-Y1drF0Y3Oe0-unsplash – Photo by[ Tyler Nix ](https://unsplash.com/photos/Y1drF0Y3Oe0?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* julia-rekamie-Z72YujnOrlY-unsplash – Photo by[ Julia Rekamie ](https://unsplash.com/photos/Z72YujnOrlY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* bruce-mars-jY-GlbKeTDs-unsplash – Photo by[ Bruce Mars ](https://unsplash.com/photos/jY-GlbKeTDs?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)

* alexander-redl-d3bYmnZ0ank-unsplash – Photo by[ Alexander Redl ](https://unsplash.com/photos/d3bYmnZ0ank?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* charles-gaudreault-xXofYCc3hqc-unsplash – Photo by[ Charles Gaudreault ](https://unsplash.com/photos/xXofYCc3hqc?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)

* damir-spanic-BzJO7pO1K3g-unsplash – Photo by[ Damir Spanic ](https://unsplash.com/photos/BzJO7pO1K3g?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* alora-griffiths-aVrZMPgN_Vg-unsplash – Photo by[ Alora Griffiths ](https://unsplash.com/photos/aVrZMPgN_Vg?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* lorenzo-fatto-offidani-LjftLaNrhkw-unsplash – Photo by[ Lorenzo Fatto ](https://unsplash.com/photos/LjftLaNrhkw?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)

* anastase-maragos-lJeAWbFfQUA-unsplash – Photo by[ Anastase Maragos ](https://unsplash.com/photos/lJeAWbFfQUA?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* samuel-girven-fqMu99l8sqo-unsplash – Photo by[ Samuel Girven ](https://unsplash.com/photos/fqMu99l8sqo?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)

* nathan-dumlao-NXMZxygMw8o-unsplash – Photo by[ Nathan Dunlao ](https://unsplash.com/photos/NXMZxygMw8o?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* joshua-coleman-xo2Euf3aPMs-unsplash – Photo by[ Joshua Coleman ](https://unsplash.com/photos/xo2Euf3aPMs?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* kelly-sikkema-IZOAOjvwhaM-unsplash – Photo by[ Kelly Sikkema ](https://unsplash.com/photos/IZOAOjvwhaM?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)

* cathy-pham-3jAN9InapQI-unsplash – Photo by[ Cathy Pham ](https://unsplash.com/photos/3jAN9InapQI?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* ctrl-a-meal-replacement-03e4RajfFAE-unsplash – Photo by[ CTRL ](hhttps://unsplash.com/photos/03e4RajfFAE?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)

* hayley-kim-design-eot-ka5dM7Q-unsplash – Photo by[ Hayley Kim ](https://unsplash.com/photos/eot-ka5dM7Q?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)on[ Unsplash ](https://unsplash.com/)
  
* munbaik-cycling-clothing-gPXh9Nl7KHk-unsplash – Photo by[ Munbaik Cycling ](https://unsplash.com/@munbaik_cycling?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)

* zachary-kadolph-CoTJ4Srrl5E-unsplash – Photo by[ Zachary Kadolph ](https://unsplash.com/@zacharykadolph?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[ Unsplash ](https://unsplash.com/)
  
I’d like to say a huge thank you to the photographers who provided the content above, free of charge via Unsplash, for the creation of this E-Commerce store app.
<br/><br/>

**Content:**

The content for this site is based on research sessions carried out in preparation. 
The initial wireframes and design thoughts were in part, created based on existing online sports stores like Sports Direct & JD Sports. 

I was initially inspired by [ Sports Directs ](https://www.sportsdirect.com/) website and it laid the standard for the photo images that would be required.
The finished product looks a lot different from the Sports Direct website, but I feel it ticks all the boxes and remains true to the initial wireframes and colour scheme.
<br/><br/>



## My Data Base Layout and Structure <a name="db_structure"></a>

Please see below, a line diagram created with [Draw.io](https://app.diagrams.net/) which depicts my Database scheme for the categories and associated products.

I have placed the first category "Mens Activewear" and the first product "Mens Workout Set 1" at the top of the Schema as an example.

![](media/readme_images/SCHEMA.png)

## Previous Assessment Comments and How I Have Addressed Them <a name="previous_comments"></a>

To Be Completed.
<br/><br/>

## Acknowledgements <a name="acknowledgements"></a>

I'd like to say a special thank you to my mentor Maranatha Ilesanmi. Maranatha has provided excellent constructive feedback at all of our project review meetings.
I have made many great changes to my projects based on Maranatha's wisdom and huge wealth of knowledge in the industry standards.
Once again I have learned alot from him and I am thankful for all the constructive feedback given during our sessions.