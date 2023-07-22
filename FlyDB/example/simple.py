from pathlib import Path
from FlyDB import db

# Create a FlyDB2 client
db_client = db.FlyDB()

# Connect to the FlyDB2
path = Path.cwd().joinpath("data")
db_client.connect_option(str(path), 256*1024*1024, True)

# Set a key-value pair
db_client.set("key", "value", 0)

# Get the value of a key
value = db_client.get("key")
print(value)

# Delete a key-value pair
db_client.delete("key")