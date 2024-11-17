# Purchase/Sale Management Web Application Using Flask

This web application is designed to streamline the inventory and sales management processes for businesses. Built with Flask, it provides an intuitive interface for managing products, tracking purchases and sales, and reviewing transaction history.

---

## Features

- **Home**: Overview of inventory and quick navigation to key features.
- **Add Item**: Add new products to the inventory with ease.
- **Purchase**: Record purchases and update stock automatically.
- **Sale**: Enables the sale of items while updating inventory accordingly.
- **Purchase History**: View detailed records of all purchase transactions.
- **Sale History**: Access and analyze sales data for better decision-making.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite

---
## Setup and Installation

Follow the steps below to set up and run the **Purchase/Sale Management Web Application** using **Flask** and **SQLite**.

### Prerequisites

Make sure you have the following installed:
- **Python 3.x**
- **pip** (Python package installer)

### Clone the Project

1. Open your terminal (Command Prompt or any terminal you use).
2. Clone the repository using the following command:<br>
    Git clone https://github.com/dhanush-r0119/BreadcrumbsPurchase-Sale-Management-Web-Application-using-Flask.git

## Web Page Functionalities
## 1.Home Page

The Home Page serves as the central hub of the Purchase/Sale Management Web Application, providing a detailed overview of the inventory along with easy navigation to other pages.

### Features:
- **Inventory Overview**: Displays all items from the database in a detailed table format, showing:
  - **Stock Quantity**: Indicates the available quantity of each item.
  - **Out-of-Stock Status**: Highlights items that are out of stock.
  - **Last Purchase Price**: Shows the most recent purchase price for each item.
  - **Last Sale Price**: Displays the most recent sale price.
  - **Profit Earned**: Calculates the profit earned from the sales of each item.
- **Quick Navigation**: Easy routing to:
  - Purchase
  - Sale
  - Purchase History
  - Sale History
- **Comprehensive Data**: View detailed product information at a glance to help manage inventory effectively.

### Screenshot:
![Home Page Screenshot](https://drive.google.com/uc?id=1-C3t2XqumvyaxIUB2Lf5f5IVQrBj_2Gt)


The Home Page allows users to monitor inventory levels, track product sales, and quickly identify any out-of-stock items, making it an essential tool for inventory management.
## 2.Purchase Page

The **Purchase Page** allows users to add new stock to the inventory. This page not only enables users to purchase products but also displays the current balance and updates the stock accordingly. In case the purchase exceeds the available balance, an error message will be shown.

### Features:
- **Item Selection**: Choose an item from the list of available products.
- **Quantity Input**: Enter the quantity of the item to be purchased.
- **Rate**: Specify the purchase rate for the item.
- **Stock Update**: Once a purchase is made, the item quantity in the database is updated accordingly.
- **Current Stock Display**: Shows the current stock level of each item in the inventory.
- **Current Balance Display**: Displays the available balance for the user to make a purchase.
- **Flash Messages**: If the purchase exceeds the available balance, an error message is displayed.

### How it Works:
1. **Select Item**: From the dropdown list, choose the item you want to purchase.
2. **Enter Quantity**: Input the quantity you wish to add to the stock.
3. **Set Purchase Rate**: Specify the rate at which you purchased the item.
4. **Check Balance**: The page will show the current balance, helping you to verify if you have enough funds.
5. **Submit Purchase**: If the purchase total is within the available balance, the purchase will be processed, and the stock will be updated.
6. **Error Flash Message**: If the purchase exceeds the current balance, an error message will be displayed, preventing the purchase from going through.
This page helps in managing the inventory by keeping track of purchases and updating product quantities efficiently.

### Screenshots:

1. **Purchasing product**  
   ![Purchase Page Screenshot](https://drive.google.com/uc?id=1rokVttFGhRkV7bKfcS9KJMJZ_bUG4Qnv)
2. **Product Purchased Successfully**
   ![Purchase Page Screenshot](https://drive.google.com/uc?id=1PqulUKDxPl32tXzb_8g4ERVxiIakE_0z)
   
## 3.Sale Page

The **Sale Page** allows users to sell products from the inventory. It facilitates tracking the sales, updating the stock, and increasing the company's cash balance based on the sale. If the requested sale quantity exceeds the available stock, an error message is displayed to prevent selling the product.

#### Features:
- **Item Selection**: Users can choose an item to sell from the available stock.
- **Quantity Input**: Enter the quantity of the item to be sold.
- **Sale Rate**: Specify the sale price for the item.
- **Stock Update**: The stock quantity of the item is updated after the sale.
- **Cash Balance Update**: The sale amount is added to the company's cash balance.
- **Out-of-Stock Error**: If the requested sale quantity exceeds the available stock, an error message is shown.

#### How it Works:
1. **Select Item**: Choose the item to be sold from a dropdown list populated with available products.
2. **Enter Quantity**: Input the quantity of the item to be sold.
3. **Set Sale Price**: Specify the rate at which the item will be sold.
4. **Check Stock**: If the stock quantity is sufficient, the sale proceeds, and the item's quantity is updated accordingly.
5. **Update Cash Balance**: The cash balance of the company is updated based on the total sale amount (quantity * rate).
6. **Error Flash Message**: If the sale quantity exceeds the available stock, an error message is displayed.

#### Example of Flash Messages:
- **Success Message**: "Sale successful! Cash balance updated."
- **Error Message**: "Insufficient stock to complete the sale."

#### Screenshots:
1. **Selling Product**
   ![Sale Page Screenshot](https://drive.google.com/uc?id=1HLvgug-eGdPIPpzDxTlKUQZQTWO4vGsJ)

2. **Out of stock error**
   ![Item Dropdown Screenshot](https://drive.google.com/uc?id=1KtR6t9KC9BY6Q-NBIlp4RlZnzk9SIhGw)

## 3.Purchase History Page

The **Purchase History Page** displays all the purchases made in the system. It provides a detailed view of each purchase, including the item name, purchase time, quantity, and price of the product. This page helps track and review all past purchases made by the company.

#### Features:
- **Purchase Details**: The page shows a table with all the relevant details for each purchase:
  - **Time**: The timestamp of when the purchase was made.
  - **Item Name**: The name of the purchased item.
  - **Quantity**: The number of units purchased.
  - **Price**: The price at which the product was purchased.
- **View All Purchases**: Displays all purchases in a table format for easy tracking.
- **Pagination**: If there are too many records, pagination will help navigate between multiple pages of purchase history.

#### How it Works:
1. **Table Display**: The page automatically loads a table showing all the purchase history records.
2. **Columns**: The table contains the following columns:
   - **Item Name**: Name of the item purchased.
   - **Quantity**: Quantity purchased.
   - **Price**: Price of the purchased item.
   - **Time**: Date and time the purchase was made.
3. **Sorting and Filtering**: Depending on implementation, users can sort the records by date or item name for easy access.
4. **View Details**: Users can click on specific purchases to view more detailed information if needed.

#### Screenshots:
1. **Purchase History Table**
   ![Purchase History Table Screenshot](https://drive.google.com/uc?id=153C2NKzsdXg0vfy-7h28wazMZamSs8om)

## 4.Sale History Page

The **Sale History Page** displays all the sales transactions made in the system. It provides a detailed view of each sale, including the item name, sale time, quantity sold, and rate at which the product was sold. This page helps track and review all past sales, including details of items sold and their sale values.

#### Features:
- **Sale Details**: The page shows a table with all the relevant details for each sale:
  - **Sale Time**: The timestamp of when the sale occurred.
  - **Item Name**: The name of the item sold.
  - **Quantity Sold**: The number of units sold.
  - **Sale Rate**: The rate at which the item was sold.
- **View All Sales**: Displays all sales records in a table format for easy tracking.
- **Pagination**: If there are too many records, pagination will help navigate between multiple pages of sale history.

#### How it Works:
1. **Table Display**: The page automatically loads a table showing all the sale history records.
2. **Columns**: The table contains the following columns:
   - **Sale Time**: Date and time the sale was made.
   - **Item Name**: Name of the sold item.
   - **Quantity Sold**: Number of items sold.
   - **Sale Rate**: The rate at which the item was sold.
3. **Sorting and Filtering**: Depending on implementation, users can sort the records by date or item name for easy access.
4. **View Details**: Users can click on specific sale records to view more detailed information if needed.

#### Screenshots:
1. **Sale History Table**
   ![Sale History Table Screenshot](https://drive.google.com/uc?id=1GMfC1iDycLEWkh6dQ1drJgHUfRi__0KY)

## 5.Add Item Page

The **Add Item Page** allows users to add new products to the inventory. This page is crucial for managing products in the system by enabling the addition of new items with all necessary details, such as item name, quantity, and price. It also checks whether the item already exists in the inventory to prevent duplication.

#### Features:
- **Add New Product**: The form allows users to input new product details and submit them to the inventory.
  - **Item Name**: The name of the product.
  - **Quantity**: The quantity of the product to be added.
  - **Price**: The price at which the product will be sold.
- **Duplicate Check**: Before adding a new item, the system checks if the product name already exists in the inventory to avoid duplicate entries.
- **Form Validation**: Ensures that all fields are correctly filled before submission.
- **Error Handling**: Flash messages are shown for any errors during form submission (e.g., missing fields, duplicate item names, or invalid inputs).

#### How it Works:
1. **Input Fields**: The form contains fields to input the item’s:
   - **Item Name**: The name of the new product.
   - **Quantity**: The available stock quantity of the product.
   - **Price**: The selling price of the product.
2. **Duplicate Check**: When submitting the form, the system checks if an item with the same name already exists in the database. If it does, a flash message will notify the user that the item already exists, and no new item will be added.
3. **Submission**: If the item does not exist, the form submits the data to the database.
4. **Validation**: Before submission, the form checks if all required fields are filled out. If any field is missing or incorrect, an error message will be displayed.
5. **Confirmation**: After a successful addition, a flash message confirms the successful addition of the new item.


#### Screenshots:
1. **Add Item Form**
   ![Add Item Screenshot](https://drive.google.com/uc?id=1CpJcaH_pCioy_M4SZEobG3Oq5I1OYgUA)

2. **Item already exist**
   ![Confirmation Screenshot](https://drive.google.com/uc?id=1U7j02m6D6kMKiFH65gXUf7WNGKqyRCWg)

## 6.Edit Item Page

The **Edit Item Page** allows users to update the details of an existing product in the inventory. This page is used to modify the product name or any other editable information for an item that already exists in the database.

#### Features:
- **Edit Product Information**: Users can edit the name of a product in the inventory.
- **Search for Existing Items**: A list of products can be accessed, and the user can select the item they wish to edit.
- **Form Validation**: Ensures that the new product name is entered correctly before submission.
- **Duplicate Check**: If the new name entered already exists for another product, an error message will be displayed to avoid duplicates.
- **Error Handling**: Flash messages will appear for any errors, such as invalid or empty fields.

#### How it Works:
1. **Item Search**: The user selects an item from the list to edit. This action pre-fills the form with the current product information.
2. **Edit Form**: The form allows users to modify the product name.
   - **Product Name**: The user can enter the new name for the item.
3. **Duplicate Check**: The system checks if the new product name already exists in the inventory. If it does, an error message will notify the user that the name is taken.
4. **Submission**: After the user updates the information and submits the form, the new details will be saved in the database.
5. **Confirmation**: After a successful update, a confirmation message is displayed, indicating that the product details have been successfully edited.


## Database Schema

Below is the screenshot showing the database schema of the application:
1. **Items table**
![Database Data](https://drive.google.com/uc?id=1W7kiw6wlMFpuAJzjV2eQ8putUHMzr5Es)
2. **Purchase table**
![Database Data](https://drive.google.com/uc?id=1RHPk-6KgSfTSRbfNr19ercM17enkLnrq)
3. **Sales Table**
![Database Data](https://drive.google.com/uc?id=1nYedGesySEs3tIGkqIQqfs62rshE6Zj5)
3. **Company Table**
![Database Data](https://drive.google.com/uc?id=1xBPcmGy45c91W_5AEVjHYLcn5066pP9O)




