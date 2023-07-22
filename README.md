![Banner](/media/banner.gif)

![GitHub last commit](https://img.shields.io/github/last-commit/kc-7/ecommerce?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/kc-7/ecommerce?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/kc-7/ecommerce?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/kc-7/ecommerce?color=yellow&style=for-the-badge)

# onlineAI.art | E-Commerce Project

This is a django project for an E-Commerce Store.

Live Link: https://kc-ecommerce-434e6f88dca9.herokuapp.com/

Custom Domain: [onlineAI.art](onlineAI.art)

---

## User Stories

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
25. As a Site User, I want to be able to create custom AI Art so that I can view it or purchase a product made using the custom image.
26. As a Shopper, I want to be able to leave comments on products so that I can review the item.
27. As a Shopper, I want to be able to create a wishlist so that I can save my favorite products to purchase later.
28. As a Shopper, I want to be able to complain or inquire about a product so that I can express my dissatisfaction or find out more information about a product.
29. As a Site User, I want to be able to sign up for a mailing list so that I can stay up to date with the latest products and deals.
30. As a Site User, I want to be able to customize my profile so that I can personalize my shopping experience.

---

## Design

### Colour Scheme
The below custom colour scheme was designed and set up for the site. 

<details> <summary>Click here to see the colour palatte 🎨</summary> 

    :root {
        --pink: #FF00FF;
        /* Electric Pink */
        --cyan: #00FFFF;
        /* Cosmic Cyan */
        --purple: #800080;
        /* Mystical Purple */
        --teal: #008080;
        /* Transcendent Teal */
        --gold: #FFD700;
        /* Divine Gold */
        --orange: #FFA500;
        /* Energetic Orange */
        --black: #000000;
        /* Onyx Black */
        --grey: #808080;
        /* Gun Metal Grey */
        --white: #FFFFFF;
        /* Pearl White */
    }

<img src="media/colors1.png" alt="Color Palette" style="max-width: 66%;"> </details>

### Typography
The font Audiowide has been used throughout the site to give it a modern, futuristic feel. This was imported into the CSS file from the main base template using Google Fonts.
<details> <summary>Click here to see the custom font 🔤</summary> <img src="media/googleFontsAudiowide.png" alt="Audiowide Font" style="max-width: 66%;"> </details>


---

## Custom Features

### Custom Admin Portal

The admin portal was customized by using the following [installation guide for Jazzmin](https://django-jazzmin.readthedocs.io/installation/): 

Step 1 - Install the latest `pypi` release with `pip install -U django-jazzmin`

Step 2 - Add jazzmin to your `INSTALLED_APPS` __before__ `django.contrib.admin`:

    INSTALLED_APPS = [
        'jazzmin',
        'django.contrib.admin',
        [...]
    ]

---

### Custom Admin Features

The admin panel also allows the amdministrator to: 

- Sort, Filter & Search Products by name, sku and has_sizes

- Batch select products and update if they have sizes or not, this was very useful when setting up the products catalogue

---

### Stripe Integration

[Stripe](https://stripe.com/gb) has been integrated into the project to handle the payment system.

Stripe is currently in developer mode for the website to allow test payments to be processed to ensure the site's functionality is operating as intended.

#### Test Card Details

Here are some test card details you can use to simulate different scenarios:

| Type               | Card No            | Expiry             | CVC          | ZIP          |
| :----------------- | :----------------- | :----------------- | :----------- | :----------- |
| Success            | Visa               | 4242 4242 4242 4242 | A future date| Any 3 digits | Any 5 digits |
| Require authorization | 4000 0027 6000 3184 | A future date    | Any 3 digits | Any 5 digits |
| Declined           | 4000 0000 0000 0002 | A future date    | Any 3 digits | Any 5 digits |

For more details on setting up Stripe elements to accept payment, refer to the [Stripe Documentation](https://stripe.com/docs/).

---

## Python Package Requirements

The table below lists the Python packages and their respective versions required for running this project as per the requirements.txt file. These packages provide essential functionalities and integrations to support various features within the application and are required for running the project.

| Name                | Version  | Use                                         |
| ------------------- | -------- | ------------------------------------------- |
| asgiref             | 3.7.2    | ASGI (Asynchronous Server Gateway Interface) reference implementation |
| boto3               | 1.28.5   | AWS SDK for Python (Boto3)                 |
| botocore            | 1.31.5   | Low-level interface to AWS services        |
| dj-database-url     | 0.5.0    | Django database configuration from URL     |
| Django              | 3.2.20   | Web framework for Python                   |
| django-allauth      | 0.41.0   | Integrated set of Django authentication views, URLs, and more |
| django-countries    | 7.2.1    | Provides country choices for Django forms  |
| django-crispy-forms | 1.14.0   | Django forms rendering                    |
| django-jazzmin      | 2.6.0    | Admin Panel Customization for Django      |
| django-storages     | 1.13.2   | Custom storage backends for Django         |
| gunicorn            | 21.1.0   | Python WSGI HTTP Server                    |
| jmespath            | 1.0.1    | JSON Matching Expressions                  |
| oauthlib            | 3.2.2    | OAuth library for Python                   |
| Pillow              | 10.0.0   | Python Imaging Library (PIL) fork          |
| psycopg2            | 2.9.6    | PostgreSQL adapter for Python              |
| python3-openid     | 3.2.0    | OpenID support for modern servers and consumers |
| pytz                | 2023.3   | World timezone definitions for Python      |
| requests-oauthlib   | 1.3.1    | OAuthlib support for Requests              |
| s3transfer          | 0.6.1    | S3 Transfer Manager                        |
| sqlparse            | 0.4.4    | SQL parsing and formatting library         |
| stripe              | 5.5.0    | Stripe API library for Python              |
| urllib3             | 1.26.16  | HTTP client library for Python             |

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

#### **Heroku App Setup**

1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the "New" button in the top right corner and select "Create New App."
2. Give your app a name (this must be unique), select the region that is closest to you, and then click the "Create App" button at the bottom left.
3. Open the "Settings" tab and create a new config var of `DATABASE_URL`. Paste the database URL you copied from ElephantSQL into the value (the value should not have quotation marks around it).

#### **Preparation for Deployment in GitPod**

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

#### **Generate a SECRET KEY & Updating Debug**

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

#### **Set up AWS hosting for static and media files**

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

#### **Creating AWS groups, policies and users**

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

#### **Connecting Django to our S3 bucket**

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

#### **Setting up Stripe**

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

- Credit to Code Institute for creating the above guide in their Boutique Ado Walkthrough Project and to github user and CI Alumna, [kera-kudmore](https://github.com/kera-cudmore), for documenting the above deployment and local development process in her [README](https://github.com/kera-cudmore/Boutique-Ado/commit/f0170c57a0d92d80cc14bdefa8f281020469a406) which I have copied and adapted to suit the documentation of this process for this project.

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

---

## Bugs & Issues

### Allauth Templates Directory Not Found

#### Issue

The following file path used in the Boutique Ado tutorial that I was following to set up the basics does not exist in the project directories:

    `cp -r ../.pip-modules/lib/python3.7/site-packages/alluth/templates/* ./templates/allauth/`

#### Resolution

To find the correct file path for the allauth packages, follow these steps:

1. Start the Python interpreter by running the `python` command in the terminal:
2. Once the Python interpreter starts, enter the `help('allauth')` command to access the Python help system:
3. The help information for the allauth package will be displayed, including the path to the site-packages directory where it is installed.
4. Copy the site-packages path from the output and replace [your site-package path] in the command `cp -r [your site-package path]/allauth/templates/* ./templates/allauth/` with the actual path.
5. Run the modified command to copy the allauth templates to the appropriate directory, I used:
    `cp -r /workspace/.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`

---

### Heroku Invalid Credentials Provided

#### Issue

When attempting to disable static using `heroku config:set DISABLE_COLLECTSTATIC=1 --app kc-ecommerce` as part of the deployment to Heroku, it returned ___Invalid credentials provided___ and gives an option to login to CLI via web browser.

When attempting to login through the browser, it directs to a page that says ___IP address mismatch___.

When attempting to login to Heroku via the terminal using `heroku login -i`, it would return the following error message when using my accounts email address and password: 

    ›   Error: Invalid credentials provided.
    ›
    ›   Error ID: unauthorized

#### Resolution

To resolve this issue: 

1. Login to Heroku via terminal using: `heroku login -i`.
2. Enter your email address.
3. Go to your __Heroku Dashboard__ in a new tab.
4. Go to __Account Settings__ --> __Applications__ --> __Authorizations__.
5. Select __Create Authorization__ --> Enter a Description (Project Name) --> __Confirm__.
6. Copy the __Authorization token__ and use it as your password back in the terminal.
7. You should now be able to login and continue with the deployment.

---

### Initialize Heroku Git Remote

#### Issue

Unable to push to Heroku first attempt.

    gitpod /workspace/ecommerce (main) $ git push heroku main
    fatal: 'heroku' does not appear to be a git repository
    fatal: Could not read from remote repository.
    Please make sure you have the correct access rights
    and the repository exists.

#### Resolution

I initialized the the git remote by using the following code `heroku git:remote -a your-heroku-project-name-here` and was then able to successfully push to Heroku.

    gitpod /workspace/ecommerce (main) $ heroku git:remote -a kc-ecommerce
    set git remote heroku to https://git.heroku.com/kc-ecommerce.git

    gitpod /workspace/ecommerce (main) $ git push heroku main
    Enumerating objects: 363, done.
    ...

---

### Programmatic Access for AWS User

#### Issue

Since the walkthrough Boutique Ado video tutorial and updated text guide by the Code Institute, the AWS layout has changed.

Previously setting up programmatic access was an option during User set up however now you need to set it up after the account has been created so that you can get your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

#### Resolution 

To get an `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for the user, follow these steps: 

1. Create User
2. In the IAM section, select Users
3. Select the new user
4. Select Security Credentials
5. Select 'Other'
6. Save your access keys to Heroku config vars

---

## Resources

### Technologies Used

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

### Credits

I would like to give special thanks to the following: 

- [The Code Institute's Boutique Ado Walkthrough Project](), this project is the final tutorial project in their Diploma in Full Stack Software Development (E-commerce Applications) course. I used this project as a basis for the project and expanded on it by customising how it works, how its styled, its products, categories, styling, branding, functionality, etc. I found this project very useful for setting up the overall site infrastructure such as setting up and deploying the application alongside setting up the bag, checkout and stripe functionality.

- I reused some code where possible from my previous project, [Cre8AI.art](). I reused the color set up in the CSS as I found this was an effecient way to apply colours. I also used..........................

- I have had the same mentor, Rohit, throughtout my course in The Code Institute and get 3 sessions with him for each of the 5 milestone projects, as usual, I have found his insight and time as a very valuble contribution to the project.

