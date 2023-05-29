# simply run this file. All the dependencies will be installed in a virtual environment named venv
# to exit the virtual environment simply type deactivate in you command prompt or terminal where the
# project directory is open

import subprocess
import os

subprocess.call("cls" if os.name == "nt" else "clear", shell=True)
subprocess.check_call(["pip", "install", "virtualenv"])
subprocess.check_call(["virtualenv", "venv"])
subprocess.check_call(["venv\\Scripts\\activate.bat"])
subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
subprocess.check_call(["deactivate"])
subprocess.call("cls" if os.name == "nt" else "clear", shell=True)
print(
    "You can now run the runserver.py file. It activate the virtual environment and start the FastApi server..."
)
