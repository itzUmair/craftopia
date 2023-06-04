# This file contains all the queries.
# I have seperated this file to simplify the files

getAllItemQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id;"

getItemQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id HAVING product.product_id = %s"

getCustomerDetailQuery = "SELECT CONCAT(fname,' ',lname) as 'Customer Name', address, email FROM customer WHERE customer_id = %s"

getAllProductOfSellerQuery = "SELECT product_name, price_per_unit, stock_in_inventory FROM product WHERE seller_id = %s"

getAllProductsByCategoryQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id HAVING category_id = %s"

getSearchedProductQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id HAVING product.product_name LIKE %s"

sellerUpdateProfileQuery = "UPDATE seller SET fname = %s, lname = %s, username = %s, phone=%s ,email = %s,password = %s WHERE seller_id = %s"

customerUpdateProfileQuery = "UPDATE customer SET fname = %s, lname = %s, address = %s, email = %s,password = %s WHERE customer_id = %s"

setShippedOrderQuery = "UPDATE orders SET status = 'Shipped' WHERE order_id = %s"

setCompletedOrderQuery = "UPDATE orders SET status = 'Completed' WHERE order_id = %s"

addProductQuery = "INSERT INTO product (product_name, price_per_unit, stock_in_inventory, category_id, seller_id) VALUES (%s, %s, %s, %s, %s)"

deleteProductQuery = "DELETE FROM product WHERE product_id = %s"

updateProductQuery = "UPDATE product SET product_name = %s, price_per_unit = %s, stock_in_inventory = %s, category_id = %s WHERE product_id = %s"
