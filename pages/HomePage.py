from seleniumbase import BaseCase
from utilities.commons import Commons

class ComposeEmail(BaseCase):
    # Compose Email Page Locators

    # All Functions for Actions Performed on Login Page
    def load_page(self):
        self.open(Commons.url)

