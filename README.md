# dinorun
#### A different way to play Chrome's dinosaur game.

## What is it?
A python script that uses opencv and multiple-screenshot module to capture the screen, check for obstructions in an windowed area and emulate keypress.

## How to run?
* clone the github repository
```
git clone https://github.com/svkbaksi/dinorun.git
```
* go into the directory.
```
cd dinorun
```
* Install all dependencies.
```
pip install -r requirements.txt
```
Note : you can also use a virtual environment if you want.
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

## Demo Video
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/0uoFlpgAE3U/0.jpg)](http://www.youtube.com/watch?v=0uoFlpgAE3U)
