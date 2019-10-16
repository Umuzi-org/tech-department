---
title: Coding Horrors
ready: true
---

# Common TDD pitfalls.

- **Write tests**. Recruits in the past have done the mistake of not writing tests for TDD assignments, make sure you avoid this weird mistake. always write tests for your TDD projects.
- Write your tests before you write your code (Red, Green, refactor).
- Please make sure you understand .gitignore, please don't add your node_modules to git
- name your files according to what is inside them. E.g. if you have a file called add.js that only contains a multiply function then something is wrong. Do this:
<!-- examples -->
**Python**:

`add.py`
```py
def add(***):
  # some operations
```
**Javascript**

`add.js`
```js
function add(***){
  // operations
}
```
- Good code makes it's intentions clear. Good code is never misleading or surprising.

- You can't define test case(function) inside a function.

---
**Python example:**

```py
def testOne():

  def testSomething():
    assert add("1,23,5") == 25

  def testSomething():
    assert add("1,23,5") == 29

```
instead you should put your tests into classes as methods, like so:

```py
class TestOne():

  def testSomething():
    assert add("1,23,5") == 25

  def testSomething():
    assert add("1,23,5") == 29

```
notice **def** keyword in the first cell is replaced with the **class** keyword in the second cell, this difference makes a major difference. The first case would **pass** as a single test, even though it contains two test cases and one of them must fail, in contrary the second case would run both tests, the first one would fail and the second one would pass.

---

- Test classes/describe function should focus on one functionality and one functionality only.

---
**Python example:**

Do not do this:
```py
  class TestFunctions():

    def test_addition(self):
      assert add("1,2,3,4") == 10

    def test_multiply(self):
      assert multiply("1,2,3") == 9

```
Do this instead:
```py
# test add function.
class TestAdd():
  """docstring for TestAdd"""

  def test_add_two_values(self):
    assert add("1,2") == 3

  def test_add_multiple_values(self):
    assert add("1,2,3,4,5,6") == 21
    assert add("2,3,4,5") == 14

# test multiply function.
class TestMultiply():
  """docstring for TestMultiply"""

  def test_multiply_two_values(self):
    assert multiply("1,2") == 2
    assert multiply("3,3") == 9

  def test_multiply_multiple_values(self):
    assert multiply("1,2,4") == 8
    assert multiply("3,5,2") == 30
```

**Javascript example:**

Don't do this:
```js
  describe('Test one', () => {
    it('Should add', () => {
      let sum = add('1, 23, 5');
      expect(sum).toBe(29);
    })
    it('Should multiply', () => {
      let prod = multiply('1, 23');
      expect(prod).toBe(23);
    })
  })
```

Each Function should have it's own describe object_

Do this:
```js
  describe('add()', () => {
    it('Should add', () => {
      let sum = add('1, 23, 5');
      expect(sum).toBe(29);
    })
  })
  describe('multiply()', () => {
    it('Should multiply', () => {
      let prod = multiply('1, 23');
      expect(prod).toBe(23);
    })
  })
```
---
- Javascript: Test strings are there to be descriptive:
  - eg: `it("should be able to multiply negative numbers")`


### Some useful Readings
  1. [Common mistakes in TDD](https://cmatskas.com/common-mistakes-in-tdd/)
  2. {{% contentlink "/topics/unit-testing/_index.md" %}}
  3. {{% contentlink "/topics/clean-code/_index.md" %}}
