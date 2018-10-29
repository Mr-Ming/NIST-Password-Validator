# coding=utf-8
import os
import sys

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64

ERROR_INVALID_INPUT = ('Please check that your input is in the correct format. \n' + 
'python password_validator.py input_password.txt commonly_used_password_file.txt')
ERROR_FILE_NOT_FOUND = 'File {} is not found.'
ERROR_PASSWORD_IS_TOO_SHORT = 'Too Short'
ERROR_PASSWORD_IS_TOO_LONG = 'Too Long'
ERROR_PASSWORD_IS_NOT_ASCII = 'Invalid Characters'
ERROR_PASSWORD_IS_TOO_COMMON = 'Too Common'

NOTICE_READING_WEAK_PASSWORDS_VALIDATION_FILE = '--- Attempting to read in weak password validation file ---'
NOTICE_CHECKING_INPUT_PASSWORDS_FILE = '--- Validating input password ---'
NOTICE_SUMMARY = '--- Printing summary ---'
NOTICE_COUNT_BAD_PASSWORD = 'Number of bad password: {}'
NOTICE_COUNT_GOOD_PASSWORD = 'Number of good password: {}'
NOTICE_COUNT_TOTAL_PASSWORD = 'Number of password found: {}'

def main():
	print('\n')
	password_validator()
	print('\n')

def password_validator():
	if validate_input_from_command_line(sys.argv) is False:
		print(ERROR_INVALID_INPUT)
		return

	input_passwords_file = sys.argv[1]
	weak_passwords_validation_file = sys.argv[2]

	is_file_exist = validate_files_exist(input_passwords_file, weak_passwords_validation_file)
	if is_file_exist is not True:
		print(is_file_exist)
		return

	perform_validation(input_passwords_file, weak_passwords_validation_file)

def perform_validation(input_passwords_file, weak_passwords_validation_file):
	print(NOTICE_READING_WEAK_PASSWORDS_VALIDATION_FILE)

	weak_passwords_list = set([])
	bad_password_count = 0
	line_number = 0

	with open(weak_passwords_validation_file) as file:
		for password in file:
			password = password.strip('\n')

			if validate_password(password, None, False) is True:
				weak_passwords_list.add(password)

	file.close()

	print(NOTICE_CHECKING_INPUT_PASSWORDS_FILE + '\n')

	with open(input_passwords_file) as file:
		for password in file:
			line_number+=1
			password = password.strip('\n')

			is_valid_password = validate_password(password, weak_passwords_list, True)
			if is_valid_password is not True:
				print ('Line [{}]: '.format(line_number) + is_valid_password)
				bad_password_count+=1

	file.close()
	
	print('\n')
	print(NOTICE_SUMMARY)
	print(NOTICE_COUNT_BAD_PASSWORD.format(bad_password_count))
	print(NOTICE_COUNT_GOOD_PASSWORD.format(line_number - bad_password_count))
	print(NOTICE_COUNT_TOTAL_PASSWORD.format(line_number))
	
def validate_input_from_command_line(command):
	if len(command) != 3:
		return False

	return True

def validate_files_exist(input_passwords_file, weak_passwords_validation_file):
	error_message = []

	if os.path.isfile(input_passwords_file) is False:
		error_message.append(ERROR_FILE_NOT_FOUND.format(input_passwords_file))

	if os.path.isfile(weak_passwords_validation_file) is False:
		error_message.append(ERROR_FILE_NOT_FOUND.format(weak_passwords_validation_file))

	if (len(error_message)) > 0:
		return '\n'.join(error_message)

	return True

def validate_password(password, compare_with_weak_passwords_set, with_error_message):
	if with_error_message is False:
		if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH or validate_ascii(password) is False:
			return False
	else:
		error_message = []

		if len(password) < MIN_PASSWORD_LENGTH:
			error_message.append(ERROR_PASSWORD_IS_TOO_SHORT)

		if len(password) > MAX_PASSWORD_LENGTH:
			error_message.append(ERROR_PASSWORD_IS_TOO_LONG)

		if validate_ascii(password) is False:
			error_message.append(ERROR_PASSWORD_IS_NOT_ASCII)

		if password in compare_with_weak_passwords_set:
			error_message.append(ERROR_PASSWORD_IS_TOO_COMMON)

		if len(error_message) > 0:
			return password + ' -> Error: ' + ', '.join(error_message)

	return True

def validate_ascii(password):
  return all(ord(character) < 128 for character in password)

if __name__== "__main__":
	main()
