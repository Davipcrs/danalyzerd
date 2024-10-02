''''''
# Feito por Davi Coelho 28/09/2024
#
# Arquivo que efetua a leitura dos arquivos de configuração
#
''''''




import configparser
def _load_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    config_data = {}

    for section in config.sections():
        config_data[section] = {}
        for key in config[section]:
            config_data[section][key] = config[section][key]

    return config_data


# cfg = _load_config_file(r"/etc/danalyzer/defines.conf")
# db_cfg = _load_config_file(r"/etc/danalyzer/db_defines.conf")
with open('./conf.location', 'r') as file:
    location = file.read()
db_cfg = _load_config_file(location)
