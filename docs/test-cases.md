# Test Cases — SauceDemo

## Module 1: Login

| TC ID | Test Scenario | Steps | Expected Result | Status |
|-------|--------------|-------|-----------------|--------|
| TC001 | Valid login | 1. Go to saucedemo.com 2. Enter standard_user / secret_sauce 3. Click Login | Redirected to product page | |
| TC002 | Invalid password | 1. Enter standard_user / wrongpassword 2. Click Login | Error message shown | |
| TC003 | Empty username | 1. Leave username empty 2. Enter password 3. Click Login | Error: Username required | |
| TC004 | Empty password | 1. Enter username 2. Leave password empty 3. Click Login | Error: Password required | |
| TC005 | Locked out user | 1. Enter locked_out_user / secret_sauce 2. Click Login | Error: User locked out | |
| TC006 | Both fields empty | 1. Leave both empty 2. Click Login | Error message shown | |

## Module 2: Product Listing

| TC ID | Test Scenario | Steps | Expected Result | Status |
|-------|--------------|-------|-----------------|--------|
| TC007 | Products displayed | 1. Login 2. Observe product page | All products visible with name, price, image | |
| TC008 | Sort by price low to high | 1. Login 2. Select Price low to high filter | Products sorted correctly | |
| TC009 | Sort by price high to low | 1. Login 2. Select Price high to low filter | Products sorted correctly | |
| TC010 | Sort by name A-Z | 1. Login 2. Select Name A to Z filter | Products in alphabetical order | |

## Module 3: Product Detail

| TC ID | Test Scenario | Steps | Expected Result | Status |
|-------|--------------|-------|-----------------|--------|
| TC011 | View product detail | 1. Login 2. Click any product | Product detail page opens with name, description, price | |
| TC012 | Add to cart from detail | 1. Login 2. Open product 3. Click Add to Cart | Cart icon updates to show 1 item | |
| TC013 | Go back to products | 1. Login 2. Open product 3. Click Back | Returns to product listing | |

## Module 4: Shopping Cart

| TC ID | Test Scenario | Steps | Expected Result | Status |
|-------|--------------|-------|-----------------|--------|
| TC014 | Add item to cart | 1. Login 2. Click Add to Cart on any product | Cart badge shows 1 | |
| TC015 | Remove item from cart | 1. Login 2. Add item 3. Go to cart 4. Click Remove | Item removed, cart empty | |
| TC016 | Cart persists after navigation | 1. Login 2. Add item 3. Browse other pages 4. Return to cart | Item still in cart | |

## Module 5: Checkout

| TC ID | Test Scenario | Steps | Expected Result | Status |
|-------|--------------|-------|-----------------|--------|
| TC017 | Complete checkout | 1. Login 2. Add item 3. Checkout 4. Fill John / Doe / 12345 5. Finish | Order confirmation shown | |
| TC018 | Checkout with empty first name | 1. Login 2. Add item 3. Checkout 4. Leave first name empty 5. Continue | Error: First name required | |
| TC019 | Checkout with empty zip code | 1. Login 2. Add item 3. Checkout 4. Leave zip empty 5. Continue | Error: Zip code required | |

## Module 6: Logout

| TC ID | Test Scenario | Steps | Expected Result | Status |
|-------|--------------|-------|-----------------|--------|
| TC020 | Logout successfully | 1. Login 2. Click burger menu 3. Click Logout | Redirected to login page | |