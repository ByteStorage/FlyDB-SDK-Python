<img src="./assets/FlyDB-logo.png" alt="FlyDB-logo" style="display: block; margin: 0 auto; width: 45%;" />

>FlyDB's github address: https://github.com/ByteStorage/FlyDB
> 

English | [中文](https://github.com/ByteStorage/flydb/FlyDB-SDK-Python/master/README_CN.md)

# FlyDB-SDK-Python

FlyDB-SDK-Python is a software development toolkit (SDK) for interacting with the FlyDB key-value database in Python.

FlyDB is a high-performance, lightweight key-value database, and with this SDK, you can easily use FlyDB to store and retrieve data in Python.

## Installation

To use FlyDB-SDK-Python, you first need to install the FlyDB server and ensure it is running.

You can install FlyDB-SDK-Python using pip, by running the following command:

```
pip install FlyDB-SDK-Python
```

## Quick Start

Here's a simple example showing how to use FlyDB-SDK-Python to connect to the FlyDB server and perform data storage and retrieval:

```python
from pathlib import Path
from database import db

# Create a database client
db_client = db.FlyDB()

# Connect to the database
path = Path.cwd().joinpath("data")
db_client.connect_option(str(path), 256*1024*1024, True)

# Set a key-value pair
db_client.set("key", "value", 0)

# Get the value of a key
value = db_client.get("key")
print(value)

# Delete a key-value pair
db_client.delete("key")
```

## API ReferenceAPI

FlyDB-SDK-Python currently supports the following APIs:

set(key, value, expire): Stores a key-value pair in the database. The key should be a string, and the value can be a string, integer, float, boolean, or byte stream. The expire parameter represents the expiration time in milliseconds. When expire is set to 0, the data will never expire.

get(key): Retrieves the value of a specified key from the database. The return value type depends on the actual stored data type. 

delete(key): Deletes the specified key-value pair from the database. 

> For more API reference and detailed usage, please refer to the official documentation or the SDK source code.
>

## Contributions and Feedback

If you encounter any issues or have any suggestions, please feel free to raise them. We welcome contributions from the community. If you want to contribute to the FlyDB-SDK-Python project, please submit a Pull Request or contact our development team.

## License

FlyDB-SDK-Python is licensed under the MIT License. For details, please refer to the LICENSE file.

## Disclaimer

FlyDB-SDK-Python is the official Python SDK for the FlyDB project, maintained and supported by the FlyDB team. Thank you for using FlyDB-SDK-Python, and we hope it brings convenience to your data storage and retrieval tasks!