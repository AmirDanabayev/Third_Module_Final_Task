import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    result = browser.find_element_by_css_selector("#add_to_basket_form").is_displayed()
    assert result, '"Add to cart" button does not display!'
