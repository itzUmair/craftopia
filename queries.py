# This file contains all the queries.
# I have seperated this file to simplify the files

getAllItemQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id;"

getItemQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id; WHERE product.product_id = %s"

getCustomerDetailQuery = "SELECT CONCAT(fname,' ',lname) as 'Customer Name', address, email FROM customer WHERE customer_id = %s"

getAllProductOfSellerQuery = "SELECT product_name, price_per_unit, stock_in_inventory FROM product WHERE seller_id = %s"

getAllProductsByCategoryQuery = "SELECT product.*, AVG(reviews.rating), category.category_name, COUNT(reviews.review_id) FROM product LEFT JOIN reviews ON product.product_id = reviews.product_id LEFT JOIN category ON product.category_id = category.category_id GROUP BY product.product_id HAVING category_id = %s"
