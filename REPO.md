![Aspose Words a24c1642-e5ec-4825-8036-44a419b48d93 001](https://github.com/user-attachments/assets/962a4fd9-5669-4594-8b06-f14aeffe7792)


**Software Quality Assurance ![ref1](COMP 6710)** 

**Project Report** 

**Done By:   Koushik Govardhanam – kzg0099 Mounika Ghanta-mgz0144** 

**Pavan Kalyan Annadevara- pza0045** 

**Summary: ![ref1]**

The goal of this project is to embed software quality assurance practices into an existing  Python  application.  These  efforts  focus  on  improving  the  codebase's reliability,  security,  and  maintainability  by  applying  principles  discussed  in workshops. Key activities included in the project are as follows: 

1. **Git Hooks Implementation:** 

A Git Hook was added to automatically scan Python files for security vulnerabilities whenever changes are committed. The system generates a result.csv  file  detailing  any  identified  issues,  ensuring  developers  are promptly alerted to potential weaknesses. 

2. **Fuzz Testing:** 

A script named fuzz.py was developed to randomly test five selected methods using various input combinations. This script is integrated into GitHub Actions, enabling it to  run automatically during commits and continually test the application for errors or inconsistencies. 

3. **Forensic Logging:** 

Logging mechanisms were incorporated into five critical methods to track their usage. This includes capturing parameters, outputs, and execution flows,  providing  developers  with  detailed  traceability  to  simplify debugging and improve overall transparency. 

4. **Continuous Integration with GitHub Actions:** 

A set of workflows was configured to automate static analysis, fuzz testing, and  linting  whenever  changes  are  pushed  to  the  repository.  These workflows ensure that errors and potential issues are identified early in the development cycle, streamlining quality assurance processes. 

By integrating these activities, the project highlights a well-rounded approach to software quality assurance. It leverages static analysis, fuzz testing, forensic logging, and automation via continuous integration pipelines to uphold coding best practices. The outcomes and lessons learned through this integration are comprehensively documented in the accompanying project report. 

**Project  for  Software  Quality  Assurance  (CSSE/6710) ![ref1]CODECRAFTERS-SQA2024-Auburn** 

**Task 4.a: Setting Up a Pre-Commit Hook and Conducting Security Analysis with Bandit** 

The objective was accomplished by integrating a Git Hook into the development process. The Git Hook enables static analysis to operate seamlessly within the workflow, providing real-time detection of potential weaknesses whenever code changes are committed. This approach ensures a proactive and consistent enhancement of code security during development. 

**Repository Initialization:** 

- Initialized a Git repository and cloned it onto the local machine for development. 
- Verified the repository structure to ensure readiness for customization. 

**Pre-Commit Hook Creation**: 

- Navigated to the ./git/hooks/ directory and reviewed the pre-commit.sample file. 
- Used the sample file as a template to create a new file named pre-commit. 
- Customized the new pre-commit script to include specific checks or validations to execute before commits. 

**Testing the Hook**: 

- Made changes to the report.py file in empirical within the repository to test the functionality of the pre-commit hook. 
- Attempted a commit to confirm that the hook was correctly triggered and enforced the configured rules. 

**Security Analysis:** 

- Executed the bandit -r command to scan the repository for potential security vulnerabilities. 
- Focused on identifying weaknesses in the updated report.py file. 
- Documented the results provided by Bandit, including flagged warnings or suggestions for improvement. 

**Outcomes: ![ref1]**

- The custom pre-commit hook was successfully implemented, tested, and validated. 
- Bandit’s analysis provided actionable insights into potential vulnerabilities in the repository, particularly in the modified report.py file. 
- These steps combined reinforce code quality and security in the repository, making it better equipped for reliable and secure development. 
- The results are stored in security-report.csv file. 

![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.003.jpeg)

![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.004.jpeg)

**2. Fuzzing: ![ref1]**

**Creating the fuzz.py File: A Step-by-Step Overview Objective:** 

The primary goal of this task is to develop a Python script named fuzz.py that tests five selected methods within the project for vulnerabilities or bugs. This script will integrate with GitHub Actions to ensure automated quality checks during each workflow run. 

**Key Steps and Actions: Method Selection for Fuzzing:** 

1. fuzz\_checkIfParsablePython() 
1. fuzz\_join() 
1. fuzz\_pop() 
1. fuzz\_update() 
1. fuzz\_float() 

` `**Preparation and Setup:** 

- Extracted the project files and validated their structure. 
- Reviewed and documented the functionality of Python methods to identify candidates for fuzzing. 

**Script Development:** 

- Created the fuzz.py script using a simple text editor (nano). 
- Wrote the script to generate diverse inputs (including edge cases and invalid data) for the selected methods. 
- Ensured thorough coverage by testing scenarios that simulate realistic and unexpected use cases. 

**Version Control:** 

- Staged the newly created fuzz.py file along with other relevant changes using git add .. 
- Committed the changes with a concise message to maintain a clear project 

  history. ![ref1]

**GitHub Actions Integration:** 

- Configured the script to execute automatically during each workflow run by editing the GitHub Actions YAML file. 
- Incorporated logging mechanisms to capture errors and unexpected outputs systematically. 

**Details of the fuzz.py Script: Focus Areas:** 

- Selected  five  methods  with  varying  levels  of  complexity  to  provide  a comprehensive test scope. 
- Designed the script to log errors and unexpected outputs in a structured, readable format. 

**Outputs:** 

- Generates a summary report highlighting test case results and anomalies. 
- Provides developers with actionable insights into potential vulnerabilities. 
- This process establishes a robust framework for early detection of errors, enhancing the project's reliability and security. 

  ![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.005.jpeg)

**Task 4.c: Integrating Forensic Capabilities into Python Methods** 

**Objective: ![ref1]**

The aim of this task is to enhance five selected Python methods by embedding forensic logging. This integration enables detailed tracking of each method's behavior, including inputs, outputs, and errors. The improvements ensure greater transparency and traceability, facilitating debugging and analysis. 

**Implementation:** 

1. **Forensic Logging**: 
- Incorporated the log\_forensics function into each method for capturing key details, including: 
  - Input values. 
  - Output results or error messages. 
  - Execution timestamps. 
- Designed the logs to provide granular insights into method behavior during execution. 
2. **Modification of Methods**: 
- **checkIfParsablePython**: 
  - Enhanced logging to track input files. 
  - Documented detailed error messages for scenarios like syntax errors, missing files, or unsupported input types. 
- **str.join**: 
  - Captured information about list contents and separators. 
  - Logged exceptions raised during invalid operations. 
- **list.pop**: 
  - Recorded list states and index values before and after removing elements. 
  - Logged errors for invalid index usage. 
- **dict.update**: 
  - Monitored all dictionary updates and captured errors due to invalid formats (e.g., lists provided instead of dictionaries). 
- **float()**: 
- Logged inputs passed to the function. 
- Recorded error details for inputs that could not be converted to numeric values. 
3. **Bug Tracking**: 
- All detected issues were documented in a CSV file ![ref1](fuzz\_report.csv) to enable efficient analysis. 
- **Examples of Identified Bugs**: 
- **checkIfParsablePython**: Errors related to missing files (FileNotFoundError) and invalid input types (NoneType). 
- **float()**: Conversion failures for non-numeric strings. 
4. **Automated Reporting**: 
- Configured the script to save logs and error summaries in fuzz\_report.csv. 
- Structured logs offer a clear overview of method performance under varied test conditions, including edge cases. 
- ![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.006.jpeg)

**Outcomes:** 

- **Enhanced Debugging and Traceability**: 
  - Forensic logging provided insights into previously unidentified issues, such as syntax errors and type mismatches. 
- **Sample Findings**: 
  - Syntax errors in invalid Python scripts. 
  - Errors in dictionary updates caused by incorrect input types. 
  - Conversion failures when float() processed non-numeric strings. 
- **Automation**: 
- Seamless integration with GitHub Actions ensures that forensic logs and error reports are updated automatically during each workflow run. 

By implementing forensic logging, the project achieves a new level of robustness, ![ref1]enabling consistent monitoring and issue resolution across the selected methods. 

![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.007.jpeg)

**Task 4.d: Integrate Continuous Integration with GitHub Actions** 

**Objective:** The goal of Task 4.d was to integrate Continuous Integration (CI) into the project using GitHub Actions. This ensures that every commit and push to the repository triggers automated testing to maintain code quality and reliability. 

**Implementation:** 

- Created a .github/workflows/testing.yaml file to define the CI pipeline. 
- Configured the workflow to automatically trigger on every push event to the repository. 
- Installed all necessary project dependencies using pip based on the requirements.txt file. 
- Executed the fuzz.py script to perform fuzz testing on the selected Python methods 

**Successful Integration:** ![ref1]

- The workflow was tested and confirmed successful, as indicated by the "All checks have passed" message in the GitHub repository. 
- Logs from the GitHub Actions dashboard show that the CI pipeline executed without errors. 

**Outcome:** 

- Continuous Integration is now fully integrated into the repository. 
- Each commit automatically triggers the testing pipeline, ensuring high code quality and rapid feedback on any issues. 

  ![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.008.jpeg)

![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.009.jpeg)

![](Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.010.jpeg)

**Conclusion ![ref1]**

In this project, we successfully integrated software quality assurance practices into an existing Python project, demonstrating the application of concepts learned throughout the course. By incorporating activities such as security analysis, fuzz testing, forensics integration, and continuous integration using GitHub Actions, we ensured the robustness and reliability of the codebase. The systematic approach and collaborative effort not only enhanced our technical skills but also provided valuable insights into the importance of quality assurance in software development. This project reinforces the significance of integrating SQA practices to achieve reliable, secure, and maintainable software solutions. 

[ref1]: Aspose.Words.a24c1642-e5ec-4825-8036-44a419b48d93.002.png
