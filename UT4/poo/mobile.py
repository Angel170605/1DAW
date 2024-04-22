class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = False
        self.apps = []

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app: str):
        if isinstance(app, str) and app not in self.apps:
            self.apps.append(app)
        elif isinstance(app, list):
            for target_app in app:
                if target_app not in self.apps:
                    self.apps.append(app)

    def uninstall_app(self, app: str):
        if isinstance(app, str) and app in self.apps:
            self.apps.remove(app)
        elif isinstance(app, list):
            for target_app in app:
                if target_app in self.apps:
                    self.apps.remove(app)
