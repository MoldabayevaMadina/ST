import os
def get_caps(browser, username, access_key, test_name):
    caps = {
        "browserName": browser,
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "userName": username,
            "accessKey": access_key,
            "projectName": "Homework 3+4",
            "buildName": f"Jenkins-{os.getenv('JOB_NAME')}-{os.getenv('BUILD_NUMBER')}",
            "sessionName": test_name
        }
    }
    return caps
