from fixtures.constants import OrderMessages


class TestOrderPage:
    def test_booking_hotel(self, app):
        """
        Valid booking a hotel.
        """
        "Open login page"
        app.order_page.open_login_page()
        "Sing in"
        username = OrderMessages.LOGIN
        password = OrderMessages.PASSWORD
        app.order_page.login(username=username, password=password)
        "See accommodation"
        app.order_page.button_click()
        assert app.order_page.card_on_list()
        "Go to hotel page"
        app.order_page.button_click()
        assert app.order_page.description_accommodation_details()
        "To book a hotel"
        app.order_page.button_click()
        "Go to cart"
        app.order_page.enter_on_basket_page()
        "Go to create order"
        app.order_page.click_button_to_the_design()
        assert app.order_page.text_on_order_create() == OrderMessages.CUSTOMER
        "Save order"
        app.order_page.click_button_order_save()
        assert app.order_page.text_on_order() == OrderMessages.YOUR_ORDER
        "View the order"
        app.order_page.click_button_look_order()
        assert app.order_page.customer_order() == OrderMessages.CUSTOMER
