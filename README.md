
<a  href="https://pypi.org/project/PyHand-Earth"><img  src="https://i.ibb.co/X8KY0Ry/TopImg.png"  title="# PyHand-Earth"  alt="# PyHand-Earth"></a>
  

# PyHand-Earth 

  

>Welcome to <i>PyHand Earth</i>!


  

## Table of Contents 

 -  [Overview](#overview)
 -  [Special Comments](#comments)
 -  [Installation](#installation)
 -  [Start](#start)
 -  [Usage](#usage)
 -  [Team](#team)
 -  [License](#license)

---
  

## Overview

PyHand Earth is a Python-based software project that incorporates and integrates multiple high-performant concepts, libraries, tools, and techniques to optimize and maximize user experience in navigating the Google Earth Pro Desktop application relying only on simple hand gestures and an ordinary Webcam.

As a programming language, Python owes much of its popularity to its predilection for rapid deployment and to the ever-growing ecosystem of third-party open-source libraries and tools that add scalability, thereby freeing up precious time to more directly focus energies on solving the problems around us.  Yet, that type of flexibility comes with a price - which is paid in the currency of performance.  However, there is no shortage of high-performant tools and libraries that leverage all that Python has to offer with the inherent speed of these optimized solutions, many of which are written in high-performing languages such as C++.

Despite advances in computer vision and deep learning neural networks, there are not many open-source software deployments that advance hand-gesture recognition in any appreciable direction towards the kinds of user interfaces depicted in movies such as those in the Marvel universe ... think Tony Stark navigating a holographic interface.  Those that do exist seem to require the use of special hardware that includes depth sensors (e.g., Microsoft's Xbox Kinect and ultraleap's Leap Motion controllers).

This project serves as an attempt to take a first step towards user interfaces of the future but without such specialized hardware.


## Special Comments

For a smooth experience, users should review the following special comments, which include important instructions, tips, and suggestions.

- This project is designed to run on a dedicated Linux (Ubuntu 20.04) machine.  Because of certain limitations that are inherent with Virtual Boxes and Microsoft's Windows Subsystem for Linux (WSL), Webcams cannot be counted on to reliably operate on these substitute platforms.
- During the setup installation, multiple libraries upon which the program is dependendent will be downloaded, and so please be a little patient during this process.
- As noted further below, due to dependencies that are required in order for the principal pip installed libraries to <i>play nice together</i>, certain other libraries will need to be apt-get installed (as previously cleared by J.B.).
- This package requires Google Earth Pro desktop to be installed on the local machine.  If it is not already installed, the Google Earth Pro application automatically will be installed the first time you run the program.  A relatively large neural network learning model .h5 file also will be downloaded.  Consequently, please make allowances the first time you run the program.
- This project requires many other pip3 installed high-performant libraries to work in unison, which due to all the threading involved, was not the easiest task to accomplish.  Therefore, please also be patient while these libraries load and initialize.  Whereas some projects may require only one or two such libraries, this one incorporates TensorFlow/Keras, OpenCV, PyQt, maplotlib, and numpy, among others.  Consequently, it may take a few seconds for the user interface to fully load, and for certain video windows to open and close.
- Because of the inherent physical limitations of an ordinary Webcam, the hand gesture prediction will work most accurately when a blank, light-colored (e.g., white or cream) wall is positioned behind the user.
- There are eight available hand gestures to control navigation in Google Earth.  For a smoother experience, a few moments should be taken to familiarize yourself with these different gestures.  These gestures, together with their corresponding navigation motions, will be displayed once the program runs.
- When starting gesture navigation, the user's hand should be positioned so that it fills a good portion of the orange bounding rectangle in the live video window once it opens.
- In the event the prediction gets stuck on the wrong gesture, merely shake your hand a little and let it reset until the desired motion is achieved.  The learning model is based on over 26,000 images, but the limitation of ordinary Webcams, when coupled with varied lighting, and backgrounds, and skin tones, can sometimes result in incorrect predictions, which easily can be reset as described.
- If you remove your hand completely such that only a blank wall occupies the orange bounding rectangle, all navigation and motion should halt.
- In case you need a refresher on the above, the program includes a "Gesture Navigation Tips" button that will display the most important tips.
- For academic purposes (as discussed in advance with J.B.), the live video window also contains text displaying the deep learning model's prediction values for each of the available eight hand gestures, as well as that for a blank wall.  (A future, non-academic, deployment instead will just display the controlling navigation motion in order to simplify the user's experience.)
- The GitHub repository root folder (under `master` branch) includes two sub-folders:
  - `new_main`:  Contains the most up-to-date files.
  - `old_code_structure`:  Archived files.
- A PDF file detailing contributions made outside of GitHub to this project is included in the `master` branch of the root folder.


## Installation

 ### Requirements

- Python 3.8 or higher 
- Compatible with Ubuntu 20.04


### Dependencies needed:

- Google Earth desktop (will be installed automatically the first time the program is run if it is not already present in the environment)
- apt-get dependencies required to make pip installed packages work together 

```shell
$ sudo apt-get install python3-tk
```

Needed for pip installed pyautogui

```shell
$ sudo apt-get install libxcb-xinerama0
```
Required in order to start PyQt, which is pip installed

```shell
$ sudo apt-get install wmctrl
```
Necessary for us to manage certain windows

```shell
$ sudo apt-get install scrot
```
needed in order to locate images in the Google Earth application so that we can make sure it behaves properly

### Setup

  - This section will include all the `code` necessary to get  PyHand-Earth going
  
  #### Requirements: 
  
- TensorFlow 2.2.0
- OpenCV 4.2.0.34
- matplotlib 3.2.2
- Keras 2.4.2
- pyautogui 0.9.50
- PyQt5
- psutil 5.7.0



> install all the requirements for PyHand-Earth from a terminal command line with:

```shell

$ pip3 install PyHand-Earth==0.2.24

```



## Start 


#### To launch PyHand-Earth:

From the command line, run:


```shell

$ PyHand-Earth

```

OR

navigate to ....... and run:

```shell

$ python3 main_qt.py
```

- The display should be filled with two areas:

	- Google Earth Pro: Targeted window to control with hand gestures
	
	- Gestures and buttons area : Demonstrating different possible gestures and buttons to start the OpenCV window video, Stop it and Exit the program which closes all the windows. 
	
### Initial view	
<img  src="https://i.ibb.co/k9MZSFp/two.png"  title="# PyHand-Earth"  alt="# PyHand-Earth"></a>

### Starting VIdeo

<img  src="https://i.ibb.co/X8KY0Ry/TopImg.png"  title="# PyHand-Earth"  alt="# PyHand-Earth"></a>


## Usage 

 
- This section will go over all menu buttons and functionalities.

### DISCLAIMER: Optimization of both of the programs has to be improved in order to make Google Earth more responsive. Model must be further developed to improve accuracy. 

 ### Buttons
<img  src="https://i.ibb.co/JqjgZPP/menu.png"  title="# PyHand-Earth"  alt="# PyHand-Earth"></a>

### DISCLAIMER: These are only preliminary hand gestures to demonstrate something in ... something out

 #### To Start Video:

![](https://s7.gifyu.com/images/start05a813aea53fe405.gif)

 #### To Stop Video:

![](https://s7.gifyu.com/images/stop6ee4ca56ae58c6da.gif)


  #### To Exit the Program:
 
![](https://s7.gifyu.com/images/end3dbe56bddb5bedae.gif)

---

  

## Team


- The PyHandlers team was formed for "CIS4930 - Performant Python Programming" from the University of Florida.

### Formed by:
- Grant H. Wise
- Tyler Allen
- Vanessa Orantes Murillo
- John Liu
- Ying Xu
 
---
  

## License

  

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

  

-  **[MIT license](http://opensource.org/licenses/mit-license.php)**

- Copyright 2020 © 
