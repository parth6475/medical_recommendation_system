import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Choose the collection
db = client["ADBS_Dataset"]
collection = db["heart_disease"]

# Define the projection to exclude the "_id" field
projection = {"_id": 0}

# Execute a query with the projection
cursor = collection.find({}, projection)

# Create an empty list to store the results
data = []

# Iterate over the cursor and append each document to the list
for document in cursor:
    data.append(document)

# Print the results
print(data[0])