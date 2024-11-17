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
   

