from seleniumbase import BaseCase

# importing common Files from the utilities folder
from utilities.commons import Commons


class SignInPage(BaseCase):
    # Login Page Locators
    Email_or_phone = "#identifierId"
    Forgot_email = "[jsname='Cuz2Ue']"
    Learn_more = "[jsname='JFyozc']"
    Create_account = "//span[.='Create account']"
    For_myself = "//span[.='For myself']"
    To_manage_my_business = "//span[.='To manage my business']"
    Next = "//span[.='Next']"
    Help = "//a[.='Help']"
    Privacy = "//a[.='Privacy']"
    Terms = "//a[.='Terms']"
    DropDownCountryList = "[role='option'][data-value='af']"
    email_label_OnPasswordPage = ".YZrg6"
    welcome_label_OnPasswordPage = "//span[.='Welcome']"
    password_field_OnPasswordPage = "[name='password']"
    checkbox_OnPasswordPage = ".VfPpkd-muHVFf-bMcfAe"
    showPasswordText_OnPasswordPage = ".jGAaxb"
    Forgot_password_OnPasswordPage = "//span[.='Forgot password?']"
    protectAccount = ".N4lOwd"
    Update_Button_OnProtectAccountPage = "//div[@class='n6Gm2e']//span[@class='RveJvd snByac']"
    Confirm_Button_OnProtectAccountPage = "//div[@class='yKBrKe']//span[@class='RveJvd snByac']"
    welcomePageMessage = "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[3]/div/div/header/h1"
    GetStartedButton_OnWelcomePage = "#yDmH0d > c-wiz > div > div:nth-child(2) > c-wiz > c-wiz > div > div.s7iwrf.gMPiLc.Kdcijb > div > div > c-wiz > section > div:nth-child(1) > div > div.b3FPXb > div > div.kwVK0c > div > div > a"
    compose_Button = "//div[@class='T-I T-I-KE L3']"
    Compose_TextBox = "//span[.='New Message']"


    # All Functions for Actions Performed on Login Page

    def load_page(self):
        self.open(Commons.url)

    def login(self,username, password):
        self.load_page()
        self.type(self.Email_or_phone, username)
        self.type(self.Email_or_phone, password)




