import os
import sys
import subprocess

if os.path.exists("dist"):
    os.system("rm -rf dist")
if os.path.exists("build"):
    os.system("rm -rf build")
if os.path.exists("centerer.egg-info"):
    os.system("rm -rf centerer.egg-info")
subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel"], check=True)
subprocess.run(["twine", "upload", "dist/*", "-u", "__token__", "-p", "pypi-AgEIcHlwaS5vcmcCJGY3MzlmYjZhLTcyOGUtNGY4MS05MGUzLTYwMTEyNWJmMzU3OQACKlszLCIwZWMzNDQ0Zi03YzkzLTQwNTYtOTg3MC0wZWYzNjhjYmYyOGIiXQAABiANQWmn_mivKgdpAzxQxNCY9S3n-gvgZgK4L-vl4nHSjg"], check=True)