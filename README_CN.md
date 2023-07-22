<img src="./assets/FlyDB-logo.png" alt="FlyDB-logo" style="display: block; margin: 0 auto; width: 45%;" />

>FlyDB's github address: https://github.com/ByteStorage/FlyDB
> 

# FlyDB-SDK-PythonFlyDB-SDK-Python

FlyDB-SDK-Python是用于与FlyDB键值数据库交互的Python软件开发工具包（SDK）。

FlyDB是一个高性能、轻量级的键值数据库，通过这个SDK，您可以方便地在Python中使用FlyDB进行数据的存储和检索。

## 安装

要使用FlyDB-SDK-Python，您首先需要安装FlyDB服务器，并确保其正常运行。

安装FlyDB-SDK-Python可以通过pip进行，运行以下命令：

```bash
pip install FlyDB2-SDK-Python
```

## 快速上手

以下是一个简单的示例，展示了如何使用FlyDB-SDK-Python来连接到FlyDB服务器，并进行数据的存储和检索。

```python
from pathlib import Path
from FlyDB import db

# Create a FlyDB2 client
db_client = db.FlyDB()

# Connect to the FlyDB2
path = Path.cwd().joinpath("data")
db_client.connect_option(str(path), 256 * 1024 * 1024, True)

# Set a key-value pair
db_client.set("key", "value", 0)

# Get the value of a key
value = db_client.get("key")
print(value)

# Delete a key-value pair
db_client.delete("key")
```

## API参考

FlyDB-SDK-Python目前支持以下几个API：

`set(key, value, expire)`: 存储一个键值对到数据库中，`key`为字符串，`value`可以是字符串、整数、浮点数、布尔值或字节流, `expire`为过期时间，以`ms`为单位，当`expire`为0时，永不过期。

`get(key)`: 从数据库中检索一个键的值，返回值的类型根据实际存储类型而定。

`delete(key)`: 从数据库中删除指定键的数据。

> 更多API参考和详细用法，请参阅官方文档或SDK源代码。
>

## 贡献和问题反馈

如果您发现任何问题或有任何建议，请随时提出。我们欢迎社区的贡献，如果您想为FlyDB-SDK-Python项目做出贡献，请提交Pull Request或者联系我们的开发团队。

## 许可证

FlyDB-SDK-Python项目使用MIT许可证，详情请参阅LICENSE文件。

## 声明

FlyDB-SDK-Python是FlyDB项目的官方Python SDK，由FlyDB团队维护和支持。感谢您使用FlyDB-SDK-Python，希望它能为您的数据存储和检索带来便利！