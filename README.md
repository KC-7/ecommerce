# E-Commerce Project

This project is for an E-Commerce Store.

Live Link: TBA

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

## Bugs & Issues

### Allauth Templates Directory Not Found

#### Issue

The following file path used in the Boutique Ado tutorial does not exist in the project directories:

    cp -r ../.pip-modules/lib/python3.7/site-packages/alluth/templates/* ./templates/allauth/

#### Resolution

To find the correct file path for the allauth packages, follow these steps:

1. Open a terminal or command prompt.

2. Start the Python interpreter by running the python command:

    python

3. Once the Python interpreter starts, enter the following command to access the Python help system:

    help('allauth')

4. The help information for the allauth package will be displayed, including the path to the site-packages directory where it is installed.

5. Copy the site-packages path from the output and replace [your site-package path] in the command `cp -r [your site-package path]/allauth/templates/* ./templates/allauth/` with the actual path.

6. Run the modified command to copy the allauth templates to the appropriate directory, I used:

    `cp -r /workspace/.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`

---

### Heroku Invalid credentials provided

#### Issue

When attempting to disable static using `heroku config:set DISABLE_COLLECTSTATIC=1 --app kc-ecommerce` as part of the deployment to Heroku, it returned `Invalid credentials provided.` and gives an option to login to CLI via web browser.

When attempting to login through the browser, it directs to a page that says `IP address mismatch`.

When attempting to login to Heroku via the terminal using `heroku login -i`, it would return the following error message when using my accounts email address and password: 

    ›   Error: Invalid credentials provided.
    ›
    ›   Error ID: unauthorized

#### Resolution

To resolve this issue: 

1. Login to Heroku via terminal using: `heroku login -i`.

2. Enter your email address.

3. Go to your Heroku Dashboard in a new tab.

4. Go to Account Settings --> Applications --> Authorizations.

5. Select `Create Authorization` --> Enter a Description (Project Name) --> Confirm.

6. Copy the `Authorization token` and use it as your password back in the terminal.

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

