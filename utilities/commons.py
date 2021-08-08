import random
import string


# All Common Data that are being shared by the Test are listed here

class Commons:
    url = "https://jiji.com.gh"
    username_valid = "itsforme60@gmail.com"
    password_valid = "ymlilgee1991"
    username_invalid = "georgerobertkplivi2@gmail.com"
    password_invalid = "ymlilgee19912"
    username_empty = ""
    password_empty = ""


    # Generate Emaill Address for Sign Up
    def genEmail(self):
        # get random string of length 10 without repeating letters for Email Address
        extensions = ['com']
        domains = ['gmail']

        winext = extensions[random.randint(0, len(extensions) - 1)]
        windom = domains[random.randint(0, len(domains) - 1)]

        acclen = random.randint(1, 20)

        winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

        finale = winacc + "@" + windom + "." + winext
        return finale

    # Generate Password for Sign Up
    def genPassword(self):
        # get random string of length 10 without repeating letters for Password
        password_str_gen = ''.join(random.sample(string.ascii_lowercase, 10)) + "2001"
        return (password_str_gen)

    # Generate Names for Sign Up
    def genNames(self):
        # get random string of length 10 without repeating letters for Names
        names_str_gen = ''.join(random.sample(string.ascii_lowercase, 10))
        return (names_str_gen)
