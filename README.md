# dinorun
#### A different way to play Chrome's dinosaur game.

## What is it?
A python script that uses opencv and multiple-screenshot module to capture the screen, check for obstructions in an windowed area and emulate keypress.

## How to run?
* Install all dependencies.
```
pip install -r requirements.txt
```
* Start the script.
```
python dinorun.py
```
Note : It is recommended to use sleep command along with script invocation. This will give the required time to setup windows. 
```
sleep 5s; python dinorun.py
``` 
* Start chrome and goto [chrome://dino](chrome://dino).

Note : Chrome should the active tab. Maximise Chrome and enter full screen. The window is caliberated for full screen performance with screen resolution 1366x768.
