import os
import json
from Crypto.PublicKey import RSA


class Settings:

    def __init__(self):
        self.settings_file = "settings.json"
        self.rsa_vault = 'rsa.key'
        if not os.path.isfile(self.settings_file):
            self.create_settings()

    def create_settings(self):
        with open(self.settings_file, 'w') as file:
            settings = {'login': 'User', 'password': 'None', 'email': 'None', 'servers': ''}
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
        return f'Login: {settings["login"]}, password: {settings["password"]}, email: {settings["email"]}, servers: {settings["servers"]}'
