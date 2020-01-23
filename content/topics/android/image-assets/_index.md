---
title: Working with image assets
ready: true
---

In Android images can be uploaded into the drawables folder that will be packaged along with the apk when it is compiled. These  images are uploaded into your project 
and are referenced through the drawables folder. But it's not just uploading a single image and then you're finished. In Android you have to account for 
various `screen resolutions` to make sure the images don't appear blurry on the top of the range models and that the images aren't so high in quality that it slows down older devices.

# Adding an image to an Android application

[Here](https://www.youtube.com/watch?v=Ab7U7lqikfU) is a video with a simple example of adding an image to the `drawable` folder and then displaying it in an imageview.

# Supporting the various pixel densities

As mentioned above, accounting for multiple screen resolutions plays a role in both `performance` and `overall user experience`.
Luckily though, Android has a simple way to handle this.

You can read more about it in the [documentation](https://developer.android.com/training/multiscreen/screendensities).

# Important Note

When adding image assets to the drawable folder, the names of the images are not allowed to contain `capital letters` or `spaces` between the words.

Example: Adding the following files will provide the following results

Cars.png	//Error
Toyotal Corolla.png	//Error
Cars!.jpg	//Error
cars.jpg	//Pass
toyota_corolla.png	//Pass
