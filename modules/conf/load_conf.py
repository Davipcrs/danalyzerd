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


cfg = _load_config_file(r"/etc/danalyzer/db_defines.conf")
