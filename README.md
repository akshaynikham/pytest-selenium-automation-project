# Amazon Automation Project

This project automates interactions with Amazon's website using Selenium and pytest.

## Project Structure

- `amazon/`: Contains application code.
- `tests/`: Contains test code.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.

## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Ensure `chromedriver` is in your system PATH.

## Running Tests

To run the tests, execute:
    ```
    pytest    
    ```
## Allure - to generate report

1. **Java and Allure CLI Installation**:
   - **Java**: Allure requires Java to run, so install Java on local system. This is a one-time installation.
   - **Allure CLI**: The Allure Command-Line Interface (CLI) is also a standalone tool that needs to be install on local system. This allows you to generate and serve Allure reports.

2. **Allure-Pytest Plugin**:
   - **Within Your `venv`**: The Allure-Pytest plugin is installed within Python virtual environment (`venv`). This plugin enables pytest to generate the necessary files (results) that the Allure CLI will use to create reports.

### Step-by-Step Guide

#### 1. Install Java on Local System

Ensure Java is installed:

```bash
java -version
```

If not installed, download and install it from [here](https://www.oracle.com/java/technologies/javase-downloads.html).

#### 2. Install Allure CLI on Local System

Follow the steps to install Allure CLI:

##### Windows

1. **Download Allure**:
   - Download from [Allure releases](https://github.com/allure-framework/allure2/releases).

2. **Extract Allure**:
   - Extract to `C:\allure`.

3. **Add to PATH**:
   - Add `C:\allure\bin` to your system PATH.


#### 3. Install Allure-Pytest Plugin in `venv`

Activate virtual environment and install the Allure-Pytest plugin:

```bash
source path/to/venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install allure-pytest
```

#### 4. Configure `pytest.ini`

Create or update the `pytest.ini` file in project root:

```ini
[pytest]
addopts = --alluredir=allure-results
```



#### 6. Run Tests and Generate Allure Report

1. **Run Your Tests**:

   ```bash
   pytest
   ```

   This will generate Allure results in the `allure-results` directory.

2. **Serve the Allure Report**:

   ```bash
   allure serve allure-results
   ```

### Summary

- **Java and Allure CLI**: Install on your local system, not within the `venv`.
- **Allure-Pytest Plugin**: Install within your `venv`.
- **Configuration and Annotations**: Set up pytest to use Allure and annotate your tests.
- **Generate and Serve Reports**: Use pytest to run tests and the Allure CLI to generate and view reports.