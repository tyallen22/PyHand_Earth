
<a  href="https://pypi.org/project/PyHand-Earth"><img  src="https://i.ibb.co/X8KY0Ry/TopImg.png"  title="# PyHand-Earth"  alt="# PyHand-Earth"></a>
  

# PyHand-Earth 

  

>Welcome to <i>PyHand-Earth</i>!


  

## Contents 

 -  [Overview](#overview)
 -  [Special Comments](#comments)
 -  [Installation](#installation)
 -  [Start](#start)
 -  [Usage](#usage)
 -  [Team](#team)
 -  [License](#license)

---
  

## Project Description and Overview

PyHand-Earth is a Python-based software project that incorporates and integrates multiple high-performant concepts, libraries, tools, and techniques to optimize and maximize user experience in navigating the Google Earth Pro Desktop application relying only on simple hand gestures and an ordinary Webcam.

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

### Preliminary Matters

This project's installation package, and its dependencies, is hosted on PyPI at:

https://pypi.org/project/PyHand-Earth/


#### General Requirements

- Linux machine with Webcam
- Compatible with Ubuntu 20.04 installation
- Python 3.8 or higher 

#### Third-party pip installed library packages are included in setup.py as part of PyHand-Earth package install:

- TensorFlow 2.2.0
- OpenCV 4.2.0.34
- matplotlib 3.2.2
- Keras 2.4.2
- pyautogui 0.9.50
- PyQt5
- psutil 5.7.0

#### Required dependencies that will be apt-get installed with setup.py as part of PyHand-Earth package install:

Although the libraries listed above that provide high-performant optimization all can be pip installed, there are unavoidable dependencies that must be apt-get installed in order for these libraries to coexist.  (Prior approvals have been obtained from J.B.).  Although the process is automated with the setup instructions given in the next section below entitled <b>Installation</b>, to provide the user with advance notice of their installation, these apt-get dependencies are individually listed as follows:

- `apt-get install python3-tk`		(needed for pip installed pyautogui)
- `apt-get install libxcb-xinerama0`	(required in order to start PyQt, which is pip installed)
- `apt-get install wmctrl`		(necessary to be able to manage certain windows)
- `apt-get install scrot`		(needed in order to locate images in the Google Earth application to ensure it behaves properly)


### PyHand-Earth pip installation package name

As documented at the PyPI repository page for PyHand-Earth, the entire software package can be installed from the command-line with the following pip installation:

```shell
$ pip3 install PyHand-Earth==0.2.24
```
Except as mentioned further below, this will install all the Python code developed for the project, third-party optimization libraries, and other required dependencies, as discussed above.


### Executable command to run PyHand-Earth

From the command line, simply run the following to execute the PyHand-Earth program:

```shell
$ PyHand-Earth
```

OR

alternatively, you may navigate to the appropriate directory where the `site-packages` were installed, and run:

```shell
$ python3 main_qt.py
```

If you used a virtual environment to `pip3 install PyHand-Earth`, this directory may look something like

```shell
/home/username/Projects/myvirtualenv/lib/python3.8/site-packages/PyHand_Earth
```
As previously stated above, if you do not have the Google Earth Pro desktop application already installed on your local machine, the first time you run `PyHand-Earth`, the program will install the .deb package for Google Earth Pro.  In addition, it automatically will download from a google drive link a Keras .h5 file where the training model for the hand gesture recognition neural network is stored.



## User Guide

### Initial view	
<img  src="https://i.ibb.co/k9MZSFp/two.png"  title="# PyHand-Earth"  alt="# PyHand-Earth"></a>

After launching the Py-Earth program, the user's initial view consists of the top portion of the display being filled by Google Earth and a smaller area at the bottom of the display featuring a pictoral index of eight hand gestures and three user buttons.

The eight hand gestures and their corresponding navigation motions on Google Earth are as follows:

| Hand Gesture		| Navigation Motion |
| --------------------- |:-----------------:|
| Index finger up	| Move Up	    |
| Peace sign      	| Move Down    	    |
| Left thumb extended	| Move Left    	    |

- The display should be filled with two areas:

	- Google Earth Pro: Targeted window to control with hand gestures
	
	- Gestures and buttons area : Demonstrating different possible gestures and buttons to start the OpenCV window video, Stop it and Exit the program which closes all the windows. 
	


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

### Project team members:
- Grant H. Wise
- Tyler Allen
- Vanessa Orantes Murillo
- John Liu
- Ying Xu
 
---


## GitHub Repository

This README.md file and all other files and source code is located at the following GitHub Repository:

https://github.com/liujohnj/PyHand_Earth

Access has been furnished to J.B., N.S., and J.C.



## License

  

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

  

-  **[MIT license](http://opensource.org/licenses/mit-license.php)**

- Copyright 2020 © 
