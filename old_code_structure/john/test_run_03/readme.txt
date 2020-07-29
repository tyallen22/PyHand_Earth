This version is a stand-alone file that embeds an OpenCV window, together with
the TensorFlow training model.  Not included is the PyAutoGui manipulation
feature. It is still in a very rudimentary form.  Note that the Start button at
the bottom of the screen will pause/restart the image capturing.

You must include the .h5 Keras training model fil in the same directory, as
well as the PyQt helper module interface.py.

Also, you will need to install PyQt into your environment.  I foolishly followed some different advice I found online as to how to do this, none of which seemed to work.  At the end, I believe I just used "pip3 install PyQt5".  You may wish to start with this.  You can read more here:  https://pypi.org/project/PyQt5/

Also, you can download the latest .h5 file, which is too large to upload to GitHub apparently, at this link:  https://drive.google.com/file/d/18oXums8kjOF6iPw9iMwdXVlqqxswEiRm/view?usp=sharing
