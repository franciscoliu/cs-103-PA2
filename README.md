# cs-103-PA2

#pylint

(base) michael@Michaels-MBP-2 pa02 % pylint tracker.py                

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.04/10, +0.96)

(base) michael@Michaels-MBP-2 pa02 % pylint test_transaction.py       

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

(base) michael@Michaels-MBP-2 pa02 % pylint transaction.py            

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)




#pytest

(base) michael@Michaels-MBP-2 pa02 % pytest test_transaction.py       
====================================================================== test session starts =======================================================================
platform darwin -- Python 3.9.7, pytest-7.1.1, pluggy-0.13.1
rootdir: /Users/michael/Documents/Github_Desktop/cs-103-PA2/pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 6 items                                                                                                                                                

test_transaction.py ......                                                                                                                                 [100%]

======================================================================= 6 passed in 0.19s ========================================================================





#script for demonstrating all of the features

Script started on Sat Mar 19 21:08:38 2022
[1m[7m%[27m[1m[0m                                                                                                                                                                 
 

[0m[27m[24m[J(base) michael@Michaels-MacBook-Pro-2 pa02 % [K[?2004hppython3 

[J__pycache__/         pytest.ini           test_transaction.py  transaction.py       
category.py          test_category.py     tracker.py           typescript           [A[A[0m[27m[24m
[45Cpython3[K[1C__pycache__[1m/[0m[12Dcategory.py[0m [11Dpy[2Cst.ini [10Dtest_category.py[11Dtransaction.py[18Dracker.py         [9D[?2004l

[J
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. clear the transaction database

> 2
category name: food
category description: test food
> 1
id  name       description                   
------------------------------
1   food       test food                     
> 3
modifying category
rowid: 1
new category name: n foods     new o food
new category description: test modify category name
> 1
id  name       description                   
------------------------------
1   new food   test modify category name     
> 5
item number: 1
item amount: 100
category name: f nrw  ew food
transaction date: 20010612
transaction description: test transaction1
> 4
Test second


row_id     item_number amount     category   date       description                   
----------------------------------------------------------------------
1          1          100        new food   20010612   test transaction1             
> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. clear the transaction database

> 5
item number: 2
item amount: 100
category name: cars
transaction date: 20010613
transaction description: test transaction2
> 1
id  name       description                   
------------------------------
1   new food   test modify category name     
> 4
Test second
Test second


row_id     item_number amount     category   date       description                   
----------------------------------------------------------------------
1          1          100        new food   20010612   test transaction1             
2          2          100        cars       20010613   test transaction2             
> 7
Summarize by date

date       total amount
------------------------------
20010612   100       
20010613   100       
> 8
Summarize by month

month      total amount
------------------------------
6          200       
> 9
Summarize by year

year       total amount
------------------------------
2001       200       
> 10
Summarize by category

category   total amount
------------------------------
cars       100       
new food   100       
> 12
> 1
id  name       description                   
------------------------------
1   new food   test modify category name     
> 4
no items to print
> 0
bye
[1m[7m%[27m[1m[0m                                                                                                                                                                 
 

[0m[27m[24m[J(base) michael@Michaels-MacBook-Pro-2 pa02 % [K[?2004heexit[?2004l


Script done on Sat Mar 19 21:11:28 2022