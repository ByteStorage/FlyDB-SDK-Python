import time
from pathlib import Path
from FlyDB import db

# Create a FlyDB2 client
db_client = db.FlyDB()

# Connect to the FlyDB
path = Path.cwd().joinpath("data")
db_client.connect_option(str(path), 256*1024*1024, True)

# Set a key-value pair
db_client.set("key", "value",0)

# Get the value of a key
value = db_client.get("key")
print(value)

# Get the type of a key
types = db_client.type("key")
print(types)

# Get the length of a value
length = db_client.len("key")
print(length)

# Set the value and return the old value
new_value = db_client.get_set("key", "value22222", 0)
print(new_value)
value = db_client.get("key")
print(value)

# Exist a key
ok = db_client.exist("key")
print(ok)

# Persist expire time
db_client.set("key1", "value1", 2)
db_client.persist("key")
time.sleep(3)
value = db_client.get("key")
print(value)

# mgset
db_client.set("key2", "value2", 0)
v = db_client.mget(["key", "key2"])
print(v)

# Delete a key-value pair
db_client.delete("key")