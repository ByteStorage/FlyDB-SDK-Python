from setuptools import setup, find_packages

setup(
    name='FlyDB',
    version='0.0.2',
    packages=find_packages(),
    author='GodQI',
    author_email='bsgodqi@163.com',
    description='FlyDB python version of the sdk',
    url='https://github.com/ByteStorage/FlyDB-SDK-Python',
    install_requires=[
        'grpcio','protobuf',
    ],
)
