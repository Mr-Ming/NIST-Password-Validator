# coding=utf-8
import unittest
import os.path
import password_validator

class TestPasswordValidator(unittest.TestCase):
    """
    Run unit test for password_validator script
    """
    def test_constant(self):
        """
        Test that constant value are correct
        """
        self.assertEqual(password_validator.MIN_PASSWORD_LENGTH, 8)
        self.assertEqual(password_validator.MAX_PASSWORD_LENGTH, 64)

        self.assertEqual(
            password_validator.ERROR_INVALID_INPUT, 
            ('Please check that your input is in the correct format. \n' + 
            'python password_validator.py input_password.txt commonly_used_password_file.txt')
        )
        
        self.assertEqual(password_validator.ERROR_FILE_NOT_FOUND, 'File {} is not found.')
        self.assertEqual(password_validator.ERROR_PASSWORD_IS_TOO_SHORT, 'Too Short')
        self.assertEqual(password_validator.ERROR_PASSWORD_IS_TOO_LONG, 'Too Long')
        self.assertEqual(password_validator.ERROR_PASSWORD_IS_NOT_ASCII, 'Invalid Characters')
        self.assertEqual(password_validator.ERROR_PASSWORD_IS_TOO_COMMON, 'Too Common')

        self.assertEqual(password_validator.NOTICE_READING_WEAK_PASSWORDS_VALIDATION_FILE, '--- Attempting to read in weak password validation file ---')
        self.assertEqual(password_validator.NOTICE_CHECKING_INPUT_PASSWORDS_FILE, '--- Validating input password ---')
        self.assertEqual(password_validator.NOTICE_SUMMARY, '--- Printing summary ---')
        self.assertEqual(password_validator.NOTICE_COUNT_BAD_PASSWORD, 'Number of bad password: {}')
        self.assertEqual(password_validator.NOTICE_COUNT_GOOD_PASSWORD, 'Number of good password: {}')
        self.assertEqual(password_validator.NOTICE_COUNT_TOTAL_PASSWORD, 'Number of password found: {}')

    def test_validate_input_from_command_line_when_valid_argument_is_passed(self):
        """
        Test that validate_input_from_command_line 
        return True when there are valid number of arguments
        """
        is_argument_correct = password_validator.validate_input_from_command_line({'command', 'input.txt', 'weakpass.txt'});
        self.assertTrue(is_argument_correct) 

    def test_validate_input_from_command_line_when_invalid_argument_is_passed(self):
        """
        Test that validate_input_from_command_line 
        return False when there are invalid number of arguments
        """
        is_argument_correct = password_validator.validate_input_from_command_line({'command', 'input.txt'});
        self.assertFalse(is_argument_correct) 

    def test_validate_file_exist_when_one_file_does_not_exist(self):
        """
        Test that validate_files_exist 
        return error when one of the file does not exist
        """
        os.path.isfile = lambda path: path == 'file2'
        is_file_exist = password_validator.validate_files_exist('file1', 'file2')

        self.assertEqual(is_file_exist, password_validator.ERROR_FILE_NOT_FOUND.format('file1')) 

    def test_validate_file_exist_when_both_files_does_not_exist(self):
        """
        Test that validate_files_exist 
        return error when both files does not exist
        """
        is_file_exist = password_validator.validate_files_exist('file1', 'file2')

        self.assertEqual(
            is_file_exist, 
            password_validator.ERROR_FILE_NOT_FOUND.format('file1') +
            '\n' + password_validator.ERROR_FILE_NOT_FOUND.format('file2')
        ) 

    def test_validate_password_when_password_is_valid(self):
        """
        Test that validate_password
        can return true when password is valid
        """
        password = 'balloon is wanted'
        result = password_validator.validate_password(password, {'balloon'}, True)
        self.assertTrue(result) 

    def test_validate_password_when_password_less_than_minimum(self):
        """
        Test that validate_password 
        can return correct error when password is less than minimum length
        """
        password = 'balloon'
        result = password_validator.validate_password(password, {}, True)
        self.assertEqual(result, password + ' -> Error: ' + password_validator.ERROR_PASSWORD_IS_TOO_SHORT)

    def test_validate_password_when_password_greater_than_maximum(self):
        """
        Test that validate_password 
        can return correct error when password is greater than maximum length
        """
        password = ('thisisahugerepeatedstringthisisahugerepeatedstringthisisahugerepeatedstringthisisahugerepeatedstr' +
        'ingthisisahugerepeatedstringthisisgerepeatedstringthisisahugerepeatedstringthisisahugerepeatedstringthisisahu' + 
        'gerepeatedstringthisisahugerepeatedstringthisisahugerepeatedstringthisisahugerepeatedstringthisisahugerepeatedstring')
        result = password_validator.validate_password(password, {}, True)
        self.assertEqual(result, password + ' -> Error: ' + password_validator.ERROR_PASSWORD_IS_TOO_LONG)

    def test_validate_password_when_password_is_not_ascii(self):
        """
        Test that validate_password 
        can return correct error when password is not ascii
        """
        password = '的中文翻譯 | 英漢字典'
        result = password_validator.validate_password(password, {}, True)
        self.assertEqual(result, password + ' -> Error: ' + password_validator.ERROR_PASSWORD_IS_NOT_ASCII)

    def test_validate_password_when_password_is_common(self):
        """
        Test that validate_password 
        can return correct error when password is common
        """
        password = 'this is a common password'
        result = password_validator.validate_password(password, {password}, True)
        self.assertEqual(result, password + ' -> Error: ' + password_validator.ERROR_PASSWORD_IS_TOO_COMMON)

    def test_validate_password_when_there_are_more_than_one_error(self):
        """
        Test that validate_password 
        can return correct errors when there are more than one error
        """
        password = '12345'
        result = password_validator.validate_password(password, {password}, True)
        self.assertEqual(result, 
            password + ' -> Error: ' + password_validator.ERROR_PASSWORD_IS_TOO_SHORT + ', ' 
            + password_validator.ERROR_PASSWORD_IS_TOO_COMMON)

    def test_validate_ascii_when_password_validate_ascii(self):
        """
        Test that validate_ascii 
        can return True when password is ascii
        """
        password = 'this is ascii'
        result = password_validator.validate_ascii(password)
        self.assertTrue(result) 

    def test_validate_ascii_when_password_is_not_ascii(self):
        """
        Test that validate_ascii 
        can return False when password is not ascii
        """
        password = '英漢字典'
        result = password_validator.validate_ascii(password)
        self.assertFalse(result) 

if __name__ == '__main__':
    unittest.main()

