*** Settings ***
Library    SeleniumLibrary
Variables  ./locators.py
Variables  ./testData.py

*** Keywords ***
Open Login Page
    Open Browser    ${baseUrl}    edge
    Maximize Browser Window

Close Browser
    Close All Browsers


Login User
    Input Text      ${username_field}      ${username}
    Input Text      ${password_field}   ${password}
    Click Button    ${login_button}
    Sleep    2s

Add Product To Cart
    Sleep    2s
    Wait Until Element Is Visible    ${add_to_cart_backpack}    timeout=3s
    Click Element    ${add_to_cart_backpack}
    Click Element    ${cart_icon}
    Page Should Contain    Sauce Labs Backpack
    Sleep    2s

Remove Product From Cart
    Wait Until Element Is Visible    ${remove_backpack}    timeout=3s
    Click Element    ${remove_backpack}
    Sleep    1s
    Page Should Not Contain    Sauce Labs Backpack
    Sleep    2s

Logout User
    Wait Until Element Is Visible    ${menu_button}    timeout=5s
    Click Element    ${menu_button}
    Wait Until Element Is Visible    ${logout_link}    timeout=5s
    Click Element    ${logout_link}
    Sleep    2s
    Wait Until Element Is Visible    ${login_button}    timeout=10s
    Sleep    2s
    Page Should Contain Element      ${login_button}

