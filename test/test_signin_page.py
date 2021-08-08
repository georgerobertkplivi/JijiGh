from pages.SignInPage import SignInPage
from utilities.commons import Commons


class TestLoginPage(LoginPage):
    dropdowncountrytext = "Afrikaans"
    protectAccountText = "Protect your account"
    composeBoxText = "New message"




    # Login Page Test Case Functions
    def test_Verify_user_login_with_valid_username_and_password(self):
        self.load_page()
        self.type(self.Email_or_phone, Commons.username_valid)
        self.click(self.Next)
        self.type(self.password_field_OnPasswordPage, Commons.password_valid)
        self.click(self.Next)


    def test_Verify_user_login_with_invalid_username_and_password(self):
        pass

    def test_Verify_user_login_with_valid_username_and_invalid_password(self):
        pass

    def test_Verify_user_login_with_invalid_username_and_valid_password(self):
        pass

    def test_Verify_validation_message_user_login_with_empty_username_and_empty_password(self):
        pass

    def test_verify_login_screen_having_option_to_enter_username_password_submit_button_option_forgot_password(self):
        pass

    def test_Verify_Validation_message_when_user_exceeds_character_limit_username_and_password_fields(self):
        pass

    def test_Verify_Reset_Button(self):
        pass

    def test_Verify_Reset_Button_Clears_TextBoxes(self):
        pass

    def test_Verify_Remember_Me_CheckBox(self):
        pass

    def test_Verify_Remember_Me_CheckBox_Is_Clickable(self):
        pass

    def test_Verify_Password_Is_Encrypted(self):
        pass

    def test_Verify_Limit_of_unsuccessful_password_attempt(self):
        pass

    def test_Verify_once_logged_in_clicking_back_button_does_not_logout_user(self):
        pass



