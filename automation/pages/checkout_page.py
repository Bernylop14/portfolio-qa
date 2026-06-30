class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def rellenar_formulario(self, nombre, apellido, codigo_postal):
        self.page.fill("[data-test='firstName']", nombre)
        self.page.fill("[data-test='lastName']", apellido)
        self.page.fill("[data-test='postalCode']", codigo_postal)
        self.page.click("[data-test='continue']")

    def finalizar_compra(self):
        self.page.click("[data-test='finish']")

    def verificar_confirmacion(self):
        from playwright.sync_api import expect
        expect(self.page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")