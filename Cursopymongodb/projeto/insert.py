from pymongo import MongoClient
# creating connectioons for communicating with Mongo DB
client = MongoClient('192.168.90.10:27017')
db = client.EmployeeData


# Function to insert data into mongo db
def insert():
    try:
        employeeid = input('Enter Employee id :')
        employeename = input('Enter Name :')
        employeeage = input('Enter age :')
        employeecountry = input('Enter Country :')
        db.Employees.insert_one(
        {
            "id": employeeid,
            "name": employeename,
            "age": employeeage,
            "country": employeecountry
        })
        print ('Inserted data successfully')

    except ImportError:
        platform_specific_module = None
        #print str(e)

