''''''
# Feito por Davi Coelho 28/09/2024
#
# Arquivo de constanstes recuperadas dos arquivos de configuração
#
''''''


from modules.conf.load_conf import db_cfg  # , cfg
USER = db_cfg["database"]["user"]
PASSWORD = db_cfg["database"]["password"]
HOST = db_cfg["database"]["host"]
PORT = db_cfg["database"]["port"]
DATABASE = db_cfg["database"]["database"]
# AES_FILE = cfg["Paths"]["database_aes"]
