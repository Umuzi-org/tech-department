---
title: password-checker
pre: "<b>MEDIUM: </b>"
ready: true
---

Implement the following function by following a TDD methodology:

```
password_is_valid(password)
```

password_is_valid will check a a few different conditions. If a condition is fails then an error/exception should be raised/thrown. That error/exception can have a message of your choosing.

1. password should be larger than 8 chars
2. password should not be null
3. password should have at least one uppercase letter
4. password should have at least one lowercase letter
5. password should have at least one number

Next, implement a function called `password_is_ok(password)`. If the given password meets at least three of the criteria listed above then this function should return true, otherwise it should return false.

Add a feature: the password is never OK if conditions 1 and 2 are not met

## JS Resources

- [JS Errors](https://www.w3schools.com/js/js_errors.asp)
- [Errors and Jasmine](https://stackoverflow.com/questions/4144686/how-to-write-a-test-which-expects-an-error-to-be-thrown-in-jasmine)

## Python Resources

- [Python Errors](https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9?referral=sheena-kvo1e6ewh)
- [Exceptions and Pytest](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest)


