# Installing Flask Version of Demoroom
* Make sure git is installed (with git bash if using Windows)
* Make sure Python 3 and pip are both installed and up to date.  
* Clone this repository onto your machine
* Navigate to the cloned repository and install a python virtual environment with `python -m venv venv`  
* In Windows envinroment, .flaskenv needs `export`s changed to `set`s. (Not needed for Cygwin-like setup)  
* Start the envinroment with `venv/Scripts/activate` on Windows and `source venv\bin\activate` on Linux/Mac 
* In the venv, run `pip install -r requirements.txt` to download and install all needed packages.  
* Change the filenames of "_config.py" and "_app.config" to "config.py" and "app.config" respectively. 
* Change the entry "ENTER_SECRET_HERE" to a key of your choosing.
* Run `db_reset.sh i` to initiate the database and populate it with demos
* Enter command `flask run` to start a local debug server. The website can be found locally at localhost:5000 

