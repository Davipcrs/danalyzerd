import configparser
import os
import subprocess


def create_database_config_file(file_path: str, user, password, host, port, database):
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


def create_defines_config_file(file_path: str, keypath: str, db_path: str):
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
