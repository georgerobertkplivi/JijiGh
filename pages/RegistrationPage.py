
from seleniumbase import BaseCase

# importing common Files from the utilities folder
from utilities.commons import Commons


class RegistrationPage(BaseCase):


    # Registration Buttons Locators
    registration = "//a[@href='/registration.html']/div[contains(.,'Registration')]"
    register_via_Google = ".bc-google .fw-button__slot-wrapper"
    register_via_Facebook = ".bc-facebook"
    register_via_Email_or_Phone = ".//div[@class='fw-popup__body']//button[1]//span[@class='fw-button__slot-wrapper']"
    sign_in_link_OnRegisterPage = ".h-base-link"
    already_have_account_OnRegisterPage = ".b-auth-card__form-holder"
    registration_link_OnSignInPage = "//div[@class='b-auth-card__form-holder']/a[contains(.,'Registration')]"
    signInWithGoogle = "//span[.='Choose an account']"



    # Registration via Email or Phone Button Register Form Locators
    form_label_text = ".b-auth-popup__title"
    email = "#email"
    password = "#password"
    password_hint = ".fw-field__hint"
    first_name = ".qa-first-name-field"
    last_name = ".qa-last-name-field"
    phone_number = ".qa-phone-field"
    i_agree_with_rules_checkbox = ".fw-icon-valid-wrapper"
    rules_link = ".b-registration-form__base-link"
    via_Google_OnRegisByEmailForm = ".bc-google"
    via_Facebook_OnRegisByEmailForm = ".bc-facebook"
    password_show = ".password-show"
    register_Button = ".h-bold"

    # Registration Data
    emailAddress = Commons.genEmail(self='')
    userPassword = Commons.genPassword(self='')
    firstName = Commons.genNames(self='')
    lastName = Commons.genNames(self='')
    phoneNumber = "0240000000"

    # All Functions for Actions Performed on Login Page

    def load_page(self):
        self.open(Commons.url)

    def regisViaEmaial(self):
        self.click(self.registration)
        self.click(self.register_via_Email_or_Phone)
        self.type(self.email, self.emailAddress)
        self.type(self.password, self.userPassword)
        self.type(self.first_name, self.firstName)
        self.type(self.last_name, self.lastName)
        self.type(self.phone_number, self.phoneNumber)
        self.click(self.register_Button)


