import pytest
from playwright.sync_api import expect

def test_titulo_pagina_login(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"

@pytest.mark.parametrize("usuario, contrasena, login_exitoso",
    [("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "contraseña_mal", False),])

def test_login(page, usuario, contrasena, login_exitoso):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", usuario)
    page.fill("#password", contrasena)
    page.click("#login-button")

    if login_exitoso:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator("[data-test='error']")).to_be_visible()

def test_anadir_producto_al_carrito(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")

    page.click("[data-test='shopping-cart-link']")
    expect(page.locator("[data-test='inventory-item-name']")).to_have_text("Sauce Labs Backpack")

def test_completar_compra(page):
    # Login
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Añadir producto y entrar al carrito
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='shopping-cart-link']")

    # Iniciar checkout
    page.click("[data-test='checkout']")

    # Rellenar formulario de envío
    page.fill("[data-test='firstName']", "Berny")
    page.fill("[data-test='lastName']", "Lopez")
    page.fill("[data-test='postalCode']", "29001")
    page.click("[data-test='continue']")

    # Finalizar compra
    page.click("[data-test='finish']")

    # Verificar mensaje de confirmación
    expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")

def test_logout(page):
    # Login
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Abrir menú y cerrar sesión
    page.click("#react-burger-menu-btn")
    page.click("[data-test='logout-sidebar-link']")

    # Verificar que volvemos a la página de login
    expect(page).to_have_url("https://www.saucedemo.com/")