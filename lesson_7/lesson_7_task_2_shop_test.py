from selenium import webdriver
from ShopPages.LoginPage import LoginPage
from ShopPages.MainPage import MainPage
from ShopPages.CartPage import CartPage
from ShopPages.OrderPage import OrderPage


def test_shop():
    driver = webdriver.Firefox()
    log_page = LoginPage(driver)
    log_page.user_name("standard_user")
    log_page.pass_word("secret_sauce")
    log_page.log_in()

    main_page = MainPage(driver)
    main_page.add_to_cart()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.cart_checkout()

    order = OrderPage(driver)
    order.first_name("Лариса")
    order.last_name("Шушкевич")
    order.postal_code("12345")
    expected_total = "$58.29"
    actual_total_value = order.check_sum()

    assert actual_total_value == expected_total

    driver.quit()
