#!/usr/bin/env python

#Enter valid values in this file - then save as testsetup.py.  Without this step, tests will not run correctly.

from selenium import webdriver

browser = webdriver.Firefox() #BROWSER TO USE FOR TESTING
base_url = "http://dalmatia.mirocommunity.org/" #URL OF THE SUT
admin_user = "janet" # ADMIN USER
admin_pass = "janet" # ADMIN PASSWORD

#check if we are running on local server and override url, user, pass, browser settings.
try:
    from testsetup_local import *
except ImportError:
    pass
