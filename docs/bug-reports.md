# Bug Reports — SauceDemo (problem_user)

---

## BUG-001
**Title:** All product images display the same dog image instead of correct product images

**Environment:** Chrome/Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce

**Steps to reproduce:**
1. Go to https://www.saucedemo.com
2. Login with username: problem_user, password: secret_sauce
3. Observe the product listing page

**Expected result:** Each product displays its own unique correct image

**Actual result:** All products display the same dog image regardless of the product

**Severity:** Major

**Evidence:** ![BUG-001](docs/screenshots/all item image are same.png)

---

## BUG-002
**Title:** Add to Cart button does not function for 3rd, 4th and 6th products on listing page

**Environment:** Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce

**Steps to reproduce:**
1. Login with problem_user / secret_sauce
2. On product listing page click Add to Cart on the 3rd product
3. Repeat for 4th and 6th products
4. Observe cart icon

**Expected result:** Items added to cart and cart badge count increases

**Actual result:** Clicking Add to Cart on 3rd, 4th and 6th products has no effect — cart count does not update

**Severity:** Critical

**Evidence:** ![BUG-002](docs/screenshots/add to cart button does not work.png)

---

## BUG-003
**Title:** Added items cannot be removed from cart on product listing page

**Environment:** Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce. At least one item added to cart.

**Steps to reproduce:**
1. Login with problem_user / secret_sauce
2. Add any available product to cart
3. Click the Remove button on the same product
4. Observe whether item is removed

**Expected result:** Item is removed from cart and button changes back to Add to Cart

**Actual result:** Clicking Remove has no effect — item stays in cart

**Severity:** Critical

**Evidence:** ![BUG-003](docs/screenshots/remove button does not work.png)

---

## BUG-004
**Title:** Clicking a product opens a completely different product's detail page

**Environment:** Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce

**Steps to reproduce:**
1. Login with problem_user / secret_sauce
2. Click on any product on the listing page
3. Observe which product detail page opens

**Expected result:** The clicked product's detail page opens with correct information

**Actual result:** A different product's detail page opens instead of the one clicked

**Severity:** Critical

**Evidence:** 
- After click: ![BUG-004-after](docs/screenshots/backpack clicking shows jacket details.png)

---

## BUG-005
**Title:** Clicking cart icon redirects to login page or shows blank white page

**Environment:** Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce. Items in cart.

**Steps to reproduce:**
1. Login with problem_user / secret_sauce
2. Add any item to cart
3. Click the cart icon in the top right corner
4. Observe what happens

**Expected result:** Cart page loads showing all added items

**Actual result:** User is either redirected to login page or a completely blank white page loads

**Severity:** Critical — users cannot access or complete their cart at all

**Evidence:** ![BUG-005](docs/screenshots/cart icon redirects to login page.png)
[BUG-005](docs/screenshots/cart icon not accessible .png)

---

## BUG-006
**Title:** Cart icon shows incorrect item count — displays 4 but only 3 items selected

**Environment:** Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce

**Steps to reproduce:**
1. Login with problem_user / secret_sauce
2. Add 3 items to cart from product listing page
3. Observe the cart icon badge number

**Expected result:** Cart badge displays 3 to match number of items added

**Actual result:** Cart badge displays 4 despite only 3 items being added

**Severity:** Major — incorrect cart count misleads users

**Evidence:** ![BUG-006](docs/screenshots/3 item selected but 4 shown in cart icon.png)

---

## BUG-007
**Title:** Fleece Jacket product detail page shows item not found

**Environment:** Edge latest, Windows 11, https://www.saucedemo.com

**Preconditions:** Logged in as problem_user / secret_sauce

**Steps to reproduce:**
1. Login with problem_user / secret_sauce
2. Click on Sauce Labs Fleece Jacket from product listing
3. Observe the product detail page

**Expected result:** Fleece Jacket detail page opens with correct name, image, price and description

**Actual result:** Page shows item not found error — product detail is completely unavailable

**Severity:** Critical — users cannot view or purchase the Fleece Jacket at all

**Evidence:** ![BUG-007](docs/screenshots/fleece jacket is not found while clicking.png)