from typing import Union
import grpc
from database.client_grpc import db_pb2_grpc, db_pb2


class FlyDB:
    def __init__(self):
        """
        Initializes a new instance of the client class.

        The constructor sets up the gRPC channel and creates a stub to interact with the gRPC server.

        Parameters:
            None

        Returns:
            None
        """
        # Create an insecure gRPC channel to connect to the gRPC server running on
        # localhost at port 8999.
        self.channel = grpc.insecure_channel("localhost:8999")

        # Create a stub for the GStringService service using the gRPC channel.
        # The stub provides methods to call the gRPC service methods defined in db.proto.
        self.stub = db_pb2_grpc.GStringServiceStub(self.channel)


    def _validate_input(self, value, value_type, param_name):
        if not isinstance(value, value_type):
            raise TypeError(f"{param_name} must be of type {value_type}")

    def connect_option(self, dir_path: str, data_file_size: int, sync_write: bool):
        """
        Connects to the gRPC server with provided options.

        Parameters:
            dir_path (str): The directory path for the database.
            data_file_size (int): The size of data files.
            sync_write (bool): Indicates whether to use synchronous writes.

        Returns:
            None
        """
        # Validate the types of input parameters using the _validate_input function.
        self._validate_input(dir_path, str, "dir_path")
        self._validate_input(data_file_size, int, "data_file_size")
        self._validate_input(sync_write, bool, "sync_write")

        request = db_pb2.FlyDBOption()
        request.DirPath = dir_path
        request.DataFileSize = data_file_size
        request.SyncWrite = sync_write

        response = self.stub.NewFlyDBService(request)
        if response.ResponseMsg == "start success!":
            print("Start success!")
        else:
            print("Start failed!")

    def set(self, key: str, value: Union[str, int, float, bool, bytes], expire: int):
        """
        Sets the key-value pair in the database.

        Parameters:
            key (str): The key to be set.
            value (Union[str, int, float, bool, bytes]): The value to be set.
            expire (int): The expiration time for the key-value pair in nanoseconds.
                            When expire is 0, it never expires. Expire is in milliseconds.

        Returns:
            None
        """
        self._validate_input(key, str, "key")

        request = db_pb2.SetRequest()
        request.key = key

        if isinstance(value, str):
            request.StringValue = value
        elif isinstance(value, int):
            request.Int64Value = value
        elif isinstance(value, float):
            request.Float64Value = value
        elif isinstance(value, bool):
            request.BoolValue = value
        elif isinstance(value, bytes):
            request.BytesValue = value
        else:
            raise TypeError("Unsupported type")

        request.expire = expire * 1000000
        response = self.stub.Put(request)
        if response.ok:
            print("Put data success!")

    def get(self, key):
        """
        Retrieves the value associated with the given key from the database.

        Parameters:
            key (str): The key for which the value needs to be retrieved.

        Returns:
            Union[str, int, float, bool, bytes]: The value associated with the given key.

        Raises:
            KeyError: If the key is not found in the database.
            TimeoutError: If the key has expired in the database.
        """
        request = db_pb2.GetRequest()
        request.key = key
        try:
            response = self.stub.Get(request)
            # Determine the type of value and return accordingly
            if response.HasField("StringValue"):
                return response.StringValue
            elif response.HasField("Int64Value"):
                return response.Int64Value
            elif response.HasField("Float64Value"):
                return response.Float64Value
            elif response.HasField("BoolValue"):
                return response.BoolValue
            elif response.HasField("BytesValue"):
                return response.BytesValue
            else:
                raise ValueError("Unsupported value type")
        except grpc._channel._InactiveRpcError as e:
            if "KeyNotFoundError" in str(e):
                raise KeyError("key is not found in the database")
            elif "Wrong value" in str(e):
                raise TimeoutError("key expired")
            else:
                raise

    def delete(self, key):
        """
        Deletes the key-value pair from the database.

        Parameters:
            key (str): The key to be deleted.

        Returns:
            None

        Raises:
            KeyError: If the key is not found in the database.
        """
        request = db_pb2.DelRequest()
        request.key = key
        try:
            response = self.stub.Del(request)
            if response.ok:
                print("Delete data success!")
        except grpc._channel._InactiveRpcError as e:
            if "KeyNotFoundError" in str(e):
                raise KeyError("key is not found in the database")
            else:
                raise

