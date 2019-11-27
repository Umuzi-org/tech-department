---
title: Ceasar cipher

weight: 5
---


 **What is ceasar cipher?**

> Caesar Cipher: 

> Is a type of substitution cipher  [encryption](https://en.wikipedia.org/wiki/Encryption) in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who apparently used it to communicate with his generals.

 **Example** 

>To pass an encrypted message from one person to another, it is first necessary that both parties have the 'key' for the cipher, so that the sender may encrypt it and the receiver may decrypt it. For the caesar cipher, the key is the number of characters to shift the cipher alphabet.In the example below, text we will encrypt is 'defend the east wall of the castle', with a shift (key) of 1.

**Input**

```
plaintext:  defend the east wall of the castle
```

**Output**

```
ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf
```

**TASK**

**1.**
write a function that takes in a string and number arguments and shifts each and every alphabet of the given string by/to [n] steps after the  character

```js
//javascript
function ceasarCipher(string,n) =>
```
**Input**
```js
ceasarCipher("fmjkbi",3)
```
**Output**
```
Expected output =ipmnel
```

>calling function ceasarCipher("fmjkbi",3) must return output like Below

>The Expected output =ipmnel

>Note Be: notice that every character from given String is shifted to three positions/ steps ahead

