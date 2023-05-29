import subprocess
import os

env = "source venv/bin/activate" if os.name != "nt" else "venv\\Scripts\\activate.bat"
subprocess.check_call(env, shell=True)
subprocess.check_call(["uvicorn", "app:main", "--reload"])
