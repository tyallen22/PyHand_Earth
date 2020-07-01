"""
File handler that downloads the machine learning model from Google Drive
"""
import os.path
import requests

class FileDownload():
    """
    This is a class that downloads an .h5 machine learning model from Google Drive
    if it does not already exist in the current directory

    Attributes:
        url (str) : Static Google Drive url that hosts the .h5 file
        fname (str) : Name of the file being saved
        current_directory (str) : Holds the string value of the current directory
        session : Instantiate Session class from requests
                response : Holds response object returned from HTTP request
        token (str) : Holds response token from Google Drive that is given when downloading
            large files
    """
    def __init__(self):
        """
        Please see help(FileDownload) for more info
        """
        self.url = 'https://drive.google.com/uc?export=download&id=18oXums8kjOF6iPw9iMwdXVlqqxswEiRm'
        self.fname = '/pyearth_cnn_model_200612_1744.h5'
        self.current_directory = ''
        self.session = requests.Session()
        self.response = None
        self.token = None
        self.chunk_size = 32768

    def get_drive_file(self):
        """
        Checks if model already exists in current directory. If it does not exist, downloads the
        model to the current directory.
        """
        # Gets current working directory and appends the target file name to it
        self.current_directory = os.getcwd() + self.fname
        # Checks if the model file already exists in the current directory, returns if so
        if os.path.isfile(self.current_directory):
            return
        # Sends get request to Google Drive and stores response object
        self.response = self.session.get(self.url, stream=True)
        # If the file is large, a download warning is issued by Google Drive. Gets token
        # from this warning and stores it.
        for key, value in self.response.cookies.items():
            if key.startswith('download_warning'):
                token = value
                break
        # If the token exists, uses token to confirm large download.
        if token:
            params = {'confirm' : token}
            self.response = self.session.get(self.url, params=params, stream=True)
        # Opens current directory and saves model to it
        with open(self.current_directory, "wb") as my_file:
            for chunk in self.response.iter_content(self.chunk_size):
                if chunk:
                    my_file.write(chunk)
