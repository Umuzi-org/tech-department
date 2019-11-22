---
title: Ceasar cipher
pre: "<b>1. </b>"
weight: 5
---

## Ceaser cipher

 **What is ceasar cipher?**

> Caesar Cipher: 
Is an earlier encryption technique which is/was used to substitute/shift the current alphabets with alphabet after a number of count.
Is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who apparently used it to communicate with his generals.

 **Example** 

>To pass an encrypted message from one person to another, it is first necessary that both parties have the 'key' for the cipher, so that the sender may encrypt it and the receiver may decrypt it. For the caesar cipher, the key is the number of characters to shift the cipher alphabet.In the example below, text we will encrypt is 'defend the east wall of the castle', with a shift (key) of 1.
```
plaintext:  defend the east wall of the castle
ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf
```

>It is easy to see how each character in the plaintext is shifted up the alphabet. Decryption is just as easy, by using an offset of -1.
```
plain:  abcdefghijklmnopqrstuvwxyz
cipher: bcdefghijklmnopqrstuvwxyza
```

**TASK**

**1.**
write a function that takes in a string and number arguments and shifts each and every alphabet of the given string by/to [n] steps after the  character

```js
//javascript
function ceasarCipher(string,n) =>

Expected output =ipmnel

example 
calling function ceasarCipher("fmjkbi",3) must return output like Below
The Expected output =ipmnel
Note Be: notice that every character from given String is shifted to three positions/ steps ahead
```

```py
#py

def ceasarCipher(string,n):

Expected output = ipmnel

example 
calling method ceasarCipher("fmjkbi",3): must return output like Below
The Expected output = ipmnel
Note Be: notice that every character from given String is shifted to three positions/ steps ahead

```