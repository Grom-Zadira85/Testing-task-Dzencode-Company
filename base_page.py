from playwright.sync_api import Page, expect

base_url = "https://rahulshettyacademy.com/seleniumPractise/#/"


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_base_page(self):
        self.page.goto(base_url)

    def search(self):
        search = self.page.locator('[placeholder="Search for Vegetables and Fruits"]')
        search.fill("ro")

    def add_carrot(self):
        carrot = self.page.locator('//div[h4[text()="Carrot - 1 Kg"]]//a[@class="increment"]')
        carrot.click()
        carrot.click()
        carrot.click()
        carrot.click()

    def expect_pieces_carrot(self, quantity: str):
        carrot_number = self.page.locator('(//*[@class="quantity"])[3]')
        expect(carrot_number).to_have_value(quantity)

    def add_mushroom(self):
        mushroom = self.page.locator('//div[h4[text()="Mushroom - 1 Kg"]]//a[@class="increment"]')
        mushroom.click()
        mushroom.click()

    def expect_pieces_mushroom(self, quantity: str):
        carrot_number = self.page.locator('(//*[@class="quantity"])[4]')
        expect(carrot_number).to_have_value(quantity)

    def add_mushroom_to_basket(self):
        mushroom = self.page.locator('//div[h4[text()="Mushroom - 1 Kg"]]//*[@type="button"]')
        mushroom.click()

    def add_carrot_to_basket(self):
        carrot = self.page.locator('//div[h4[text()="Carrot - 1 Kg"]]//*[@type="button"]')
        carrot.click()

    def open_cart(self):
        cart = self.page.locator('//img[@class=" "]')
        cart.click()

    def delete_carrot(self):
        carrot = self.page.get_by_role("list").locator("li").filter(has_text="Carrot - 1 Kg561 No. 56×").get_by_role(
            "link")
        carrot.click()
        expect(carrot.get_by_role("list").get_by_text("Carrot - 1 Kg")).not_to_be_visible()

    def pause(self):
        self.page.pause()

    def expect_carrot_not_to_be_visible(self):
        carrot = self.page.get_by_role("list").locator("li").filter(has_text="Carrot - 1 Kg561 No. 56×").get_by_role(
            "link")
        expect(carrot.get_by_role("list").get_by_text("Carrot - 1 Kg")).not_to_be_visible()
