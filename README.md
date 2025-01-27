# parachute_pig

![Version](https://badgen.net/badge/version/1.0.0/blue)
![Python](https://badgen.net/badge/python/3.8%2B/blue)
![License](https://badgen.net/badge/license/MIT/green)

Parachute Pig is a Doodle Jump clone that I developed for the final in a Python 
programming class.

This game is a Doodle Jump clone where the player is controlled by the position of 
the mouse cursor. The graphics are create in the turtle module, the random module 
is used to add spontaniety to where the platforms spawn, and the time module is 
used for timing the frames. It was tough to program the collision for the platforms 
because they must be permeable from below, but solid from above. It was also 
difficult to fine-tune the gravity so that the pig icon would fall slower than it 
jumps. I hope to make this project mor graphically impressive. I would also like to 
add a highscore system, multiplayer, and sound effects.

This project uses the libraries:
 - turtle
 - time
 - random

Using the project just requires running it in your IDE of choice with the
correct libraries installed. Once the project is running, it will open the 
game window. Move the mouse to control where the pig moves, and land on platforms 
from above to jump higher and increase your score.

MIT License

Copyright (c) [2024] [Marshall Pigford]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
