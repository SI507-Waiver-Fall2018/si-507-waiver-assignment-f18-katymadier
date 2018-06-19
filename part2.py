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

# python3 part2.py customers
# prints the list of all customers

if argument=="customers":
    table_name = 'Customer'
    c.execute('SELECT * FROM {tn}'.\
            format(tn=table_name))
    all_rows = c.fetchall()
    print("ID       Customer Name\n")
    for row in all_rows:
        print("{}    {}\n".format(row[0],row[1]))


# python3 part2.py employees
# prints the list of all employees

if argument=="employees":
    table_name = 'Employee'
    c.execute('SELECT * FROM {tn}'.\
            format(tn=table_name))
    all_rows = c.fetchall()
    print("ID   Employee Name\n")
    for row in all_rows:
        print("{}    {} {}\n".format(row[0],row[2],row[1]))


# python3 part2.py orders cust=<customer id>
# prints the list of order dates for all orders placed for the specified customer. Use the customer ID for this command.
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

# python3 part2.py orders emp=<employee last name>
# prints the list of order dates for all orders managed by the specified employee. Use the employee last name for this command.

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
