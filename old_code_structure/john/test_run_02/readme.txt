This is a stand-alone python program that will predict hand gestures and return percentage.

Please read the notes, ESPECIALLY THE LAST ONE.

Notes:

1. Create a special directory and download both the .py and .h5 (which is the deep learning model) files.
2. Create a virtual environment to install needed packages.
3. The required packages are listed in requirements.txt.  Supposedly you can run something like "pip install -r requirements.txt" but I have not tried this.
4. What I did is install all of these in order using "pip3 install --upgrade tensorflow", just as one example, into my virtual environment, which is activated with "source myenv/bin/activate" after creating it with "virtual myenv".
5. There is a line of code in there where you will need to change the setting from 0 to 1 if you are using a different webcam other than your default one.
6. The training model was limited and so you will have mixed results.  It works very well with me so long as I maintain the same background.  Otherwise, it's a little spotty.
7. Hit the 'q' key to quit the program.
8. The training model is too large (192MB) to upload onto GitHub.  Here is a download link to Google Drive: https://drive.google.com/file/d/18oXums8kjOF6iPw9iMwdXVlqqxswEiRm/view?usp=sharing
