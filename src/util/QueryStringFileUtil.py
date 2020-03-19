query_create_table_product = "CREATE TABLE IF NOT EXISTS product (" \
                          "cod integer PRIMARY KEY, " \
                          "description text NOT NULL," \
                          "ean text NOT NULL," \
                          "stock integer NOT NULL," \
                          "price double NOT NULL, " \
                          "url text)"

# Select
query_select_product = "SELECT * FROM product;"
query_check_product_id_has_exists = "SELECT COUNT(*) > 0 FROM product WHERE COD=?;"

# Insert
query_insert_product = 'INSERT INTO product VALUES(?,?,?,?,?,?)'

# Delete
query_delete_all_products = 'DELETE * FROM product'
query_delete_by_cod = 'DELETE * FROM product WHERE cod=?;'
