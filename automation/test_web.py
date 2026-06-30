import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_titulo_pagina_login(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"


@pytest.mark.parametrize("usuario, contrasena, login_exitoso", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "contraseña_mal", False),
])
def test_login(page, usuario, contrasena, login_exitoso):
    login = LoginPage(page)
    login.iniciar_sesion(usuario, contrasena)

    if login_exitoso:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator("[data-test='error']")).to_be_visible()


def test_anadir_producto_al_carrito(page):
    login = LoginPage(page)
    login.iniciar_sesion("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.anadir_al_carrito()
    inventory.verificar_cart_badge("1")
    inventory.ir_al_carrito()

    cart = CartPage(page)
    cart.verificar_producto("Sauce Labs Backpack")


def test_completar_compra(page):
    login = LoginPage(page)
    login.iniciar_sesion("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.anadir_al_carrito()
    inventory.ir_al_carrito()

    cart = CartPage(page)
    cart.ir_a_checkout()

    checkout = CheckoutPage(page)
    checkout.rellenar_formulario("Berny", "Lopez", "29001")
    checkout.finalizar_compra()
    checkout.verificar_confirmacion()


def test_logout(page):
    login = LoginPage(page)
    login.iniciar_sesion("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.logout()

    expect(page).to_have_url("https://www.saucedemo.com/")