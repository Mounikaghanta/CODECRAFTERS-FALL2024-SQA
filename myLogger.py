import logging
import csv
import datetime

# Set up logging
logging.basicConfig(
    filename="fuzz_forensics.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("FuzzLogger")

# Global bug reports list
bug_reports = []

def log_forensics(method_name, inputs, output=None, error=None):
    """Log detailed forensic information for debugging."""
    if error:
        logger.error(f"Forensics - Method: {method_name}, Inputs: {inputs}, Error: {error}")
        bug_reports.append({
            "Method": method_name,
            "Input": inputs,
            "Error": error,
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
    else:
        logger.info(f"Forensics - Method: {method_name}, Inputs: {inputs}, Output: {output}")

def save_bug_reports(filename="fuzz_report.csv"):
    """Save bug reports to a CSV file."""
    if bug_reports:
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["Method", "Input", "Error", "Timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(bug_reports)
        logger.info(f"Bug report saved to {filename}")
    else:
        logger.info("No bugs discovered during fuzzing.")
