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

1) The Qt window wrapping the opencv video capture doesn't look quite the same as it did before. At the very least, the inner box is cut off but there may be other details I've missed because I don't know the opencv stuff as well.
   - The window is now being resized programatically based on the resolution of the monitor. The roi window will likely need to be resized in the same way.

2) The commands don't seem to be issuing as quickly to the Google Earth window now. This is likely a side effect of the opencv window now running inside the Qt app using the Qt timers.

3) There should be error checking for when the camera is not located. It sends an opencv warning when the camera is not found by index, so we might need to throw an exception based on this warning.
