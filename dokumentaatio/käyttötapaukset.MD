# Käyttötapaukset

## User Story # 1 Completed  
As a customer, I want to see what items are available, so that I can decide what I want to order  
## User Story # 2 Completed  
As a customer, I want to make an order, so that I can get food    
I should be able to add items to the order  
The order should be passed to the server    
The order should be saved in the DB  
I should be able to see a confirmation of the order I have placed  
## User Story # 3 Completed  
As a customer, I want to save my info, so that I an place an order faster the next time I use the app  
## User Story # 4 Completed  
As a restaurant owner, I want to see the orders that have been placed, so that I can send the customer food    
    - I shouldn't be able to see other restaurants' orders  
    - I shouldn't be able to see the orders if I'm not logged in  
## User Story # 5 Completed  
As a restaurant owner, I want to add menu items, so that users can order new menu items    
-  I shouldn't be able to add items on to other restaurants' menus  
## User Story # 6 Completed  
As a restaurant owner, I want to delete menu items, so that I can stop serving items that do not create profit  
- I shouldn't be able to delete other restaurants' menu items
- Items do not actually get deleted, since they're needed for old orders.  
## User Story # 7 Completed
As a restaurant owner, I want to update menu items, so that I don't have to delete and create a new one whenever I want to make a small change to a menu item       
- I shouldn't be able to edit other people's menu items  
- Old versions of the item do not actually get deleted, since they're needed for old orders.  
   
  
## --- Potential future user stories, not prioritized     
As a customer, I want to save an order template, so that I can place an order faster the next time I use the app  
As a customer, I want to see my old orders, for whatever reason   
As a restaurant owner, I want to create a new restaurant on the app  
As a restaurant employee, I want to filter the orders list so that I can find relevant stuff faster  

## Technical tasks  
Differentiate between restaurant OWNER (see orders, menu CRUD) and restaurant EMPLOYEE (can browse orders, but not manage menu).      
Error messages to user from stupid stuff (like trying to browse nonexistent restaurant's orders, or manipulating order data manually before sending it to the server)  
CSS styling needs work, especially for the manager view  
