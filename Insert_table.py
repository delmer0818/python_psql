#!/usr/bin/python



import psycopg2

import sys



con = None



try:
    
	con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='tmac1966'")
    
	cur = con.cursor()
    
    

	cur.execute("insert into py_Customers (cname, address, age, income_level, username, pass_word) values ('John Doe', '123 Main St. Anytown USA', 52, 60000.00, 'jdoe1234', 'py122566');")
    
	cur.execute("insert into py_Customers (cname, address, age, income_level, username, pass_word) values ('Jane Smith', 'PO Box 678 Someplace USA', 59, 65000.00, 'smit4567', 'js!333mn');")

    

	cur.execute("insert into py_Publisher (publisherid, name, address, discount) values ('SM-0001', 'SAMS', '201 W 103rd St. Indianapolis IN', 7.00);")
    
	cur.execute("insert into py_Publisher (publisherid, name, address, discount) values ('OR-0001', 'OReily', '77 Decimal Ln. Los Angeles CA', 8.50);")

    

	cur.execute("insert into py_Books (isbn, title, author, qty_in_stock, price, cost, year_published, publisherid) values ('0-596-52746-2', 'JavaScript', 'Shelley Powers', 12, 38.99, 29.99, 2007, 'OR-0001');")
    
	cur.execute("insert into py_Books (isbn, title, author, qty_in_stock, price, cost, year_published, publisherid) values ('0-672-32442-3', 'SQL in 24 Hours', 'Ryan Stephens', 25, 29.99, 24.99, 2015, 'SM-0001');")
    
	cur.execute("insert into py_Books (isbn, title, author, qty_in_stock, price, cost, year_published, publisherid) values ('0-672-32276-5', 'Perl', 'Clinton Pierce', 3, 44.95, 35.99, 2018, 'SM-0001');")

    

	cur.execute("insert into py_StockManager (isbn, quantity) values ('0-596-52746-2', 12);")
    
	cur.execute("insert into py_StockManager (isbn, quantity) values ('0-672-32442-3', 25);")
    
	cur.execute("insert into py_StockManager (isbn, quantity) values ('0-672-32276-5', 3);")

    

	cur.close()
    
	con.commit()

except (Exception, psycopg2.DatabaseError) as error:
    
	print(error)



finally:
    
	if con is not None:
        
		con.close()

