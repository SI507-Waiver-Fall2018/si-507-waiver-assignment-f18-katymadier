#Katy Madier | kmadier
#SI507 Waiver Part 2

# these should be the only imports you need
import sys
import sqlite3

# write your code here
argument=sys.argv[1]

#connect to database
conn = sqlite3.connect('Northwind_small.sqlite')
c = conn.cursor()

#list of tables
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())

# [('Employee',), ('Category',), ('Customer',), ('Shipper',), ('Supplier',), ('Order',), ('Product',), ('OrderDetail',), ('CustomerCustomerDemo',), ('CustomerDemographic',), ('Region',), ('Territory',), ('EmployeeTerritory',)]

#list of column names
# c.row_factory=sqlite3.Row
# c.execute('SELECT * FROM "employee"')
# row = c.fetchone()
# names = row.keys()
# print(names)

#order columns
 # ['Id', 'CustomerId', 'EmployeeId', 'OrderDate', 'RequiredDate', 'ShippedDate', 'ShipVia', 'Freight', 'ShipName', 'ShipAddress', 'ShipCity', 'ShipRegion', 'ShipPostalCode', 'ShipCountry']

#Employee columns
 # ['Id', 'LastName', 'FirstName', 'Title', 'TitleOfCourtesy', 'BirthDate', 'HireDate', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'HomePhone', 'Extension', 'Photo', 'Notes', 'ReportsTo', 'PhotoPath']


# python3 part2.py customers
# part2.py customers: prints the list of all customers

if argument=="customers":
    table_name = 'Customer'
    c.execute('SELECT * FROM {tn}'.\
            format(tn=table_name))
    all_rows = c.fetchall()
    print("ID       Customer Name\n")
    for row in all_rows:
        print("{}    {}\n".format(row[0],row[1]))


# python3 part2.py employees
# part2.py employees: prints the list of all employees

if argument=="employees":
    table_name = 'Employee'
    c.execute('SELECT * FROM {tn}'.\
            format(tn=table_name))
    all_rows = c.fetchall()
    print("ID   Employee Name\n")
    for row in all_rows:
        print("{}    {} {}\n".format(row[0],row[2],row[1]))


#  python3 part2.py orders cust=<customer id>
# part2.py orders cust=<customer id>: prints the list of order dates for all orders placed for the specified customer. Use the customer ID for this command.
if argument=="orders":
    if "cust=" in sys.argv[2]:
        id=sys.argv[2][5:]
        table_name="'Order'"
        column_name= 'CustomerId'
        c.execute('SELECT * FROM {tn} WHERE {cn}="{nm}"'.\
                format(tn=table_name, cn=column_name, nm=id))
        all_rows = c.fetchall()
        print("Order dates\n")
        for row in all_rows:
            print("{}\n".format(row[3]))

#  python3 part2.py orders emp=<employee last name>
# part2.py orders emp=<employee last name>: prints the list of order dates for all orders managed by the specified employee. Use the employee last name for this command.

    if "emp=" in sys.argv[2]:
        last=sys.argv[2][4:]
        #id will be employee last name
        table_name = 'Employee'
        column_name= 'LastName'
        c.execute('SELECT * FROM {tn} WHERE {cn}="{nm}"'.\
                format(tn=table_name, cn=column_name, nm=last))
        all_rows = c.fetchall()
        for row in all_rows:
            id=row[0]
        #need to match last name with employeeid
        table_name="'Order'"
        column_name= 'EmployeeId'
        c.execute('SELECT * FROM {tn} WHERE {cn}="{nm}"'.\
                format(tn=table_name, cn=column_name, nm=id))
        all_rows = c.fetchall()
        print("Order dates\n")
        for row in all_rows:
            print("{}\n".format(row[3]))


#DIRECTIONS
# Part 2: Create a Simple Database application
# For part 2, you will create a program to access information in the Northwind database (included in the repository)
#
# FILENAME: part2.py
#
# USAGE: the program does different things based on the arguments passed in.
# part2.py customers: prints the list of all customers
#
# part2.py employees: prints the list of all employees
#
# part2.py orders cust=<customer id>: prints the list of order dates for all orders placed for the specified customer. Use the customer ID for this command.
#
# part2.py orders emp=<employee last name>: prints the list of order dates for all orders managed by the specified employee. Use the employee last name for this command.
#
# SAMPLE OUTPUT: The sample output is large, so it's on another page: Sample Output
#
# NOTE: Use sqlite3.
