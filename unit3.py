from string import punctuation
def read_file(file_name):
    try:
        print("__contenet start__")
        f = open(file_name, "r")
        try:
            print(f.readlines())
        except OSError:
            print("problem in content")
    except OSError:
        print("not exsist")
        f.close()
    finally:
        print("__content end__")


class UnderAge(BaseException):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"your age is {self._age}, lower then 18, you can try again in {18-self._age} years."


def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)


def get_pnc_count(string):
    # getting punctuation count
    return len([ele for ele in string if ele in punctuation])


def get_pnc_count_without___(string):
    # getting punctuation count
    return len([ele for ele in string if ele in punctuation.replace("_", "")])


def get_pnc_indexes_without___(string):
    indexes = []
    i = 0
    for char in string:
        if char in punctuation.replace("_", ""):
            indexes.append(f"'{char}'" + " in index " + str(i))
        i += 1
    indexes_in_string = ", ".join(indexes)
    return indexes_in_string


class UsernameContainsIllegalCharacter(BaseException):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "you used an elegal char in your username"


class UsernameTooShort(BaseException):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "your username is shorter then 3 chars"


class UsernameTooLong(BaseException):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "your username is longer then 16 chars"


class PasswordMissingCharacter(BaseException):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "your password does not contane all the  requierd types of chars "


class PasswordMissingSmallLetter(PasswordMissingCharacter):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "your password does not have a small letter"


class PasswordMissingBigLetter(PasswordMissingCharacter):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "your password does not have a Big letter"


class PasswordMissingSpecialChar(PasswordMissingCharacter):
    def __init__(self, password):
        self._password = password
        #if get_pnc_count("".join(list(self._password))) > 0:
          # self._pass_is_good = True
        #else:
         #  self._pass_is_good = False

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + "(special)"


class PasswordMissingNumber(PasswordMissingCharacter):
    def __init__(self, password):
        PasswordMissingCharacter.__init__(self, password)

    def __str__(self):
        return "your password does not contane all the  requierd types of chars (Digit)"


class PasswordTooShort(BaseException):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "your password is shorter then 8 chars"


class PasswordTooLong(BaseException):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "your password is longer then 40 chars"


def check_input(username, password):
    pass_is_good = False
    if len(password) > 7:
        if len(password) < 41:
            if len([char_in_pass for char_in_pass in password if char_in_pass.isupper()]):
                if len([char_in_pass for char_in_pass in password if char_in_pass.islower()]):
                    if len([char_in_pass for char_in_pass in password if char_in_pass.isnumeric()]):
                        if get_pnc_count(password) > 0:
                            pass_is_good = True
                        else:
                            #raise PasswordMissingSpecialChar(password)
                            print(PasswordMissingSpecialChar(password))
                    else:
                        raise PasswordMissingNumber(password)
                else:
                    raise PasswordMissingSmallLetter(password)
            else:
                raise PasswordMissingBigLetter(password)
        else:
            raise PasswordTooLong(password)
    else:
        raise PasswordTooShort(password)
    username_is_good = False
    if get_pnc_count_without___(username) == 0:
        if len(username) < 17:
            if len(username) > 2:
                username_is_good = True
            else:
                raise UsernameTooShort(username)
        else:
            raise UsernameTooLong(username)
    else:
        indexes_in_string = get_pnc_indexes_without___(username)
        print("the ileagal chars are: " + indexes_in_string)
        raise UsernameContainsIllegalCharacter(username)
    if username_is_good and pass_is_good:
        print("ok")
    elif username_is_good and pass_is_good == False:
        print("your pass is not good but username is good ")
    elif pass_is_good and username_is_good == False:
        print("your username is not good but pass is good ")
    else:
        print("both are not good!")


def main():
    if __name__ == '__main__':
        #username = input("enter username: ")
        #password = input("enter the password: ")
        check_input("user", "passAofffff1fffffrd")


main()

