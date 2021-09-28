# App Testing & User Stories

# Contents

- [Code Check Validation](#code-check-validation)
- [Responsiveness of The App and Applied Testing](#responsiveness-of-the-app-and-applied-testing)
- [Physical Device Testing](#physical-device-testing)
- [Varying Browser Testing](#varying-browser-testing)
- [Using Lighthouse Chrome Dev-Tools](#using-lighthouse-chrome-dev-tools)


# Code Check Validation

## All CSS files were checked with the W3C CSS Validator

All files were validated by direct input at https://jigsaw.w3.org/css-validator/#validate_by_input

Each file was edited until there were no errors or warnings remaining.

![CSS_PASS](Testing_User_Stories_Images/CSS_Pass.png)

## All HTML files were checked with the W3C Markup Validator 

All individual site pages were validated by URI at https://validator.w3.org/

Each file was edited until there were no errors or warnings remaining.

A warning was showing for the JS script "type" attribute which was contained in every template that has JS scripts included at the bottom.

![HTML_PASS](Testing_User_Stories_Images/HTML_Pass.png)

To counter act this I have removed the type attribute and placed a comment outside the initial closing script chevron. Please see below:

![JS_TYPE](Testing_User_Stories_Images/Remove_JS_type.png)

![JS_TYPE_COMMENT](Testing_User_Stories_Images/JS_type_comment.png)

## All Javascript code and scripts were checked with jshint

These tests were carried out by copying and pasting the JS code into the input field at https://jshint.com/

![JSHINT_Pass](Testing_User_Stories_Images/JSHINT_Pass.png)

The code was edited until there were no errors but some warnings still remain.

There are multiple warnings relating to the use of "$" suggesting it is an undefined variable.

There is one reference to "Stripe" suggesting it is also an undefined variable.

I have left these as is as they are only warnings and dont impact the intended functions of the code.

## All Python files were assessed using Flake8 in Gitpod and PEP8 online checker. 

All .py files were initially checked in the Gitpode IDE using Flake8 lynting and hints to correct errors, spacing and line size.

After editing until no errors were present, each individual .py files contents was copy and pasted into the input field at http://pep8online.com/

The PEP8 online checker shows no errors in all .py files.

![PEP8_Pass](Testing_User_Stories_Images/PEP8_Pass.png)

# Responsiveness of The App and applied Testing

The responsiveness of the website was assessed and achieved using Google Chrome Inspect Tools.

I manually assessed the views through the array of different size devices and resolutions and made adjustments to CSS until happy with its cross device display.

Please see a reference screenshot below:

![Google_Inspect](Testing_User_Stories_Images/Google_Inspect.png)

# Physical Device Testing

The physical devices available to me for testing were: Iphone6, Iphone7, Lenovo Tablet and a Dell 15inch Laptop with extended 21inch display monitor.

# Varying Browser Testing

The browsers used during creation and testing phases of the APP were: Google Chrome, Mozilla Firefox and Safari.

# Using Lighthouse Chrome Dev-Tools

I am unfamiliar in this territory at present but took some time to install the Chrome addon package. 

I utilised the returned reports to maximise efficiencies accross the project.

The performance section varied and this is mainly due to third party script includes like jQuery, Popper and Stripe.

Please see a screenshot below of the landing page where Accessibility, Best Practices and Search Engine Optimisation have been awarded 100%

![Chrome_LH](Testing_User_Stories_Images/Chrome_LH.png)

