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
    5. [Header & Description Text](#header_description)
    6. [Page Links and Button Navigation](#page_links)
    7. [flash_messages](#flash_messages)
    8. [Search Products](#search_recipes)
    9. [Default Product Image](#default_recipe)
    10. [Footer](#footer)
4. [Utilising the 5 Planes of UX Design](#ux_design)
    1. [The Strategy Plane](#strategy_plane)
    2. [The Scope Plane](#scope_plane)
    3. [The Structure Plane](#structure_plane)
    4. [The Skeleton Plane](#skeleton_plane)
    5. [The Surface Plane](#surface_plane)
5. [Typography](#typography)
6. [User Stories](#user_stories)
    1. [External pdf User Stories Document Link](#external_document)
7. [Bugs and Fixes](#bug_fixes)
8. [References and Credits Section](#references_and_credits)
    1. [Code](#code)
    2. [Media](#media)
9. [User Testing](#testing)
    1. [External pdf Manual Testing Document Link](#testing_procedure)
10. [Future "Nice to Have" Additions to The Website](#additions)
11. [Deployment of Project](#project_deployment)
    1. [Creating a New Project](#new_project)
    2. [Commands Utilised Throughout The Project After Changes](#commands)
    3. [How to Deploy My Milestone\_Project\_04 on Heroku](#how_to_deploy)
    4. [How to Download, View and Edit and Run this project locally](#how_to_download)
12. [My Data Base Layout and Structure](#db_structure)<br/><br/>
13. [Previous Assessment Comments and How I Have Addressed Them](#previous_comments)<br/><br/>
14. [Acknowledgements](#acknowledgements)<br/><br/>

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