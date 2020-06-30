# Current Status

As of the latest push:

There are two different versions:

1) Old Version (Two seperate .py files need to be run in different command terminals)

   - When the main.py file is run within the virtual environment it opens Google Earth, repositions it, starts the opencv window, and outputs commands.
   
   - When the qt_overlay.py file is run within the virtual environment, it opens a borderless window below the position of the Google Earth window.

2) New Version (One main .py file runs everything in a Qt app)

   - When main_qt.py runs, it starts a Qt application, opens Google Earth, and opens a Qt window below Google Earth with 6 hand gestures, a start and stop button, and an exit button
   
   - When start is pressed, it opens a Qt window with the opencv window inside of it. The commands from this window are recognized and sent as outputs to the Google Earth window
   
   - When stop is pressed, it freezes the Qt opencv window video feed on the last captured frame and stops sending commands to the Google Earth window
   
   - When start is pressed again, video processing resumes and commands start being sent to the Google Earth window again
   
   - When exit is pressed, all windows close and program terminates

### To-Do

1) **Please test out the gesture recognition in the Qt opencv window, especially if you are more familiar with the opencv/image recognition stuff.** The Qt opencv window and the corresponding ROI frame are now resized based on monitor resolution. I don't know if this impacted the accuracy of the hand recognition.

2) **Please look at the positioning of all three windows on your monitors.** All three windows now resize and position themselves based on monitor resolution. They look reasonable on my 2560x1440 and 1920x1080 monitors but further testing is needed.

   - The Google Earth window should be in the middle of the screen 
   
   - The gesture icon window should be flush below the Google Earth window with the same width 
   
   - The opencv window should be in the top right next to the Google Earth window and should be a reasonable size for your monitor (not massive, not too tiny, clearly visible)

3) There should be error checking for when the camera is not located. It sends an opencv warning when the camera is not found by index, so we might need to throw an exception based on this warning.
