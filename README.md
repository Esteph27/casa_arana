![Device Screen images](/assets/images/multiple_screen_devices.png)

# Welcome to Casa Arana.

This is a Full-Stack Framework project built using Django, Python, HTML, CSS, BootStrap and JavaScript. The purpose of this project was to build an an e-commerce website based on business logic used to control a centrally-owned dataset. The website includes an authentication mechanism provided by Django and allows users to purchase products online.

This project has been built on GitHub workspaces and deployed on Heroku. This project was built for educational purposes. No commercial revenue is generate from this project. 

The live site can be found [here](https://casa-arana.herokuapp.com/)

*** 

## Table of Contents

1. [UX](#ux)
    - [Strategy](#strategy)
    - [User Stories](#user-stories)
    - [Scope](#scope)
    - [Structure](#structure)
2. [Marketing](#marketing)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

***

## UX

Following UX core principles, the development of Casa Arana had to take into account; strategy, design thinking, the site owners business goals and the target audience’s needs, all whilst allowing for intuitive and responsive navigation to create a pleasurable experience for the user - with the ultimate goal for the user to return again. In order to achieve the current UX, the planning of this project was outlined in the following stages.

To help me keep track all of the development steps involved I created a GitHub project board. You can view it the project board [here](https://github.com/Esteph27/casa_arana/projects/2)

***

### Strategy

For the strategy it was important to understand who were the intended target audience, what their needs are and what the site owner’s business goals are in order to determine what features to include. These are outlined below:

The target audience CA intends to target are;
- People from 29 years old and up
- Most likely shop at places such as Harrods, Made and Sweetpea & Willow for their home wear and decor items 
- Interested in interior design and decor, have an understanding of style and trends and have sufficient level of disposable income
- People who are conscious buyers and have an appreciation for hand-made goods
- People who prefer to support smaller and boutique business rather than large business chains
- People who enjoy travel

This user will be looking for:
- An informative website with information about a particular product, including information about where and how it was made
- Have the ability to view and leave product reviews
- Make a secure and easy online payment 
- Browse a selection of products with the ability to filter by price and category
- Create a user account where they can view their online history, as well as update any personal contact or delivery information 
- The ability to login and out of their account as needed
- The abilitity to add items to wishlist so they can store their favourite items in one place
- The ability to connect with the business via connecting through social channels,  email, signing up to their email subscription

The site owner’s goals would be to promote and sell their products online, all whilst building a community to support their makers (the one’s who make the products). 

The site owner would be looking for:
- A responsive and intuitive website to promote their products in an elegant and elevated way 
- Provide the users with the right and important inforamtion to help them make a purchase and encourage sales
- Encourage users to buy from their site by implementing promotions such as free delivery over a certain amount, promotion through a facebook account and newsletter sign ups
- Build a sense of trust, transparency and rapport by proving information about the maker of the products and how the user can support the makers further
- Build a community via social channels, email subscriptions and marketing strategy 
- Provide a secure payment system where the users can safely make payment online with no hassle

This website will offer all of these things whilst also allowing for intuitive navigation and ease of use.

Due to the age group of the users, it is assumed that there will be an even split between users viewing the website on their mobiles phone and laptops. Therefore creating something responsive is integral to the design, I have used Bootstrap grids and elements & custom CSS to allow for this.

***

### User Stories

This website has two main users; the Site owner (admin) and the end User (shopper). Please find all of my defined user stories and acceptance [here](https://docs.google.com/spreadsheets/d/1XdgCMRVrfw2YlieImYsSJ_6mn5kbYvmL0O8vrmCCRKM/edit?usp=sharing)

My users stories were obtained by personal research. I explored a range of e-commerce websites including made.com and liberty.com (who are considered to be fictional competitors) to gain inspiration for UX and navigation design as well as potential features to include to include.

***

### Scope 

When planning the initial design for this project, I had to outline which features were absolutely essential to include in this current release, and other features that would become part of the scalability plan to include in future releases. Below I have outlined the scope for this current release:

Version 1:
A project that meets all the user stories;
- Home/Landing page with a short introduction and call-to-action links
- About page with information about the company 
- Responsive navigation bar allowing the user to navigate throughout the site
- Product page displaying all products and include sorting functionality by price and category
- Product information page displaying the product’s information and add to basket functionality 
- E-commerce functionality allowing users to make an online purchase 
- Register/login feature using Django AllAuth so that users can create an account.
- User account where the user can view their past orders and store default delivery information 
- Product review page where logged users can leave a reviews for a specific item 
- Review section on product information page displaying previous customer reviews
- Wish list feature enabling login in users to save their favourite products 
- Footer with business information and social media links 
- Custom 404 and 505 error pages

For future release, please see the Scaleability section below outlining the features Casa Arana would hope to include. 

***

## Structure

### Databases

During development I worked with a local sqlite3 database supplied by Django, for production I connected to the Heroku Postgree databsae which is provided by Heroku as an add-on. For all app apart from the home app I have created Entity Relation Diagrams to illustrate the database models and the relationships to each other. Please note that not all fields have been updated since the making of this database

Link to models - [drawsql](https://drawsql.app/esteph/diagrams/casa-arana-db)

### Home App

A simple app to store and display the Home and About pages.

### User Profile App

This app enables authenticated users to save their information so that when they are logged in the order form is pre-filled, creating an improved user experience. The UserProfile model has a one-to-one field that is linked to the Django AllAuth user account, upon logging in the model method create_or_update_user_profile creates the profile if it doesn’t already exist in the model.

The second and third models are the WishList and WishListItem. These are used to manage the user’s wishlist; the WishList models stores a User’s Wishlist and the WishListItem model enables to get a specific item from a User’s Wishlist. The add_to_wish_list and remove_from_wishlist views handle updating the Wishlist as required by the user. Also, to allow for better user experience, the add_to_wishlist view also allows for existing products not to be added in the Wishlist if they already exist to avoid having the same item twice.

### Product App

This app controls the business’s products for sale. There are 4 models to handle the relative data needed for this e-commerce business; Products, Category, Artisan and Reviews.

The Product model enables individual products to be added to the database either via the Django admin interface or via the front end where only Admin users can add, edit or delete items all of which are handled by their respective views. This model has a FK relationship with the Category and Artisan models.

Category model stores the category types of products for sale, this allows the user to filter the shop page by the category if they are looking for something specific.

The Artisan model holds information about the artisan (the person who made the product). This information is connected to the Product model via a FK in the product model with a related_name of ‘products’ in order to easily access and display products made by a particular Artisan. This information is also used to display the Artisan Profile where the User can find out about specific artisan and view products made by that artisan in one place. This is part is important to both the business values and user experience. 

The Review model handles, stores and display product reviews. The product_review view and ReviewsForm allows logged in users to leave a product review for a selected product and display them in the product information page. The model also allows a User to leave a product rating by selecting a score from 1-5 which is good for user experience. 

### Checkout App

The checkout app is used solely for the user to make purchases via the online shop; this app contains two models Order and OrderLineItem.

OrderLineItem contains all of the information regarding the products that have been purchased as part of a specific order. It has a foreign key to both the Order and Product models, it also contains the quantity purchased of that product and then the item total. This information is used to calculate the total cost for the order. 

Order contains all of the relevant address information for billing/shipping, a foreign key to the UserProfile, email and contact number. It also contains delivery cost, the order sub total and the grand total information as well as the payment itself by storing the the stripe PID and original bag contents (so that if the order is changed, the admin user can see what was purchased initially). Each order has a unique order number which is automatically generated when a new order is added to the database using UUID.

There are a few methods used, the update_grand_total calculates the overall total depending on the order items linked to the order, ensuring the value is always correct.

### Stripe
Payments are accepted via Stripe’s test card details. For further information on which card number you should use, please refer to Stripe's official documentation - [Stripe Test Integration](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details)

***

## Surface

### Design

Keeping the target audience in mind it very much helped to determine the overall aesthetic and design of the website. Considering the target audience might be shopping at places like Harrods and perhaps enjoy the finer things in life, the design had to be elegant and modern with a touch of luxury. The following have been considered in order to achieve this:

### Color scheme 

With luxury design in mind, I opted for a soft and neutral palette consisting of warm beige and yellow hues and a dark grey/orange as the main contrasting colour. The below colours were selected for my main colour palette;

![colour palette](/assets/images/colour-palette.png)

**#A4917E** - Used for font awesome icons, on hover colour contrast, nav bar and links. This is a dark beige colour and although it’s a neutral colour, it has been used as a highlight colour in order to add a soft level of contrast, as oppose to harsh contrast which you might find on some other sites. This soft level of contras I find is in keeping with the theme of luxury. 

**#F3ECE4** - One of the main colours is this is a lights stone beige colour which has been used for background colours for containers and buttons. This colour is soft and together with the other colours it adds a level of modernity and brings all the colours together in a harmonious way. 

**#EFE9E2** - This is the background colour for the mail chimp sign up form. I wanted this container to be clean and an important feature, without taking too much attention away from the other connect on the page, especially the product page. This colour provided a nice balance for this.

**#F9F4EE** - This is the colour selected for the footer. The footer is always an important feature to any website so I wanted to make sure the footer stood out in a clean and elegant and this colour allows to that whilst complimenting the other features and tones throughout the site. 

**#C8C1B9** - This colour is used for the back to top scroll arrow and drop down nav items when activated. This colour provided a nice gentle and visual contrast to improve the UX. It has also been used as the background colours for images to fall back on incase loading is slow or if the images do not load. 


### Typography

The ‘Libre Caslon Display’ font is the main font used throughout the whole website with Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Although its primary use is for web headlines, I have used ’Libre Caslon Display’ for both text and headlines as I feel it’s an elegant and clean font which is both attractive and appropriate for the design of Casa Arana.  
 
Read more about it [here](https://fonts.google.com/specimen/Libre+Caslon+Display#glyphs) 

### Images 

As the main business goal for any commerce website is to sell products, imagery is a very important component to the design. The images had to be not only be of high quality, but also aesthetically pleasing in order to promote the products and entice a sale. The images are displayed in a large format mostly taking up 100vw width on mobile screens and 50% on larger screens, (apart from in the shopping bag) in order to display the products in a clean and impactful way. The users can also open the product images in a new tab allowing them to view the image on a larger scale to improve their user experience.

On the Lading page, a large background hero image is designed to be striking and catch the user's attention whilst representing what the business us about. The About page also features impactful and colourful images which are not only aesthetically pleasing, but also denote the intentions of the business and their values. 

All images are not of real products and are not for sale. All images have been taken from Unsplash.com

### Wireframes 

Development/Initial wireframes - view(link)

Final wireframes - view(link)

### Accessibility and Responsiveness:

The website is deigned to be responsive and accessible across a range of devices using a combination of Bootstrap grip system and classes with custom css to achieve this.

***

## Marketing

### Plan
Casa Arana is a business to customer e-commerce platform, built and designed to sell products to the User and provide customers with information about who made the products and where they come from. Whilst working on this project I wrote a marketing plan to guide me during the development process and keep the commerce goals in mind. 

(Link to marketing plan)

To further enhance sales and promote the business, there is also a Casa Arana FaceBook page (this is also linked in the site’s footer):

https://www.facebook.com/casaaranaofficial/


### SEO 

I conducted SEO research to help me determine which Key word would be most relevant and most important to my web application to reach potential customers. I wrote a list of words based on the business goals and user stories of Casa Arana and typed them into Google search engine to see what websites and other key phrases would be returned back. Here are the results 

![keywordsearch](/assets/images/keywordsearch1.png)

![keywordsearch](/assets/images/keywordsearch4.png)

![keywordsearch](/assets/images/keywordsearch8.png)

*** 

## Existing Features

### Navigation menu

For the nav bar I have used Bootswatch Lux Theme nav bar and have customised it to better suite the design of the website. I chose this because the responsiveness of this nav bar is great across all screen sizes.

- On mobile and medium screens it collapses to a hamburger menu and laptop and desktop screens in spans across the width of the device and split into two sections. The left side displays the company’s Logo name (which when clicked, takes the user back to the home page) and links to the store and about page, and on the left of the nav bar is the profile icon with dropdown links to view user profile, admin management (is site owner), wish list and login/log out. The left also contains the shopping bag icon which displays the number of items inside the user’s shopping bag to inform to improve their online shopping experience. 

![nav bar full width](/assets/images/navbar-fullwidth.png)

![nav bar hamburger](/assets/images/navbar-collapse.png)
 
- The nav bar is fixed at the top of the screen at all times, allowing the user to easily navigate through the website

- The nav bar links also change colour on hover to a darker colour to improve accessibility and allow the user to easily see what they are clicking. 

### Footer

I wanted to keep the footer clean and decluttered in order to keep with the luxury theme. To achieve this I used a soft beige tone colour to provide contrast as well as keep the information nicely centred across all screen widths. The footer contains the company's contact details and social media links which are most likely sort after by the User so keeping them avaible in the footer at all times allows the user to eaisly find them.

![footer](/assets/images/footer.png)

### Mailchimp news letter sign up 

This is an important marketing feature so I wanted to make it accessible across the entire site and responsive across all screen devices. I have used a soft block colour for the background to make it standout whilst also complimenting the surrounding features. 

![MailChimp signup form](/assets/images/mailchimp-signup.png)

### Home Page

With the name Casa in mind (casa is home in Spanish) I wanted the Landing page to echo the meaning of the word home as well as provide the user with the information needed to explore the site easily. To do this the home page is made up of four main sections; the hero Image, short introduction, Links to the store and links to the About page:

- I have used an impactful hero image that takes up the full width of the screen in order to provide visual impact and excitment for the User. Ontop of the hearo image I have placed a h1 tag saying 'Welcom Home' to provide a nice welcome to the User to engage them to come in and take a look. 

![hero image](/assets/images/hero-image.png)

- To accompany this, below the hero image is a brief introduction to the business so that first time visitors can quickly understand what the site is about and what they can expect to find withouth trolling through the website. This section also includes a call-to-action link promting the user to view the website's products as soon as they land on this page.

![intro section](/assets/images/intro.png)

- Then there is the product section which provides links to view the products sold via their category, this acts as a sort of filter making easier for the customer narrow down what they're looking for. These links are displayed over a respective product images to create impact whilst promoting the propduct itself. These images are responsive across all mobile screens, they stack on top of each other on mobile screens and display horizontally across larger screens. This section makes it clear to the User what is for sale in this website and what sort of things they can expect to find. 

![category images](/assets/images/category-images.png)

- The last section is a section introducing the company values and a link to the About page. This is to gain a connection with the user as the intended target audience are most likely to be interested in company values and ethos as they are conscious buyers. 

![values](/assets/images/values-section.png)

### About Page 

The about page provides information about the company including how they are, how they work and who they work with. The aim of this page is to not only provide useful informaiton for the user but also hopefully gain rapport and confidence with the business to reassure them they are buying for a legit website.

![about page](/assets/images/aboutpage.png)

- A feature of this page is the 'Support More' where the company's extends their support by providing link to external Charitires. This type of iformation is not only important for the business oener but will most likely be of interest to the inteded target audience. All the external links open in new tabs for better user experience. 

- At the bottom of the page is also a section where it prompts the User to 'join them' and create an account if they havn't done so already. This is to encourage the user to sign up and encourage sales. If the user is already loggin in then this section will not display as the user already has an account. 

![create account](/assets/images/create-account.png)


### All Products 

This page display all of the products sold by the company. The images are displayed in a Bootstrap cards where each card contains the product image, category tag, name and price. The images are links that take the user to view the selected products information and the category tag is also a link which takes the user to view a list of products under that category. I have done this in order to make the site more intuitive for the user.

- Each card stacks on stop of each other on mobile screens and are paginated by 2 on larger screens in order to keep the images displayed in a nice and impactful way. 

![all products page](/assets/images/all-products-page.png)

- The search bar allows the User to filter by key words which are found in the product name and description. If no products are found then a message will appear in the header to notfy them 0 items have been found with a link that takes them back to view all the products.

![search bar 0 products](/assets/images/searchbar.png)

- The User can also search products by category by selected the navbar dropdown menu. The header will notify the user how may items have been found within each category

![category links in navbar](/assets/images/navbar-category-links.png) ![number of items found](/assets/images/items-in-catefory.png)

- The 'Sort By' features allows Users to sort products by price from highest to lowest and vice versa. However please note that the user can only perform this function on All products, they are not able to sort categories by price. Please see features left to include below for further information. 

![srot by filter](/assets/images/shopby-filter.png)

### Product page

This page displays the product information relating a to a specific product. The information included is;

- The product details such as colour, description, composition, dimenstions and any special features (such as washing instructions)

- Quantity increase and descrease buttons enabling the users to select the quantity they would like to purchase.

- A 'Add to Bag' button that adds the selected item and quantity to their shopping baseket. Upon submission a toast message will appear confirming to the user that the item was added successfully to their shopping bag.  

- ‘Add to Wish List ’ and ‘Remove from Wish List’ links with enables the user to add or delete the product to their Wishlist which improves their overall shopping experience. Only logged in users have access to this feature. 

![procut info](/assets/images/product-info.png)

- 'Made By' feature shows the Artisan who made the product. This section shows the Artisan name, bio, image as we as a link to view their profile. The intended target audience are mostly conscious buyers so having information about the person who made the product will hopefully make for a good and informative experience.

![artisan section](/assets/images/artisan-section.png)

- The last section on this page is the Product Reviews section. If a product has a review then it will be displayed with the user’s name, date posted and comment as the main features. If an item has no reviews, then the User is encouraged to leave a Rewview by the call-to-action button. Only login in users are able to leave a review, if they are not logging in then they are encouraged to sign up. This review are here in order to help the customer make an informed decision. 

![reviews](/assets/images/product-reviews.png)

### Shopping bag

This page provides an overview of what the User currently has in their basket. It displays the product image, name, unit price, quantity, delivery cost and order total. The User can easily amend the quantity of each item and also remove any item from the bag. The order total is outlined clearly and neatly at the bottom of the product list along with a ‘checkout’ button to make the UX more intuitive and easy. 

![shopping bag](/assets/images/shopping-bag-desktop.png)

- To accompany this, the Shopping bag icon in the nav bar tells the user how many itmes they currently have in their shopping bag so that this information is always visible. 

![shopping bag icon](/assets/images/shopping-bag-icon.png)


### Checkout

This page is where the user can complete their purchase. It’s split into two columns, billing & card details on one side and their basket overview on the other. On mobile screen this layout collapses so that each column is stacked on top of each order allowing for good responsive design.

![checkout page](/assets/images/checkoutpage.png)

- The forms are simple, with placeholders explaining what each input is for. For logged in Users there is a checkbox the User can tick to save their delivery information for their next order. This information is saved to their User Profile page.

![chec box](/assets/images/save-info-checkbox.png)

- At the bottom of the checkout order is an ‘Order Summary’ where the user can review their order and adjust it if they need to before making a payment. 

![checkout order summary](/assets/images/checkout-order-summary.png)

- The card element feature has been built using Stripe, to make test payments I have used the card details found in [Stripe Testing documentation](https://stripe.com/docs/testing). Upon submission of the payment form, information is passed to stripe and then back, if successful the user is taken to the 'checkout success' page, which displays the order and delivery details.

![chekcout success page](/assets/images/checkput-success-page.png)

- If the payment is not successful, the form does not submit, an inline error message is displayed and the user is able to rectify the issues.

![invalid card details](/assets/images/invalid%20-card-number.png)

### User profile 

A logged in User can access this link via the ‘View Account’ link in the profile icon dropdown menu found in the nav bar. This is where a User can view their order history and update their default delivery information. These are displayed in an accordion where the user can toggle between the two making each section easy to access.

![accordion](/assets/images/user-profile.png)

![order history list](/assets/images/order-history-list.png)

- The Order History shows the past orders placed by the User so that they can easily access this information whenever they need to. The user can click on the Order number and the User will be redirected to that order’s checkout out success page where they can view the full order details. An alert message appears on the screen to confirm the User that they are viewing a past order. A handy link also brings the user back to their account for easy navigation.

![order history toast](/assets/images/order-history-toast.png)

- For Users who have no order hisgory yet, then a message will be displayed to encourgae the user to browse the products to help encourage a sale.

![no order history](/assets/images/order-history.png)


### Wish List

- A logged in User can access their Wishlist via the ‘View Wish List’ link in the profile icon dropdown menu found in the nav bar. This page displays all of the items a User has saved to their wish list. The items are displayed in Boostrap Cards containing the product image, name, price, a link to view the full product details, and a link to remove the item from the wish list.

![wishlist](/assets/images/wishlist-item.png)

- If the user has no items saved to their wish list a message is displayed informing the User including a link to take them to the store.

![wishlist empty](/assets/images/wishlist-empty.png)

- A user can add an item to their wishlsit by clicking on the 'add to wishlist' link featured in the prodcut information page. This feature is only aviable to loged in users. 


### Artisan profile

This page displays information about a selected Artisan. It includes their profile image, biography, location as well as images of all the products that Artisan has made.

![artisan profile](/assets/images/artisan-profile.png)

- The product images are displayed in Bootstrap cards containing product name, price and a link to view the full product details and Add to wish list link. 

![artisan products](/assets/images/artisan-products.png)

- This page is promote the Artisans and the products they make. 

### Admin 
The admin section of this website allows site owners (superusers) to update, add or delete product from the store on the front end via the Product Management link found in the profile icon dropdown link. 

Add Product - products can be added using the form provided and on submission, they are notified this product is added via a toast message. 

- ‘Edit’ and Delete’ links where it takes admin users to either the ‘edit_product’ page where they can edit the product’s information, or delete the product from the website. Only Store admin users have access to this functionality. If the user is either unauthorised or not signed in this feature won't be aviable.

![edit / delete buttons](/assets/images/edit-delete-links.png)

Edit Product - this link is found in the product information page. Product information can be edited using the form provided. On submission of the form, the user is updated on the changes via toast message. 

Delete Product - his link is found in the product information page. Once clicked the product is instantly deleted without any warning so the site admin would have to extra careful. See scalability section to read up on improving this feature.

### 404 and 500 pages 
I have designed custom 404 and 500 pages to easily allow users to navigate back to the home page should they encounter any errors. 

### Back to top scroll 
Allows users to scroll back to the top of the page when scrolling pst 20px. This is to improve their experience. 

### Back to previous page link
Allows the user to go back to the previous page 

### Back to Account
Allows logged in users to easily navigate back to their account

*** 

## Features Left To Implement 

### Rating stars in review section
As part of the product review section, it would have been a better user experience to display star ratings. Due to time constraints this part of the feature was not developed for this release. 

### WishList heart icon
Instead of wordy links, it would have been a lot cleaner and more appreciate to user heart icons to indicated the Add to Wish List Features. This heart icon would have been empty to signify that the product has not been added to the Wishlist, or the heart would be a solid colour in order to signify that this product has already been added to the wish list. 
Due to time constraints this was added. 

### Sort Category by Price 
At the moment the user can sort ALL products by price, however the user is un able to sort category by price which is not good UX. Due to time constraints this functionality was not added. 

*** 

## Technologies Used 
I have used several technologies that have enabled this design to work:

- Django
    - Django is the framework that has been used to build the over project and its apps.
- Python
    - Python is the core programming language used to write all of the code in this application to make it fully functional.
- Bootstrap
    - Used for creating responsive design.
- Google Fonts
    - Used to obtain the fonts linked in the header, fonts used were Raleway and Lobster
- Font Awesome
    - Used to obtain the icons used on the high scores and rules pages.
- Google Developer Tools
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- GitHub
    - Used to store code for the project after being pushed.
- Git
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- Gitpod
    - Used as the development environment.
- Heroku
    - Used to deploy my application.
- Lucid
    - Used to create the ERD for the project.
- ImageResizer
    - Used to resize images to reduce loading time.
- Flake8
    - Used to test my code for any issues or errors.
- Unicorn Revealer
    - Used to detect overflow of elements, which allowed me to quickly debug any issues.
- Favicon.io
    - Used to create favicon for my website
- Color Contrast Accessibility Validator
    - Allowed me to test the colour contrast of my webpage.
- W3C Markup Validation Service
    - Used to validate all HTML code written and used in this webpage.
- W3C CSS Validation Service
    - Used to validate all CSS code written and used in this webpage.
- JSHint
    - Used to validate JS code
- AmIResponsive
    - Used to generate responsive image used in README file.
- SQLite
    - I have SQLite to run my database tests locally.
- PostgreSQL
    - I have used Heroku's PostgreSQL relational database in deployment to store the data for my models.
- AWS
    - I used Amazon AWS S3 to store all of my media files.

***

## Testing 

### Manual Testing  - (link to separate document)

### Code Validation

All of my code has been validated using online validators specific to the language, results are below:

[W3C Markup Validation Service](https://validator.w3.org/)
- Used to validate HTML code written and used in this webpage. 
Passed with zero errors 

(Screenshot here) 

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) 
- Used to validate CSS code written and used in this webpage.
- Code passed with 1 error and 1470 warnings, but these are coming from the vendor extensions and so not sure to my part.

(Screenshot here)

[JSHint](https://jshint.com/) 
- Used to validate JavaScript code 
- Code passed with no errors 

(Screenshot here)

Flake8
- Used to test Python code for any issues or errors
- No errors however there were warnings which were mainly due to lines being too long most of which were in migration files or Django files so have left them as they are. 

(Screenshot here)

[Google Dev Tools Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- Used to test performance and accessibility of the website 

(Screenshot here) 

**Performance scored 64;**
- This is mainly due to the download time being slowed down by the image sizes. Due to the nature of my website, it relies on high quality images so I was reluctant to compress the image files. 
- Another cause was due to render-blocking resources such as bootstrap CDN and query links, however these are needed for the design and responsiveness of the website so I did not take these out. 

**Accessibility scored 100;**
- Passed 17 audits 

**Best Practices scored 83;**
- This is due to safety and 2 vulnerabilities detected in the bootstrap jQuery can 

**SEO scored 100;**
- Passed 11 audits

[Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) 
Used to test colour contrast of the webpage
All contrast test passed

(Screenshot here)

***

## Fixed Bugs 

I encountered a few bugs whilst developing Casa Arana, some of them were typo errors which have been noted in the project board (link here), below are some of the more complex errors I faced and the steps I took to resolve them.

## Existing Bugs 

***

## Deployment 

The master branch of this repository has been used for the deployed version of this application.

### Using Github & Gitpod

To deploy my Django application, I had to use the Code Institute Python Essentials Template.

- Click the Use This Template button.
- Add a repository name and brief description.
- Click the Create Repository from Template to create your repository.
- To create a Gitpod workspace you then need to click Gitpod, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than - - - create a new one. You should pin the workspace so that it isn't deleted.
- Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    - git add .: adds all modified files to a staging area
    - git commit -m "A message explaining your commit": commits all changes to a local repository.
    - git push: pushes all your committed changes to your Github repository.


***Forking the GitHub Repository***
If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under your account)
3. Your repository has now been 'Forked' and you have a copy to work on

***Cloning the GitHub Repository***
Cloning your repository will allow you to download a local version of the repository to be worked on. Cloning can also be a great way to backup your work.

1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Gitpod & select the directory location where you would like the clone created
5. In the terminal type 'git clone' & then paste the link you copied in GitHub
6. Press enter and your local clone will be created.

### Gmail SMTP
I have used Gmail SMTP to send confirmation emails and all AllAuth related emails when the deployed version is used. I used the following documentation to set it up and add these settings to my settings.py file:

### Stripe
In order to take payments for the online store, I implemented Stripe; you first must create an account with them and then using the documentation add the relevant HTML, python & JS code suitable for your needs

### AWS static and media storage
All static and media files are stored in the cloud using Amazon AWS S3; i have created a bucket, user group and user that can access this site and the relevant files. In order for the files to be correctly served the following settings have to be added to your main settings.py file:

## Creating an Application with Heroku
I followed the below steps using the Code Institute tutorial and Django Blog cheatsheat

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies pip3 freeze --local > requirements.txt. Please note this file should be added to a .gitignore file to prevent the file from being committed. A Procfile is also required that specifies the commands that are executed by the app on startup.

1. Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
2. Click the New dropdown and select Create New App.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

***Heroku Settings*** You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

- In the Settings tab, click on Reveal Config Vars and set the following variables:

In the resources tab you must install 'Heroku Postgres'

***Heroku Deployment using website In the Deploy tab:***
1. Connect your Heroku account to your Github Repository following these steps:
    - Click on the Deploy tab and choose Github-Connect to Github.
    - Enter the GitHub repository name and click on Search.
    - Choose the correct repository for your application and click on Connec
2. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.
3. Once you have chosen your deployment method and have clicked Deploy Branch your application will be built and you should see the below View button, click this to open your application:

Heroku CLI deployment Whilst building this project there was a security breach on Heroku which caused issues with deployment via their website. Due to this, I had to add a runtime.txt file specifying which version of Python to build the app with and used the following commands to push the code to Heroku:

1. Login to Heroku via the CLI using heroku login -i
2. Enter your email and password
3. Connect to the Heroku git remote using the heroku git:remote -a YOURAPPNAME
4. Push to the Heroku git remote using git push heroku main.

***

## Credits 

Throughout the process of building Casa Arana I used a mixture of online resources to help me with a range of different things from fixing bugs, build functionality and design features. Below are the resources I used :

[Unsplash](https://unsplash.com/) - For all imagery 

[Bootswatch Lux theme](https://bootswatch.com/lux/ )- For nav bar functionality

[Skolo online](https://skolo.online/) - for Django model and image help 

Code Institute’s Boutique Ado project walk through videos - for Django logic code and structure

W3schools - for code 

Crispy Forms 

Django Alauth 

DrawSQL - for database schema design

Figma - for firebase designs 

XML Sitemaps 

***

## Acknowledgements
I’d like to take this chance to thank my course mentor Jack for his guidance and support throughout the development of this project. My colleague Harry Dhillon for their support and feedback and the Tutors at Code Institute for their help with debugging and overall support. 