---
title: JS code review May 2019
---

## Use the git

From the command line. Seriously. For all further projects forever.

The next person who gives us a drag and drop upload will be shamed with a bell.

## Take pride in your work

There are some pieces of feedback that were given before that were not incorporated into your code. It makes the review process a pain in the neck because I like to keep my code review comments DRY.

To learn as much as you can from this feedback:

- make your work excellent
- don't copy from tutorials you found on the internet, make sure you know how to make it work yourself

You are here to learn. So learn.

Learn your technical skills and learn to produce like a professional

- your code should work
- if there is a front-end it should not be a complete mess. A lot of the time we don't need something beautiful. But don't give us something un-usable
- and did I mention git?

## Obvious comments

Obvious comments shouldn't be left in the code. It just means there is more stuff to read, it doesn't add value:

```
    /**
     * this contructor initialises variables and the variables are called by functions below
     */
    constructor(totalTime, cards)
    {<!--  -->
```

Ideally:

- code should be self-documenting. Meaning, your code should be so obvious that comments aren't even necessary
- if comments are required then that is OK, but don't say obvious things.

```
    /**
     * this contructor does constructor like things in order to allow my code to execute in an object orientated manner.
     */
    constructor(totalTime, cards)
    {
```

## Mixing UI and data

This is a common thing that happens a lot. Should have spoken about it more before but...

Think about your project as a number of layers. You have a data and logic layer, this holds information about...information. It doesn't care about HTML. It doesn't KNOW about HTML.

Then there is the UI layer stuff. It generates DOM elements from the data. And it triggers data-layer functionality based on DOM events.

You'll get to play with this concept more soon.

Things to know about: Loose coupling

## Labelling your code with your name isn't necessary. We have Git

```
/** Michael: codeblock ends**/

//_________________________________________This is where Wandile's Edits starts__________________________________________________
```

Git can tell us the exact commit that made the change on every line of code. So we have all the info we can eat.

## Don't leave junk lying around

Usually it's bad to leave stuff like this in your codebase:

```
  //  var getSection = document.getElementById("memory-game");
  // getSection.parentNode.removeChild(getSection);
```

## Looooong comments

```
    let nums = createArray(),
        ranNums = [],
        i = nums.length,
        j = 0;

    /*
    the array nums will be shuffled and saved into
    array ranNums in their random order.
    The values of ranNums will be used as the index
    for the array of cards to randomly sort them
    when they are shuffled.
    * */
```

These tend to get out of date. It's better to just have self-documenting code.

## Functions should be short and have one purpose

Let's take a moment to appreciate

```
function loadCards()
{
  //  var getSection = document.getElementById("memory-game");
 // getSection.parentNode.removeChild(getSection);

        /**Michael: added the array created dynamically with users input**/
        let nums = createArray(),
        ranNums = [],
        i = nums.length,
        j = 0;

    /*
    the array nums will be shuffled and saved into
    array ranNums in their random order.
    The values of ranNums will be used as the index
    for the array of cards to randomly sort them
    when they are shuffled.
    * */

    /*******   ranNums   *******/
    while (i--)
    {
        j = Math.floor(Math.random() * (i+1));
        ranNums.push(nums[j]);
        nums.splice(j,1);
    };

    /*
    Create an HTML section and add the class
    memory-game to section.
    * */

    /*******   section   *******/
    let section = document.createElement("section");
    section.classList.add("memory-game");


    /*
    store the filenames of all the images that will
    be used in the game in an array.
    **/

    let cards = ["img/U_black.png", "img/U_black.png", "img/M.jpeg", "img/M.jpeg", "img/U_orange.jpeg",
        "img/U_orange.jpeg", "img/Z.jpg", "img/Z.jpg", "img/I.jpeg", "img/I.jpeg", "img/umuzi.png", "img/umuzi.png"];
    console.log("WE're about to go in...");

    /**Michael: set card length to the value of the users input.**/
    cards.length = userLevel;

    /*
    for-loop to load and shuffle cards.
    **/
    for (let index = 0; index < cards.length; index++)
    {
        /** create a div then add to the div; a class named memory-card as well as a dataset of the card's filename **/
        let cardDiv = document.createElement('div');
        cardDiv.classList.add("memory-card");
        cardDiv.dataset.card = cards[ranNums[index]];

        /** create an image tag then add to the tag a class named front and the source of the image **/
        let frontImage = document.createElement("img");
        frontImage.classList.add("front");
        frontImage.src = cards[ranNums[index]];
        /** make the image tag as a child of the div **/
        cardDiv.appendChild(frontImage);

        /** create an image tag then add to the tag a class named back and the source of the image **/
        let backImage = document.createElement("img");
        backImage.classList.add("back");
        backImage.src = "img/umuzi_logo.png";
        /** make the image tag as a child of the div **/
        cardDiv.appendChild(backImage);

        /** make the meomry-card div a child of the memory-game div **/
        section.appendChild(cardDiv);
    }

    /** once all cards have been loaded, add div memory-game a child of section **/
    document.body.appendChild(section);
    console.log(cards);

    cardSelector()

    var sectionId = document.getElementsByTagName("section")[0].setAttribute("id", "memory-game");
};
```

If you try to explain the low level functionality of a functions and you end up saying: "it does x, and it does y, and it does z, but only if q, until the condition w". Stop. Just stop.

## Pay attention to naming conventions even when naming files and directories

```
Bk.js ?
```

## If working with web, make sure your slashes are in the right direction:

```
const cardPack = ["img\\a.jpg.jpg", "img\\a.jpg.jpg", "img\\body.jpg.jpg",
                  "img\\body.jpg.jpg", "img\\br.jpg.jpg", "img\\br.jpg.jpg",
                  "img\\Class.jpg.jpg", "img\\Class.jpg.jpg", "img\\em.jpg.jpg",
                  "img\\em.jpg.jpg", "img\\html.jpg.jpg", "img\\html.jpg.jpg"]
```

This game only works on windows. Seriously, what URL looks\like\this?

## funky indenting

```
function loadGame(selection) {

        if (document.getElementById('gameDisplay').hasChildNodes())
        {
          document.getElementById("gameDisplay").removeChild(gameDisplay.childNodes[0]);
        }

  //The arrays that store all the URLs to picks and the dataset names
  const cardPack = [...stuff
        for (var i = 0; i < selection * 2; i++) {

```

```
inconsistent indenting
   is
      hard to
 follow
                        JUST USE PRETTIER   (demo with Bk.js)
```

## caPitalisatopn Matters

```
 	var Section = document.createElement('section')
```

Be consistent. It makes your code easier to work with.

## names should be meaningful

Can anyone guess what this means?

```
function IncreaseCards(selection) {
```

Do they get bigger? Does the number of cards increase? None of the above.

Call a hammer a hammer. Call a nail a nail. Etc

## One git repo one project

Don't put arbitrary things that have nothing to do with each other in the same repo. What does a memory game have to do with bowling?

## If it walks like a loop and quacks like a loop, try using a loop

```
    frame1.innerHTML = game.frameScore['1']
    frame2.innerHTML = game.frameScore['2']
    frame3.innerHTML = game.frameScore['3']
    frame4.innerHTML = game.frameScore['4']
    frame5.innerHTML = game.frameScore['5']
    frame6.innerHTML = game.frameScore['6']
    frame7.innerHTML = game.frameScore['7']
    frame8.innerHTML = game.frameScore['8']
    frame9.innerHTML = game.frameScore['9']
    frame10.innerHTML = game.frameScore['10']
```

```
frames = [frame1,frame2, etc]
then loop...
```

## there are still memory games that are js embedded in HTML

Take some pride in your work. You are here to learn. Pursue excellence.

## Flat is better than nested

```
			} else {
				function flip2Back(){
				    var tile_1 = document.getElementById(memory_tile_ids[0]);
				    var tile_2 = document.getElementById(memory_tile_ids[1]);
				    tile_1.style.background = 'url(tile_bg.jpg) no-repeat';
            	    tile_1.innerHTML = "";
				    tile_2.style.background = 'url(tile_bg.jpg) no-repeat';
            	    tile_2.innerHTML = "";
				    memory_values = [];
            	    memory_tile_ids = [];
				}
				setTimeout(flip2Back, 700);
			}
```

The technical term for this kind of thing is: ugly

## Initialise arrays the simple way

```
var cards = [];
...
cards[22]="images/JPEG/10S.jpg";
cards[23]="images/JPEG/10S.jpg";
cards[24]="images/JPEG/2S.jpg";
cards[25]="images/JPEG/2S.jpg";
cards[27]="images/JPEG/JS.jpg";
cards[27]="images/JPEG/JS.jpg";
cards[28]="images/JPEG/KD.jpg";
cards[29]="images/JPEG/KD.jpg";
cards[30]="images/JPEG/JD.jpg";
cards[31]="images/JPEG/JD.jpg";
cards[32]="images/JPEG/QD.jpg";
cards[33]="images/JPEG/QD.jpg";
... even more stuff
```

I made a typo above, can you see it?

## Comments should be useful for the next person reading the code

```
//To randomise the positions of the cards on the board  --> Learnt this syntax on ES6(Call right after creating function)
```

Sometimes if you are doing something novel it is good to talk about it a bit, something I often do in my code is:

```
// the following is based on https://something.cool/I/found
complicated_code_begins_here()
```

## Loose coupling

- https://stackoverflow.com/questions/226977/what-is-loose-coupling-please-provide-examples

- https://medium.com/clarityhub/low-coupling-high-cohesion-3610e35ac4a6

- SOLID: https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design

## Model-view

One way to make complicated logic easier to test and understand and more portable is to have a clear separation of concerns. Think of it as a bunch of layers.

Create a bunch of code that is all about describing data. This is frontend-agnostic. Then have a visual layer that ties into that and makes your data visible and accessible.

This is an example of loose-coupling

## TDD specific

- your tests should be small and specific. Gigantic tests should not

## some code just isn't self documenting. In these cases add documentation

Eg:
```
    scores(){
        this.updateTotals();
        if (this.firstRoll[this.index] && this.firstRoll[this.index].innerHTML == 10)
            this.secondRoll[this.index].innerHTML = 0;

        if (this.firstRoll[this.index] && this.index < 9){
            //one strike
            if (this.firstRoll[this.index - 1] && this.firstRoll[this.index - 1].innerHTML == 10)
                this.frameScore[this.index - 1].innerHTML = Number(this.firstRoll[this.index - 1].innerHTML) + Number(this.firstRoll[this.index].innerHTML) + Number(this.secondRoll[this.index].innerHTML);
            //two strikes
            if ((this.firstRoll[this.index - 2] && this.firstRoll[this.index - 2].innerHTML == 10) && (this.firstRoll[this.index - 1].innerHTML == 10))
                this.frameScore[this.index - 2].innerHTML = Number(this.firstRoll[this.index - 2].innerHTML) + Number(this.firstRoll[this.index - 1].innerHTML) + Number(this.firstRoll[this.index].innerHTML);
            //three strikes
            if (this.firstRoll[this.index - 2] && this.firstRoll[this.index - 2].innerHTML == 10 && this.firstRoll[this.index - 1].innerHTML == 10 && this.firstRoll[this.index].innerHTML == 10)
                this.frameScore[this.index - 2].innerHTML = Number(this.firstRoll[this.index - 2].innerHTML) + Number(this.firstRoll[this.index - 1].innerHTML) + Number(this.firstRoll[this.index].innerHTML);
            //spare
            if (this.firstRoll[this.index - 1] && Number(this.firstRoll[this.index - 1].innerHTML) != 10 && (Number(this.firstRoll[this.index - 1].innerHTML) + Number(this.secondRoll[this.index - 1].innerHTML) == 10))
                this.frameScore[this.index - 1].innerHTML = Number(this.firstRoll[this.index - 1].innerHTML) + Number(this.secondRoll[this.index - 1].innerHTML) + Number(this.firstRoll[this.index].innerHTML);
            this.frameScore[this.index].innerHTML = Number(this.firstRoll[this.index].innerHTML) + Number(this.secondRoll[this.index].innerHTML);
            this.totalScore[0].innerHTML = Number(this.frameScore[0].innerHTML);

            if (this.index >= 1)
                this.updateTotals();
        } else if (this.index == 9) {
          this.secondRoll[9].innerHTML = Math.floor(Math.random() * this.pins + 1);
          this.thirdRoll[0].innerHTML = Math.floor(Math.random() * this.pins + 1);
        }
    }
```

I shouldn't have to read the body of the function to know what it does. The name and optional documentation should be enough. What would be a better name for this function?

## Your tests are not your application

Don't put the specrunner in your index.html file. Imagine you are building this for a client. They care about bowling. You care about doing a good job. The test runner and test results are not client-facing.

## Play by the rules

If this is a TDD project then do it in a test driven way. There are big parts of many people's codebases without tests at all. Eg: if the manner in which players take turns in the game has some complexity, maybe it would be good to test the logic that chooses whose turn it is?

Untested code is a form of technical debt.

Also, we give you these exercises for a reason. If we are playing chess then the easiest way to win might be to drop-kick your opponent but that's not the point. If you have a TDD assignment then figure out how you can use your tests to inform the structure of your code, and figure out how to write testable code.

## HTML in JS

Try make it tidy at least. Use one notation at a time. Care about indentation and readability.

```
document.getElementById("currentNext").innerHTML =
        `<strong>Round: </strong> ${Player.list[showPlayer].round - Player.list[showPlayer].numOfStrikes + 1}  Throw#: ${Player.list[showPlayer].throw+1}` +
        "<div id='" + Player.list[showPlayer].name + "'><strong>Current Player: </strong>" + Player.list[showPlayer].name + " - " +
        Player.list[showPlayer]. totalScore + " points" +
        "<br><strong>Next Player: </strong>" + Player.list[nextPlayer].name +
        " - " + Player.list[nextPlayer]. totalScore + " points</div>";
```

## A cool example of separating concerns

This function is all about drawing a picture of some details. It is in no way concerned with calculating those details. It just shows them. This function does only one thing, and it does that one thing well.

```
function showDetails(player) {
    console.log("Show details for " + Player.list[player -1].name);
    document.getElementById("showDetails").innerHTML =
        "<strong>Player Name: </strong>" + Player.list[player - 1].name +
        "<br><strong>Points: </strong>" + Player.list[player - 1].totalScore +
        "<br><strong>Position: </strong>" + Player.list[player - 1].pos +
        "<br><strong>scores: </strong> [" + Player.list[player - 1].score + "]";
}
```

(Nice one Axel)

This idea is at the core of modern js frontend frameworks. Exciting things are on the horizon for you guys.

## names people

```
function getPos() {
```

FTW?


## ok this is just a bit strange

```
  this.addPlayer = (playerName = new Player()) => {
    this.players.push(playerName);
  }
```

What is playerName suposed to be here. A string or an object?
