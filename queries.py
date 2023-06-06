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

findCustomerAccountQuery = "SELECT customer_id FROM customer WHERE email = %s"

findSellerAccountQuery = (
    "SELECT seller_id FROM seller WHERE email = %s OR phone = %s OR username = %s"
)

createCustomerAccountQuery = "INSERT INTO customer (fname, lname, address, email, password) VALUES (%s, %s, %s, %s, %s)"

createSellerAccountQuery = "INSERT INTO seller (fname, lname, username, phone, email, password) VALUES (%s, %s, %s, %s, %s, %s)"

loginCustomerQuery = "SELECT * FROM customer WHERE email = %s"

loginSellerQuery = "SELECT * FROM seller WHERE email = %s"

getAllProductsCoverImageQuery = "SELECT product.product_id, ( SELECT image_url FROM images WHERE images.product_id = product.product_id LIMIT 1 ) AS image_url FROM product ORDER BY product.product_id ASC"

getSearchedProductsCoverImageQuery = "SELECT product.product_id, ( SELECT image_url FROM images WHERE images.product_id = product.product_id LIMIT 1 ) AS image_url FROM product WHERE product.product_name LIKE %s ORDER BY product.product_id ASC"

getCategoryProductsCoverImageQuery = "SELECT product.product_id, ( SELECT image_url FROM images WHERE images.product_id = product.product_id LIMIT 1 ) AS image_url FROM product WHERE product.category_id = %s ORDER BY product.product_id ASC"

getProductDetailsImagesQuery = "SELECT * FROM images WHERE images.product_id = %s"
