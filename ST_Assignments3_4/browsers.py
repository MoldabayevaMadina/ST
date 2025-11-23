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
            "buildName": "Build 1",
            "sessionName": test_name
        }
    }
    return caps
