from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        # Complete this create method to implement the C in CRUD.
    def create(self, data):
        #try except claise to test insert result
        try:
            result = self.collection.insert_one(data) #boolean result for insert attempt
            return True if result.inserted_id else False
        #exception for if insert fails
        except Exception as e:
            print(f"Document did not insert: {e}")
            return False
        
# Create method to implement the R in CRUD.
    def read(self, query):
        #try except clause for search
        try:
            search = self.collection.find(query)#boolean for search
            return list(search)
        #exception for failed search function
        except Exception as e:
            print(f"Document query unsuccessful: {e}")
  
  # Update method to implement U in CRUD
    def update(self, query, new_data):
      #This will allow entries in the document to be updated in MongoDB
      try:
        result = self.collection.update_many(query, {'$set': new_data})
        return result.modified_count
      except Exception as e:
        print(f"Update failed due to error: {e}")
        return 0
      
# Delete method to implement D in CRUD
    def delete(self, query):
      #This will allow me to delete entries in the document in MongoDB
      try:
        result = self.collection.delete_many(query)
        return result.deleted_count
      except Exception as e:
        print(f"Delete failed due to error: {e}")
        return 0
      
            
