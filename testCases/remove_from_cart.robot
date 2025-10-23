*** Settings ***
Resource    ../resources/resources.robot

*** Test Cases ***
Verify User Can Add to Cart
    Open Login Page
    Login User
    Add Product To Cart
    Remove Product From Cart
    Close Browser



