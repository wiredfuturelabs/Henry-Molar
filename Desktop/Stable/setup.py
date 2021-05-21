from setuptools import setup

APP = ['app.py']
APP_NAME = "Henry Molar"
DATA_FILES = ['resources']
OPTIONS = {'argv_emulation': False,
		   'includes':[ 'tkinter', 'requests'],
		   'packages':['requests','bs4','molmass','termcolor'],
		   'iconfile':'resources/henrymolar.icns',
		   'plist': {
		        'CFBundleName': APP_NAME,
		        'CFBundleDisplayName': APP_NAME,
		        'CFBundleGetInfoString': "Periodic Table app",
		        'CFBundleIdentifier': "com.metachris.osx.sandwich",
		        'CFBundleVersion': "0.0.3",
		        'CFBundleShortVersionString': "0.0.3",
		        'NSHumanReadableCopyright': u"Copyright © 2020, Wired Future Labs, All Rights Reserved"
    		}
		   }

setup(
    app=APP,
    data_files=DATA_FILES,
    py_modules=['tkinterplus','calculator','feedbackGui','feedbackProcess','image',
    			'infoGui','legend','notification','periodictable','version'],
    options={'py2app': OPTIONS},
    setup_requires=['py2app','pillow']
)