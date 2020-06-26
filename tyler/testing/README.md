# Current Status

As of the latest push:

There are now two different versions:

1) Old Version (Two seperate .py files need to be run in different command terminals)

   - When the main.py file is run within the virtual environment it opens Google Earth, repositions it, starts the opencv window, and outputs commands.
   
   - When the qt_overlay.py file is run within the virtual environment, it opens a borderless window below the position of the Google Earth window.

2) New Version (One main .py file runs everything in a Qt app)

   - When main_qt.py runs, it starts a Qt application, opens Google Earth, and opens a Qt window below Google Earth with 6 hand gestures and a start and stop button

### To-Do
1) The Qt app has to be run in main, so here is what's left:

   - Since Qt has to run in main, there are multiple options for threading within the Qt app that can replace the current threading being used in main.py. QThreadPool, QRunnable, QThread, and QObject are what I'm looking at here. The regular Python Thread class can also be used but I haven't looked into this yet.
   
   - With everything inside a Qt app, it seems to want the opencv window to be rendered with PyQt. I don't know if this absolutely required but it is throwing a lot of errors for me. Here is a couple of things I found on this, so I think it should be possible to convert the window to PyQt:
     - https://iosoft.blog/2019/07/31/rpi-camera-display-pyqt-opencv/
     
     - https://stackoverflow.com/questions/44404349/pyqt-showing-video-stream-from-opencv

2) Qt UI elements still needing to be implemented:
   
   - Start/stop button needs to be functional. The functionality shouldn't be too difficult once the Qt window is integrated with the other threads.
