import configparser
import os
import subprocess


def _create_database_config_file(file_path: str, user, password, host, port, database):
    if not os.path.exists(file_path):
        config = configparser.ConfigParser()

        config["database"] = {
            "user": user,
            "password": password,
            "host": host,
            "port": port,
            "database": database
        }

        with open(file_path, 'w') as configfile:
            config.write(configfile)
        print(f"Configuration file created at: {file_path}")

    else:
        print(f"Configuration file already exists at: {file_path}")


def _create_defines_config_file(file_path: str, keypath: str):
    if not os.path.exists(file_path):
        config = configparser.ConfigParser()

        config["paths"] = {
            "database_aes": keypath
        }
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        print(f"Configuration file created at: {file_path}")

    else:
        print(f"Configuration file already exists at: {file_path}")


def init_server():
    if not os.path.exists(r"/home/davi/db_defines.conf"):
        user = input("Database user: ")
        password = input("database password: ")
        host = input("hostname or ip: ")
        port = input("database port: ")
        database = input("database name: ")

        _create_database_config_file(
            r"/home/davi/db_defines.conf", user, password, host, port, database)

    # if not os.path.exists(file_path):
    #    key_path = input("Insert a Full Path for the Secret Encryption key: ")

    #    _create_defines_config_file(file_path, key_path)


init_server()
