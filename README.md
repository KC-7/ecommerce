![Banner](readme_images/general/banner.gif)

![GitHub last commit](https://img.shields.io/github/last-commit/kc-7/ecommerce?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/kc-7/ecommerce?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/kc-7/ecommerce?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/kc-7/ecommerce?color=yellow&style=for-the-badge)

# onlineAI.art | E-Commerce Project

## Live Links

[onlineAI.art](https://onlineai.art/)

[onlineAI.art - Admin Portal](https://onlineai.art/admin/)

[Heroku App Link](https://kc-ecommerce-434e6f88dca9.herokuapp.com/)

[Facebook Page](https://www.facebook.com/people/Onlineaiart/61550214234067/)

---

## Project Preview 

### Project Description

This is a django project for an E-Commerce Store which specializes in offering custom printed products, each designed uniquely using AI image generation.

The site allows users to view and add products to their bags, search and filter products by category, price, etc. They can checkout using Stripe payments. The can view about pages and blog posts. They can sign up for a profile, save delivery information, view past orders etc. An algorithimically generaterad avatar called an aiPunk is created for each user.

Admin users can create, modify or delete the about pages, blog posts and products. They can also access a custom admin portal for additional admin functionality.

### Main Site Preview

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

TBC

### Admin Portal Preview

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

TBC

---

## Table of Contents

- [onlineAI.art | E-Commerce Project](#onlineaiart---e-commerce-project)
  * [Live Links](#live-links)
  * [Project Preview](#project-preview)
    + [Project Description](#project-description)
    + [Main Site Preview](#main-site-preview)
    + [Admin Portal Preview](#admin-portal-preview)
  * [Table of Contents](#table-of-contents)
  * [Business Overview](#business-overview)
    + [Purpose of Website](#purpose-of-website)
    + [Business Type](#business-type)
    + [Target Audience](#target-audience)
    + [Primary Marketing Strategy](#primary-marketing-strategy)
    + [Marketing Solutions to Meet Audience Needs](#marketing-solutions-to-meet-audience-needs)
  * [User Story Test Cases](#user-story-test-cases)
    + [View and Navigation](#view-and-navigation)
    + [Registration and User Accounts](#registration-and-user-accounts)
    + [Sorting and Searching](#sorting-and-searching)
    + [Purchasing and Checkout](#purchasing-and-checkout)
    + [Admin and Store Management](#admin-and-store-management)
    + [Additional Features](#additional-features)
  * [Design](#design)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + [Wireframes](#wireframes)
    + [Data Schema](#data-schema)
  * [Site Features](#site-features)
    + [Custom Admin Portal](#custom-admin-portal)
    + [Custom Admin Features](#custom-admin-features)
    + [E-commerce functionality](#e-commerce-functionality)
      - [Stripe Integration & Test Card Details](#stripe-integration---test-card-details)
    + [CKEditor](#ckeditor)
      - [Set Up Guide](#set-up-guide)
    + [Custom About Pages (CRUD)](#custom-about-pages--crud-)
      - [Project Conception](#project-conception)
      - [Usability](#usability)
    + [CRUD Operations](#crud-operations)
      - [Custom Editor](#custom-editor)
    + [Custom Blog Posts (CRUD)](#custom-blog-posts--crud-)
      - [Project Conception](#project-conception-1)
      - [Usability](#usability-1)
    + [CRUD Operations](#crud-operations-1)
      - [Custom Editor](#custom-editor-1)
    + [Algorithmically Generated Pixel Art Avatars](#algorithmically-generated-pixel-art-avatars)
      - [What are CryptoPunks?](#what-are-cryptopunks-)
      - [Project Conception and Implementation](#project-conception-and-implementation)
      - [Development and Research Process](#development-and-research-process)
      - [Leveraging Existing Work](#leveraging-existing-work)
      - [Customization and Integration](#customization-and-integration)
      - [Administrative Enchancement](#administrative-enchancement)
    + [User Feedback, Error Handeling and 404 Redirection](#user-feedback--error-handeling-and-404-redirection)
  * [Dependencies & Their Use Cases](#dependencies---their-use-cases)
  * [Deployment & Local Development](#deployment---local-development)
    + [Deployment](#deployment)
      - [Create the Live Database](#create-the-live-database)
      - [Heroku App Setup](#heroku-app-setup)
      - [Preparation for Deployment in GitPod](#preparation-for-deployment-in-gitpod)
      - [Generate a SECRET KEY & Updating Debug](#generate-a-secret-key---updating-debug)
      - [Set up AWS hosting for static and media files](#set-up-aws-hosting-for-static-and-media-files)
      - [Creating AWS groups, policies and users](#creating-aws-groups--policies-and-users)
      - [Connecting Django to our S3 bucket](#connecting-django-to-our-s3-bucket)
      - [Setting up Stripe](#setting-up-stripe)
    + [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
    + [Environment Variables](#environment-variables)
  * [Custom Domain & SSL Cert](#custom-domain---ssl-cert)
    + [Custom Domain Set Up on Namecheap](#custom-domain-set-up-on-namecheap)
    + [SSL Cert & HTTPS Redirection Set Up on Cloudflare](#ssl-cert---https-redirection-set-up-on-cloudflare)
    + [Cloudflare Scecurity](#cloudflare-scecurity)
  * [Product Creation Process](#product-creation-process)
    + [AI Images usign ComfyUI with Stable Diffusion XL](#ai-images-usign-comfyui-with-stable-diffusion-xl)
      - [Setup Guide](#setup-guide)
    + [Custom Product using Printify](#custom-product-using-printify)
    + [Product Descriptions using ChatGPT](#product-descriptions-using-chatgpt)
    + [Custom Products Fixtures](#custom-products-fixtures)
  * [Bugs & Issues](#bugs---issues)
    + [Allauth Templates Directory Not Found](#allauth-templates-directory-not-found)
    + [Heroku Invalid Credentials Provided](#heroku-invalid-credentials-provided)
    + [Issue while Initializing the Heroku Git Remote](#issue-while-initializing-the-heroku-git-remote)
    + [Programmatic Access for AWS User](#programmatic-access-for-aws-user)
    + [Navbar too large](#navbar-too-large)
    + [Order number too long](#order-number-too-long)
    + [Navbar not displayed correctly on Profile](#navbar-not-displayed-correctly-on-profile)
    + [Images sizes too large](#images-sizes-too-large)
    + [Custom CKEditor not responding well](#custom-ckeditor-not-responding-well)
    + [Custom CKEditor not responding well](#custom-ckeditor-not-responding-well-1)
  * [Testing](#testing)
    + [Manual Testing for User Stories](#manual-testing-for-user-stories)
    + [Automated Testing](#automated-testing)
      - [Coverage Installation](#coverage-installation)
      - [Run Django tests with coverage](#run-django-tests-with-coverage)
      - [Generate Coverage Report](#generate-coverage-report)
      - [Run All Tests](#run-all-tests)
      - [Results for Automated Tests](#results-for-automated-tests)
      - [Coverage Report](#coverage-report)
    + [Lighthouse Testing](#lighthouse-testing)
    + [Console Log Testing](#console-log-testing)
    + [W3 Nu HTML Checker Testing](#w3-nu-html-checker-testing)
    + [W3C Jigsaww CSS Validation Testing](#w3c-jigsaww-css-validation-testing)
    + [JSHint JS Testing](#jshint-js-testing)
    + [Flake8 Python Testing](#flake8-python-testing)
    + [Responsiveness Testing](#responsiveness-testing)
      - [Visual Testing on Physical Devices](#visual-testing-on-physical-devices)
      - [Visual Testing using Google Inspect](#visual-testing-using-google-inspect)
      - [Visual Testing using AmIRepsponsive](#visual-testing-using-amirepsponsive)
  * [Future Development](#future-development)
  * [Summary of charges and monitoring costs](#summary-of-charges-and-monitoring-costs)
  * [Web Marketing & Search Engine Optimization (SEO)](#web-marketing---search-engine-optimization--seo-)
    + [Facebook Page](#facebook-page)
    + [Mailchimp Newsletter](#mailchimp-newsletter)
    + [Google Search Console](#google-search-console)
    + [Google Business](#google-business)
    + [Google Analytics](#google-analytics)
    + [GDPR](#gdpr)
  * [Learning Goals](#learning-goals)
    + [Learning Goals 1: Integrate an e-commerce payment system and product structure in a cloud-hosted Full-Stack web application](#learning-goals-1--integrate-an-e-commerce-payment-system-and-product-structure-in-a-cloud-hosted-full-stack-web-application)
    + [Learning Goals 2: Employ advanced User Experience Design to build a commercial-grade Full Stack Web Application](#learning-goals-2--employ-advanced-user-experience-design-to-build-a-commercial-grade-full-stack-web-application)
    + [Learning Goals 3: Employ Search Engine Optimisation (SEO) techniques to improve audience reach](#learning-goals-3--employ-search-engine-optimisation--seo--techniques-to-improve-audience-reach)
    + [Learning Goals 4: Create a secure Full Stack Web application with Authentication and role-based Authorization functionality](#learning-goals-4--create-a-secure-full-stack-web-application-with-authentication-and-role-based-authorization-functionality)
    + [Learning Goals 5: Employ marketing techniques to create brand reach](#learning-goals-5--employ-marketing-techniques-to-create-brand-reach)
    + [Learning Goals 6: Understand the fundamentals of E-commerce applications](#learning-goals-6--understand-the-fundamentals-of-e-commerce-applications)
    + [Learning Goals 7: Additional Learning Outcomes (M)](#learning-goals-7--additional-learning-outcomes--m-)
    + [Learning Outcome 8: Additional Learning Outcomes (D)](#learning-outcome-8--additional-learning-outcomes--d-)
  * [Resources & Credits](#resources---credits)
    + [Useful Links & Resources](#useful-links---resources)
    + [Credits & Special Thanks](#credits---special-thanks)
  * [Conclusion & Contact](#conclusion---contact)

TBC

---

## Business Overview

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Purpose of Website

The purpose of the website is a robust e-commerce platform that meets the needs of its potential customers. The site is designed to sell products with custom printed AI artwork such as clothing, homeware and tech products.

### Business Type

The site primarily uses a B2C (business to consumer) business model. The site caters directly to consumers and is designed to be easy to interact and allow for swift checkout without the need for user registration. This allows for potential customers to make a purchase as quickly and as easily as possible. Return customers can set up an account which allows them to save their delivery information to simply the checkout process even further.

### Target Audience

The target audience is fulti-faceted and includes but is not limited to the below consumer types. We envisage our target audience will be both male and female, mainly ranging from 18 to 60 years old. 

- **Tech Enthusiasts:** Indviduals interested in AI technology and generative art
- **Design and Art Enthusiasts:** Individuals interested in art and design
- **E-Commerce Shoppers:** Regular online shoppers looking for unique products

### Primary Marketing Strategy

The primary marketing strategy is to leverage the uniqueness of the product range, our products are not available anywhere else as they are custom designed for the store. Our unique products range will attract general E-Commerce Shoppers, our custom designs will attract Art Enthusiasts and our tech related blog posts will attract Tech Enthusiasts. 

### Marketing Solutions to Meet Audience Needs

Alongside our primary marketing strategies we will implement additional marketing solutions to meet the needs of our target audience:

- **Social Media:** A dedicated [Facebook Business Page](https://www.facebook.com/people/Onlineaiart/61550214234067/) has been created to showcase our unique designs and products. We will also create Twitter and Instagram pages to expand our out reach on different platforms. Alongside this we can set up a Discord channel to create a social community. We will also be able to share our custom images and products on additional platforms such as Reddit, TikTok, etc.
- **Engaging Content:** We intend to utilize the Blog and About applications on the website to create engaging content about generative art and AI technology which will improve user engagement on the site.
- **Email newsletter:** We have set up a newsletter using MailChimp so we can send free, regular newsletters to our subscribers.
- **Affiliant Marketing:** We intend to utilize the blog platform for affiliate marketing for non-competing products such as generative AI services etc. 
- **Collaborations:** We intend to collaborate with influencers in the tech and fashion industries to showcase our products.
- **Promotions and Discounts:** We have implemented a clearance and sale section on the site. We will also send discounts to our newsletter subscribers in future.
- **Advertising & SEO:** Monitor our analytics using Google Analytics and monitor search results with Google Search Console. Potentially set up Google Business and Google Advertising in future to attract additional customers.

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## User Story Test Cases

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

[Click here to see the Github User Stories Board](#)

### View and Navigation
1. As a Shopper, I want to be able to view a list of products so that I can select some to purchase.
2. As a Shopper, I want to be able to view a list of products so that I can quickly find products I'm interested in without having to filter through all products.
3. As a Shopper, I want to be able to view individual product details so that I can identify the price, description, product rating, product image, and available sizes.
4. As a Shopper, I want to be able to quickly identify deals, clearance items, and special offers so that I can take advantage of special savings on products I'd like to purchase.
5. As a Shopper, I want to be able to easily view the total of my purchases at any time so that I can avoid spending too much.

### Registration and User Accounts
6. As a Site User, I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.
7. As a Site User, I want to be able to easily login and logout so that I can access my personal account information.
8. As a Site User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
9. As a Site User, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.
10. As a Site User, I want to be able to have a personalized user profile so that I can view my personal order history and confirmations, and save my payment information.

### Sorting and Searching
11. As a Shopper, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced, and categorically sorted products.
12. As a Shopper, I want to be able to sort a specific category of product so that I can find the best priced or best rated product in a specific category, or sort the products in that category by name.
13. As a Shopper, I want to be able to sort multiple categories of products simultaneously so that I can find the best priced or best rated products across broad categories, such as "clothing" or "homeware".
14. As a Shopper, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
15. As a Shopper, I want to be able to easily see what I've searched for and the number of the results so that I can quickly decide whether the product I want is available.

### Purchasing and Checkout
16. As a Shopper, I want to be able to easily select the size and the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product quantity or size.
17. As a Shopper, I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all of the items I will receive.
18. As a Shopper, I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
19. As a Shopper, I want to be able to easily enter my payment information so that I can check out quickly and without issues.
20. As a Shopper, I want to be able to feel that my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
21. As a Shopper, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
22. As a Shopper, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.

### Admin and Store Management
23. As a Store Owner, I want to be able to add a product so that I can add new items to my store.
24. As a Store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
25. As a Store Owner, I want to be able to delete a product so that I can remove items that are no longer for sale.

### Additional Features
26. As a Site User, I want to be able to sign up for a mailing list so that I can stay up to date with the latest products and deals.
27. As a Site User, I want to be able to find out more information so that I can find out additional information about the company such as shipping, etc.
28. As a Site User, I want to be able to navigate the content easily and quickly so that I can find the content that I am looking for.
29. As a Store Owner, I want to set up a blog so that I can draw more site attention, recommend my products to the target audience, and potentially affiliate marketing and sponsered articles.
30. As a Store Owner, I want create a unique custom avatar with unique traits for each user so that I can enhance the personalized shopping experience to create increased customer engagement and retention.
31. As a Store Owner, I want to allow admin to control the products, blogs and about pages via the site and dedicated admin panel so that I can allow admins to run the store without the need for website modifications.

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Design

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Colour Scheme

The below custom colour scheme was designed and set up for the site. 

    :root {
        /* Electric Pink */
        --pink: #ffa0ff;
        /* Cosmic Cyan */
        --cyan: #00FFFF;
        /* Mystical Purple */
        --purple: #800080;
        /* Transcendent Teal */
        --teal: #008080;
        /* Divine Gold */
        --gold: #FFD700;
        /* Energetic Orange */
        --orange: #FFA500;
        /* Onyx Black */
        --black: #000000;
        /* Gun Metal Grey */
        --grey: #808080;
        /* Silver Blush */
        --silver: #dddddd;
        /* Pearl White */
        --white: #FFFFFF;
    }

<img src="readme_images/general/colors1.png" alt="Color Palette" style="max-width: 40%;">

### Typography

The font Audiowide has been used throughout the site to give it a modern, futuristic feel. This was imported into the CSS file from the main base template using [Google Fonts](https://fonts.google.com/).

</summary> <img src="readme_images/google/googleFontsAudiowide.png" alt="Audiowide Font" style="max-width: 40%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

### Wireframes

I created the wireframes for the Home, Products and Product Page using [Figma](https://www.figma.com/)

<img src="readme_images/wireframes/wireframe-home.png" style="max-width: 60%;">

<img src="readme_images/wireframes/wireframe-products.png" style="max-width: 60%;">

<img src="readme_images/wireframes/wireframe-product.png" style="max-width: 60%;">

### Data Schema

I used [Lucid Chart](https://lucid.app/) to create the **Entity Relationship Diagram**:

<img src="readme_images/data_schema/entity-relationship-diagram.png" style="max-width: 60%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Site Features

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Custom Admin Portal

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

The admin portal was customized by using the following [installation guide for Jazzmin](https://django-jazzmin.readthedocs.io/installation/): 

1. Install the latest `pypi` release with `pip3 install -U django-jazzmin` in the terminal

2. Add jazzmin to your `INSTALLED_APPS` __before__ `django.contrib.admin`:

    INSTALLED_APPS = [
        'jazzmin',
        'django.contrib.admin',
        [...]
    ]

3. Add [custom jazzmin configuration settings](https://django-jazzmin.readthedocs.io/configuration/) to settings.py.

See my custom Jazzmin settings ⬇️

    # Custom Jazzmin Settings
    JAZZMIN_SETTINGS = {
        # title of the window (Will default to current_admin_site.site_title if absent or None)
        "site_title": "onlineAI.art Admin",

        # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
        "site_header": "onlineAI.art",

        # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
        "site_brand": "onlineAI.art",

        # Logo to use for your site, must be present in static files, used for brand on top left
        "site_logo": SITE_LOGO,

        # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
        "login_logo": SITE_LOGO,

        # Logo to use for login form in dark themes (defaults to login_logo)
        "login_logo_dark": SITE_LOGO,

        # Custom user avatar function to display their Punk
        "user_avatar": SITE_LOGO,

        # Welcome text on the login screen
        "welcome_sign": "Welcome to the onlineAI.art Admin Portal",

        # Copyright on the footer
        "copyright": "onlineAI.art Ltd 2023",

        # List of model admins to search from the search bar, search bar omitted if excluded
        # If you want to use a single search field you dont need to use a list, you can use a simple string
        "search_model": ["auth.User", "blog.blogpage", "about.aboutpage"],

        # Top Menu:

        # Links to put along the top menu
        "topmenu_links": [

            # Url that gets reversed (Permissions can be added)
            {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

            # external url that opens in a new window (Permissions can be added)
            {"name": "Site Link", "url": LIVE_LINK, "new_window": True},

            # App with dropdown menu to all its models pages (Permissions checked against models)
            {"app": "products"},

            # model admin to link to (Permissions checked against model)
            {"model": "avatar.avatar"},
        ],

        # User Menu:

        # Additional links to include in the user menu on the top right ("app" url type is not allowed)
        "usermenu_links": [
            {"name": "Site Link", "url": LIVE_LINK, "new_window": True},
            {"model": "products.product"},
            {"model": "products.category"},
            {"model": "auth.user"},
            {"model": "avatar.avatar"},
            {"model": "blog.blogpage"},
            {"model": "about.aboutpage"},
            {"name": "Developer", "url": "https://github.com/kc-7", "new_window": True},
        ],
    }

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

---

### Custom Admin Features

The admin panel also allows the amdministrator to: 

- Sort, Filter & Search Products by name, sku and has_sizes

- Batch select products and update if they have sizes or not, this was very useful when setting up the products catalogue

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

---

### E-commerce functionality

The site has integrated the following apps to allow customers to interact with and purchase items: bag, checkout & products.

It also has a profile app to allow the users to save their delivery information.

#### Stripe Integration & Test Card Details

[Stripe](https://stripe.com/) has been integrated into the project to handle the payment system.

Stripe is currently in developer mode for the website to allow test payments to be processed to ensure the site's functionality is operating as intended.

**Test Card Details:**

Here are some test card details you can use to simulate different scenarios at checkout:

| Type                   | Card No             | Expiry                  | CVC                | ZIP                  |
| :--------------------- | :------------------ | :---------------------- | :----------------- | :------------------- |
| Success                | 4242 4242 4242 4242 | A future date (04/24)   | Any 3 digits (242) | Any 5 digits (42424) |
| Requires authorization | 4000 0027 6000 3184 | A future date           | Any 3 digits       | Any 5 digits         |
| Declined               | 4000 0000 0000 0002 | A future date           | Any 3 digits       | Any 5 digits         |

For more details on setting up Stripe elements to accept payment, refer to the [Stripe Documentation](https://stripe.com/docs/).

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

---

### CKEditor

<img src="readme_images/ckeditor/ckeditor-mobile.png" style="max-width: 60%;">

I installed the [CKEditor Classic Editor](https://ckeditor.com/docs/ckeditor5/latest/installation/getting-started/predefined-builds.html#classic-editor) to allow customisable text inputs for the Admins to add About Pages. This allows the site management team to add and update these pages without the need of a web developer. The CKEditor easily allows them to customise the text. 

#### Set Up Guide

1. In your HTML page add an element that CKEditor 5 should replace:

    <div id="editor"></div>

1. Load the classic editor build (here, the CDN location is used):

    <script src="https://cdn.ckeditor.com/ckeditor5/39.0.1/classic/ckeditor.js"></script>

Alternatively, you may install CKEditor 5 from npm:

    npm install --save @ckeditor/ckeditor5-build-classic

1. Then bundle it together with your app.

Call the ClassicEditor.create() method.

    <script>
        ClassicEditor
            .create( document.querySelector( '#editor' ) )
            .catch( error => {
                console.error( error );
            } );
    </script>

I have customized the editor to only display certain suitable options, for example H1 has been removed as it used for the Title for the page so there is no need to have it in the content section, the customizations are added as a postload js script on the pages where the editor has been implemented, eg create & edit blog and create & edit about pages.

See my custom CKEditor settings below ⬇️

    <script>
    ClassicEditor
        .create(document.querySelector('#id_content'), {
        toolbar: ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote'],
        heading: {
            options: [{
                model: 'paragraph',
                title: 'Paragraph',
                class: 'ck-heading_paragraph'
            },
            {
                model: 'heading2',
                view: 'h2',
                title: 'Heading 2',
                class: 'ck-heading_heading2'
            },
            {
                model: 'heading3',
                view: 'h3',
                title: 'Heading 3',
                class: 'ck-heading_heading3'
            },
            {
                model: 'heading4',
                view: 'h4',
                title: 'Heading 4',
                class: 'ck-heading_heading4'
            }
            ]
        }
        })
        .then(editor => {
        window.editor = editor;
        })
        .catch(error => {
        const errorMessage = 'There was a problem initializing the editor.'
        });
    </script>

Admin users can access the additional editor functionality via the admin portal.

<img src="readme_images/ckeditor/ckeditor-admin.png" style="max-width: 60%;">

The custom editor is disabled on very small mobile devices to ensure responsiveness.

<img src="readme_images/ckeditor/ckeditor-removed-xs-mobile.png" style="max-width: 60%;">

---

### Custom About Pages (CRUD)

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

#### Project Conception

The implementation of this app felt like a neccessity as I wanted an easy way for admin users to modify site about page details to ensure customers are kept up to date with relevant site information without the requirement for someone with coding knowledge to make the modifications. 

#### Usability

All site users can read the about pages, they are accessible by the footer nav links or by clicking on the account drop menu in the main navigation bar. The about page serves as a list of the pages and the specific about pages contain the content. This provide users with direct access to the information and effecitivly serves its intended purpose.

### CRUD Operations

This application offers full CRUD functionality for the admin users to Create, Read, Update & Destroy about pages, both on the main site and the admin portal.

#### Custom Editor

I felt the standard text editor was insufficent for creating and modifying about pages so I have added the CKEditor. I have detailed the customization and implementation of the CKEditior in this README. This editor allows admins to adjust heading sizes, add bold, italic, links, etc. when creating the about pages. I have chosen to restrict access to heading size 1, colours and fonts so that the website it maintained and styled consistently with the sites colour schema and typography. Admin users can access the additional editor functionality via the admin portal. In the admin portal they have full access to the custom editor and can also modify the pages as HTML which allows them to add videos or embded content. This was useful when creating the Contact page with embed Google Maps location alongside the embed Youtube video in the Generative AI Video. The custom editor is disabled on very small mobile devices to ensure responsiveness.

---

### Custom Blog Posts (CRUD)

#### Project Conception

To gain site visitors, I have set up a blog application that allows the admin users to generate blog posts. This will be an effective way to attract users to the site and also serve as a vehicle for affiliate marketing links in future. The site onlineai.art will be able to created AI, art or tech related blogs that are relevant to the business's target audience.

#### Usability

All site users can read the blog pages, they are accessible by the footer nav links or by clicking on the account drop menu in the main navigation bar. The blog page serves as a list of the pages, its designed to be visually appealing to the user and displays the Blog titles alongside a short preview of the content and a preview of the image used in the blog post to draw the users interest. It also utilises sorting to rotate the preview direction for each post in an alternating order and then paginates the list into multiple pages which can be controlled by the page navigation buttons at the end of the blog posts page. The blog post detail pages include the Title, Preview Image and Content. The pages also allow direct navigation to older and newer posts to keep the user reading the blog posts.

### CRUD Operations

This application offers full CRUD functionality for the admin users to Create, Read, Update & Destroy about pages, both on the main site and the admin portal.

#### Custom Editor

A similar approach was taken when setting up the custom CKEditor for the blog as the about application. Admins have limited options when creating modifications using the Create or Edit blog pages as intented to ensure the site is maintained with consitent content. The admins can however access the full editor by the admin portal, this will allow them to make unusual styling modifications or add embeded content if ever required. The custom editor is disabled on very small mobile devices to ensure responsiveness.

---

### Algorithmically Generated Pixel Art Avatars

<img src="readme_images/general/aipunk.png" style="max-width: 100px;">

The custom avatar app takes inspiration from the CryptoPunks NFT series, but what are Crypto Punks?

#### What are CryptoPunks?

"The CryptoPunks are a collection of 10,000 unique, algorithmically generated digital artworks on the Ethereum blockchain. Each CryptoPunk is a distinct pixel art image of a character with various attributes like hairstyles, accessories, and more. They are considered one of the first examples of non-fungible tokens (NFTs), which are digital tokens representing ownership of a specific item or piece of content. CryptoPunks hold value due to their rarity and historical significance in the NFT space, often being bought, sold, and traded as collectible digital assets."

#### Project Conception and Implementation

I wanted to experiment with this concept and learn more about the generation process so decided to implement this into the project, each new user has a unique avatar, called an aiPunk, algorithmically generated for them when they sign up for an account. This avatar is there digital identify on the onlineAI.art platform, it can not be modified, exchanged or destroyed by the user, its unique and one off to them (it intentionally does not include CRUD functionality). It also acts as a security feature, you can ensure you are connected the real onlineai.art domain as when you sign in and access your profile, you'll be greeted by a familiar face. We do not store or hold your personal credit or debit card information on our servers so you can be sure you are safely logged into our site before entering your payment information to make any purchase.

#### Development and Research Process

I started off reseaching the algorithmic generative process online and founds a lot of relevent resounces and medium articles etc. I found this [Youtube video on creating crypto punk style images using python](https://www.youtube.com/watch?v=o0qNS_pOVqw) which was a great resource for learning the creation process.

#### Leveraging Existing Work

I ended up finding this small [CryptoPunk themed GitHub Repo by Snoozesecurity](https://github.com/snoozesecurity/cryptopunkgenerator) and decided to use the logic, probabilities and image layers to server the core functionality for this application.

#### Customization and Integration

The codebase was then extensively modified to fit the Model-View-Controller (MVC) structure within the Django project. I also added extra functionality by creating a custom view to create the images on new user registration and also another view to display the attributes.

The custom avatar image was added to the user's profile and I also created a custom avatar template so the user can view their avatar and its unique custom attributes, this page is accessible via the users profile or account dropdown menu.

#### Administrative Enchancement

A custom admin view was created to display the avatar image and their attributes. It also allows for custom sorting.

<img src="readme_images/general/aipunks.png" style="max-width: 60%;">

---

### User Feedback, Error Handeling and 404 Redirection

The site has integrated user feedback by displaying toast messages for info, success, errors etc. Apps have built in error handeling to notify users of issues in a user friendly manner. 404 page has been configured to show when the page the user is looking for can not be found.

<img src="readme_images/general/aipunks.png" style="max-width: 60%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Dependencies & Their Use Cases

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

The project relies on a range of Python packages to ensure its smooth operation and delivery of features. Here's a brief overview of each dependency in the `requirements.txt` and its use case:

| **Package**           | **Version** | **Use Case**                                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------------------------|
| asgiref               | 3.7.2       | Interface between your web service and ASGI server, ensuring asynchronous capabilities.          |
| boto3                 | 1.28.5      | Amazon Web Services (AWS) SDK for Python, allowing for AWS service integrations.                 |
| botocore              | 1.31.5      | Core foundation for the AWS SDK for Python, powering `boto3`.                                    |
| dj-database-url       | 0.5.0       | Utilities to utilize database URLs with Django for configuration simplicity.                     |
| Django                | 3.2.20      | The core Django framework powering the entire web application.                                   |
| django-allauth        | 0.41.0      | Provides authentication, registration, and account management features.                          |
| django-ckeditor       | 6.6.1       | Rich-text WYSIWYG editor for Django models and forms.                                            |
| django-countries      | 7.2.1       | Utility to handle country fields in Django models and forms.                                     |
| django-crispy-forms   | 1.14.0      | Enables rendering of Django forms with crispy Bootstrap styles.                                  |
| django-jazzmin        | 2.6.0       | A fresh take on the Django admin interface, for improved UX.                                     |
| django-js-asset       | 2.1.0       | Helps with generating URLs for your static files with Django.                                    |
| django-storages       | 1.13.2      | Collection of custom storage backends for Django, notably for cloud storage.                     |
| gunicorn              | 21.1.0      | A Python WSGI HTTP Server for deploying Django applications in production environments.          |
| jmespath              | 1.0.1       | Allows querying JSON documents, used internally by `boto3` and `botocore`.                       |
| numpy                 | 1.24.4      | Fundamental package for numerical computations in Python.                                        |
| oauthlib              | 3.2.2       | OAuth library integration for Django, used with `django-allauth`.                                |
| Pillow                | 10.0.0      | Python Imaging Library, for handling image processing tasks in Django.                           |
| psycopg2              | 2.9.6       | PostgreSQL adapter for Django, allows using PostgreSQL as the database backend.                  |
| python3-openid        | 3.2.0       | Provides OpenID support for Python, used in conjunction with `django-allauth` for authentication.|
| pytz                  | 2023.3      | World timezone definitions for Python, utilized by Django for timezone-aware operations.         |
| requests-oauthlib     | 1.3.1       | Provides OAuthlib authentication support for Python's `requests` module.                         |
| s3transfer            | 0.6.1       | Amazon S3 Transfer Manager for Python, used internally by `boto3`.                               |
| sqlparse              | 0.4.4       | A utility to parse SQL strings, used by Django during database operations.                       |
| stripe                | 5.5.0       | Enables Stripe payment integrations for Django, allowing secure payment processing.              |
| urllib3               | 1.26.16     | HTTP client for Python, used internally by several packages for making HTTP requests.            |

For installation, simply run `pip3 install -r requirements.txt`.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Deployment & Local Development

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Deployment

The project is deployed using Heroku.  🚀

To deploy the project, follow these steps:

#### Create the Live Database

In development, we have been using the sqlite3 database. However, this is only suitable for development, so we need to create a new external database accessible by Heroku.

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click the "Create New Instance" button on the top right.
2. Name the plan (your project name is a good choice), select the "Tiny Turtle Plan" (the free plan), and choose the region that is closest to you, then click the "Review" button.
3. Check the details and click "Create Instance" in the bottom right.
4. Go to the dashboard and select the newly created database.
5. Copy the URL (you can click the clipboard icon to copy).

#### Heroku App Setup

1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the "New" button in the top right corner and select "Create New App."
2. Give your app a name (this must be unique), select the region that is closest to you, and then click the "Create App" button at the bottom left.
3. Open the "Settings" tab and create a new config var of `DATABASE_URL`. Paste the database URL you copied from ElephantSQL into the value (the value should not have quotation marks around it).

#### Preparation for Deployment in GitPod

1. Install `dj_database_url` and `psycopg2` (both needed for connecting to the external database you've just set up):

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. Update your requirements.txt file with the packages just installed:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

    (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

    ```python
    DATABASES = {
        'default': dj_database_url.parse('paste-elephantsql-db-url-here')
    }
    ```

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```

8. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.

9. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
          }
        }
    ```

10. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

11. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

    ```Procfile
    web: gunicorn ecommerce.wsgi:application
    ```

12. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
    ```

13. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

    ```python
    ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
    ```

14. Save, add, commit and push the changes to GitHub. You can then also initialise the Heroku git remote in the terminal and push to Heroku with:

    ```bash
    heroku git:remote -a {app name here}
    git push heroku master
    ```

15. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

16. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

#### Generate a SECRET KEY & Updating Debug

1. Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.
2. [Djecrety's Django Secret Key Generator](https://djecrety.ir/) is an example of a site we could use to create our secret key. Create a new key and copy the value.
3. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key we just created. Click add.
4. In settings.py we can now update the `SECRET_KEY` variable, asking it to get the secret key from the environment, or use an empty string in development:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

5. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

6. Save, add, commit and push these changes.

#### Set up AWS hosting for static and media files

! NOTE: These instructions are subject to change slightly in future versions of AWS.

1. Sign up or login to your [aws amazon account](https://aws.amazon.com) on the top right by using the manage my account button and then navigate to S3 to create a new bucket.
2. The bucket will be used to store our files, so it is a good idea to name this bucket the same as your project. Select the region closest to you. In the object ownership section we need to select ACLs enabled and then select bucket owner preferred. In the block public access section uncheck the block public access box. You will then need to tick the acknowledge button to make the bucket public. Click create bucket.
3. Click the bucket you've just created and then select the properties tab at the top of the page. Find the static web hosting section and choose enable static web hosting, host a static website and enter index.html and error.html for the index and error documents (these won't actually be used.)
4. Open the permissions tab and copy the ARN (amazon resource name). Navigate to the bucket policy section click edit and select policy generator. The policy type will be S3 bucket policy, we want to allow all principles by adding `*` to the input and the actions will be get object. Paste the ARN we copied from the last page into the ARN input and then click add statement. Click generate policy and copy the policy that displays in a new pop up. Paste this policy into the bucket policy editor and make the following changes: Add a `/*` at the end of the resource value. Click save.
5. Next we need to edit the the cross-origin resource sharing (CORS). Paste in the following text:

    ```json
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```

6. Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

#### Creating AWS groups, policies and users

1. Click the services icon on the top right of the page and navigate to IAM - manage access to AWS services. On the left hand navigation menu click user groups and then click the create group button in the top right. This will create the group that our user will be placed in.
2. Choose a name for your group - for example manage-boutique-ado, and click the create policy button on the right. This will open a new page.
3. Click on the JSON tab and then click the link for import managed policy on the top right of the page.
4. Search for S3 and select the one called AmazonS3FullAccess, then click import.
5. We need to make a change to the resources, we need to make resources an array and then change the value for resources. Instead of a `*` which allows all access, we want to paste in our ARN. followed by a comma, and then paste the ARN in again on the next line with `/*` at the end. This allows all actions on our bucket, and all the resources in it.
6. Click the next: tags button and then the next:review .
7. Give the policy a name and description (e.g. boutique-ado-policy | Access to S3 bucket for boutique ado static files.) Click the create policy button.
8. Now we need to attach the policy we just created. On the left hand navigation menu click user groups, select the group and go to the permissions tab. Click the add permissions button on the right and choose attach policies from the dropdown.
9. Select the policy you just created and then click add permissions at the bottom.
10. Now we'll create a user for the group by clicking on the user link in the left hand navigation menu, clicking the add users button on the top right and giving our user a username (e.g. boutique-ado-staticfiles-user). Select programmatic access and then click the next: permissions button.
11. Add the user to the group you just created and then click next:tags button, next:review button and then create user button.
12. You will now need to download the CSV file as this contains the user access key and secret access key that we need to insert into the Heroku config vars. Make sure you download the CSV now as you won't be able to access it again.

#### Connecting Django to our S3 bucket

1. Install boto3 and django storages and freeze them to the requirements.txt file.

    ```bash
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```

2. Add `storages` to the installed apps in settings.py
3. Add the following code in settings.py to use our bucket if we are using the deployed site:

    ```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }
        
        AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
        AWS_S3_REGION_NAME = 'enter the region you selected here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

4. In Heroku we can now add these keys to our config vars:

    | KEY | VALUE |
    | :--- | :--- |
    | AWS_ACCESS_KEY_ID | The access key value from the amazon csv file downloaded in the last section |
    | AWS_SECRET_ACCESS_KEY | The secret access key from the amazon csv file downloaded in the last section |
    | USE_AWS | True |

5. Remove the DISABLE_COLLECTSTATIC variable.
6. Create a file called custom_storages.py in the root and import settings and S3Botot3Storage. Create a custom class for static files and one for media files. These will tell the app the location to store static and media files.
7. Add the following to settings.py to let the app know where to store static and media files, and to override the static and media URLs in production.

    ```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

8. Save, add, commit and push these changes to make a deployment to Heroku. In the build log you should be able to see that the static files were collected, and if we check our S3 bucket we can see the static folder which has all the static files in it.
9. Navigate to S3 and open your bucket. We now want to create a new file to hold all the media files for our site. We can do this by clicking the create folder button on the top right and naming the folder media.

#### Setting up Stripe

1. We now need to add our Stripe keys to our config vars in Heroku to keep these out of our code and keep them private. Log into Stripe, click developers and then API keys.
2. Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.
3. Now we need to add the WebHook endpoint for the deployed site. Navigate to the WebHooks link in the left hand menu and click add endpoint button.
4. Add the URL for our deployed sites WebHook, give it a description and then click the add events button and select all events. Click Create endpoint.
5. Now we can add the WebHook signing secret to our Heroku config variables as STRIPE_WH_SECRET.
6. In settings.py:

    ```python
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```

---

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for [this project](https://github.com/KC-7/ecommerce).

3. Click on the fork button in the top right of the page.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for [this project](https://github.com/KC-7/ecommerce).

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute's custom template and have opened the repository in GitPod as this will have been set up for you).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

    ```bash
    pip3 install -r requirements.txt
    ```

8. Set up required 3rd party accounts.

9. Create a .env file with the required environment variables.

10. Apply database migrations and create a superuser account.

        python manage.py migrate

        python manage.py createsuperuser

11. Run the Django development server.

        python manage.py runserver

---

### Environment Variables

I set the local Environment Config Variables on GitPod workspaces buy you can also set it up as a `env.py` file (note: `env.py` is already included in the `.gitignore` file).

I have set up the deployed Environment Config Variables on Heroku, see below for list of inclusions:

<img src="readme_images/heroku/heroku-config-vars.png" style="max-width: 60%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Custom Domain & SSL Cert

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

I set up a custom domain with SSL certification to improve the authencity of the online e-commerce store. The custom domain on Namecheap cost €3 and the Cloudflare account is free.

### Custom Domain Set Up on Namecheap

1. Sign up / login in to Namecheap (or alt domain registrar however please note the following how to is written for Namecheap). Find and purchase suitable domain. While purchasing the domain you should set up Domain Privacy to protect your identity, Namecheap offer this service for free however other registrars charge for this service. 

<img src="readme_images/namecheap/namecheap-1.png" style="max-width: 60%;">

1. Add your new domain name to `ALLOWED_HOSTS` your `settings.py` file. Your allowed hosts should now look like the following so its accessible locally, on heroku and on the custom domain: 

    `ALLOWED_HOSTS = ['.onlineai.art', '.herokuapp.com', '.gitpod.io', 'localhost']`

1. Use the following in the terminal to check if migrations are required. If needed run as per usual.

    `python3 manage.py makemigrations --dry-run`

    `python3 manage.py migrate --plan`

1. Commit changes to GitHub as per usual: `git add .` ➡️  `git commit -m "Added custom domain to settings.py"` ➡️ `git push`.

1. Deploy site on Heroku via the Heroku Dashboard, this will be done automatically when you made the above commit to GitHub if you have Automatic Deploys set up on Heroku.

1. Go to Heroku ➡️ Your App ➡️ Settings ➡️ Domains ➡️ Add Domain ➡️ Enter your custom domain name (eg: customdomain.tdl) ➡️ Submit ➡️ Copy the generated "DNS Target".

1. Go to Namecheap (if you have a parking page set up turn it off now) ➡️ Your Domain ➡️ Advanced DNS ➡️ Host Records ➡️ Add New Record ➡️ Type: Alias Record, Host: @, Target: [Paste your Heroku DNS Target Value], TTL: Automatic ➡️ Submit.

1. Check your new domain URL to see if the page loads (eg. http://customdomain.tdl). Note, we have not set up www. or https yet. 

1. To set up the www. subdomain, go back to Heroku ➡️ Set up new domain as per previous step except this time add www. to the custom domain url (eg. http://customdomain.tdl) ➡️ Copy the new generated "DNS Target".

1. Go back to Namecheap ➡️ Your Domain ➡️ Advanced DNS ➡️ Host Records ➡️ Add New Record ➡️ Type: CNAME, Host: www, Target: [Paste your Heroku DNS Target Value], TTL: 1 min ➡️ Submit.

1. Test your customdomain with the www. subdomain: (eg. http://www.customdomain.tdl). It may take a couple of minutes to work.

1. Use [DNS Checker](dnschecker.org) website to see if the domain has propegated successfully.

<img src="readme_images/general/dns-checker.png" style="max-width: 60%;">

### SSL Cert & HTTPS Redirection Set Up on Cloudflare

1. Sign in to / Set up Cloudflare account.

1. From the Cloudflare Home, go to ➡️ Add a site ➡️ Enter your domain name ➡️ Select Free Plan ➡️ Review DNS Records & Continue (No changes required) ➡️ From Change Your Nameservers, copy the Nameservers (1 & 2).

1. Open Namecheap in new tab, go to ➡️ Your domain ➡️ Domain ➡️ Nameservers ➡️ Custom DNS ➡️ Copy the nameservers from Cloudflare in above step to the Nameservers 1 & 2 ➡️ Submit.

1. Go back to Cloudfare and click confirm to check the Nameservers ➡️ Configure Domain Settings: Automatic HTTPS = Yes, always use HTTPS = Yes, Optimize preformace with Brotli = Yes ➡️ Done.

1. Click "Check Nameservers" to confirm above steps have worked (this may take a while). When ready you will see a "Cloudlflare is protecting your site" confirmation message on the Cloudflare site overview.

1. Your site will now redirect to do HTTPS and will have a valid SSL Certificate (eg. https://customdomain.tdl / https://www.customdomain.tdl).

<img src="readme_images/general/https-ssl.png" style="max-width: 60%;">

<img src="readme_images/cloudflare/cloudflare-dns.png" style="max-width: 60%;">

<img src="readme_images/cloudflare/cloudflare-overview.png" style="max-width: 60%;">

### Cloudflare Scecurity

Cloudlfare options a range of options to provide additional protection for your site against malicous traffic. 

It has notified me about a lot of bot traffic, presumably due to registering the site on a custom domain, that have tried to gain root or env access such as the below example, there has also been a noticable amount of traffic from Tor and Russia:

<img src="readme_images/cloudflare/firewall-alert-get-env-cloudflare.png" style="max-width: 60%;">

<img src="readme_images/cloudflare/firewall-alert-cloudflare.png" style="max-width: 60%;">

Alonside threat alerts, it also shows bot and crawler traffic, example google and apple bots:

<img src="readme_images/cloudflare/cloudflare-threats-crawlers.png" style="max-width: 60%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Product Creation Process

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

I used fixtures files to upload the bulk of the categories and products, the categories fixtures were the same as the Boutique Ado project as I used this project as inspiration for my site. The products fixtures was created by enterinf the details for my custom products, to assist with process, I created custom names and then used ChatGPT to create the descriptionss for the products. I generated the unique AI images using SDXL on ComfyUI which was run locally on my PC, as it takes time to generate the images, I created a custom list of prompts and then set up a que so that I could generate a lot of unique images over a couple of hours. I then used Printfy to create the unqiue product images by adding the images I generated to products from their catalogue and downloading the images. The site could be used with an API on OnlineAI.art to sell the products by print on demand, so once the site accepts the payment, it will send the order to Printify to create and dispatch the custom product, however this was not implemented for the scope of this project, it has however been listed as a potential future development.

<img src="readme_images/general/mugs.png" style="max-width: 60%;">

### AI Images usign ComfyUI with Stable Diffusion XL

The majority of the images used for the creation of products or added to articles on the site where generated using ComfyUI with SDXL and refiner (ver:0.9).

Previouslly I was using Automatic1111 for local AI image generation however you will need to use ComfyUI if you would like to utilize the new SDXL and refiner models.

The image is initially generated using your positive and negative prompts using the SDXL base model. The base image is then refined by reviewing your prompts again and then modifying the base image with the refiner model. The refined image is returned with noticable improvements over the base output, this can also be upscalled if required.

See below guide to set up ComfyUI with SDXL base and refiner models locally. Note you will need a nVidea GPU with minimum 10gb vram, alternativly you could research setting it up using Google Collab. If this sounds like too much work for you, you can generate images for FREE (currently set to 5 per day per user) on my django website with DALL-E 2 integrated for creating custom images, [Cre8ai.art](cre8ai.art), just sign up and go to generate art, enter your prompt and hit generate, its that simple. You can then download your image by selecting the download button, its free and yours to use how you'd please and its watermark free!

<img src="readme_images/general/painting.png" style="max-width: 60%;">

#### Setup Guide

To create images using SDXL v1.0 and the node-based interface ComfyUI, follow these steps:

1. **Download SDXL v1.0 Models:**
   - Download both the base and refiner models from HuggingFace.co: [SDXL-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [SDXL-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0).
   - For image upscaling, use NMKD Superscale x4, available at Icedrive.net using [this link](https://icedrive.net/s/14BM8qlGO6).

2. **Get ComfyUI:**
   - Download ComfyUI using this [direct download GitHub link](#https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_cu118_or_cpu.7z).
   - Extract the downloaded file using 7-Zip.
   - Place the downloaded models in the folder: `ComfyUI_windows_portable\ComfyUI\models\checkpoints`.
   - If you downloaded the upscaler, place it in the folder: `ComfyUI_windows_portable\ComfyUI\models\upscale_models`.

3. **Download Sytan's SDXL Workflow:**
   - Get the JSON workflow file from [this link](#link-to-json-workflow).
   - Save the downloaded JSON file.

4. **Start ComfyUI:**
   - Run `run_nvidia_gpu.bat` to open ComfyUI in your web browser.
   - Click the "Load" button and select the JSON workflow file you downloaded.

5. **Run Your Prompt:**
   - Connect models: In the yellow Refiner Model box, select `sd_xl_refiner_1.0.safetensors`. In the yellow Base Model box, select `sd_xl_base_1.0.safetensors`.
   - If you downloaded the upscaler, choose it in the Upscale Model node.
   - Run the default prompt by clicking "Queue Prompt".
   - Observe faster generation times compared to AUTOMATIC1111.
   - Right-click the image and choose "Save Image" to download it.

**Settings to Explore:**
- **Linguistic Positive and Supporting Terms:** Use CLIP_G for natural language sentences and CLIP_L for comma-separated tags.
- **Fundamental Negative:** Set the negative prompt here.
- **Image Resolution:** Optimal at 1024 x 1024 or equivalent total pixels.
- **Steps:** Default value of 20 is good for high-quality images.
- **Base CFG:** Adjust for prompt adherence and freedom.
- **Seed:** Optionally set a seed for consistent results.
- **Refiner CFG:** Default value of 7.5 is recommended.
- **Positive and Negative Aesthetic Scores:** Influence image aesthetics based on score bias.

**Additional Resources**

You can find more information on setting up this application using the following resources: 

- [Set up tutorial by Yubin on aituts.com](https://aituts.com/comfyui-sdxl/) - I used the links and info from this guide to recreate above tutorial as I have ver0.9 installed instead of the new ver1.0.
- [Pixoverts Youtube Beginners Guide](https://www.youtube.com/watch?v=yamusLEyt4g) - Here is a detailed video if you are interesting in learning more about this process.

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

### Custom Product using Printify

I created the product images by adding the gennerated AI images to print on demand products using [Printful](https://www.printful.com/)

To do this, simply set up an account, go to the product catalogue, select your product to edit, import image and adjust positioning then save the modifed product with images.

<img src="readme_images/general/printify.png" style="max-width: 60%;">

<img src="readme_images/general/suitcase.png" style="max-width: 60%;">

TBC

### Product Descriptions using ChatGPT

I used ChatGPT to create meaningful, creative, SEO friendly, product descriptions and titles by giving it brief details on my store, target audience and the products I was going to list.

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

TBC

### Custom Products Fixtures

I added all of the images, titles and description to the custom products fixtures file, `products.json`. This allowed me to dd the majority of the listed products simultaneously. I later added additional products using the admin accounts.

I loaded the custom product fixtures file to Heroku using the following command: 

    heroku run python3 manage.py loaddata products/fixtures/products.json -a kc-ecommerce

<img src="readme_images/general/TBC.png" style="max-width: 60%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Bugs & Issues

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

I have documented some of the bugs and issues I have encountered through out the project for future reference below:

### Allauth Templates Directory Not Found

**Issue**

The following file path used in the Boutique Ado tutorial that I was following to set up the basics does not exist in the project directories:

    cp -r ../.pip-modules/lib/python3.7/site-packages/alluth/templates/* ./templates/allauth/

**Resolution**

To find the correct file path for the allauth packages, follow these steps:

1. Start the Python interpreter by running the `python` command in the terminal:
2. Once the Python interpreter starts, enter the `help('allauth')` command to access the Python help system:
3. The help information for the allauth package will be displayed, including the path to the site-packages directory where it is installed.
4. Copy the site-packages path from the output and replace [your site-package path] in the command `cp -r [your site-package path]/allauth/templates/* ./templates/allauth/` with the actual path.
5. Run the modified command to copy the allauth templates to the appropriate directory, I used:
    `cp -r /workspace/.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`

---

### Heroku Invalid Credentials Provided

**Issue**

When attempting to disable static using `heroku config:set DISABLE_COLLECTSTATIC=1 --app kc-ecommerce` as part of the deployment to Heroku, it returned ___Invalid credentials provided___ and gives an option to login to CLI via web browser.

When attempting to login through the browser, it directs to a page that says ___IP address mismatch___.

When attempting to login to Heroku via the terminal using `heroku login -i`, it would return the following error message when using my accounts email address and password: 

    ›   Error: Invalid credentials provided.
    ›
    ›   Error ID: unauthorized

**Resolution**

To resolve this issue: 

1. Login to Heroku via terminal using: `heroku login -i`.
2. Enter your email address.
3. Go to your __Heroku Dashboard__ in a new tab.
4. Go to __Account Settings__ ➡️ __Applications__ ➡️ __Authorizations__.
5. Select __Create Authorization__ ➡️ Enter a Description (Project Name) ➡️ __Confirm__.
6. Copy the __Authorization token__ and use it as your password back in the terminal.
7. You should now be able to login and continue with the deployment.

---

### Issue while Initializing the Heroku Git Remote

**Issue**

Unable to push to Heroku first attempt.

    gitpod /workspace/ecommerce (main) $ git push heroku main
    fatal: 'heroku' does not appear to be a git repository
    fatal: Could not read from remote repository.
    Please make sure you have the correct access rights
    and the repository exists.

**Resolution**

I initialized the the git remote by using the following code `heroku git:remote -a your-heroku-project-name-here` and was then able to successfully push to Heroku.

    gitpod /workspace/ecommerce (main) $ heroku git:remote -a kc-ecommerce
    set git remote heroku to https://git.heroku.com/kc-ecommerce.git

    gitpod /workspace/ecommerce (main) $ git push heroku main
    Enumerating objects: 363, done.
    ...

**Additional Heroku Tips**

Use the following commands to interact with Heroku once logged in: 

1. Make Migrations:

    `heroku run python3 manage.py makemigrations -a -kc-ecommerce`


2. Migrate:

    `heroku run python3 manage.py migrate -a -kc-ecommerce`


3. Load Fixtures:

    `heroku run python3 manage.py loaddata products/fixtures/products.json -a kc-ecommerce`

    `heroku run python3 manage.py loaddata products/fixtures/categories.json -a kc-ecommerce`

---

### Programmatic Access for AWS User

**Issue**

Since the walkthrough Boutique Ado video tutorial and updated text guide by the Code Institute, the AWS layout has changed.

Previously setting up programmatic access was an option during User set up however now you need to set it up after the account has been created so that you can get your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

**Resolution** 

To get an `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for the user, follow these steps: 

1. Create User
2. In the IAM section, select Users
3. Select the new user
4. Select Security Credentials
5. Select 'Other'
6. Save your access keys to Heroku config vars

---

### Navbar too large

**Issue**

The navbar was too large for small devices, the checkout element was dropping onto a new row. 

**Resolution**

I resolved this issue by adding the following CSS media query: 

    @media (max-width: 400px) {
        .navbar {
            padding-left: 0;
            padding-right: 0;
        }
    }

---

### Order number too long

**Issue**

The order number was too long to be displayed correctly on smaller devices, it was impacting the styling for the order confirmation page. 

**Resolution**

I resolved this issue by using the truncate feature to restrict it to 16 characters instead of displaying all 32: 

    `<p class="mb-0">{{ order.order_number|truncatechars:16 }}</p>`

---

### Navbar not displayed correctly on Profile

**Issue**

The navbar was not being displayed correctly on the profiles view, it was being positioned at the end of the container instead of the end of the page like the rest of the site. 

**Resolution**

I identified that a closing div tag, `</div>`, was missing from the end of the `profile.html` template. The navbar was correctly styled after the missing tag was enetered.

---

### Images sizes too large

**Issue**

A lot of images sizes not appropriatly sized for web pages.

**Resolution**

I used [TinyPNG](https://tinypng.com/) to reduce the image sizes.

<img src="readme_images/general/tinypng.png" style="max-width: 60%;">

I converted the homepage background images to WEBP files using [Convertio](https://convertio.co/png-webp/).

Ideally all of the images should be served in WEBP format going forward but converting the file types for the exisiting images would require the database urls for the images to be updated as well, all further images will be uploaded in WEBP format.

<img src="readme_images/aws/s3-delete.png" style="max-width: 60%;">

<img src="readme_images/aws/s3-upload.png" style="max-width: 60%;">

---

### Custom CKEditor not responding well

**Issue**

The CKEditor on the Add About, Edit About, Add Blog & Edit Blog Pages was not responding well on devices with a screen width below 380px. 

**Resolution**

To resolve this issue I tried removing buttons and adjusting formatting for the smaller devices but it still render correctly.

I added the below JS to the CKEditor script to disable the editor on devices with screen width below 380px:

    if (window.innerWidth >= 380) {
    ... [REDACTED FOR BREVITY] ...
    } else {
    // Fallback UI for small screens here if needed
    let textarea = document.querySelector('#id_content');
    if (textarea) {
        textarea.style.width = '100%';
        textarea.placeholder =
        "Simple editor mode enabled. Please use a larger screen to enable the integrated HTML editor.";
        alert(
        'Simple editor mode enabled. For a better experience, please use a larger screen to endable the integrated HTML editor.'
        );
    }

The alert is only triggered on the edit pages as the placeholder is not visible behind the text. A future UX improvement could be to trigger a modal or toast (using toastify) instead of an alert.

---

### Custom CKEditor not responding well

**Issue**

I have set it up so that you can add HTML to the blogs through the admin panel which works well when creating and editing text. It also allows the admin to add embed items such as iframes for Youtube or Google Maps. Unfortuntly when you try to edit a page with an embeded item, the code for the embed part is not displayed.

**Resolution**

This minor bug is outstanding and does not affect the MVP, the uploaded pages still work as intended.


[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Testing

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Manual Testing for User Stories

| **User Story Number** | **User Story Description**                                 | **User Story Test**                                             | **Image**     | **Passed Test** | **Test Result** |
|-----------------------|-----------------------------------------------------------|-----------------------------------------------------|-----------|-----------------|-----------------|
| 1                     | As a Shopper, I want to be able to view a list of products. | Navigate to the main product page. Check if a list of products displays. | ![test-image-1](#) | ✅              | TBC             |
| 2                     | As a Shopper, I want a quick product view.                 | Check if a "Quick View" or "Highlight" section exists on the main page. | ![test-image-1a](#) | ✅           | TBC             |
| 3                     | As a Shopper, I want to view individual product details.   | Click on a product. Verify that detailed info (price, rating, sizes, etc.) appears. | ![test-image-2](#) | ✅         | TBC             |
| 4                     | As a Shopper, I want to identify deals and special offers.  | Check for a "Deals" or "Clearance" section or tags on products indicating a sale. | ![test-image-3](#) | ✅         | TBC             |
| 5                     | As a Shopper, I want to view my purchase total.            | Add items to cart. Check if a constantly updated total appears somewhere visible. | ![test-image-4](#) | ✅        | TBC             |
| 6                     | As a Site User, I want to register for an account.         | Navigate to registration. Complete registration form and submit. | ![test-image-5](#) | ✅           | TBC             |
| 7                     | As a Site User, I want to login and logout.                | Log in with a test account and then log out.          | ![test-image-6](#) | ✅           | TBC             |
| 8                     | As a Site User, I want password recovery.                  | Click "Forgot Password" and follow recovery process.   | ![test-image-7](#) | ✅           | TBC             |
| 9                     | As a Site User, I want email confirmation on registration. | Register and check email for a confirmation message.   | ![test-image-8](#) | ✅           | TBC             |
| 10                    | As a Site User, I want a personalized user profile.        | Log in and navigate to the profile. Check if personal data, orders, and saved payment info appear. | ![test-image-9](#) | ✅        | TBC             |
| 11                    | As a Shopper, I want to sort the list of available products. | Use sorting options like best rated, best priced, or by category on the product page. | ![test-image-10](#) | ✅    | TBC             |
| 12                    | As a Shopper, I want to sort a specific category of product. | Navigate to a category and use sorting options for the best price or rating. | ![test-image-11](#) | ✅      | TBC             |
| 13                    | As a Shopper, I want to sort multiple categories of products. | Use filters to sort multiple categories simultaneously by the best price or rating. | ![test-image-12](#) | ✅ | TBC             |
| 14                    | As a Shopper, I want to search for a product by name.       | Use the search bar to find a product by name or description. | ![test-image-13](#) | ✅        | TBC             |
| 15                    | As a Shopper, I want to easily see what I've searched for.  | Search for a product and verify the search terms and number of results are displayed. | ![test-image-14](#) | ✅ | TBC             |
| 16                    | As a Shopper, I want to select the size and quantity when purchasing. | Choose a product and select different size and quantity options. | ![test-image-15](#) | ✅   | TBC             |
| 17                    | As a Shopper, I want to view items in my bag.                | Add items to the bag and view them in the shopping cart or bag page. | ![test-image-16](#) | ✅    | TBC             |
| 18                    | As a Shopper, I want to adjust the quantity in my bag.       | Change the quantity of a product in the shopping cart or bag. | ![test-image-17](#) | ✅        | TBC             |
| 19                    | As a Shopper, I want to enter my payment information easily. | Proceed to checkout and enter payment information.        | ![test-image-18](#) | ✅        | TBC             |
| 20                    | As a Shopper, I want to feel that my information is safe.    | Check for security badges and HTTPS in the checkout process. | ![test-image-19](#) | ✅      | TBC             |
| 21                    | As a Shopper, I want to view an order confirmation after checkout. | Complete checkout and verify the order confirmation page. | ![test-image-20](#) | ✅ | TBC             |
| 22                    | As a Shopper, I want email confirmation after checkout.       | Complete checkout and check email for a confirmation message. | ![test-image-21](#) | ✅      | TBC             |
| 23                    | As a Store Owner, I want to add a product.                   | Use the admin panel to add a new product and verify its appearance on the site. | ![test-image-22](#) | ✅   | TBC             |
| 24                    | As a Store Owner, I want to edit/update a product.           | Edit a product's details in the admin panel and verify changes on the site. | ![test-image-23](#) | ✅ | TBC             |
| 25                    | As a Store Owner, I want to delete a product.                | Delete a product from the admin panel and verify its removal from the site. | ![test-image-24](#) | ✅  | TBC             |
| 26                    | As a Site User, I want to sign up for a mailing list.        | Sign up for the mailing list and verify subscription (e.g. welcome email). | ![test-image-25](#) | ✅ | TBC             |
| 27                    | As a Site User, I want to find out more information.         | Navigate to pages like "About Us," "Shipping Information," etc. | ![test-image-26](#) | ✅   | TBC             |
| 28                    | As a Site User, I want to navigate the content easily.       | Test site navigation, ensuring it's intuitive and quick.  | ![test-image-27](#) | ✅          | TBC             |
| 29                    | As a Store Owner, I want to set up a blog.                   | Create a blog post through the admin panel and verify its appearance on the site. | ![test-image-28](#) | ✅ | TBC             |
| 30                    | As a Store Owner, I want a unique custom avatar for users.   | Customize an avatar for a user profile and verify its appearance. | ![test-image-29](#) | ✅ | TBC             |
| 31                    | As a Store Owner, I want admin control of products, blogs, etc. | Use the admin panel to control various site aspects and verify changes. | ![test-image-30](#) | ✅ | TBC             |

---

### Automated Testing

Thirty three automated tests were created for the project using ChatGPT. They are located in the tests.py files in the following apps: about, avatar, bag, blog, checkout, home, products & profiles. These were created to support the thorough manual testing process.

#### Coverage Installation

The following code was used to install the `coverage` package:

    pip3 install coverage

#### Run Django tests with coverage

The following code is used to initiate the tests for each app:

    coverage run manage.py test your_app_name

#### Generate Coverage Report

The following code is used to generate the coverage report:

    coverage report

#### Run All Tests

The following code was used to run all tests in the project: 

    python3 manage.py test

#### Results for Automated Tests

No issues with the 33 automated tests: 

    System check identified no issues (0 silenced).
    .................................
    ----------------------------------------------------------------------
    Ran 33 tests in 3.241s

    OK

#### Coverage Report 

See the coverage report below: ⬇️

| Name                                                  | Stmts | Miss | Cover |
|-------------------------------------------------------|-------|------|-------|
| about/__init__.py                                     |     0 |    0 |  100% |
| about/admin.py                                        |    14 |    0 |  100% |
| about/apps.py                                         |     4 |    0 |  100% |
| about/forms.py                                        |     8 |    0 |  100% |
| about/migrations/0001_initial.py                      |     5 |    0 |  100% |
| about/migrations/0002_alter_aboutpage_content.py      |     5 |    0 |  100% |
| about/migrations/__init__.py                          |     0 |    0 |  100% |
| about/models.py                                       |     8 |    1 |   88% |
| about/tests.py                                        |    40 |    0 |  100% |
| about/urls.py                                         |     3 |    0 |  100% |
| about/views.py                                        |    71 |   24 |   66% |
| avatar/__init__.py                                    |     0 |    0 |  100% |
| avatar/admin.py                                       |    16 |    4 |   75% |
| avatar/apps.py                                        |     4 |    0 |  100% |
| avatar/generate.py                                    |   125 |   48 |   62% |
| avatar/migrations/0001_initial.py                     |     7 |    0 |  100% |
| avatar/migrations/0002_auto_20230730_1422.py          |     4 |    0 |  100% |
| avatar/migrations/0003_alter_avatar_image.py          |     4 |    0 |  100% |
| avatar/migrations/__init__.py                         |     0 |    0 |  100% |
| avatar/models.py                                      |     9 |    0 |  100% |
| avatar/probability.py                                 |     6 |    0 |  100% |
| avatar/tests.py                                       |    40 |    0 |  100% |
| avatar/urls.py                                        |     3 |    0 |  100% |
| avatar/views.py                                       |    21 |    4 |   81% |
| bag/__init__.py                                       |     0 |    0 |  100% |
| bag/admin.py                                          |     1 |    0 |  100% |
| bag/apps.py                                           |     4 |    0 |  100% |
| bag/contexts.py                                       |    28 |   12 |   57% |
| bag/migrations/__init__.py                            |     0 |    0 |  100% |
| bag/models.py                                         |     1 |    0 |  100% |
| bag/templatetags/__init__.py                          |     0 |    0 |  100% |
| bag/templatetags/bag_tools.py                         |     5 |    1 |   80% |
| bag/tests.py                                          |    31 |    7 |   77% |
| bag/urls.py                                           |     3 |    0 |  100% |
| bag/views.py                                          |    70 |   29 |   59% |
| blog/__init__.py                                      |     0 |    0 |  100% |
| blog/admin.py                                         |    31 |    6 |   81% |
| blog/apps.py                                          |     4 |    0 |  100% |
| blog/forms.py                                         |    10 |    0 |  100% |
| blog/migrations/0001_initial.py                       |     6 |    0 |  100% |
| blog/migrations/0002_blogpage_image.py                |     4 |    0 |  100% |
| blog/migrations/__init__.py                           |     0 |    0 |  100% |
| blog/models.py                                        |     9 |    1 |   89% |
| blog/tests.py                                         |    40 |    0 |  100% |
| blog/urls.py                                          |     3 |    0 |  100% |
| blog/views.py                                         |    83 |   25 |   70% |
| blog/widgets.py                                       |     7 |    0 |  100% |
| checkout/__init__.py                                  |     1 |    0 |  100% |
| checkout/admin.py                                     |    12 |    0 |  100% |
| checkout/apps.py                                      |     5 |    0 |  100% |
| checkout/forms.py                                     |    18 |   11 |   39% |
| checkout/migrations/0001_initial.py                   |     7 |    0 |  100% |
| checkout/migrations/0002_order_user_profile.py        |     5 |    0 |  100% |
| checkout/migrations/__init__.py                       |     0 |    0 |  100% |
| checkout/models.py                                    |    51 |    1 |   98% |
| checkout/signals.py                                   |     9 |    1 |   89% |
| checkout/tests.py                                     |    16 |    0 |  100% |
| checkout/urls.py                                      |     4 |    0 |  100% |
| checkout/views.py                                     |    91 |   75 |   18% |
| checkout/webhook_handler.py                           |    77 |   61 |   21% |
| checkout/webhooks.py                                  |    28 |   19 |   32% |
| ecommerce/__init__.py                                 |     0 |    0 |  100% |
| ecommerce/settings.py                                 |    72 |   21 |   71% |
| ecommerce/urls.py                                     |     8 |    0 |  100% |
| ecommerce/views.py                                    |     3 |    1 |   67% |
| home/__init__.py                                      |     0 |    0 |  100% |
| home/admin.py                                         |     1 |    0 |  100% |
| home/apps.py                                          |     4 |    0 |  100% |
| home/migrations/__init__.py                           |     0 |    0 |  100% |
| home/models.py                                        |     1 |    0 |  100% |
| home/tests.py                                         |    10 |    0 |  100% |
| home/urls.py                                          |     4 |    0 |  100% |
| home/views.py                                         |     3 |    0 |  100% |
| manage.py                                             |    12 |    2 |   83% |
| products/__init__.py                                  |     0 |    0 |  100% |
| products/admin.py                                     |    25 |    7 |   72% |
| products/apps.py                                      |     4 |    0 |  100% |
| products/forms.py                                     |    15 |    0 |  100% |
| products/migrations/0001_initial.py                   |     6 |    0 |  100% |
| products/migrations/__init__.py                       |     0 |    0 |  100% |
| products/models.py                                    |    22 |    0 |  100% |
| products/tests.py                                     |    51 |    0 |  100% |
| products/urls.py                                      |     3 |    0 |  100% |
| products/views.py                                     |   100 |   60 |   40% |
| products/widgets.py                                   |     7 |    0 |  100% |
| profiles/__init__.py                                  |     0 |    0 |  100% |
| profiles/admin.py                                     |     1 |    0 |  100% |
| profiles/apps.py                                      |     4 |    0 |  100% |
| profiles/forms.py                                     |    18 |    1 |   94% |
| profiles/migrations/0001_initial.py                   |     8 |    0 |  100% |
| profiles/migrations/0002_userprofile_avatar.py        |     4 |    0 |  100% |
| profiles/migrations/0003_remove_userprofile_avatar.py |     4 |    0 |  100% |
| profiles/migrations/__init__.py                       |     0 |    0 |  100% |
| profiles/models.py                                    |    21 |    1 |   95% |
| profiles/tests.py                                     |    22 |    0 |  100% |
| profiles/urls.py                                      |     3 |    0 |  100% |
| profiles/views.py                                     |    34 |    8 |   76% |
|-------------------------------------------------------|-------|------|-------|
| TOTAL                                                 |  1531 |  431 |   72% |

TBC

---

### Lighthouse Testing

| Page                  | Result                |
|-----------------------|-----------------------|
| Home                  |                       |
| Products              |                       |
| Product Detail        |                       |
| Edit Product          |                       |
| Create Product Page   |                       |
| Profile               |                       |
| AiPunk                |                       |
| About Pages           |                       |
| About Page Detail     |                       |
| Edit About Page       |                       |
| Create About Page     |                       |
| Blog Posts            |                       |
| Blog Post Detail      |                       |
| Edit Blog Post        |                       |
| Create Blog Post      |                       |
| Shopping Bag          |                       |
| Checkout              |                       |
| Checkout Success      |                       |
| 404 Page              |                       |

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

---

### Console Log Testing

I tested the following pages in Chrome Incognito and they displayed no error messages.

I noticed I receive errors using normal Chrome browser due to one of my extensions.

| Page                  | Result                 |
|-----------------------|------------------------|
| Home                  | ✅                    |
| Products              | ✅                    |
| Product Detail        | ✅                    |
| Edit Product          | ✅                    |
| Create Product Page   | ✅                    |
| Profile               | ✅                    |
| AiPunk                | ✅                    |
| About Pages           | ✅                    |
| About Page Detail     | ✅                    |
| Edit About Page       | ✅                    |
| Create About Page     | ✅                    |
| Blog Posts            | ✅                    |
| Blog Post Detail      | ✅                    |
| Edit Blog Post        | ✅                    |
| Create Blog Post      | ✅                    |
| Shopping Bag          | ✅                    |
| Checkout              | ✅                    |
| Checkout Success      | ✅                    |
| 404 Page              | ✅                    |

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

---

### W3 Nu HTML Checker Testing

| Page                  | Result                |
|-----------------------|-----------------------|
| Home                  |                       |
| Products              |                       |
| Product Detail        |                       |
| Edit Product          |                       |
| Create Product Page   |                       |
| Profile               |                       |
| AiPunk                |                       |
| About Pages           |                       |
| About Page Detail     |                       |
| Edit About Page       |                       |
| Create About Page     |                       |
| Blog Posts            |                       |
| Blog Post Detail      |                       |
| Edit Blog Post        |                       |
| Create Blog Post      |                       |
| Shopping Bag          |                       |
| Checkout              |                       |
| Checkout Success      |                       |
| 404 Page              |                       |

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

---

### W3C Jigsaww CSS Validation Testing

| Page                  | Result                |
|-----------------------|-----------------------|
| Home                  | <img style="border:0;width:88px;height:31px" src="https://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!"> |
| Products              |                       |
| Product Detail        |                       |
| Edit Product          |                       |
| Create Product Page   |                       |
| Profile               |                       |
| AiPunk                |                       |
| About Pages           | <img style="border:0;width:88px;height:31px" src="https://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!"> |
| About Page Detail     |                       |
| Edit About Page       |                       |
| Create About Page     |                       |
| Blog Posts            |                       |
| Blog Post Detail      | <img style="border:0;width:88px;height:31px" src="https://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!"> |
| Edit Blog Post        |                       |
| Create Blog Post      |                       |
| Shopping Bag          |                       |
| Checkout              |                       |
| Checkout Success      |                       |
| 404 Page              |                       |

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

---

### JSHint JS Testing

| Page                  | Result                |
|-----------------------|-----------------------|
| Home                  |                       |
| Products              | ✅                    |
| Product Detail        |                       |
| Edit Product          |                       |
| Create Product Page   |                       |
| Profile               |                       |
| AiPunk                |                       |
| About Pages           |                       |
| About Page Detail     |                       |
| Edit About Page       |                       |
| Create About Page     |                       |
| Blog Posts            |                       |
| Blog Post Detail      |                       |
| Edit Blog Post        |                       |
| Create Blog Post      |                       |
| Shopping Bag          |                       |
| Checkout              |                       |
| Checkout Success      |                       |
| 404 Page              | N/A                   |

<img src="readme_images/tests/jshint/products-btt-button.png" style="max-width: 60%;">

TBC

---

### Flake8 Python Testing

Flake8 was used to test the python code by running the following command in the terminal: 

    python3 -m flake8

TBC

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

---

### Responsiveness Testing

Its important that the website responds well across a variety of device sizes such as PC monitors, tablets and mobile devices. I carried out tests on a variety of device sizes, both physically and by simulation, to ensure the website responds well. The smallest device that the site has been tested for is the Samsung Galaxy Fold with a screen width of only 280px.

#### Visual Testing on Physical Devices

| **Device**                           | **Width (px)** | **Height (px)** |
|--------------------------------------|----------------|-----------------|
| **Dell Monitor - 27" (Landscape)**   | 3840           | 2160            |
| **Dell Monitor - 24" (Portrait)**    | 1920           | 1200            |
| **Samsung Galaxy S10 - 5.8"**        | 360            | 760             |

#### Visual Testing using Google Inspect

| **Device**                   | **Width (px)** | **Height (px)** |
|------------------------------|---------------|------------------|
| **iPhone SE**                | 375           | 667              |
| **iPhone XR**                | 414           | 896              |
| **iPhone 12 Pro**            | 390           | 844              |
| **Pixel 5**                  | 393           | 851              |
| **Samsung Galaxy S8+**       | 360           | 740              |
| **Samsung Galaxy S20 Ultra** | 412           | 915              |
| **iPad Air**                 | 820           | 1180             |
| **iPad Mini**                | 768           | 1024             |
| **Surface Pro 7**            | 912           | 1368             |
| **Galaxy Fold**              | 280           | 653              |
| **Nest Hub**                 | 1024          | 600              |
| **Nest Hub Max**             | 1280          | 800              |

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

#### Visual Testing using AmIRepsponsive

| **Device**  | **Width (px)** | **Height (px)** | **Scale** |
|-------------|----------------|-----------------|-----------|
| **Desktop** | 1600           | 992             | 0.3181    |
| **Laptop**  | 1280           | 802             | 0.277     |
| **Tablet**  | 768            | 1024            | 0.219     |
| **Mobile**  | 320            | 480             | 0.219     |


<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Future Development

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

- Change URLs to unique, shortened slugs based off of the corrosponding pages titles instead of pks - eg, for the about pages, blog and products.

- Add comments and like functionality to blog posts.

- Set up user reviews on ordered products.

- Add order processing app for store owners to add tracking number once dispatched, etc. 

- Set up email address on the custom domain, eg: contact@onlineai.art. Below video tutorial demonstrates free work around to set up custom email domain on Google with Cloudflare.
 - [YouTube: Gmail Custom Email Domain on Cloudflare using ImprovMX](https://www.youtube.com/watch?v=T4n8EvtVDBE)
 - [ImprovMX: Website to create free Alias](https://improvmx.com/)

- Set up the footer as an app so the admins can modify links via the admin portal without changing the websites code.

- Update products to include has_geneder with male, female and unisex options then add to filtering etc.

- Set up products to allow multiple images and videos.

- Set up automated dropshipping usinging service provider such as Printify.

- Set up a delete profile function to allow users to delete their profile after confirming their intentions.

- Implement Google translate on the site it can target people that speak languages other than English.

- Add integrated mailchimp newsletter signup to an about page.

- Look into adding services such as Hotjar and Facebook Pixel.

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Summary of charges and monitoring costs

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

<img src="readme_images/general/tbc.png" style="max-width: 60%;">

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Web Marketing & Search Engine Optimization (SEO)

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Facebook Page

<img src="readme_images/facebook/fb3.png" style="max-width: 60%;">

A [Facebook Page](https://www.facebook.com/people/Onlineaiart/61550214234067/) has been set up to the support the ecommerce store.

I have added the store details, profile picture, header image and series of posts about our store and topics.

I also experimented with Meta Business Manager and scheduled posts to be posted in future as I thought this was a useful feature.

<img src="readme_images/facebook/fb-schedule-post.png" style="max-width: 60%;">

See images of posts content below:

<img src="readme_images/facebook/fb-posts-content.png" style="max-width: 60%;">

Note: Facebook often removes inactive store pages.

### Mailchimp Newsletter

A pop up for newsletter sign up has been added to the products page using MailChimp. 

It has been styled to integrate well with the site.

<img src="readme_images/general/mailchimp-popup.png" style="max-width: 60%;">

TBC

### Google Search Console

I set up Google Search Console as it allows you to closely monitor how your website performs in Google search results, providing data on search queries, click-through rates, and website indexing.

<img src="readme_images/google/google-search-console.png" style="max-width: 60%;">

It's easy to set up, just follow the simple [registration process here](https://search.google.com/search-console/welcome).

<img src="readme_images/google/google-search-console-registration.png" style="max-width: 60%;">

### Google Business

I took a look at the set up procedure for registering the website with Google Business, I entered the set up information but did not verify the account with my personal information as its not an actual business.

<img src="readme_images/google/google-business-view.png" style="max-width: 60%;">

"By creating a Google Business listing, your company gains visibility on Google Search and Maps, making it easier for potential customers to find essential information such as location, hours of operation, contact details, and customer reviews. This free service allows you to manage your online reputation, engage with customers, and provide accurate and up-to-date information. Google Business acts as a digital storefront, boosting your credibility and trustworthiness in the eyes of online shoppers."

### Google Analytics

- Set up an account with [Google Analytics](https://analytics.google.com/) and add the web domain.

- Follow the set up process.

- Copy and paste the GTAG into the base template, just below the `</head>` tag as per Google's instructions.

- Save, commit and push changes.

- You should now be able to monitor your site's traffic after 1 - 2 days.

- If you would like to test the GTAG sooner, you can download [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna) from the Chrome Extensions Store - simply install, access the web page and view the console. Note you will need to disable your ad blocker if you have one installed while testing the page. This allowed me to ensure the GTAG was configured correctly without waiting, it took about 12 hours for the analytics to start working.

<img src="readme_images/google/google-analytics-2.png" style="max-width: 60%;">

<img src="readme_images/google/google-analytics-1.png" style="max-width: 60%;">

### GDPR

Since user data is collected in the data base and cookies have been enabled using Google Analytics, I have added a GDPR pop up notification that I got from [https://www.cookieconsent.com/](cookieconsent.com) and included the site's custom privacy policy page.

I then customized the styling using the Google Chrome Inspection Tool to indentify the corrosponding classes and IDs to modify using the main CSS stylesheet. I ensured that the trackers are not activated until the user has accepted to them to stay in line with EU GDPR legislation.

<img src="readme_images/general/cookies-consent.png" style="max-width: 60%;">
<img src="readme_images/general/cookies-consent-2.png" style="max-width: 60%;">

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Learning Goals

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

Throughout the development, I have aimed to meet the following learning outcomes:

### Learning Goals 1: Integrate an e-commerce payment system and product structure in a cloud-hosted Full-Stack web application

| Criteria Description                                                                                                     | Completion Status   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------|
| Implement at least one Django app with e-commerce functionality using an online payment processing system (e.g. Stripe). | ✅ Implemented Stripe payments system.              |
| Implement a feedback system for successful and unsuccessful purchases with helpful messages.                             | ✅ Set up toast messages and email order confirmation alongside an order success page.              |
| Develop and implement a Full-Stack web application using Django, relational database, and interactive Front-End.         | ✅ Created and deployed a Django-based full-stack web app with interactive front-end, backed by a relational database.               |
| Implement at least one form with validation for creating and editing models in the backend.                              | ✅ Implemented forms with validation to create and edit models in the backend.              |
| Build a Django file structure following Django conventions.                                                              | ✅ Followed Django conventions when structuring the file layout.              |
| Write code demonstrating characteristics of 'clean code.'                                                                | ✅ Aimed to write clean, well commented and clear code.              |
| Define application URLs consistently.                                                                                    | ✅ Consistent approach when defining URLs.              |
| Incorporate main navigation menu and structured layout.                                                                  | ✅ Incorporated nav bar for mobile and desktop. Add additional navigation in footer.              |
| Demonstrate proficiency in Python language with sufficient custom logic.                                                 | ✅ Python was used extensively through out the project & accounts for 40% of the overall coding languages used in the project.      |
| Write Python code with compound statements (if conditions, loops, etc.).                                                 | ✅ Compound statements implemented as required and practical.              |
| Design a relational database schema with clear relationships between entities.                                           | ✅ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   TBC           |
| Create at least THREE original custom Django models.                                                                     | ✅ A variety of custom model where created such as the about, avatar and blog apps.              |
| Implement CRUD functionality for models.                                                                                 | ✅ CRUD has been implemented in the about, blog and products apps (note: avatars are intentionally creation only)              |
| Deploy the final version to a hosting platform and test against the development version.                                 | ✅ The site is hosted on Heroku. It's also set up with a custom namecheap domain. I used Cloudflare for the SSL Cert and Security.     |
| Remove commented-out code and broken internal links from the deployed code.                                              | ✅ Commented out code removed prior to final deployment.              |
| Ensure security of the deployed version by handling passwords and secret keys properly.                                  | ✅ Passwords and secret keys stored securly on Heroku Config Vars for the deployed site.              |
| Use a git-based version control system with regular commits and project documentation in README.                         | ✅ Coding carried out using GitPod IDE. Regular git commits to GitHub with clear messages. Project documented in README file.   |
| Document the complete deployment and testing procedures in README, explaining the application's purpose.                 | ✅ Thorough documentation has been created for the deployment & testing procedures alongside details on applications purpose.  |

### Learning Goals 2: Employ advanced User Experience Design to build a commercial-grade Full Stack Web Application

| Criteria Description                                                                                                                       | Completion Status |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Design a Front-End meeting accessibility guidelines, UX principles, and addressing specific user interactions.                             | ✅ Careful consideration has been given to ensure the site meets accessibility, UX and user interaction expectations. |
| Document and implement all User Stories in an Agile tool, mapping them to project goals.                                                   | ✅ xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx TBC              |
| Design and implement manual or automated test procedures to assess functionality, usability, responsiveness, and data management.          | ✅ Manual and automated tests have been added to ensure the site operates as intended.              |
| Present a clear rationale for the development of the project in the README, addressing the needs of the target audience and user stories.  | ✅ Clear rational for developing the project alongside addressing the needs of the users & the target audience has been documented. |
| Document the UX design work, including wireframes, mockups, diagrams, etc., and demonstrate implementation following the design process.   | ✅ The UX design has been documented and includes wireframe mockups. XXXXXXXXXXXXXXX TBC              |
| Use an Agile tool effectively for managing planning and implementation of primary functionality.                                           | ✅ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX TBC              |
| Document and implement all User Stories and map them to the project within an Agile tool.                                                  | ✅ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX TBC              |

### Learning Goals 3: Employ Search Engine Optimisation (SEO) techniques to improve audience reach

| Criteria Description                                                                              | Completion Status |
|---------------------------------------------------------------------------------------------------|-------------------|
| Ensure all pages can be reached by a link from another findable page.                             | ✅ All pages are reachable on the site.              |
| Include Meta Description tags in the application HTML.                                            | ✅ Meta description tag added to the base template, its overwritten by certain pages with additional more page specific meta description tags.              |
| Include a site title on the parent template.                                                      | ✅ A site title is include in the base template. Specific pages add to it using blocks.              |
| Use appropriate "nofollow" and "sponsored" attributes for links.                                  | ✅ "nofollow" attributes added through site as required.              |
| Include a sitemap and robots.txt file for search engine crawling.                                 | ✅ Sitemap and robots file added to route directory.              |
| Include a 404 response page with appropriate redirect.                                            | ✅ 404 page included with necessary redirection for same.              |
| Use meaningful text content supporting the application's purpose (no Lorem Ipsum).                | ✅ Meaningful, descriptive, SEO friendly text content has been added throughout the site to support purpose. ChatGPT was very useful for this.              |

### Learning Goals 4: Create a secure Full Stack Web application with Authentication and role-based Authorization functionality

| Criteria Description                                                                           | Completion Status |
|------------------------------------------------------------------------------------------------|-------------------|
| Implement authentication mechanism allowing user registration and login for specific reasons.  | ✅ Authentification has been implemented for registration and as required.              |
| Implement login and registration pages available only to anonymous users.                      | ✅ Login and registration has been implemented and is only visible to logged out or un-signed up users.              |
| Prevent non-admin users from accessing the data store directly without going through the code. | ✅ Non admin users cant access data store without going through the code.              |
| Apply role-based login and registration functionality.                                         | ✅ Admin users have additional privilages on main site such as edit or create alongside access to the admin portal with more features. |
| Ensure current login state is reflected to the user.                                           | ✅ Login state is clearly identifable by the Account dropmenu as the options are modified based on login state.              |
| Restrict access to restricted content/functionality before role-based login.                   | ✅ Access to content is restricted as required.              |

### Learning Goals 5: Employ marketing techniques to create brand reach

| Criteria Description                                       | Completion Status |
|------------------------------------------------------------|-------------------|
| Create a Facebook Business Page dedicated to the product.  | ✅ A Facebook page has been created for the site.              |
| Add a newsletter signup form to the application.           | ✅ A MailChimp newsletter has been added to the site as a pop up on the products page.            |

### Learning Goals 6: Understand the fundamentals of E-commerce applications

| Criteria Description                                                   | Completion Status |
|------------------------------------------------------------------------|-------------------|
| Document the e-commerce business model underlying the application.     | ✅ The e-commerce busines model has been documented in the readme.              |

### Learning Goals 7: Additional Learning Outcomes (M)

| Criteria Description                                                                                                                 | Completion Status |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Design and build a real-world full stack MVC e-commerce application with a Front-End that is easy to navigate and intuitive.         | ✅ Developed a comprehensive full-stack Model-View-Controller (MVC) e-commerce platform with user friendly, intuitive design. |
| Produce a fully robust codebase with CRUD actions immediately reflected in the user interface.                                       | ✅ Robust codebase enabling Create, Read, Update, & Delete (CRUD) operations with real-time updates reflected in the UI. |
| Follow thorough manual and/or automated test procedures demonstrated in git commits.                                                 | ✅ Thorough manual and automated testing has been implemented and documented.              |
| Efficiently configure the project through well-kept Procfile, requirements.txt file, settings files, and data store configuration.   | ✅ Procfile, rerquirements, settings and data store config has been efficiently configured.             |
| Fully describe the data schema in the project README file.                                                                           | ✅ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX TBC              |
| Use version control software effectively with a record of the development process.                                                   | ✅ Detailed git commits have been added regularly throughout the project to record the development process.              |
| Ensure users have full control of their interaction with the application and the site's purpose is immediately evident to new users. | ✅ Sites pupose is immediately event to users and the UI allows them full control of their permitted interactions. |
| Control access to sitemap via a robots.txt file and ensure all sitemap links are canonical.                                          | ✅ Access to the sitemap is controlled by the robots file and all sitemap links are canonical.              |
| Use descriptive metadata for SEO that accurately reflects the site's purpose.                                                        | ✅ Descriptive meta deta has been addedd to reflect site purpose and improve SEO.              |
| Users only have access to intended views and functionality.                                                                          | ✅ User access to site functionality has been resricted as intended.              |
| Document the primary marketing strategy behind the application.                                                                      | ✅ The primary marketing strategy has been documented.              |
| The solution has a clear, well-defined purpose addressing the needs of a particular target audience.                                 | ✅ Solutions to address the needs of the target audience have been documented.              |

### Learning Outcome 8: Additional Learning Outcomes (D)

| Criteria Description | Completion Status |
|----------------------|-------------------|
| The learner has documented a clear, justified rationale for a real-world application. The development of the project has resulted in a fully-functioning, interactive web application. | ✅ Clear rational has been documented for the development of this real world, fully functioning, interactive application.              |
| The finished project is publishable in its current form with an evidenced professional-grade user interface and interaction adhering to current practice. There are no logic errors in the code. | ✅ The site is ready to be published as an MVP, minimum viabable product. The site has a profesional grade UI which adheres to best practices. There are no logical errors in the code.              |
| The resulting application is original and not a copy of any other projects. | ✅ The project is unique and original but shares simularities to Code Institute's Boutique Ado project which was used as the inspiration and base for this project. The final project is heavily modified and expanded on.             |
| The design of the web application demonstrates the main principles of good UX design. | ✅ Good UX has been built into the design process for this web application.              |
| Information Hierarchy is clear and well-structured. | ✅ Information is clear and well structured.              |
| User Control is maintained throughout the application. | ✅ User control and management is implemented through out the project with a particular focus on admin controls, both via the main site and the admin portal.              |
| Consistency is evident across all pages/sections and covers interactivity as well as design. | ✅ The site design is consitent through out. It utilizes a custom colour pallette, CSS and Bootstrap to give the site a consistent, interactive design.   |
| Confirmation and feedback is given at all times. | ✅ Confirmation and user feedback has been implemented throughout the site to improve the users experience.              |
| There is evident conformity to accessibility guidelines across all pages/sections and in all interactivity. | ✅ Considerable consideration has been given to ensure the site is conforms to accessibilty guidelines which is eveident in the Lighthouse testing. |
| Any design decisions that contravene accepted user interaction, user experience design principles are identified and described. | ✅ The site has been designed to conform to UI and UX standards and through doucmentation is detailed in README.    |
| Code demonstrates characteristics of ‘clean code’. | ✅ Clean code best practices have been implemented to ensure the code is minimal yet easy to follow and maintain.              |
| Consistent and appropriate naming conventions within code and in file naming. | ✅ Consintent naming conventions have been used within the code and when naming files and folders.              |
| File structure is organized and makes sense. | ✅ The file structure is well organized and clear to follow.              |
| Code is indented in a consistent manner to ease readability. | ✅ The code has been consistently indented to for ease of readability.              |
| Defensive design has been applied. | ✅ Implemented defensive design principles to enhance application security and robustness. |
| All custom code files include clear and relevant comments explaining the purpose of code segments. | ✅ Clear comments and docstrings have been added to ensure the code is easy to understand and maintain.              |
| Code passes through appropriate validators with no issues. | ✅ Code passes through all validation checks as per the multiple testing sections in the readme.              |
| Robust code with no logic errors is found when running code. | ✅ The code is robust and runs without errors.              |
| The entire design is implemented, providing an excellent solution to the users' demands and expectations and security consideration. | ✅ The site has been developed to ensure all users have an enjoyable, functional and safe experience.  |
| Real-world application has been achieved. | ✅ Developed a practical and functional real-world e-commerce application.              |
| Testing procedures are comprehensive, with a good level of coverage, and have been followed. | ✅ Comprehensive testing has been carried out and is well documented.              |
| SEO and Marketing features are evident. | ✅ SEO and Marketing has been carefully considered and implemented on the project as demonstrated in the SEO and Web marketing sections of the README.             |
| Security features and practice are evidenced. | ✅ Security features have been implemented to protect against potential vulnerabilities and threats.               |
| Framework conventions are followed and used correctly. | ✅ Adhered to framework conventions and applied them accurately throughout the project.              |
| Placing of logic in the most relevant components demonstrates an understanding of the Model-View-Controller(Template) pattern. | ✅ The MVC template has been effectively utilized in this project.              |
| Configuration and settings files are well-organised. | ✅ Config and settings files are well organised and allow the site to operate as intended.              |
| Security features and practice are evidenced. | ✅ Security features have been implemented inline with best practises.              |
| Data is well structured. | ✅ The data is well structured to improve readability.              |
| Data is fully modelled and matches the schema. | ✅ ############################################################################################################################################################ TBC              |
| Datastore configuration is kept in a single location where it can be changed easily. | ✅ Centralized datastore configuration in a settings file for easy and convenient modification.              |
| Configuration and dependencies files are kept up to date. Separate versions/branches of these are commits where relevant. The datastore is not accessible to the regular user without going through the code. | ✅ Maintained up to date configuration and dependency files. Ensured that the datastore remains inaccessible to regular users unless accessed through the application's code.              |
| Testing procedures are comprehensive, with a good level of coverage, and have been followed. There is clear evidence of testing, and this is demonstrated in git commits. All noticeable errors have been corrected or documented. | ✅ Comprehensive testing carried out with substantial coverage though manual and automated tests, evident through well-documented testing in README and Git commits. Addressed and rectified or documented any noticeable errors encountered.              |

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

---

## Resources & Credits

<details> <summary><b> Click here to expand this section ⬇️</b></summary>

### Useful Links & Resources

Here is a list of useful links that were used as part of the project. Thanks to all contributers to the below content and services.

| Name                                                                               | Use                                    |
| ---------------------------------------------------------------------------------- | -------------------------------------- |
| [AWS](https://aws.amazon.com/)                                                     | Cloud storage services                 |
| [Figma](https://figma.com/)                                                        | Used to create wireframes              |
| [Bootstrap Documentation](https://getbootstrap.com/docs/)                          | Official Bootstrap documentation       |
| [Canva](https://canva.com/)                                                        | Graphic design and photo editing       |
| [Django Documentation](https://docs.djangoproject.com/)                            | Official Django documentation          |
| [Django Jazzmin](https://django-jazzmin.readthedocs.io/)                           | Customize the Django admin panel       |
| [ElephantSQL](https://www.elephantsql.com/)                                        | Managed PostgreSQL hosting             |
| [Favicon.io](https://favicon.io/favicon-generator/)                                | To create the favicon                  |
| [Git](https://git-scm.com/)                                                        | For version control                    |
| [GitHub](https://github.com/)                                                      | To save and store the files for this project |
| [Gitpod Workspaces](https://gitpod.io/)                                            | Online development environment         |
| [Google Dev Tools](https://developer.chrome.com/docs/devtools/)                    | To troubleshoot, test features and solve issues with responsiveness and styling |
| [Heroku](https://www.heroku.com/)                                                  | Platform as a Service (PaaS)           |
| [Pip](https://pypi.org/project/pip/)                                               | A tool for installing Python packages   |
| [Shields.io](https://shields.io/)                                                  | To add badges to the projects documentation |

-------------

- Custom Domain:
[Youtube: Use namecheap domain with Heroku hosting](https://www.youtube.com/watch?v=51j_mhje9Kk)
[Youtube: Free SSL cert with Cloudflare](https://www.youtube.com/watch?v=Y4iHXhRkpO4)

[CKEditor: ]()
[Markdown Table of Contents Generator](http://ecotrust-canada.github.io/markdown-toc/)
[]()
[]()

TBC

---

### Credits & Special Thanks

I would like to give special thanks to the following: 

- [The Code Institute's Boutique Ado Walkthrough Project](), this project is the final tutorial project in their Diploma in Full Stack Software Development (E-commerce Applications) course. I used this project as a basis for the project and expanded on it by customising how it works, how its styled, its products, categories, styling, branding, functionality, etc. I found this project very useful for setting up the overall site infrastructure such as setting up and deploying the application alongside setting up the bag, checkout and stripe functionality.

- I have had the same mentor, Rohit, throughtout my course in The Code Institute and get 3 sessions with him for each of the 5 milestone projects, as usual, I have found his insight and time as a very valuble contribution to the project.

- I reused some code where possible from my previous project, [Cre8AI.art](https://cre8ai.art). I reused the color set up in the CSS as I found this was an effecient way to apply colours except I updated the colours to using the sits custom colour pallette. I also used the footer and updated the styling, layout and links to suit the site.

- I used the styling, logic and probailities to create the aiPunks using the code and file from this [Crypto Punk Styled Generator on Github](https://github.com/snoozesecurity/cryptopunkgenerator) as the foundation for the avatar app, although the logic, probabilities and images all remain the same, the code has been extensively modified to turn it into this django app. I would like to thank the creator of this repository on Github as it was an interesting way to explore the logic behind the generation of custom NFT series. I also watched this 50 min [Youtube video on creating crypto punk style images using python](https://www.youtube.com/watch?v=o0qNS_pOVqw)

- I would like to give credit to Code Institute for creating the deployment guide in their Boutique Ado Walkthrough Project and to github user and CI Alumna, [kera-kudmore](https://github.com/kera-cudmore), for documenting the deployment and local development process in her [README](https://github.com/kera-cudmore/Boutique-Ado/commit/f0170c57a0d92d80cc14bdefa8f281020469a406) which I have copied and adapted to suit the documentation of [development process section](#deployment) for this project.

- I found the use of ChatGPT 4 useful while creating parts of this project such as the following: 
 - Creating all of the product descriptions and formatting the new fixtures file
 - Creating the about pages content
 - Creating the blog page content
 - Creating or formatting some tables in this readme such as: Useful links, learning outcomes, dependancies
 - I used it to format my external excel file that I was using to track the user stories
 - It was useful when troubleshooting errors while setting up the django app for the aiPunk generations
 - It was used when creating the automated tests although most of which requires modifcations to work
 - 

 - Despite having previously set up an [django app with DALL-E 2 integrated for creating custom images](cre8ai.art), I decided to use newly created open source, free to use, local, ai image generation software to create the images. I used model SDXL 0.9 was only released a couple of weeks ago with its refiner model as well using ComfyUI interface. You will need a nVidea graphic card with atleast 10gb vram to run the application. I found the images generated with this app are currently ahead of the images created by Dall-E and since its run locally, it has no API charges. I have also used different models on Automatic1111 (A1111) UI for creating images locally but found ComfyUI and the new SD_XL model provided better quality generation alongside increased resolution size which is great for custom printed products. Unfortuntly ComfyUI using the SDXL model with refiner is quiete slow, especially in comparison to the standard model on A111. ------------------------- PROVIDE MORE DETAIL, Create section in readme, how to etc..................

- 

[Go Back Up to Table of Contents 📗](#table-of-contents)

</details>

--- 

## Conclusion & Contact

Thanks for checking out my project!

I can be reached directly at <a href="mailto:kieran@kc-7.com">kieran@kc-7.com</a>.

Checkout my other projects at [repos.kc-7.com](repos.kc-7.com).

[Go Back Up to Table of Contents 📗](#table-of-contents)

---