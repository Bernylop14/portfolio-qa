import pytest
from playwright.sync_api import expect

def test_titulo_pagina_login(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"

@pytest.mark.parametrize("usuario, contrasena, login_exitoso", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "contraseña_mal", False),
])
def test_login(page, usuario, contrasena, login_exitoso):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", usuario)
    page.fill("#password", contrasena)
    page.click("#login-button")

    if login_exitoso:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator("[data-test='error']")).to_be_visible()