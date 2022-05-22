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
        # assert app.order_page.text_on_basket_header() == OrderMessages.BASKETS_HEADER
        # assert app.order_page.info_hotel_in_basket_count_nights() == OrderMessages.INFO_HOTEL_IN_BASKET_COUNT_NIGHTS
        # assert app.order_page.info_hotel_in_basket_accommodation() == OrderMessages.INFO_HOTEL_IN_BASKET_ACCOMMODATION
        # assert app.order_page.info_hotel_in_basket_country() == OrderMessages.INFO_HOTEL_IN_BASKET_COUNTRY
        # assert app.order_page.info_hotel_in_basket_price() == OrderMessages.INFO_HOTEL_IN_BASKET_PRICE
        "Go to create order"
        app.order_page.click_button_to_the_design()
        assert app.order_page.text_on_order_create() == OrderMessages.CUSTOMER
        "Save order"
        app.order_page.click_button_order_save()
        assert app.order_page.text_on_order() == OrderMessages.YOUR_ORDER
        # assert app.order_page.text_status_order() == OrderMessages.STATUS_ORDER
        "View the order"
        app.order_page.click_button_look_order()
        assert app.order_page.customer_order() == OrderMessages.CUSTOMER
