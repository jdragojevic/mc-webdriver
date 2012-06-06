#!/usr/bin/env python

#Enter valid values in this file - then save as testsetup.py.  Without this step, tests will not run correctly.

from selenium import webdriver
try:
    from setup_local import *
except ImportError:
    timeout = 60000
    browser = webdriver.Firefox() #BROWSER TO USE FOR TESTING
    base_url = "http://dalmatia.mirocommunity.org/" #URL OF THE SUT
    admin_user = "seleniumTestAdmin" # ADMIN USER
    admin_pass = "TestAdmin" # ADMIN PASSWORD
    normal_user = "seleniumTestUser"
    normal_pass = "selenium"

