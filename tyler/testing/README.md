# Current Status

As of the latest push: 
1) When the main.py file is run within the virtual environment it opens Google Earth, repositions it, starts the opencv window, and outputs commands.

2) When the qt_overlay.py file is run within the virtual environment, it opens a borderless window below the position of the Google Earth window.

### To-Do
1) Find a way to run the Qt window inside of main. Right now, there are problems in this area that need addressing:

   - I don't know if the Qt window can be run as a class instance. It may need to actually run in the main file which might be a problem since it can't be threaded.

   - If Qt has to run in main, it has options for threading within the Qt app that can replace the current threading being used. I don't know how to use these yet.

   - It may be possible to bring a seperate app into PyQt. I don't know for sure and I don't know how it would impact performance. It seems like the way to do this has changed a lot over time (different function names, etc.). As of right now, I think it is called QWidget::createWindowContainer(). 

2) Right now, the program can repeatedly focus the Google Earth window if the comments on Start.set_window() and the set_window() function in main.py and google_earth.py are removed. However, there are a couple of issues:

   - Just focusing Google Earth does not seem to be enough. A click has to be made inside the inner window that contains the globe. Using pyautogui.click() can be problematic because it takes over the mouse and seems to cause some unusual side effects. (If you decide to test this, there is a fail safe to get control back: move your mouse pointer to the corners of the screen)

   - Repeatedly focusing the Google Earth window without any other sort of checks technically works but can cause issues running other windows. It may not be a big deal if everything is run in one go with main. However, this might impact clicking buttons on the Qt window.

3) Qt UI elements still need to be implemented inside the borderless window:
   
   - Icons/Drawings should be added to the window to explain the commands. There should be enough horizontal space for this. I think each instruction can be inside a window (widget) that is a child of the main parent window below Google Earth.
   
   - A start/stop button needs to be added. The functionality shouldn't be too difficult once the Qt window is integrated with the other threads.
