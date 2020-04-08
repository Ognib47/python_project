from make_dict import make_dict
from db_operations import DBOperations

dict_maker = make_dict
db = DBOperations()

db_dict = make_dict()

db.createTable()

db.insertData(db_dict)
db.printData()

