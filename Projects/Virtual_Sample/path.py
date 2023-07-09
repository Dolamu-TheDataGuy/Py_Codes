from pathlib import Path
import os

print(str(Path("spam", "bacon", "eggs")))

homefolder = r'C:\Users\Al'
subfolder = 'spam'
print(homefolder + "\\" + subfolder)
print('\\'.join([homefolder, subfolder]))

print(Path.cwd())
os.chdir('/home/dolzy/code_udemy')
print(Path.cwd())

print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

print(Path.cwd().parents[1])

