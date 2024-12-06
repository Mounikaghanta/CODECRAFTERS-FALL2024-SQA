import random
import string
import ast
import os
import time
import datetime
from unittest.mock import patch
from myLogger import log_forensics, save_bug_reports

# Utility Functions
def random_string(length=10):
    """Generate a random string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Method 1 - Check if Parsable Python
def checkIfParsablePython(pyFile):
    flag = True
    try:
        full_tree = ast.parse(open(pyFile).read())
    except (SyntaxError, UnicodeDecodeError, FileNotFoundError) as err_:
        flag = False
        raise err_
    return flag

def fuzz_checkIfParsablePython():
    test_cases = ["valid_script.py", "invalid_script.py", "non_existent_file.py", None, ""]
    for file_ in test_cases:
        try:
            if file_ == "valid_script.py":
                with open(file_, "w") as f:
                    f.write("print('Hello, world!')")
            elif file_ == "invalid_script.py":
                with open(file_, "w") as f:
                    f.write("print('Hello, world!'")  # Syntax error
            result = checkIfParsablePython(file_)
            log_forensics("checkIfParsablePython", {"file": file_}, output=result)
        except Exception as e:
            log_forensics("checkIfParsablePython", {"file": file_}, error=str(e))

# Method 2 - Join Strings
def fuzz_join():
    test_list = [random.choice([random_string(5), None, 123]) for _ in range(5)]
    separator = random.choice(["-", " ", None])
    try:
        result = separator.join(test_list)
        log_forensics("str.join", {"list": test_list, "separator": separator}, output=result)
    except Exception as e:
        log_forensics("str.join", {"list": test_list, "separator": separator}, error=str(e))

# Method 3 - List Pop
def fuzz_pop():
    test_list = [random.randint(0, 100) for _ in range(random.randint(0, 10))]
    index = random.choice([random.randint(-10, 10), None])
    try:
        result = test_list.pop(index)
        log_forensics("list.pop", {"list": test_list, "index": index}, output=result)
    except Exception as e:
        log_forensics("list.pop", {"list": test_list, "index": index}, error=str(e))

# Method 4 - Dictionary Update
def fuzz_update():
    test_dict = {random_string(5): random.randint(0, 100) for _ in range(5)}
    updates = random.choice([{random_string(5): random.randint(0, 100)}, None, [("key", "value")]])
    try:
        test_dict.update(updates)
        log_forensics("dict.update", {"dict": test_dict, "updates": updates}, output=test_dict)
    except Exception as e:
        log_forensics("dict.update", {"dict": test_dict, "updates": updates}, error=str(e))

# Method 5 - Float Conversion
def fuzz_float():
    test_string = random.choice([random_string(), str(random.uniform(-1000, 1000)), None, "123.456"])
    try:
        result = float(test_string)
        log_forensics("float", {"input": test_string}, output=result)
    except Exception as e:
        log_forensics("float", {"input": test_string}, error=str(e))

if __name__ == "__main__":
    # Number of fuzz tests per method
    num_tests = 100

    for _ in range(num_tests):
        fuzz_checkIfParsablePython()
        fuzz_join()
        fuzz_pop()
        fuzz_update()
        fuzz_float()

    save_bug_reports()
    print("Fuzz testing completed. Check 'fuzz_forensics.log' and 'fuzz_report.csv'.")
