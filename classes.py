import bcrypt


class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self._salt = bcrypt.gensalt()
        self._password = self._crypt_pwd(password)

    def _crypt_pwd(self, password):
        password = password.encode('utf-8')
        return bcrypt.hashpw(password, self._salt)

    def check_pwd(self, password):
        return self._password == self._crypt_pwd(password)


john = User(1, 'john', '12345')
marc = User(2, 'marc', '67890')

print(User.check_pwd(marc, '12345'))
print(User.check_pwd(john, '12345'))


class Admin(User):
    def manage(self):
        print("Je suis l'administrateur")


root = Admin(1, 'root', 'toor')

print(root.check_pwd('toor'))
root.manage()


class Guest(User):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._salt = bcrypt.gensalt()
        self._password = ''

    def check_pwd(self, password):
        return True


guest = Guest(3, 'Guest')
# print(guest.check_pwd('password'))
print(super(Guest, guest).check_pwd('password'))
