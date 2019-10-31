---
title: TDD Horrors
ready: true
---

# Common TDD pitfalls.
These are all the most common TDD problems recruits tend to come across, read and make sure you didn't make any of these or any mistakes at all.

- **Write tests**. Recruits in the past have done the mistake of not writing tests for TDD assignments, make sure you avoid this weird mistake. always write tests for your TDD projects.
- No code in your TDD file, This is a repetition of the first point, but it's worth it. write tests people.
- Files naming convention, name your files properly and according to what's inside them. E.g. if you have a file called add.js that only contains a multiply function then something is wrong. Do this:
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

- Defining a test case(testing function) inside a function. That will pass, even when it's supposed to fail.

---
**Python example:**

```py
def testOne():

  def testSomething():
    assert add("1,23,5") == 25

  def testSomething():
    assert add("1,23,5") == 29

```
instead you could put your tests into classes as methods, like so:

```py
class TestOne():

  def testSomething():
    assert add("1,23,5") == 25

  def testSomething():
    assert add("1,23,5") == 29

```
notice **def** keyword in the first cell is replaced with the **class** keyword in the second cell, this difference makes a major difference. The first case would **pass** as a single test, even though it contains two test cases and one of them must fail, in contrary the second case would run both tests, the first one would fail and the second one would pass.
*Note:*
Although it's not necessary to put stuff inside classes. One nice thing about the `pytest` module is that it removes the need for boilerplate code. so the following code would also work:
```py
  from module import add

  # tests start here.
  def test_add_two_values():
    assert add(1,2) == 3

  def test_add_multiple_values():
    assert add(1,2,3,4) == 10
```

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
  - eg:
      Do: `it("should be able to multiply negative numbers")`
      Don't: `it("multiply")`
- Incomplete projects:
  - This is not a very good look for you, to both us, your assessors, and your report. Imagine how an incomplete project looks to an employer. BAD! is the word. If you do not  have tests, for your TDD project, then your project is incomplete.

- TDD tests fail:
  - Failing tests aren't bad during development, but make sure your **all** tests pass when you submit your project.

- Errors/Exceptions:
  - You should always make sure you test for possible errors/exceptions in your code.

- Documentation on how to setup and test the code:
  - Make use of md files, collaborators shouldn't guess/remember how to setup all the dependencies for your project, document all the necessary processes please.

- Clean code base. Need I say more?

  1. Dirty.

    Javascript:

    ```js
      // Testing if the Error Checks throw
      //var sixSided = new Dice(6,[1,"gdfdf"]);
      var sixSided = new Dice(6,[1,6,5,-16]);
      //console.log(sixSided.rollDice());
    ```

    Python:

    ```py
      # I was thinnking about This
      # Then I did this but it didn't work. so I left
      # And then, it came to me, eureka!
      die6 = Dice(6)
      # Since it works, there's no need to clean it.
    ```


  2. Clean.

      Javascript:

      ```js
        var sixSided = new Dice(6,[1,6,5,-16]);
      ```

      Python:

      ```py
        die6 = Dice(6)
      ```

  Remove useless stuff, it serves no purpose. so get rid of it.

- One test: writing one test to test everything is a bad idea, you need to separate it into multiple tests that test one and thing only.





### Some useful Readings
  1. [Common mistakes in TDD](https://cmatskas.com/common-mistakes-in-tdd/)
  2. {{% contentlink "/topics/unit-testing/_index.md" %}}
  3. {{% contentlink "/topics/clean-code/_index.md" %}}
