---
title: password-checker
pre: "<b>MEDIUM: </b>"
ready: true
---

Implement the following function by following a TDD methodology:

```
Javascript:
passwordIsValid(password)
```

```
Python:
password_is_valid(password)
```

password_is_valid will check if the password meets a few different conditions. If one of the below conditions is not met then the relevant error/exception should be thrown/raised. Your error/exception message should match one of the following conditions exactly (word-for-word).

1. password should exist
2. password should be longer than than 8 characters
3. password should have at least have one lowercase letter
4. password should have at least one uppercase letter
5. password should at least have one digit

Next, implement a function called password is ok:

```
Javascript:
passwordIsOk(password)
```

```
Python:
password_is_ok(password)
```

If the given password meets at least three of the conditions listed above then this function should return true, otherwise it should return false.

Add a feature: the password is never OK if conditions 1 and 2 are not met.

## JS Resources

- [JS Errors](https://www.w3schools.com/js/js_errors.asp)
- [Errors and Jasmine](https://stackoverflow.com/questions/4144686/how-to-write-a-test-which-expects-an-error-to-be-thrown-in-jasmine)

## Python Resources

- [Python Errors](https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9?referral=sheena-kvo1e6ewh)
- [Exceptions and Pytest](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest)


