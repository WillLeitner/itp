# FizzBuzz Assigment
I started working towards the FizzBuzz program by taking the "nested for loop" counting function from last weeks lesson, where the program would count up from 1500 to 2700, but check for the numbers that were divisible by 7 AND 5, and only show those. I changed the range of numbers to count from 1 to 100, then changed the 7 to a 3 to see what would happen. It only showed me multiples of 15, which is when I realized the current statement was using &&, and checking if both were true, not if either were true. I added ```javascript
console.log(`FizzBuzz`)``` inside of the function checking if i was divisible by 3 and 5, inthe hopes that every multiple of 15 would be replaced by FizzBuzz. This was not the case. Every multiple of 15 was preceded by a line reading FizzBuzz, but 15, 30, 45, etc. were still shown after (i.e. 13, 14, FizzBuzz, 15, 16). I went back to my code to add the other if statements, checking for numbers that were just divisible by 3 and just divisible by 5, printing Fizz for multiples of 3 and Buzz for multiples of 5. The printed set of numbers now functioned as follows:

1

2

Fizz

3

4

Buzz

5

Fizz

6

...and so on. 

I now needed to figure out how to replace the numbers. I messed around for a while with setting a different binding whenever a number was divisible by 3 or 5 and telling the program to print whatever value was assigned to "fb" instead of i. This never even remotely worked, either just giving me error messages or counting 1, 2 and then stopping. I went back to the original program where it just put the Fizz and/or Buzz before the number and started again from there. I added an if statement before the ```javascript
console.log(`${i}`)``` asking if i was divisible by 2. I set it to only print i if it was a multiple of 2, otherwise the Fizz/Buzz programs can operate as normal. The set of numbers now read as:

2

Fizz

4

Buzz

6

8

Fizz

10

12

14

FizzBuzz

etc.

This is a little closer, kind of. Numbers are now being replaced, but only if they're odd numbers. Even numbers that are divisble by 3 and/or 5 are being completely ignored by the Fizz/Buzz functions. The computer only recognizes them as being divisible by 2 and ignores any other aspect of the number and moves on to the next integer. While this is not what I'm looking for, if the "divisible by 2" check is replaced with a "NOT divisible by 3 and/or 5" this would no longer be a problem, as the two sets of numbers would have nothing in common. I started to experiment with the ! operator. At first I was misundertanding its usage from the class GitHub explaining it. It was written as "! not", so I thought the actual operator was ! not, not just !. My code did not work the first few times I tried it because of this. I then discovered the "!==" from the markdown file from two classes ago. I added a function: ```javascript
if (i % 3 !== 0 || i % 5 !== 0) {console.log(`${i}`)}
```

This would only replace multiples of 15 with FizzBuzz. I replaced the && with || and everything worked exactly the way it was supposed to.

```javascript
for (let i = 1; i < 101; i++) 
```

```javascript
{if (i % 3 !== 0 && i % 5 !== 0) {console.log(`${i}`)}
    else if (i % 3 === 0 && i % 5 === 0) {
        console.log('FizzBuzz') } 
    else if (i % 3 === 0) {
        console.log('Fizz') } 
    else if (i % 5 === 0) {
        console.log('Buzz') } };
```