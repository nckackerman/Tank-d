import sys
from cx_Freeze import setup, Executable

setup(
    name = "Tank'd",
    version = "1",
    description = "Geometry Wars Clone in Python and Pygame. Contact: ncackerman@wisc.edu",
    executables = [Executable("Tank'd.py", base = "Win32GUI", icon = "windowsIcon.ico")])