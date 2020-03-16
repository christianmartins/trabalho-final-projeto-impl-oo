querycreatetableproduct = "CREATE TABLE IF NOT EXISTS product (" \
                          "cod integer PRIMARY KEY, " \
                          "description text NOT NULL," \
                          "ean text NOT NULL," \
                          "stock integer NOT NULL," \
                          "price double NOT NULL, " \
                          "url text)"

queryselectproduct = "SELECT * FROM product;"
