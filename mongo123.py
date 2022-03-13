import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Employee']

information = mydb.employeeinformation

record ={
    'firstname':'Krish',
    'lastname':'Naik',
    'department':'Analytics'
}

# tt=information.insert_one(record)

# print(tt)
print(information.find_one())

for record in information.find({}):
    print(record)
# print(mydb)
