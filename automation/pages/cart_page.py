class CartPage:
    def __init__(self, page):
        self.page = page

    def verificar_producto(self, nombre):
        from playwright.sync_api import expect
        expect(self.page.locator("[data-test='inventory-item-name']")).to_have_text(nombre)

    def ir_a_checkout(self):
        self.page.click("[data-test='checkout']")