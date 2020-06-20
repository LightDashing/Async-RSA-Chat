from Settings import Settings


class Tests:

    def __init__(self):
        self.Settings = Settings()
        print(self.Settings)

        settings = {'login': 'TheLightDashing', 'password': 'kek', 'email': 'kekchmek@kek', 'servers': {'EbaniyZadrot': '192.168.1.1'}}
        self.Settings.set_settings(settings)
        print(self.Settings)


test = Tests()