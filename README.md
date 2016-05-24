# AI
<h3>AI using TKinter Turtle GUI [Python]</h3>

<h4>INFO:</h4>
My first attempt at creating an 'AI'. Created in Python, using the TKinter-based 'Turtle' GUI.

<h4>WHAT IT DOES:</h4>
It is giving a value of functions, a generator gives values to those functions.
The 'AI' then generates random numbers, if the number matches any of the functions, it attempts to run that function by discovering working parameters. If that function moves the AI, the AI will increase the 'preference' of that function, later increasing the chance it will run that function again.

<h4>WHAT I PLAN TO DO WITH IT:</h4>
<li>create an 'end goal' for the AI to reach:<br>
    At first static, then after getting that to work, making it move

<b>TO-DO</b>
<li>add end goal for AI
<li>find a way to properly generate string parameters
<li>fix 'parameter-finder' method [done(?)]

<b>ERRORS:</b>
<li>after passing 'None' to a function, every other function is passed 'None'