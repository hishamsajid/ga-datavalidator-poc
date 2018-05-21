# ga-datavalidator-poc

The Project is an attempt to automate the GA Analytics Audit at Marketlytics using Google Core Reporting and Management APIs. This is only a proof of concpept for a larger, more complex web-based app explained and linked in this article. http://marketlytics.com/blog/google-analytics-audit-tool

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install the python client for Google API using pip

```
$ pip install --upgrade google-api-python-client
```

Create an App on Google Cloud using the following link (assuming you already have a Google account)
https://support.google.com/cloud/answer/6158853

### Installing

1. Enable the 'Google Analytics API' and 'Google Analytics Reporting API' form the Google API console

2. Create 'OAuth client ID' Credentials from the Credentials section of the Google API console,
   in the Application type choose 'Other'

3. Download the client_secret JSON file of the created credential

4. Clone the code to your local repository

5. Give the client secrets path in the right variable
    ```
    CLIENT_SECRETS_PATH = 'client_secrets.json' #Path to client_secrets.json file
    ```

6. From your Google Analytics Account, find the IDs required for the application to function
    ```
    VIEW_ID = '88888888' #8 digit View ID
    ACCOUNT_ID = '88888888' #8 digit Account ID
    WEB_PROPERTY_ID = 'UA-88888888-9' #9 digit Web Property ID
    ```

## Running the tests

Test the program by running the following code from the terminal 
```
python ga_automation.py
```


