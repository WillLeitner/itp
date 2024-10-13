# FizzBuzz Assigment
I started working towards the FizzBuzz program by taking the "nested for loop" counting function from last weeks lesson, where the program would count up from 1500 to 2700, but check for the numbers that were divisible by 7 AND 5, and only show those. I changed the range of numbers to count from 1 to 100, then changed the 7 to a 3 to see what would happen. It only showed me multiples of 15, which is when I realized the current statement was using &&, and checking if both were true, not if either were true. I added ```console.log(`FizzBuzz`)``` inside of the function checking if i was divisible by 3 and 5, inthe hopes that every multiple of 15 would be replaced by FizzBuzz. This was not the case. Every multiple of 15 was preceded by a line reading FizzBuzz, but 15, 30, 45, etc. were still shown after (i.e. 13, 14, FizzBuzz, 15, 16). I went back to my code to add the other if statements, checking for numbers that were just divisible by 3 and just divisible by 5, printing Fizz for multiples of 3 and Buzz for multiples of 5. The printed set of numbers now functioned as follows:

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

I now needed to figure out how to replace the numbers. I messed around for a while with setting a different binding whenever a number was divisible by 3 or 5 and telling the program to print whatever value was assigned to "fb" instead of i. This never even remotely worked, either just giving me error messages or counting 1, 2 and then stopping. I went back to the original program where it just put the Fizz and/or Buzz before the number and started again from there. I added an if statement before the ```console.log(`${i}`)``` asking if i was divisible by 2. I set it to only print i if it was a multiple of 2, otherwise the Fizz/Buzz programs can operate as normal. The set of numbers now read as:

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

This is a little closer, kind of. Numbers are now being replaced, but only if they're odd numbers. Even numbers that are divisble by 3 and/or 5 are being completely ignored by the Fizz/Buzz functions. The computer only recognizes them as being divisible by 2 and ignores any other aspect of the number and moves on to the next integer. While this is not what I'm looking for, if the "divisible by 2" check is replaced with a "NOT divisible by 3 and/or 5" this would no longer be a problem, as the two sets of numbers would have nothing in common. I started to experiment with the ! operator. At first I was misundertanding its usage from the class GitHub explaining it. It was written as "! not", so I thought the actual operator was ! not, not just !. My code did not work the first few times I tried it because of this. I then discovered the "!==" from the markdown file from two classes ago. I added a function: ```if (i % 3 !== 0 || i % 5 !== 0) {console.log(`${i}`)}```

This would only replace multiples of 15 with FizzBuzz. I replaced the && with || and everything worked exactly the way it was supposed to.

```javascript
for (let i = 1; i < 101; i++)
{if (i % 3 !== 0 && i % 5 !== 0) {console.log(`${i}`)}
    else if (i % 3 === 0 && i % 5 === 0) {
        console.log('FizzBuzz') } 
    else if (i % 3 === 0) {
        console.log('Fizz') } 
    else if (i % 5 === 0) {
        console.log('Buzz') } };
```


# Pyramid Assignment
This one took a lot longer. I had a TON of trouble with this over the course of the past few days, but with the help of Yorgos I have triumphed. I am the Ancient Egypt of JavaScript. I started simple, creating a parseInt prompt to ask how big the pyramid should be and assign that value to "stacks." I then took from the code from the previous assignment, trying decrease the number by one to identify the width of each line of the pyramid. I messed around for a while trying to get it to work, eventually creating another variable called "width" that equaled "stacks + 1." I had the code only run if stacks was between 1 and 8, then print width - stacks each line, then subtract 1 from stacks so it would progressively count from 1 to whatever was originally placed in stacks. My first roadblock came here, as I needed to figure out how to convert each of these values into that amount of # marks. I created a variable called "unit" that equaled `#`. I went to the console.log command and tried to multiply "unit" by the "width - stacks" value. All that would happen was either an error message for a variety of reasons, or a singular #. I kept trying to change things to fix it but often just made it worse. I didn't really know what was going wrong so I couldn't even look up what was wrong. This was when I decided to email you, as it had already gotten to be pretty late on Sunday night. I reread the textbook to no avail, then scheduled an email for 8am Monday morning. This is when things took a turn for the better :).

Enter Yorgos. You recommended I email him for help, so we set up a 30 minute zoom call for 4:30 and spoke for an hour and 10 minutes. He helped me with both the Pyramid and the Chessboard assignment. The main piece of information that Yorgos shared with me was that each line contains space for 10 characters, so the solution wasn't printing a certain amount of # marks each line, it was printing a certain amount of spaces after. We created a variable set to 1 and a variable set to 9. The variable of 1 would correspond to # marks and the 9 would be spaces. Each time we run the program we would add 1 to the # marks and take 1 away from the spaces until the amount of marks equaled the value given to stacks at the beginning of the sequence. All that was left was adding an else statement, where a value that wasn't between 1 and 8 would result in a statement telling you that you needed to input a number between 1 and 8. Now, everything was perfect!.
```javascript
let stacks = parseInt(prompt("How tall should the pyramid be?"))
let x = 1;
let y = 9;
let a = `#`;
let b = ` `;
if (stacks >= 1 && stacks <= 8) {
    for (let i = 0; i < stacks; i++) {
        console.log(a.repeat(x) + b.repeat(y));
        x++;
        y--; }}
else {console.log(`Number needs to be between 1-8.`); }
```


# Chessboard Assignment
Yorgos also helped me with this! 
This one started off the same way as the pyramid, with a parseInt prompt asking for the width of the chessboard and assigning it to a variable called "size." Then there's a bunch of weird coding stuff that Yorgos told me about. Instead of creating variables for a space and a # mark like last time, we created a variable called x that had nothing in it. It was literally assigned with ``, so give the space for things to be added but to start with nothing in the first place. Then we created two variables, "i" to represent the rows and "j" to represent the columns, and set them in a nested for loop. i was set to 0, and would run its program as long as it was less than the value given to size at the beginning. Each time it would run, i would increase by 1. i's program would run j's program, which had the same regulations on it. j would check if sum of i and j was an even number by adding them together and doing % 2, and asking if that was equal to 0. If the sum was even, it would add a space to x, if it was odd it would add #. After each of these, 1 would be added to j, leading to the function restarting when the amount of figures in the line equaled size. "/n" would be added to x to create a new line, 1 would be added to i, and it would restart. Now the first value was odd, leading to the first figure in the line being a # mark, not a space. This process would continue until i equaled size, and the chessboard would be finished. 
```javascript
let size = parseInt(prompt("What will the size of the chessboard be?"))
let x = ``;
for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        if ((i + j) % 2 === 0) {
            x += ` `; 
            }
            else {
                x += `#`; 
            }
        } x += `\n`; }
console.log(x);
```