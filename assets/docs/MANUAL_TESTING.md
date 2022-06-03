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

![screenshot of back to top arrow](/assets/images/backtotop-arrow.png)
![screenshot of back to top arrow on hover](/assets/images/backtotop-arrow-on-hover.png)

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

- The Site owner can also delete an existing products by clicking on the the Delete link found in the production information page. Once the user has clicked on it the product will be automatically deleted without any warning. Once the product has been deleted, a toast message will appear to confirm back to the Site owner that the product has been Deleted. To further improve this feature I would have included a modal to appear to ensure the Site owner is definite sure they want to delete this product, incase they click on this link by mistake. 

![admin edti and delete links](/assets/images/edit-delete-links.png)

***

### User Account - As a Shopper (Shopper)

17. As a User I can register & login so that I can view my order history  and wishlist.

- Once a user is logged in, using the ‘View My Account’ link in the nav bar, it will bring the user to their account overview page. From here they can access either their personal details and previous orders. 

- The Default Delivery info will display the users delivery information if they have ticked the ‘save info for later’ box displayed during checkout. If the user has not previously saved their delivery information, they can easily fill out the form and by clicking the ‘Update’ button, it saves their information and is then used to pre populate the checkout form whenever the User is ready to make a new purchase. 

- On submitting the updated form, an info toast message appears notifying them that their information has been updated. 

- The Order History and Delivery information are displayed in a responsive accordion where the user can easily toggle between the two features allowing the User to easily and quickly review the information required. By Click on the Order History Id, the user is directed back to the Order’s checkout success page where the user can see again the complete order details for that particular order number.

- On this checkout success page, it contains a link taking the user back to their account to easily navigate between their account and order information.

- The User’s Wishlist is accessible by the ‘View Wishlist’ link displayed in the profile icon dropdown menu. Upon clicking this link, the user is redirected to their Wishlist page where it displays all the items they have saved to their wishlist. 

- The images are displayed in bootstrap cards for better responsively. The cards contain the product image, the product name and price with a clear link to view the product’s full details, as well as another link to remove the item for their Wishlist. If the user clicker on the remove link the Wishlist page will refresh and the user will be notified that the product was deleted from their Wishlist.

- The User can add items to their Wishlist by clicking on the ‘Add to Wishlist’ link found on the product info page. If the item has already been added to the Wishlist then the user will be notified via a toast message and the item is not added in order to have two of the same items. If the item is not already in the Wishlist, then the item will be added and the user will be notified via a toast message.


***
