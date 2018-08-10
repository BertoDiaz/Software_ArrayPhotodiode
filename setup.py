"""
Copyright (C) 2018  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

packages = ["functools", "scipy", "sys", "csv", "datetime", "numpy"]
include_files = [r'C:\Python36\DLLs\tcl86t.dll',
                 r'C:\Users\hdiaz\Documents\pyCharm_Projects\software_APortela\view.py',
                 r'C:\Users\hdiaz\Documents\pyCharm_Projects\software_APortela\viewChart.py',
                 r'C:\Users\hdiaz\Documents\pyCharm_Projects\software_APortela\viewCharts.py']
excludes = ['concurrent', 'curses', 'distutils', 'email', 'html', 'http',
            'json', 'lib2to3', 'pydoc_data', 'urllib',
            'xml', 'xmlrpc']

options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files,
        'excludes': excludes,
    },
}

icon = r'S:\Personals\Berto\pythonProjects\Image\ICO\NanoB2AICO.ico'

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="PREDICT Software",
      version="1.0",
      description="It is used to analyze the CSV file with measure of the photodiode array.",
      options=options,
      executables=[Executable("controller.py", base=base, icon=icon)])
