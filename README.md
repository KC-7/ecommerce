![Banner](/media/banner.gif)

![GitHub last commit](https://img.shields.io/github/last-commit/kc-7/ecommerce?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/kc-7/ecommerce?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/kc-7/ecommerce?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/kc-7/ecommerce?color=yellow&style=for-the-badge)

# onlineAI.art | E-Commerce Project

Custom Domain Link: [onlineAI.art](onlineAI.art)

Heroku App Link: https://kc-ecommerce-434e6f88dca9.herokuapp.com/

This is a django project for an E-Commerce Store with Stripe payments, custom products, blogs, avatars and about pages.

The site is targeted towords Art, Tech, Fashion, Entusiates and Blog Readers interested in AI generation.

A [Facebook Page](https://www.facebook.com/people/Onlineaiart/61550214234067/) has been set up for the site.

---

## Site Preview 

### Main Site Preview

TBC

### Admin Portal Preview
TBC

---

## Table of Contents

- [onlineAI.art | E-Commerce Project](#onlineaiart---e-commerce-project)
  * [User Stories](#user-stories)
    + [View and Navigation](#view-and-navigation)
    + [Registration and User Accounts](#registration-and-user-accounts)
    + [Sorting and Searching](#sorting-and-searching)
    + [Purchasing and Checkout](#purchasing-and-checkout)
    + [Admin and Store Management](#admin-and-store-management)
    + [Additional Features](#additional-features)
  * [Design](#design)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
  * [Custom Features](#custom-features)
    + [Custom Admin Portal](#custom-admin-portal)
    + [Custom Admin Features](#custom-admin-features)
    + [Stripe Integration](#stripe-integration)
      - [Test Card Details](#test-card-details)
    + [CKEditor](#ckeditor)
    + [Custom Blog Posts (CRUD)](#custom-blog-posts--crud-)
    + [Custom About Pages (CRUD)](#custom-about-pages--crud-)
    + [Custom Crypto Punk Style Avatars](#custom-crypto-punk-style-avatars)
  * [Python Package Requirements](#python-package-requirements)
  * [Deployment & Local Development](#deployment---local-development)
    + [Deployment](#deployment)
      - [**Create the Live Database**](#--create-the-live-database--)
      - [**Heroku App Setup**](#--heroku-app-setup--)
      - [**Preparation for Deployment in GitPod**](#--preparation-for-deployment-in-gitpod--)
      - [**Generate a SECRET KEY & Updating Debug**](#--generate-a-secret-key---updating-debug--)
      - [**Set up AWS hosting for static and media files**](#--set-up-aws-hosting-for-static-and-media-files--)
      - [**Creating AWS groups, policies and users**](#--creating-aws-groups--policies-and-users--)
      - [**Connecting Django to our S3 bucket**](#--connecting-django-to-our-s3-bucket--)
      - [**Setting up Stripe**](#--setting-up-stripe--)
    + [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  * [Bugs & Issues](#bugs---issues)
    + [Allauth Templates Directory Not Found](#allauth-templates-directory-not-found)
      - [Issue](#issue)
      - [Resolution](#resolution)
    + [Heroku Invalid Credentials Provided](#heroku-invalid-credentials-provided)
      - [Issue](#issue-1)
      - [Resolution](#resolution-1)
    + [Initialize Heroku Git Remote](#initialize-heroku-git-remote)
      - [Issue](#issue-2)
      - [Resolution](#resolution-2)
      - [Additional Heroku Tips](#additional-heroku-tips)
    + [Programmatic Access for AWS User](#programmatic-access-for-aws-user)
      - [Issue](#issue-3)
      - [Resolution](#resolution-3)
    + [Navbar too large](#navbar-too-large)
      - [Issue](#issue-4)
      - [Resolution](#resolution-4)
    + [Order number too long](#order-number-too-long)
      - [Issue](#issue-5)
      - [Resolution](#resolution-5)
    + [Navbar not displayed correctly on Profile](#navbar-not-displayed-correctly-on-profile)
      - [Issue](#issue-6)
      - [Resolution](#resolution-6)
  * [Learning Outcomes](#learning-outcomes)
    + [Learning Outcome 1: Integrate an e-commerce payment system and product structure in a cloud-hosted Full-Stack web application](#learning-outcome-1--integrate-an-e-commerce-payment-system-and-product-structure-in-a-cloud-hosted-full-stack-web-application)
    + [Learning Outcome 2: Employ advanced User Experience Design to build a commercial-grade Full Stack Web Application](#learning-outcome-2--employ-advanced-user-experience-design-to-build-a-commercial-grade-full-stack-web-application)
    + [Learning Outcome 3: Employ Search Engine Optimisation (SEO) techniques to improve audience reach](#learning-outcome-3--employ-search-engine-optimisation--seo--techniques-to-improve-audience-reach)
    + [Learning Outcome 4: Create a secure Full Stack Web application with Authentication and role-based Authorization functionality](#learning-outcome-4--create-a-secure-full-stack-web-application-with-authentication-and-role-based-authorization-functionality)
    + [Learning Outcome 5: Employ marketing techniques to create brand reach](#learning-outcome-5--employ-marketing-techniques-to-create-brand-reach)
    + [Learning Outcome 6: Understand the fundamentals of E-commerce applications](#learning-outcome-6--understand-the-fundamentals-of-e-commerce-applications)
  * [Additional Learning Outcomes](#additional-learning-outcomes)
  * [Additional Learning Outcomes 2](#additional-learning-outcomes-2)
  * [Resources](#resources)
    + [Technologies Used](#technologies-used)
  * [Credits](#credits)

---

## User Story Test Cases

[Click here to see the Github User Stories Board](#)

<details> <summary><b> --------------------------------------- or click here to see the list of user stories below ⬇️</b></summary>

### View and Navigation
1. As a Shopper, I want to be able to view a list of products so that I can select some to purchase.
- 1.a: As a Shopper, I want to be able to view a list of products so that I can quickly find products I'm interested in without having to filter through all products.
2. As a Shopper, I want to be able to view individual product details so that I can identify the price, description, product rating, product image, and available sizes.
3. As a Shopper, I want to be able to quickly identify deals, clearance items, and special offers so that I can take advantage of special savings on products I'd like to purchase.
4. As a Shopper, I want to be able to easily view the total of my purchases at any time so that I can avoid spending too much.

### Registration and User Accounts
5. As a Site User, I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.
6. As a Site User, I want to be able to easily login and logout so that I can access my personal account information.
7. As a Site User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
8. As a Site User, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.
9. As a Site User, I want to be able to have a personalized user profile so that I can view my personal order history and confirmations, and save my payment information.

### Sorting and Searching
10. As a Shopper, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced, and categorically sorted products.
11. As a Shopper, I want to be able to sort a specific category of product so that I can find the best priced or best rated product in a specific category, or sort the products in that category by name.
12. As a Shopper, I want to be able to sort multiple categories of products simultaneously so that I can find the best priced or best rated products across broad categories, such as "clothing" or "homeware".
13. As a Shopper, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
14. As a Shopper, I want to be able to easily see what I've searched for and the number of the results so that I can quickly decide whether the product I want is available.

### Purchasing and Checkout
15. As a Shopper, I want to be able to easily select the size and the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product quantity or size.
16. As a Shopper, I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all of the items I will receive.
17. As a Shopper, I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
18. As a Shopper, I want to be able to easily enter my payment information so that I can check out quickly and without issues.
19. As a Shopper, I want to be able to feel that my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
20. As a Shopper, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
21. As a Shopper, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.

### Admin and Store Management
22. As a Store Owner, I want to be able to add a product so that I can add new items to my store.
23. As a Store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
24. As a Store Owner, I want to be able to delete a product so that I can remove items that are no longer for sale.

### Additional Features
25. As a Site User, I want to be able to sign up for a mailing list so that I can stay up to date with the latest products and deals.
26. As a Site User, I want to be able to find out more information so that I can find out additional information about the company such as shipping, etc.
27. As a Site User, I want to be able to navigate the content easily and quickly so that I can find the content that I am looking for.
28. As a Store Owner, I want to set up a blog so that I can draw more site attention, recommend my products to the target audience, and potentially affiliate marketing and sponsered articles.
29. As a Store Owner, I want create a unique custom avatar with unique traits for each user so that I can enhance the personalized shopping experience to create increased customer engagement and retention.
30. As a Store Owner, I want to allow admin to control the products, blogs and about pages via the site and dedicated admin panel so that I can allow admins to run the store without the need for website modifications.

</details>

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Design

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

<img src="media/colors1.png" alt="Color Palette" style="max-width: 40%;">

### Typography
The font Audiowide has been used throughout the site to give it a modern, futuristic feel. This was imported into the CSS file from the main base template using Google Fonts.

</summary> <img src="media/googleFontsAudiowide.png" alt="Audiowide Font" style="max-width: 40%;">

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Custom Features

### Custom Admin Portal

The admin portal was customized by using the following [installation guide for Jazzmin](https://django-jazzmin.readthedocs.io/installation/): 

Step 1 - Install the latest `pypi` release with `pip3 install -U django-jazzmin` in the terminal

Step 2 - Add jazzmin to your `INSTALLED_APPS` __before__ `django.contrib.admin`:

    INSTALLED_APPS = [
        'jazzmin',
        'django.contrib.admin',
        [...]
    ]

Step3 - Add custom jazzmin settings to settings.py.

<details> <summary><b> --------------------------------------- Click here to see my custom Jazzmin settings ⬇️</b></summary>

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
</details>

---

### Custom Admin Features

The admin panel also allows the amdministrator to: 

- Sort, Filter & Search Products by name, sku and has_sizes

- Batch select products and update if they have sizes or not, this was very useful when setting up the products catalogue

---

### Stripe Integration

[Stripe](https://stripe.com/) has been integrated into the project to handle the payment system.

Stripe is currently in developer mode for the website to allow test payments to be processed to ensure the site's functionality is operating as intended.

#### Test Card Details

Here are some test card details you can use to simulate different scenarios at checkout:

| Type                   | Card No             | Expiry                  | CVC                | ZIP                  |
| :--------------------- | :------------------ | :---------------------- | :----------------- | :------------------- |
| Success                | 4242 4242 4242 4242 | A future date (04/24)   | Any 3 digits (242) | Any 5 digits (42424) |
| Requires authorization | 4000 0027 6000 3184 | A future date           | Any 3 digits       | Any 5 digits         |
| Declined               | 4000 0000 0000 0002 | A future date           | Any 3 digits       | Any 5 digits         |

For more details on setting up Stripe elements to accept payment, refer to the [Stripe Documentation](https://stripe.com/docs/).

---

### CKEditor 

I installed the CKEditor to allow customisable text inputs for the Admins to add About Pages. This allows the site management team to add and update these pages without the need of a web developer. The CKEditor easily allows them to vustomise the text. 

I have customized the editor to only display certain suitable options, for example H1 has been removed as it used for the Title for the page so there is no need to have it in the content section, the customizations are added as a postload js script to the pages where the editor has been implemented, eg create blog and create about pages.

https://ckeditor.com/docs/ckeditor5/latest/installation/getting-started/predefined-builds.html#classic-editor

<details> <summary><b> --------------------------------------- Click here to see my custom CKEditor settings ⬇️</b></summary>

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

</details>

---

### Custom Blog Posts (CRUD)

TBC

---

### Custom About Pages (CRUD)

TBC

---

### Custom Crypto Punk Style Avatars

https://github.com/snoozesecurity/cryptopunkgenerator 

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Dependencies & Their Use Cases

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

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. 

<details> <summary><b> --------------------------------------- Click here to see the deployment procedure! 🚀</b></summary>

To deploy the project, follow these steps:

#### **Create the Live Database**

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

</details>

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

You should now be able to access the application locally.

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Custom Domain & SSL Cert

I set up a custom domain with SSL certification to improve the authencity of the online e-commerce store. The custom domain on Namecheap cost €3 and the Cloudflare account is free.

### Custom Domain Set Up on Namecheap

1. Sign up / login in to Namecheap (or alt domain registrar however please note the following how to is written for Namecheap). Find and purchase suitable domain. While purchasing the domain you should set up Domain Privacy to protect your identity, Namecheap offer this service for free however other registrars charge for this service. 

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

### SSL Cert & HTTPS Redirection Set Up on Cloudflare

1. Sign in to / Set up Cloudflare account.

1. From the Cloudflare Home, go to ➡️ Add a site ➡️ Enter your domain name ➡️ Select Free Plan ➡️ Review DNS Records & Continue (No changes required) ➡️ From Change Your Nameservers, copy the Nameservers (1 & 2).

1. Open Namecheap in new tab, go to ➡️ Your domain ➡️ Domain ➡️ Nameservers ➡️ Custom DNS ➡️ Copy the nameservers from Cloudflare in above step to the Nameservers 1 & 2 ➡️ Submit.

1. Go back to Cloudfare and click confirm to check the Nameservers ➡️ Configure Domain Settings: Automatic HTTPS = Yes, always use HTTPS = Yes, Optimize preformace with Brotli = Yes ➡️ Done.

1. Click "Check Nameservers" to confirm above steps have worked (this may take a while). When ready you will see a "Cloudlflare is protecting your site" confirmation message on the Cloudflare site overview.

1. Your site will now redirect to do HTTPS and will have a valid SSL Certificate (eg. https://customdomain.tdl / https://www.customdomain.tdl).

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Product Creation

I used fixtures files to upload the bulk of the categories and products, the categories fixtures were the same as the Boutique Ado project as I used this project as inspiration for my site. The products fixtures was created by enterinf the details for my custom products, to assist with process, I created custom names and then used ChatGPT to create the descriptionss for the products. I generated the unique AI images using SDXL on ComfyUI which was run locally on my PC, as it takes time to generate the images, I created a custom list of prompts and then set up a que so that I could generate a lot of unique images over a couple of hours. I then used Printfy to create the unqiue product images by adding the images I generated to products from their catalogue and downloading the images. The site could be used with an API on OnlineAI.art to sell the products by print on demand, so once the site accepts the payment, it will send the order to Printify to create and dispatch the custom product, however this was not implemented for the scope of this project, it has however been listed as a potential future development.

### ComfyUI

TBC

### SDXL

TBC

### Printify

TBC

### Custom Products Fixtures

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Bugs & Issues

I have documented some of the bugs and issues I have encountered through out the project for future reference below:

### Allauth Templates Directory Not Found

**Issue**

The following file path used in the Boutique Ado tutorial that I was following to set up the basics does not exist in the project directories:

    `cp -r ../.pip-modules/lib/python3.7/site-packages/alluth/templates/* ./templates/allauth/`

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

The alert is only triggered on the edit pages as the placeholder is not visible behind the text. A future improvement could be to trigger a modal instead.

---

### Custom CKEditor not responding well

**Issue**

I have set it up so that you can add HTML to the blogs through the admin panel which works well when creating and editing text. It also allows the admin to add embed items such as iframes for Youtube or Google Maps. Unfortuntly when you try to edit a page with an embeded item, the code for the embded part is not displayed.

**Resolution**

This minor bug is outstanding and does not affect the MVP. 


[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Testing

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

Thirty three automated tests were created for the project using assistance from ChatGPT. They are located in the tests.py files in the following apps: about, avatar, bag, blog, checkout, home, products & profiles.

#### Coverage Installation

The following code was used to install the `coverage` package:

    `pip install coverage`

#### Run Django tests with coverage

The following code is used to initiate the tests for each app:

    `coverage run manage.py test your_app_name`

#### Generate Coverage Report

The following code is used to generate the coverage report:

    `coverage report`

#### Run All Tests

The following code was used to run all tests in the project: 

    `python3 manage.py test`

#### Results for Automated Tests

No issues with the 33 automated tests: 

    `System check identified no issues (0 silenced).
    .................................
    ----------------------------------------------------------------------
    Ran 33 tests in 3.241s

    OK`

#### Coverage Report 

<details> <summary><b> --------------------------------------- Click here to see the coverage report below: ⬇️</b></summary>

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

</details>

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

TBC

---

### Console Log Testing

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

TBC

---

### Flake8 Python Testing

Flake8 was used to test the python code by running the following command in the terminal: 

    `python3 -m flake8`

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

TBC

#### Visual Testing using AmIRepsponsive

| **Device**  | **Width (px)** | **Height (px)** | **Scale** |
|-------------|----------------|-----------------|-----------|
| **Desktop** | 1600           | 992             | 0.3181    |
| **Laptop**  | 1280           | 802             | 0.277     |
| **Tablet**  | 768            | 1024            | 0.219     |
| **Mobile**  | 320            | 480             | 0.219     |

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Future Development

- Change URLs to unique, shortened slugs based off of the corrosponding pages titles instead of pks - eg, for the about pages, blog and products.

- Add comments and like functionality to blog posts.

- Set up user reviews on ordered products.

- Add order processing app for store owners to add tracking number once dispatched, etc. 

- Set up email address on the custom domain, eg: contact@onlineai.art.

- Set up the footer as an app so the admins can modify links via the admin portal without changing the websites code.

- Update products to include has_geneder with male, female and unisex options then add to filtering etc.

- Set up products to allow multiple images and videos.

- Set up automated dropshipping.

- Set up a delete profile function.

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Summary of charges and monitoring costs

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Search Engine Optimization (SEO)

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Web Marketing

### Facebook Page

A [Facebook Page](https://www.facebook.com/people/Onlineaiart/61550214234067/) has been set up to the support the ecommerce store.

See images of page and content below:

###############

TBC

### Mailchimp Newsletter

TBC

### GDPR

TBC

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Learning Outcomes

Throughout the development, I have aimed to meet the following learning outcomes:

### Learning Outcome 1: Integrate an e-commerce payment system and product structure in a cloud-hosted Full-Stack web application

| Criteria Description                                                                                                     | Completion Status   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------|
| Implement at least one Django app with e-commerce functionality using an online payment processing system (e.g. Stripe). | [ x ]               |
| Implement a feedback system for successful and unsuccessful purchases with helpful messages.                             | [ x ]               |
| Develop and implement a Full-Stack web application using Django, relational database, and interactive Front-End.         | [ x ]               |
| Implement at least one form with validation for creating and editing models in the backend.                              | [ x ]               |
| Build a Django file structure following Django conventions.                                                              | [ x ]               |
| Write code demonstrating characteristics of 'clean code.'                                                                | [ x ]               |
| Define application URLs consistently.                                                                                    | [ x ]               |
| Incorporate main navigation menu and structured layout.                                                                  | [ x ]               |
| Demonstrate proficiency in Python language with sufficient custom logic.                                                 | [ x ]               |
| Write Python code with compound statements (if conditions, loops, etc.).                                                 | [ x ]               |
| Design a relational database schema with clear relationships between entities.                                           | [ x ]               |
| Create at least THREE original custom Django models.                                                                     | [ x ]               |
| Implement CRUD functionality for models.                                                                                 | [ x ]               |
| Deploy the final version to a hosting platform and test against the development version.                                 | [ x ]               |
| Remove commented-out code and broken internal links from the deployed code.                                              | [ x ]               |
| Ensure security of the deployed version by handling passwords and secret keys properly.                                  | [ x ]               |
| Use a git-based version control system with regular commits and project documentation in README.                         | [ x ]               |
| Document the complete deployment and testing procedures in README, explaining the application's purpose.                 | [ x ]               |

### Learning Outcome 2: Employ advanced User Experience Design to build a commercial-grade Full Stack Web Application

| Criteria Description                                                                                                                                                                              | Completion Status |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Design a Front-End meeting accessibility guidelines, UX principles, and addressing specific user interactions.                                                                                    | [x]               |
| Document and implement all User Stories in an Agile tool, mapping them to project goals.                                                                                                          | [ ]               |
| Design and implement manual or automated test procedures to assess functionality, usability, responsiveness, and data management.                                                                 | [ ]               |
| Present a clear rationale for the development of the project in the README, addressing the needs of the target audience and user stories.                                                         | [ ]               |
| Document the UX design work, including wireframes, mockups, diagrams, etc., and demonstrate implementation following the design process.                                                          | [ ]               |
| Use an Agile tool effectively for managing planning and implementation of primary functionality.                                                                                                  | [ ]               |
| Document and implement all User Stories and map them to the project within an Agile tool.                                                                                                         | [ ]               |

### Learning Outcome 3: Employ Search Engine Optimisation (SEO) techniques to improve audience reach

| Criteria Description                                                                              | Completion Status |
|---------------------------------------------------------------------------------------------------|-------------------|
| Ensure all pages can be reached by a link from another findable page.                             | [x]               |
| Include Meta Description tags in the application HTML.                                            | [ ]               |
| Include a site title on the parent template.                                                      | [ ]               |
| Use appropriate "nofollow" and "sponsored" attributes for links.                                  | [ ]               |
| Include a sitemap and robots.txt file for search engine crawling.                                 | [ ]               |
| Include a 404 response page with appropriate redirect.                                            | [ ]               |
| Use meaningful text content supporting the application's purpose (no Lorem Ipsum).                | [ ]               |

### Learning Outcome 4: Create a secure Full Stack Web application with Authentication and role-based Authorization functionality

| Criteria Description                                                                                                           | Completion Status |
|--------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Implement authentication mechanism allowing user registration and login for specific reasons.                                  | [ ]               |
| Implement login and registration pages available only to anonymous users.                                                      | [ ]               |
| Prevent non-admin users from accessing the data store directly without going through the code.                                 | [ ]               |
| Apply role-based login and registration functionality.                                                                         | [ ]               |
| Ensure current login state is reflected to the user.                                                                           | [ ]               |
| Restrict access to restricted content/functionality before role-based login.                                                   | [ ]               |

### Learning Outcome 5: Employ marketing techniques to create brand reach

| Criteria Description                                                       | Completion Status |
|----------------------------------------------------------------------------|-------------------|
| Create a Facebook Business Page dedicated to the product.                  | [ ]               |
| Add a newsletter signup form to the application.                           | [ ]               |

### Learning Outcome 6: Understand the fundamentals of E-commerce applications

| Criteria Description                                                   | Completion Status |
|------------------------------------------------------------------------|-------------------|
| Document the e-commerce business model underlying the application.     | [ ]               |

### Learning Outcome 7: Additional Learning Outcomes (M)

| Criteria Description                                                                                                                                                                       | Completion Status |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Design and build a real-world full stack MVC e-commerce application with a Front-End that is easy to navigate and intuitive.                                                               | [ ]               |
| Produce a fully robust codebase with CRUD actions immediately reflected in the user interface.                                                                                             | [ ]               |
| Follow thorough manual and/or automated test procedures demonstrated in git commits.                                                                                                       | [ ]               |
| Efficiently configure the project through well-kept Procfile, requirements.txt file, settings files, and data store configuration.                                                         | [ ]               |
| Fully describe the data schema in the project README file.                                                                                                                                 | [ ]               |
| Use version control software effectively with a record of the development process.                                                                                                         | [ ]               |
| Ensure users have full control of their interaction with the application and the site's purpose is immediately evident to new users.                                                       | [ ]               |
| Control access to sitemap via a robots.txt file and ensure all sitemap links are canonical.                                                                                                | [ ]               |
| Use descriptive metadata for SEO that accurately reflects the site's purpose.                                                                                                              | [ ]               |
| Users only have access to intended views and functionality.                                                                                                                                | [ ]               |
| Document the primary marketing strategy behind the application.                                                                                                                            | [ ]               |
| The solution has a clear, well-defined purpose addressing the needs of a particular target audience.                                                                                       | [ ]               |

### Learning Outcome 8: Additional Learning Outcomes (D)

| Criteria Description | Completion Status |
|----------------------|-------------------|
| The learner has documented a clear, justified rationale for a real-world application. The development of the project has resulted in a fully-functioning, interactive web application. | [ ]               |
| The finished project is publishable in its current form with an evidenced professional-grade user interface and interaction adhering to current practice. There are no logic errors in the code. | [ ]               |
| The resulting application is original and not a copy of any walkthrough projects encountered in the unit. | [ ]               |
| The design of the web application demonstrates the main principles of good UX design. | [ ]               |
| Information Hierarchy is clear and well-structured. | [ ]               |
| User Control is maintained throughout the application. | [ ]               |
| Consistency is evident across all pages/sections and covers interactivity as well as design. | [ ]               |
| Confirmation and feedback is given at all times. | [ ]               |
| There is evident conformity to accessibility guidelines across all pages/sections and in all interactivity. | [ ]               |
| Any design decisions that contravene accepted user interaction, user experience design principles are identified and described. | [ ]               |
| Code demonstrates characteristics of ‘clean code’. | [ ]               |
| Consistent and appropriate naming conventions within code and in file naming. | [ ]               |
| File structure is organized and makes sense. | [ ]               |
| Code is indented in a consistent manner to ease readability. | [ ]               |
| Defensive design has been applied. | [ ]               |
| All custom code files include clear and relevant comments explaining the purpose of code segments. | [ ]               |
| Code passes through appropriate validators with no issues. | [ ]               |
| Robust code with no logic errors is found when running code. | [ ]               |
| The entire design is implemented, providing an excellent solution to the users' demands and expectations and security consideration. | [ ]               |
| Real-world application has been achieved. | [ ]               |
| Testing procedures are comprehensive, with a good level of coverage, and have been followed. | [ ]               |
| SEO and Marketing features are evident. | [ ]               |
| Security features and practice are evidenced. | [ ]               |
| Framework conventions are followed and used correctly. | [ ]               |
| Placing of logic in the most relevant components demonstrates an understanding of the Model-View-Controller(Template) pattern is evident through the placing of logic in the most appropriate components. | [ ]               |
| Configuration and settings files are well-organised. | [ ]               |
| Security features and practice are evidenced. | [ ]               |
| Data is well structured. | [ ]               |
| Data is fully modelled and matches the schema. | [ ]               |
| Datastore configuration is kept in a single location where it can be changed easily. | [ ]               |
| Configuration and dependencies files are kept up to date. Separate versions/branches of these are commits where relevant. Datastore configuration is kept in a single location and can be changed easily. The datastore is not accessible to the regular user without going through the code. | [ ]               |
| Testing procedures are comprehensive, with a good level of coverage, and have been followed. There is clear evidence of testing, and this is demonstrated in git commits. All noticeable errors have been corrected or documented. | [ ]               |

[Go Back Up to Table of Contents 📗](#table-of-contents)

---

## Resources

### Useful Links

Here is a list of useful links that were used as part of the project. Thanks to all contributers to the below content and services.

| Name                                                                               | Use                                    |
| ---------------------------------------------------------------------------------- | -------------------------------------- |
| [AWS](https://aws.amazon.com/)                                                     | Cloud storage services                 |
| [Balsamiq](https://balsamiq.com/)                                                  | Used to create wireframes              |
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
[YouTube: Gmail Custom Email Domain on Cloudflare using ImprovMX](https://www.youtube.com/watch?v=T4n8EvtVDBE)
[ImprovMX: Website to create free Alias](https://improvmx.com/) - Not set up yet
[CKEditor: ]()
[]()
[]()
[]()

---

## Credits

I would like to give special thanks to the following: 

- [The Code Institute's Boutique Ado Walkthrough Project](), this project is the final tutorial project in their Diploma in Full Stack Software Development (E-commerce Applications) course. I used this project as a basis for the project and expanded on it by customising how it works, how its styled, its products, categories, styling, branding, functionality, etc. I found this project very useful for setting up the overall site infrastructure such as setting up and deploying the application alongside setting up the bag, checkout and stripe functionality.

- I reused some code where possible from my previous project, [Cre8AI.art](). I reused the color set up in the CSS as I found this was an effecient way to apply colours except I updated the colours to using the sits custom colour pallette. I also used the footer and updated the styling, layout and links to suite the site.

- I have had the same mentor, Rohit, throughtout my course in The Code Institute and get 3 sessions with him for each of the 5 milestone projects, as usual, I have found his insight and time as a very valuble contribution to the project.

- I used the styling, logic and probailities to create the aiPunks using the code and file from this [Crypto Punk Styled Generator on Github](https://github.com/snoozesecurity/cryptopunkgenerator) as the foundation for the avatar app, although the logic, probabilities and images all remain the same, the code has been extensively modified to turn it into this django app. I would like to thank the creator of this repository on Github as it was an interesting way to explore the logic behind the generation of custom NFT series. I also watched this 50 min [Youtube video on creating crypto punk style images using python](https://www.youtube.com/watch?v=o0qNS_pOVqw)

- I would like to give credit to Code Institute for creating the deployment guide in their Boutique Ado Walkthrough Project and to github user and CI Alumna, [kera-kudmore](https://github.com/kera-cudmore), for documenting the deployment and local development process in her [README](https://github.com/kera-cudmore/Boutique-Ado/commit/f0170c57a0d92d80cc14bdefa8f281020469a406) which I have copied and adapted to suit the documentation of [development process section](#deployment) for this project.

- I found the use of ChatGPT 4 useful while creating this project, however its use was limited to due to its current limitions, hallucenations and constant  it was used for the following: 
 - Creating all of the product descriptions
 - Creating the about pages content
 - Creating the blog page content
 - Creating or formatting the following tables in this readme: Useful links, learning outcomes, dependancies
 - I used it to format my external excel file that I was using to track the user stories
 - It was useful when troubleshooting errors while setting up the django app for the aiPunk generations
 - It was used when creating the automated tests although most of which requires modifcations to work

 - Despite having previously set up an [django app with DALL-E 2 integrated for creating custom images](cre8ai.art), I decided to use newly created open source, free to use, local, ai image generation software to create the images. I used model SDXL 0.9 was only released a couple of weeks ago with its refiner model as well using ComfyUI interface. You will need a nVidea graphic card with atleast 10gb vram to run the application. I found the images generated with this app are currently ahead of the images created by Dall-E and since its run locally, it has no API charges. I have also used different models on Automatic1111 (A1111) UI for creating images locally but found ComfyUI and the new SD_XL model provided better quality generation alongside increased resolution size which is great for custom printed products. Unfortuntly ComfyUI using the SDXL model with refiner is quiete slow, especially in comparison to the standard model on A111. ------------------------- PROVIDE MORE DETAIL, Create section in readme, how to etc..................

- 


[Go Back Up to Table of Contents 📗](#table-of-contents)