*** Settings ***
Resource    ../resources/resources.robot

*** Test Cases ***
Verify User Can Log In And Log Out
    Open Login Page
    Login User
    Close Browser
