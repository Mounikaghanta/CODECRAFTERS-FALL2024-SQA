import os
import ast
import pandas as pd
import numpy as np
import datetime
import time
import datetime
from unittest.mock import patch
from myLogger import giveMeLoggingObject
import csv

logger = giveMeLoggingObject()

# Global bug reports list
bug_reports = []

# Method 1 - checkIfParsablePython
def checkIfParsablePython(pyFile):
    flag = True
    try:
        full_tree = ast.parse(open(pyFile).read())
    except (SyntaxError, UnicodeDecodeError) as err_:
        flag = False
    return flag

# Fuzzing Method 1: checkIfParsablePython
def fuzz_checkIfParsablePython():
    logger.info("=== Fuzzing checkIfParsablePython ===")
    test_cases = [
        "valid_script.py",  # Valid Python script
        "invalid_script.py",  # Invalid Python script
        "non_existent_file.py",  # Non-existent file
        None,  # None as input
        "",  # Empty string as input
    ]
    for i, file_ in enumerate(test_cases):
        try:
            if file_ and "valid" in file_:
                with open(file_, "w") as f:
                    f.write("print('Hello, world!')")
            elif file_ and "invalid" in file_:
                with open(file_, "w") as f:
                    f.write("print('Hello, world!'")
            result = checkIfParsablePython(file_)
            logger.info(f"Test Case {i + 1}: Input={file_}, Parsable={result}")
        except Exception as e:
            logger.error(f"Test Case {i + 1}: Input={file_}, Exception={e}")
            bug_reports.append({"Method": "checkIfParsablePython", "Input": file_, "Error": str(e)})

# Method 2 - getFileLength
def getFileLength(file_):
    return sum(1 for line in open(file_, encoding="latin-1"))

# Fuzzing Method 2: getFileLength
def fuzz_getFileLength():
    logger.info("=== Fuzzing getFileLength ===")
    test_cases = [
        "empty_file.txt",  # Empty file
        "small_file.txt",  # Small file
        "large_file.txt",  # Large file
        "non_existent_file.txt",  # Non-existent file
        None,  # None as input
    ]
    for i, file_ in enumerate(test_cases):
        try:
            if file_ and "file" in file_:
                with open(file_, "w") as f:
                    if "empty" in file_:
                        pass
                    elif "small" in file_:
                        f.write("Line1\nLine2\n")
                    elif "large" in file_:
                        f.write("Line\n" * 1000)
            result = getFileLength(file_)
            logger.info(f"Test Case {i + 1}: Input={file_}, Lines={result}")
        except Exception as e:
            logger.error(f"Test Case {i + 1}: Input={file_}, Exception={e}")
            bug_reports.append({"Method": "getFileLength", "Input": file_, "Error": str(e)})

# Method 3 - dumpContentIntoFile
def dumpContentIntoFile(strP, fileP):
    with open(fileP, "w") as fileToWrite:
        fileToWrite.write(strP)
    return os.stat(fileP).st_size

# Fuzzing Method 3: dumpContentIntoFile
def fuzz_dumpContentIntoFile():
    logger.info("=== Fuzzing dumpContentIntoFile ===")
    fuzz_dir = "fuzz_test"
    os.makedirs(fuzz_dir, exist_ok=True)
    test_cases = [
        ("Hello, World!", "valid.txt"),  # Valid content and file path
        ("", "empty.txt"),  # Empty content
        ("LongContent" * 100, "long_content.txt"),  # Long content
        (None, "null_content.txt"),  # None as content
        ("Hello", ""),  # Empty file path
    ]
    for i, (content, file_name) in enumerate(test_cases):
        try:
            file_path = os.path.join(fuzz_dir, file_name)
            if not file_name:
                raise ValueError("File name cannot be empty.")
            result = dumpContentIntoFile(content, file_path)
            logger.info(f"Test Case {i + 1}: content={content}, file_path={file_path}, Size={result} bytes")
        except Exception as e:
            logger.error(f"Test Case {i + 1}: content={content}, file_path={file_name}, Exception={e}")
            bug_reports.append({"Method": "dumpContentIntoFile", "Input": file_name, "Error": str(e)})
    for file in os.listdir(fuzz_dir):
        os.remove(os.path.join(fuzz_dir, file))
    os.rmdir(fuzz_dir)

# Method 4 - getPythonCount
def getPythonCount(path2dir):
    usageCount = 0
    for root_, _, filenames in os.walk(path2dir):
        usageCount += sum(1 for file_ in filenames if file_.endswith(".py"))
    return usageCount

# Fuzzing Method 4: getPythonCount
def fuzz_getPythonCount():
    logger.info("=== Fuzzing getPythonCount ===")
    fuzz_dir = "fuzz_test"
    os.makedirs(fuzz_dir, exist_ok=True)
    test_cases = [
        (fuzz_dir, []),  # Empty directory
        (fuzz_dir, ["file1.py", "file2.py", "file3.txt"]),  # Mixed files
        ("non_existent_directory", None),  # Non-existent directory
        (None, None),  # None as directory
        ("", None),  # Empty string as directory
    ]
    for i, (dir_path, files) in enumerate(test_cases):
        try:
            if dir_path and files:
                for file in files:
                    with open(os.path.join(dir_path, file), "w") as f:
                        f.write("print('Hello, world!')")
            result = getPythonCount(dir_path)
            logger.info(f"Test Case {i + 1}: dir_path={dir_path}, Python File Count={result}")
        except Exception as e:
            logger.error(f"Test Case {i + 1}: dir_path={dir_path}, Exception={e}")
            bug_reports.append({"Method": "getPythonCount", "Input": dir_path, "Error": str(e)})
    for file in os.listdir(fuzz_dir):
        os.remove(os.path.join(fuzz_dir, file))
    os.rmdir(fuzz_dir)

# Method 5 - giveTimeStamp
class constants:
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def giveTimeStamp():
    tsObj = time.time()
    return datetime.datetime.fromtimestamp(tsObj).strftime(constants.TIME_FORMAT)

# Fuzzing Method 5: giveTimeStamp
def fuzz_giveTimeStamp():
    logger.info("=== Fuzzing giveTimeStamp ===")
    test_cases = [
        0,  # Unix epoch start
        2**31 - 1,  # Maximum 32-bit integer timestamp
        2**31,  # After 32-bit integer limit
        -1,  # Negative timestamp
        time.time(),  # Current time
    ]
    for i, mocked_time in enumerate(test_cases):
        with patch("time.time", return_value=mocked_time):
            try:
                result = giveTimeStamp()
                logger.info(f"Test Case {i + 1}: Mocked time={mocked_time}, Output={result}")
            except Exception as e:
                logger.error(f"Test Case {i + 1}: Mocked time={mocked_time}, Exception={e}")
                bug_reports.append({"Method": "giveTimeStamp", "Input": mocked_time, "Error": str(e)})

# Save bug reports to a CSV file
def save_bug_reports():
    if bug_reports:
        with open("fuzz_report.csv", "w", newline=","%Y-%m-%d %H:%M:%S"") as csvfile:
            fieldnames = ["Method", "Input", "Error", "Timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(bug_reports)
        logger.info("Bug report saved to fuzz_report.csv")
    else:
        logger.info("No bugs discovered during fuzzing.")

if __name__ == "__main__":
    fuzz_checkIfParsablePython()
    fuzz_getFileLength()
    fuzz_dumpContentIntoFile()
    fuzz_getPythonCount()
    fuzz_giveTimeStamp()
    save_bug_reports()
