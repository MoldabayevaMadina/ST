*** Settings ***
Resource    ../resources/resources.robot

*** Test Cases ***
Verify User Can Add to Cart
    Open Login Page
    Login User
    Add Product To Cart
    Close Browser



