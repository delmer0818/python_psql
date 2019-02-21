#!/usr/bin/python

import psycopg2
import sys

con = None

try:
    con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='--------'")
    cur = con.cursor()
    cur.execute("CREATE TABLE py_Customers (cid SERIAL PRIMARY KEY, cname varchar(40), address varchar(80), age integer check (age >= 18 and age <= 100), income_level numeric(10,2), username varchar(20), pass_word varchar(20));")
    cur.execute("CREATE TABLE py_Publisher (publisherid varchar(40) primary key, name varchar(40), address varchar(40), discount numeric(4,2) check (discount >= 1.00 and discount <= 10.00));")
    cur.execute("CREATE TABLE py_Books (isbn varchar(40) primary key, title varchar(40), author varchar(40), qty_in_stock integer, price numeric(10,2) check (price > 0), cost numeric(10,2) check (cost > 0), year_published numeric(4), publisherid varchar(40) references py_Publisher(publisherid) constraint con2 check (price > cost));")
    cur.execute("CREATE TABLE py_Orders (ordernum serial primary key, cid integer references py_Customers(cid), cardnum varchar(40), cardmonth numeric(2) check (cardmonth >= 1 and cardmonth <= 12), cardyear numeric(4) check (cardyear > 2018), order_date date, ship_date date constraint con1 check (ship_date > order_date));")
    cur.execute("CREATE TABLE py_OrderList (ordernum integer references py_Orders(ordernum), isbn varchar(40) references py_Books(isbn), quantity integer, constraint ordernum_isbn primary key (ordernum, isbn));")
    cur.execute("CREATE TABLE py_StockManager (isbn varchar(40) primary key references py_Books(isbn), quantity integer);")
    cur.close()
    con.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if con is not None:
        con.close()
