# Test Plan — SauceDemo

## Project Overview
Testing the SauceDemo e-commerce web application at https://www.saucedemo.com

## Scope
### In Scope
- Login and authentication
- Product listing and sorting
- Product detail page
- Shopping cart
- Checkout process
- Logout

### Out of Scope
- Payment processing
- Backend/database testing
- Performance testing

## Test Approach
Manual functional testing followed by Selenium automation

## Tools
- Browser: MicroSoft Edge
- Test management: Excel
- Automation: Python + Selenium
- CI/CD: GitHub Actions

## Test Environment
- URL: https://www.saucedemo.com
- Browser: Microsoft Edge latest
- OS: Windows 11

## Test Credentials
- Standard user: standard_user / secret_sauce
- Locked user: locked_out_user / secret_sauce
- Problem user: problem_user / secret_sauce

## Entry Criteria
- Application is accessible
- Test cases are written and reviewed
- Test data is prepared

## Exit Criteria
- 95% of test cases executed
- All critical and major bugs logged
- Test summary report completed

## Risks
- Site may be unavailable during testing
- UI may change without notice