# This file contains all the queries.
# I have seperated this file to simplify the files

getAllItemQuery = "SELECT * FROM product"

getItemQuery = "SELECT * FROM product WHERE product.product_id = %s"

getCustomerDetailQuery = "SELECT CONCAT(fname,' ',lname) as 'Customer Name', address, email FROM customer WHERE customer_id = %s"
