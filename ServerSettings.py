import os,json

class ServerSettings:
    def __init__(self):
        self.settings_file = "ServerSettings.json"
        if not os.path.isfile(self.settings_file):
            self.create_settings()

    def create_settings(self):
        with open(self.settings_file, 'w') as file:
            settings = {'whitelist': True,  'server': 'postgresql://postgres:Useles1344gh@localhost:5432/postgres'}
            json.dump(settings, file)

    def get_settings(self) -> dict:
        with open(self.settings_file, 'r') as file:
            settings = json.load(file)
        return settings

    def set_settings(self, dict):
        with open(self.settings_file, 'w') as file:
            json.dump(dict, file)

    def __str__(self):
        with open(self.settings_file, 'r') as file:
            settings = json.load(file)
        return f'whitelist: {settings["whitelist"]}, server: {settings["server"]}'