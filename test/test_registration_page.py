from pages.RegistrationPage import RegistrationPage

class TestRegistrationPage(RegistrationPage):

    # Text variable
    hint_text = "Never disclose your Jiji password to anyone"
    rules_url = "https://jiji.com.gh/rules.html"
    rules_page_title = "Terms of Use"
    home_page_title = "Free classifieds"
    partlink_fb = "https://www.facebook.com/"
    profile_head = ".user-avatar-2"

    # All function for Actions performed on Registration Page
    def test_TC001_Verify_i_agree_with_rules_checkbox_isClickable(self):
        self.load_page()
        self.click(self.registration)
        self.click(self.register_via_Email_or_Phone)
        self.assert_element(self.i_agree_with_rules_checkbox)

    # All function for Actions performed on Registration Page
    def test_TC002_Verify_via_Email_Google_Facebook_OnRegisByEmailForm_isPresent(self):
        self.load_page()
        self.click(self.registration)
        self.assert_elements(self.register_via_Email_or_Phone, self.register_via_Google, self.register_via_Facebook)

    def test_TC003_Verify_i_agree_with_rules_link_isClickable(self):
        self.load_page()
        self.click(self.registration)
        self.click(self.register_via_Email_or_Phone)
        if self.assert_element(self.rules_link):
            self.click(self.rules_link)
            if self.get_current_url() == self.rules_url:
                self.assert_title(self.rules_page_title)
            else:
                Exception("You are currently not on the Rules Page")
        else:
            Exception("Rules Link is not Clickable")


    def test_TC004_Verify_via_Google_and_via_Facebook_Button_on_Page_RegisterViaEmail(self):
        self.load_page()
        self.click(self.registration)
        self.click(self.register_via_Email_or_Phone)
        self.assert_elements(self.via_Facebook_OnRegisByEmailForm, self.via_Google_OnRegisByEmailForm)

    def test_TC005_Verify_and_Click_sign_in_link_OnRegisterPage_on_Page(self):
        self.load_page()
        self.click(self.registration)
        self.click(self.register_via_Email_or_Phone)
        if self.assert_element(self.sign_in_link_OnRegisterPage):
            self.click(self.sign_in_link_OnRegisterPage)
            self.assert_element(self.registration_link_OnSignInPage)
        else:
            Exception("Link Does not Exist")


    # def test_TC006_Verify_already_have_account_OnRegisterPage_on_Page(self):
    #     pass
    #
    def test_TC007_Verify_register_via_Google_Facebook_Email_Buttons_are_Clickable(self):
        # Register With Google Button
        self.load_page()
        self.click(self.registration)
        self.click(self.register_via_Google)
        if "Google" in self.get_page_title():
            self.go_back()
            self.assert_title(self.home_page_title)
        else:
            Exception("Google Button Error")

        # Register With Facebook Button
        self.click(self.registration)
        self.click(self.register_via_Facebook)
        if self.partlink_fb in self.get_current_url():
            self.go_back()
            self.assert_element(self.register_via_Facebook)
        else:
            Exception("Facebook Button not working")


    # Register With Email or Phone Button


    def test_TC008_Verify_registration_via_Email_or_Phone(self):
        self.load_page()
        self.regisViaEmaial()
        self.assert_element(self.profile_head)

    # def test_TC009_Verify_registration_via_Facebook(self):
    #     pass
    #
    #
    # def test_TC010_Verify_registration_via_Google(self):
    #     pass
    #
    # def test_TC011_Verify_FormSubmitWithoutFillingInOptionalFields(self):
    #     pass
    #
    # def test_TC012_Verify_Validation_for_SubmittingEmptyForm(self):
    #     pass
    #
    # def test_TC013_Verify_Validation_for_SubmittingFormWithAlreadyResgisteredEmail(self):
    #     pass
    #
    # def test_TC014_Verify_Validation_for_SubmittingFormWithNonResgisteredEmail(self):
    #     pass
    #
    # def test_TC015_Verify_Validation_for_SubmittingFormWithoutEmail(self):
    #     pass
    #
    # def test_TC016_Verify_Validation_for_SubmittingFormWithoutPassword(self):
    #     pass
    #
    # def test_TC017_Verify_Validate_password_show_IsClickableAfterEnteringPassword(self):
    #     pass
    #
    # def test_TC018_Verify_Validation_for_SuccessfulRegistration(self):
    #     pass