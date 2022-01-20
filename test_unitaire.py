import unittest
from Connection import Connection
import utilities_lib
from Register import Register


class ProjetTestCase(unittest.TestCase):
    def test_init(self):
        pass
        # with self.assertRaise(TypeNone):

    # LOGAN
    def user_exist(self):
        self.assertEqual(Cargan.check_user_exist, True)

    def user_data_from_db(self):
        self.assertEqual(Cargan.get_user_data_from_db,
                         "{'_id': ObjectId('61c243b8c8cf5d6ca1b93946'), 'username': 'Cargan', 'email': 'Cargan@gmail.com', 'password': b'$2b$12$qJlTRWr8sGTa/UhERS4GN.BGRvbi2Iw.A8.FgBgjswMLRxPGSnJ6i', 'secret_question': 'Your first pet's name', 'secret_answer': b'$2b$12$mJ5GIGqv4MazLK4tlG4kO.KQJZ3s5vUuAWcfP1GSShEJSi.QMrCHS', 'role': 'User'}")

    def insert_user(self):
        self.assertEqual(Cargan_v2.insert_user_data_to_db, 'This username already exists/invalid')
        # self.assertEqual(Cargan_v2.insert_user_data_to_db, 'This email address already exists/invalid')
        # self.assertEqual(Cargan_v2.insert_user_data_to_db, 'Password need to have a character, a letter, a maj and 8 char min')
        # self.assertEqual(Cargan_v2.insert_user_data_to_db, 'Different passwords')
        # self.assertEqual(Cargan_v2.insert_user_data_to_db, 'Question or/and answer null')

    # MATHIEU
    def test_check_password_strength(self):
        self.assertEqual(utilities_lib.check_password_strength(password_wo_maj), False)
        self.assertEqual(utilities_lib.check_password_strength(password_wo_num), False)
        self.assertEqual(utilities_lib.check_password_strength(password_wo_let), False)
        self.assertEqual(utilities_lib.check_password_strength(password_wo_8char), False)
        self.assertEqual(utilities_lib.check_password_strength(good_password), True)

    def test_check_password(self):
        self.assertEqual(user_fal.check_password, "Username or password incorrect")
        self.assertEqual(user_true.check_password, "Welcome")

    def test_check_same_password(self):
        self.assertEqual(utilities_lib.check_same_password(register_test, register_test_pass), False)
        self.assertEqual(utilities_lib.check_same_password(register_test_wo_maj, register_test_pass), False)
        self.assertEqual(utilities_lib.check_same_password(register_test2, register_test_pass), True)

    # SEBASTIAN
    def test_email(self):
        self.assertEqual(Register("", "", "", tst_email_noext, "", "").check_email_exist, False)
        self.assertEqual(Register("", "", "", tst_email_noarobase, "", "").check_email_exist, False)
        self.assertEqual(Register("", "", "", tst_email_dot, "", "").check_email_exist, False)
        self.assertEqual(Register("", "", "", tst_email_charright, "", "").check_email_exist, False)
        self.assertEqual(Register("", "", "", tst_email_charleft, "", "").check_email_exist, False)
        self.assertEqual(Register("", "", "", tst_email, "", "").check_email_exist, True)

    def test_check_permission(self):
        self.assertEqual(utilities_lib.check_permission(pseudo1, commande), (f"L'utilisateur NE peut PAS utiliser la commande {commande}", False))
        self.assertEqual(utilities_lib.check_permission(pseudo2, commande), (f"L'utilisateur peut utiliser la commande {commande}", True))

    def test_secret_question_ok(self):
        self.assertEqual(utilities_lib.secret_question_ok(default_question, empty), False)
        self.assertEqual(utilities_lib.secret_question_ok(default_question, response), False)
        self.assertEqual(utilities_lib.secret_question_ok(question, empty), False)
        self.assertEqual(utilities_lib.secret_question_ok(question, response), True)


# TEST LOGAN

Cargan = Connection("Cargan", "Lolo1234")
Cargan_v2 = Register("Cargan", "Lolo1234", "Lolo1234", "lgc.carlier@gmail.com", "Your first pet's name", "Peluche")

# TEST MATHIEU

password_wo_maj = "test1234"
password_wo_num = "testtest"
password_wo_let = "12345678"
password_wo_8char = "Test123"
good_password = "Test1234"

user_fal = Connection("Cargan", "lolo123")
user_true = Connection("Cargan", "Lolo1234")

register_test = "Test123"
register_test2 = "Test1234"
register_test_wo_maj = "test1234"
register_test_pass = "Test1234"

# TEST SEBASTIAN

tst_email_noext = "poro@gmail."
tst_email_noarobase = "porogmail.com"
tst_email_dot = "poro@gmailcom"
tst_email_charright = "poro@"
tst_email_charleft = "@gmail.com"
tst_email = "verum@gmail.com"

pseudo1 = "Verum"
pseudo2 = "Zink"
commande = "METEO"


empty = ""
default_question = "Choose your question"
question = "Your first pet's name"
response = "Peluche"


if __name__ == '__main__':
    unittest.main()
