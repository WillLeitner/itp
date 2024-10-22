# PHASE 1
I started with coming up with ideas for my image. I took the graph paper we were given in class and divided it into equal sections so I could come up with a few different ideas. After filling the page with six options, I decided that the little mushroom house I drew was my favorite. it had rectangles and ellipses, required differing colors to properly convey the idea, and still seemed relatively easy. I had some extra time in class, so I started coding.
# PHASE 2
I opened up P5 and started messing with the draw functions. I started with creating the mushroom. I made a rectangle for the base, continuously altering the width and the x coordinate until it was a size that I liked and centered. It took me a bit to realize that it was drawing from left-most edge, not the center, so I'd have to do some simple math to get it to be centered. For example, if I wanted to center a rectangle with a width of 120, I'd have to subtract 120 from 400 to get 280, understand that there would be equal space on either side of the rectangled that added to a sum of 280, find half of 280 and then use that as my x coordinate. I then similarly played around with the large ellipse to yield my desired result of an adequate mushroom. I created another rectangle for the door and a small circle for a doorknob, also by just fiddling around with the values until I was satisfied. I had the same process for the three spots on the head of the mushroom, slightly altering values until I liked the way the image looked. Now I had my end result of a quaint mushroom house. 
# PHASE 3
This phase was pretty simple. I borrowed the code from the Midterm markdown file, just replacing the code used to make the music notes with my mushroom house code. Now I had a function called drawObject that would create a mushroom house to my specifications. I'm almost hesitant to tell you I used the code on Github since it seemed way to simple to just be given to me, but it was there and it saved me a lot of time so I have no regrets!
# PHASE 4
This, understandably, was where the real work came into play. I created a function called drawGrid which would, ideally, draw my grid. I defined it with w for width, since in our square, width would be the same as height. I saw the hint about using a nested for loop, so I went back to my chessboard code for inspiration. I started by logic-ing out the solution, using 5 as my standard width value. I talked through what I needed the numbers to be each time the program would draw my image, knowing that (if the value was 5) the x and y coordinates would have to increase by 80 as needed if I wanted to fill the 400 x 400 canvas. I started off my program by creating another variable called i, equal to 400 divided by whatever w equaled. I then knew that my s value, if w was 5, would need to be .2. An s value of 1 would create a drawing that filled the 400 x 400 space by itself, so .5 would need 2, .25 would need 4, and so on. I let s = 1 divided by w.
Now I started my for loops. I created a for loop that would only run if y was less than 400, with an identical loop for x underneath it. If x was less than 400, it would run drawObject at x, y, s, then add i to x, then repeat until x equaled 400. It would then have to add i to y and start over. I believe this could have worked from the get go, but I had a bunch of syntax errors that I wasn't aware of, leading to me starting over multiple times out of frustration. I changed what variables meant what concepts, at certain points defining separate variables for width and height that would count up by i each time while adding themselves to x and y accordingly. All of my ideas would have worked but I kept getting syntax errors I couldn't understand. For a while I think it was because I had the \\` ` marks around every variable, which I guess meant they didn't actually add the values to x and y when I needed them to? I also had an issue for a while where running the program would cause Chrome to freeze for a second and then give me one of the "This page isn't responding" messages with "wait" and "exit" buttons at the bottom. I was getting really frustrated and my friends and I somehow wound up in really personal conversations about death, family, and body image in the midst of this assignment, so when I finally had a clear head I broke the problem down to its logic again. I went back to the chessboard and tried to apply the code that I understood to a problem that somewhat mirrored it. I realized that my w and h variables can count up by 1 each time and stop when they reach the original d value, not 400, since counting up by 80 until you get to 400 and counting up by 1 until you get to 5 are the same exact thing. This way I could practically copy the nest for loop from the chessboard, just changing the variables around. This also meant that x and y could be defined outside of the loop, just being added to each time, leading to my ultimately very simple solution in the end. When I finished the code and went to test it I was NOT expecting it to work because it seemed too simple, but I haven't noticed any bugs, no matter what number I put in (within reason, obviously. If I put in an egregiously high number it lags a lot and creates some issues but if I wait long enough it WILL create the grid, just at such a small size that it's barely discernible)