#!/usr/bin/env python

#Enter valid values in this file - then save as testsetup.py.  Without this step, tests will not run correctly.

from selenium import webdriver

timeout = 60000
browser = webdriver.Firefox() #BROWSER TO USE FOR TESTING
base_url = "http://dalmatia.mirocommunity.org/" #URL OF THE SUT
admin_user = "seleniumTestAdmin" # ADMIN USER
admin_pass = "TestAdmin" # ADMIN PASSWORD
normal_user = "seleniumTestUser"
normal_pass = "selenium"


#check if we are running on local server and override url, user, pass, browser settings.
try:
    from setup_local import *
except ImportError:
    pass
