import subprocess

subprocess.check_call(["venv\\Scripts\\activate"])
subprocess.check_call(["uvicorn", "app:main", "--reload"])
