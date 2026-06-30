class LoginPage:
    def __init__(self, page):
        self.page = page

    def iniciar_sesion(self, usuario, contrasena):
        self.page.goto("https://www.saucedemo.com")
        self.page.fill("#user-name", usuario)
        self.page.fill("#password", contrasena)
        self.page.click("#login-button")