# NIST-Password-Validator
This program takes in 2 files:
1. An `input file` that contains a list of passwords that you want to validate.
2. A `commonly used passwords file` that contains a list of passwords that are very common that it should not be used

The validation has the following criteria:
1. Have an 8 character minimum
2. Have a 64 character maximum
3. Must be ASCII
4. Must not be a commonly used password

## To Run The Program
1. Follow the setup instruction to install `python` and cloning the repo
2. cd into the root of the program directory `cd NIST-Password-Validator`
3. run `python password_validator.py [input_file] [commonly_used_password_file]` while replacing 
* `[input_file]` with the path to the file containing a list of passwords you want to check and
* `[commonly_used_password_file]` with the path to the file containing a list of password you want to exclude because they are commonly used. If you need one, please use this <a href="https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"> Common Password List </a>
4. An example: `python password_validator.py input_password.txt commonly_used_password_file.txt`
5. Sample of successful output includes

```
--- Attempting to read in weak password validation file ---
--- Validating input password ---

Line [1]: 123456789 -> Error: Too Common
Line [8]: dewed -> Error: Too Short
Line [9]: kckwo -> Error: Too Short
Line [10]: 123456789 -> Error: Too Common
Line [11]: 支持多件包裹打包运输‎ -> Error: Invalid Characters
Line [14]: verylongtextblobwillexceed64charactersverylongtextblobwillexceed64charactersverylongtextblobwillexceed64charactersverylongtextblobwillexceed64characters -> Error: Too Long
Line [15]: password -> Error: Too Common
Line [16]: 123123 -> Error: Too Short
Line [17]: 多件 -> Error: Too Short, Invalid Characters


--- Printing summary ---
Number of bad password: 9
Number of good password: 10
Number of password found: 19
```
6. Sample of failure output includes
* When command line is invalid
```
Please check that your input is in the correct format. 
python password_validator.py input_password.txt commonly_used_password_file.txt
```

* When Files does not exist
```
File does-not-exist.txt is not found.
File does-not-exist2.txt is not found.
```

## To Run The Unit Test
1. Follow the setup instruction to install `python` and cloning the repo
2. cd into the root of the program directory `cd NIST-Password-Validator`
3. run `python password_validator_test.py`

```
.............
----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```

## Setup Instructions
1. Let install <a href="https://brew.sh/">`homebrew`</a>, a package manager that will help us install python

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Install Python through brew

```
brew install python
```

3. Clone the Repo

```
git clone https://github.com/Mr-Ming/NIST-Password-Validator.git
```

## 
