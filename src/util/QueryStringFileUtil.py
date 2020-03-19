query_create_table_product = "CREATE TABLE IF NOT EXISTS product (" \
                          "cod integer PRIMARY KEY, " \
                          "description text NOT NULL," \
                          "ean text NOT NULL," \
                          "stock integer NOT NULL," \
                          "price double NOT NULL, " \
                          "url text)"

# Select
query_select_product = "SELECT * FROM product;"

# Select
# query_insert_product = "INSERT INTO product(cod, description, ean, stock, price, url) VALUES(?,?,?,?,?,?)"
query_insert_product = 'INSERT INTO product VALUES(?,?,?,?,?,?)'
