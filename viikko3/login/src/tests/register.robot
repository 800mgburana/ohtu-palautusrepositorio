*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Go To Register Page
    Set Username  miumau
    Set Password  12345678
    Set Password Confirmation  12345678
    Click  button >> text=Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  m
    Set Password  12345678
    Set Password Confirmation  12345678
    Click  button >> text=Register
    Registration Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  miumau
    Set Password  1
    Set Password Confirmation  1
    Click  button >> text=Register
    Registration Should Fail With Message  Password should be at least 8 characters long

Register With Username That Is Already In Use
    Go To Register Page
    Set Username  kalle
    Set Password  12345678
    Set Password Confirmation  12345678
    Click  button >> text=Register
    Registration Should Fail With Message  Username already in use


*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
