from modules.conf.load_conf import db_cfg, cfg


USER = db_cfg["Database"]["user"]
PASSWORD = db_cfg["Database"]["password"]
HOST = db_cfg["Database"]["host"]
PORT = db_cfg["Database"]["port"]
DATABASE = db_cfg["Database"]["database"]
AES_FILE = cfg["Paths"]["database_aes"]
