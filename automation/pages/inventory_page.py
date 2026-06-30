class InventoryPage:
    def __init__(self, page):
        self.page = page

    def anadir_al_carrito(self):
        self.page.click("[data-test='add-to-cart-sauce-labs-backpack']")

    def ir_al_carrito(self):
        self.page.click("[data-test='shopping-cart-link']")

    def verificar_cart_badge(self, cantidad):
        from playwright.sync_api import expect
        expect(self.page.locator("[data-test='shopping-cart-badge']")).to_have_text(cantidad)

    def logout(self):
        self.page.click("#react-burger-menu-btn")
        self.page.click("[data-test='logout-sidebar-link']")