import os
import json


class Settings:

    def __init__(self):
        self.settings_file = "settings.json"
        if not os.path.isfile(self.settings_file):
            self.create_settings()

    def create_settings(self, username, password, email):
        with open(self.settings_file, 'w') as file:
            settings = {'login': username, 'password': password, 'email': email, 'servers': ''}
            json.dump(settings, file)

    def get_settings(self) -> dict:
        with open(self.settings_file, 'r') as file:
            settings = json.load(file)
        return settings

    def set_settings(self, dct: dict):
        with open(self.settings_file, 'w') as file:
            json.dump(dct, file)

    def __str__(self):
        with open(self.settings_file, 'r') as file:
            settings = json.load(file)
        return f'Login: {settings["login"]}, password: {settings["password"]}, email: {settings["email"]}, servers: {settings["servers"]}'
