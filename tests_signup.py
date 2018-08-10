import unittest
from signup_app import Signup


class TestingSignup(unittest.TestCase):

    def setUp(self):        
        self.FirstUser =Signup('steve','opio', 'stevenviko@gmail.com')
        self.SecondUser = Signup('Ronnie', 'numusa', 'musa@yahoo.com')
        

    def test_class_creation(self):
        self.assertIsInstance(self.FirstUser, Signup)
    
    def test_Full_Names(self):
        result = self.FirstUser.Full_Names()
        self.assertEqual(result, {'steve opio'})

    
    

    def test_submit(self):         
        result = self.FirstUser.submit()
        self.assertEqual(result, [{'FirstName':'steve','LastName':'opio', 'email':'stevenviko@gmail.com'}])
        self.assertIsInstance(result, list)

    def test_validate_email(self):         
        result = self.FirstUser.validate_email('musa@yahoo.com')
        self.assertTrue(result)

if __name__ =='__main__':
    unittest.main()
