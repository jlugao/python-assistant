from git import Repo
from tempfile import TemporaryDirectory
import os
import subprocess

with TemporaryDirectory() as tmpdirname:
    repo = Repo.clone_from("https://github.com/blurg/sauron-engine", tmpdirname)
    regular_dir = os.getcwd()
    os.chdir(tmpdirname)
    result = subprocess.run(["ruff", ".", "--format", "json"], capture_output=True)
    os.chdir(regular_dir)
    with open("result.json", "w") as result_file:
        result_file.write(result.stdout.decode("utf-8"))
