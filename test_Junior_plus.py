
def test_add_vegetables(base_page):
    base_page.open_base_page()
    base_page.search()

    base_page.add_carrot("5")
    base_page.expect_pieces_carrot("5")

    base_page.add_mushroom()
    base_page.expect_pieces_mushroom("3")

    base_page.add_mushroom_to_basket()
    base_page.add_carrot_to_basket()

    base_page.open_cart()
    base_page.delete_carrot()
    base_page.expect_carrot_not_to_be_visible()

    # base_page.pause()
