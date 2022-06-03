## Manual Testing for Casa Arana 

The manual testing undertaken was used against the user stories defined in the [Casa Arana User Stories file](https://docs.google.com/spreadsheets/d/1XdgCMRVrfw2YlieImYsSJ_6mn5kbYvmL0O8vrmCCRKM/edit#gid=0)

[Back to main README](/README.md)

***

### Core Functionality - As a User (shopper)

1. As a User I can intuitively navigate through the site so that I can view the desired content.

2. As a User I can find a navigation bar so that I can see what links there are on the website and easily access them at any time. 

3. As a User I can get key information about the e-commerce site from the landing page so that I can spend less time having to search for information.

4. As a User I can find a footer containing the contact information for the e-commerce site including business email and social media accounts.

- The navigation bar is fixed at the top of the screen, meaning it is always seen by the user, allowing the user to navigate through the content easily & intuitively. Each nav link is named with an obvious link to the page content, for the shop and admin links there are dropdowns for subsections of the website so that the information is organised, as well as leaving the navbar decluttered.

- On mobile and medium screens it collapses to a hamburger menu and laptop and desktop screens in spans across the width of the device and split into two sections. The left side displays the company’s Logo name (which when clicked, takes the user back to the home page) and links to the store and about page, and on the left of the nav bar is the profile icon with dropdown links to view user profile, admin management (if site owner), wish list and login/log out links. The left also contains the shopping bag icon which displays the number of items inside the user’s shopping bag. 

![screenshot of navbar](/assets/images/navbar-fullwidth.png)

- I have added a back to top arrow which is becomes visible after the User scrolls down the page from 20px. It is visable on every page throughout the site enabling the user to quickly navigate back to the top without having to scroll. On hover, a pointer cursor appears and the arrow changes colours in order to provide a nice contrast as well as improve the visibility so that the User can easily spot it.

![screenshot of back to top arrow](/assets/images/backtotop-arrow.png) ![screenshot of back to top arrow on hover](/assets/images/backtotop-arrow-on-hover.png)

- The footer is fixed at the bottom of the page and contains key contact information including the business’s email and social media account links.The social media links open on new tabs improving the user experience as they click through the links they do not loose their initial enquiry. The business email will always be searched for the User and so including it in the footer ensures it’s always and easily accessible to find.

![screenshot of footer](/assets/images/footer.png)

4. As a User I am notified about any changes I have made so that I have a clear understanding of what has been completed/updated/failed.

- I have used bootstrap toasts to display messages to the user at various points throughout their customer journey. The success toast is used often and when adding a product to the basket and the shopping bag icon displays the number of times inside the user’s shopping bag and updates accordingly wether the user has updated the product quantity or removed. 
- If I had more time, I would have included a short overview of the shopping bag content inside the success toast so that the User can review the product and cost information is as expected. 

![success message](/assets/images/success-toast-added-to-bag.png)

- I have also used info, warning and error toasts to display various other messages; this ensures the User has awareness of any changes that have been made or have been unsuccessful:

![alert message](/assets/images/alert-toast.png)

5. As a User I can access the website on both mobile and desktop so that I can view the information regardless of my location.

- As I have used bootstrap, the website is entirely responsive and can be viewed on any size screen and have the same functionality without visually imparing the the UX. 

![responsive view on mobile screens](/assets/images/responsive-mobile.png)

- However, the only page where the responsiveness is not as great as other pages is the shopping bag page. The contents is displayed inside a table which doesn’t allow for the best responsivity, this should have been done in a Bootstrap grid in order for the information to be displayed clearer on smaller devices. Nonetheless, the shopping bag functionality works as expected and displays better to larger screens.

![shopping bag on desktop screens](/assets/images/shopping-bag-desktop.png)

***

## Products - As a User (shopper)

6. As. User I can view all products that are avialable to purchase.

- Using the Shop nav link, the User is directed to the all_produts page where all the products from the product model are displayed in a responsive and clean way. 
- The User can also view key product information as product name, price and category. 

![all products page](/assets/images/all-products-page.png)

7. As a User I can easily find all relevant product information so that I can make an informed decision before purchasing.

 - Each image displayed in the all products page are links to that specific product’s information page. Inside the information page, the user can view more information about the product including product features, description, dimensions, a short bio of the Artisan who made it and product reviews. 

![product information](/assets/images/product-info.png)

 - The Artisan section provides information about the Artisan who made that particular product. Most likely the users will be conscious buyers and so like to know/have an understanding of where their products come from in order to help them make a decision before buying a product.

![artisan section in product info page](/assets/images/artisan-section.png)

8. As a User I can read product reviews on a particular product so that I can gain more information about the product before purchase.

- Displayed at the bottom of the product info page is the review section where a User can view past product reviews. The reviews are ordered by the most recent date allowing the user to read the most recent reviews at the top of this section.

- The reviews are contained in Bootstrap cards allowing for better responsively. The contain a review tittle, comment, date and the name of the User. 

![procut review section](/assets/images/product-reviews.png)


9. As a User I can filter the products by categories to have more control over what I’m viewing.

- The Shop link in the nav bar displays a dropdown menu of all the categories, by clicking on the relevant category link, the all products page will display the products that come under that category. The header in the all products page will also inform the customer of how many products have been found for each category for their easy convenience.

![category links](/assets/images/navbar-category-links.png)

10. As a User I can sort the products by price so I can find the best priced item within the selected category 

- The all products header container contains a ‘Sort By’ function where the user  can sort all profits by price either from Highest to Lowest and vice versa by clicking on the relevant link.

![shop by filter](/assets/images/shopby-filter.png)

11. As a User I can sort products inside a particular category by price to;

- Due to time constraints, this functionality was not added. 

***

### Orders and Shopping Bag - As a User (shopper)

12. As a User I am able to prlace an order by making a secure card payment;

- Using Stripe, each time the checkout page is loaded a payment intent is created and a card element is injected into the page. Using the test card details from the Stripe documentation you can test the checkout process, if successful a success message is displayed a via a toast message and the user is redirected to the checkout success page.

![payment success page](/assets/images/checkput-success-page.png)

- If the payment process is being handled by stripe then the page loader will appear on the screen to indicate to the user that their payment is being checked and processed.

![page loder](/assets/images/loader.png)

- If a payment did not succeed then the user will be notified via a toast message and will be redirected back to their shopping bag where they’ll be able to retry the checkout process. 

- If a user inputs an invalid card number then they will be notified 

![invalid card number](/assets/images/invalid%20-card-number.png)


13. As a User I can view a breakdown of my current shopping bag so that I can make changes if required before placing my final order. 

- The shopping bag page displays all of the information regarding the users current basket, product name & image, total number of items, subtotal, delivery cost if application and order grand total

- The plus or minus buttons will change the quantity in the select box and then pressing update pushes those changes to the user's current basket.

- The remove link enables the user to remove an item from their bag is they no longer require it, after removing the product, the shopping bag information is updated to reflect the changes made. 

![shopping bag on mobile screens](/assets/images/shopping-bag-mobile.png)

- In addition to the above, the Shopping bag icon in the navbar also dispalys the current number of items inside the User's shopping bag so that they are aware of how many items are in their shopping bag without having to check their bag each time. 

![shopping bag icon](/assets/images/shopping-bag-icon.png)

14. As a User I receive order confirmations to be sure my order has been processed.

- Upon submitting the payment form, if successfully then the user is redirected to the checkout success page where they can review their order information including order number, date purchased and delivery information. A toast message also appears notifying the User their payment has gone through and an email will be sent to them with their order confirmation.

![payment success](/assets/images/payment-success.png)

***

## Admin Functionality - As a Site owner

15. As a Site owner I can log in so that I can access the site's backend.

- Using a specified superuser account, the site owner/admin user can access the /adimin URL and login, they will then be taken to the ‘Django Administration’ page where they can access the database

![admin url](/assets/images/admin-url%3B.png)

16. As a Site owner I am able to log in to see the product management page so that I can make changes in the front end.

![backend django admin interface](/assets/images/backend-admin.png)

- Once logged in as an admin superuser, the profile icon drowndown menu will then include the Procut Management link, clicking this takes the user to the Add Product page where they can upload a new product to the website. 

![product managament link](/assets/images/product-management-link.png)

- The Site owner can edit existing product information information by clicking on the Edit link found in the product information page. Clicking this link will take the site owner to the Exit Product page where they can the desired information. Once the form is submitted a toast message will appear to inform the product has been updated.

![admin add product](/assets/images/add-product-page.png)

- The Site owner can also delete an existing products by clicking on the the Delete link found in the production information page. Once the user has clicked on it the product will be automatically deleted without any warning. Once the product has been deleted, a toast message will appear to confirm back to the Site owner that the product has been Deleted. To further improve this feature I would have included a modal to appear to ensure the Site owner is definite sure they want to delete this product, incase they click on this link by mistake. 

![admin edti and delete links](/assets/images/edit-delete-links.png)

***

### User Account - As a Shopper (Shopper)

17. As a User I can register & login so that I can view my order history and wishlist.

- Once a user is logged in, using the ‘View My Account’ link in the nav bar, it will bring the user to their account overview page. From here they can access either their personal details and previous orders. 

![user profile](/assets/images/user-profile.png)

- The Default Delivery info will display the users delivery information if they have ticked the ‘save info for later’ box displayed during checkout. If the user has not previously saved their delivery information, they can easily fill out the form and by clicking the ‘Update’ button, it saves their information and is then used to pre populate the checkout form whenever the User is ready to make a new purchase. 

- On submitting the updated form, an info toast message appears notifying them that their information has been updated. 

![user default delivery info](/assets/images/user-delivery-form.png)

- The Order History and Delivery information are displayed in a responsive accordion where the user can easily toggle between the two features allowing the User to easily and quickly review the information required. By Click on the Order History Id, the user is directed back to the Order’s checkout success page where the User can see the complete order details for that particular order number.

![order history](/assets/images/order-history-list.png)

![order history checkout sucess](/assets/images/order-history-toast.png)

- On this checkout success page, it contains a link taking the user back to their account to easily navigate between their account and order information.

- The User’s Wishlist is accessible by the ‘View Wishlist’ link displayed in the profile icon dropdown menu. Upon clicking this link, the user is redirected to their Wishlist page where it displays all the items they have saved to their wishlist. If the User has no items save to their Wish List then the wishlist page will display a messge to the User notifying them of this with a link taking them back to the store for easy navigation. 

![wishlist empty](/assets/images/wishlist-empty.png)

- The images are displayed in bootstrap cards for better responsively. The cards contain the product image, the product name and price with a clear link to view the product’s full details, as well as another link to remove the item for their Wishlist. If the user clicks on the remove link the Wishlist page will refresh and the user will be notified that the product was  successfully deleted from their Wishlist.

![wishlist item info](/assets/images/wishlist-item.png)

- The User can add items to their Wishlist by clicking on the ‘Add to Wishlist’ link found on the product info page. If the item has already been added to the Wishlist then the user will be notified via a toast message and the item is not added in order to have two of the same items. If the item is not already in the Wishlist, then the item will be added and the user will be notified via a toast message.

![wishlist links](/assets/images/wishlist-links.png)

18. As a User I can easily see if I'm logged in or not so that I can choose to log in or log out as needed. 

- The profile icon downdown menu updates to display either the Log in or Log out links depending on the authentication state of the user.

- If the user is not authenticated then, the Create Account and Login link are displayed. This differentiation makes it very clear and obvious to the user if they are currently logged in.

![navbar login link](/assets/images/navbar-login.png) ![navbar log out links](/assets/images/navbar-logout.png)

19. As a User I am prompted to register for an account so that I can create an account and receive the benefits of having a profile.

- The register link in the navbar is the first prompt, if the user clicks to log in this page will prompt them to register for an account if they don't already have one.

![sign up form](/assets/images/sign-up-form.png)

- On the checkout page, if the user isn't logged in, there is a paragraph that prompts the user to register or log in to save their details for next time:

![sign in or create account link to save info for next time](/assets/images/delivery-info-not-logged-in.png)

20. As a User I can log in so that I can auto-populate forms with my information on the site.

21. As a User I can save my default billing/shipping details so that I can save time making my next purchase.

- When a user first creates an account and logs in, none of their information will be saved to their profile yet, but after completing the user profile form or making their first order (with the save details box ticked) then both the user profile form and the order form will be pre-filled with their detail.

![save delivery information checkbox](/assets/images/save-info-checkbox.png)

***

### Marketing

22. As a User I can sign up for a newsletter to company updates and items for sale. 

- Above the footer is the MailChimp sign up form. Its' placed here in order to be accessible to the user throughout the site and easily aviably to them wheber they are ready to sign up if they haven't done so already;

![MailChimp sign up form](/assets/images/mailchimp-signup.png)

23. As a Site owner, I conducted research and implemented SEO keyword research to increases traction to my website
After my research I then went onto add important key words across the website content and added keywords to the meta tags and descriptions:

![meta tag descritoins in header](/assets/images/meta-tag-descriptions.png)

24. As a Site owner I haver created a Facebook page to increase traction to my website. 

Facebook page for the Casa Arana Page can be found [here](https://www.facebook.com/casaaranaofficial/)

![facebookpage](/assets/images/facebook2.png)

***

### JavaScript testing

There is a number of JS functions across the site in order to achieve the desired functionality. For functions required across the website, they are found at the bottom of the base.html template, for specific page-related functions they are located within the respective js folders. 

**Back to Top School functionality**
The JS for this is located in the projects base.html file as it is a function used across the entire site. It’s a short piece of code therefore I did not put it in it’s own folder. 
- The function displays an up arrow after the user scrolls 20px down the screen. On clicking the arrow the user is then taken back up to the top of the page and this function works as expected across all pages. 
- This source code was taken from [W3school](https://www.w3schools.com/)

![back to top scroll function call](/assets/images/back-to-top-functioncall.png)
![back to top scroll fucntion](/assets/images/back-to-top-function.png)

**Toast Messages functionality**
The JS for this is located in the projects base.html file as it is a function used across the entire site. It’s a short piece of code therefore I did not put it in it’s own folder. 
- The function calls the ready function with calls the relevant toast message to appear after a user has done a specific action. This function words as expected.

![toast function](/assets/images/toast-function.png)

**MailChimp functionality**
The code for this is located inside the mailchimp_sign_up.html template in order to keep all MailChimp code in one location. The JS code is taken form the MailChimp website when creating the sign up form and works as intended. 

**Qty Increase and decrease functionality**
The code for this is location in the shopping_bag html page and the function is used to change the quantity value of each product in the shipping bag.
- I have added a respective classes to each of the product increase/decrease buttons, so that when the button is clicked the correct quantity field is update. 
The code works as intended  

![Quantitiy update /remove function](/assets/images/quantity-update-remove-function.png)

**Stripe Elements**
The source code for the Stripe Elements functionality is taken from the [Stripe Elements documentation](https://stripe.com/docs/payments/elements). The code is saved in a js folder in the checkout app. 
- The functions handles submission of payment forms and functionality. 
- This function submits the payment form, posting the data to Stripe via the cache_checkout_data view and returns a success message if the payment was successful and redirects the User to the checkout_sucess page:

![checkout success toast](/assets/images/checkout-success-toast.png) ![checkout success page](/assets/images/checkput-success-page.png)

- Also Stripe's webhooks will send a 200 response messages, which is a success, notifying that the payment intent worked;

![payment intent succeeded](/assets/images/payment-intent-succeeded.png)

- The user will also be sent a confirmation email confirmig their order has been procssed:

![confirmation email](/assets/images/confirmation-email.png)
