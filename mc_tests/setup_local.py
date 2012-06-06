#!/usr/bin/env python

#Enter valid values in this file - then save as testsetup.py.  Without this step, tests will not run correctly.

from selenium import webdriver

timeout = 60000
browser = webdriver.Firefox() #BROWSER TO USE FOR TESTING
base_url = "http://localhost:8000/" #URL OF THE SUT
admin_user = "seleniumTestAdmin" # ADMIN USER
admin_pass = "TestAdmin" # ADMIN PASSWORD
normal_user = "seleniumTestUser"
normal_pass = "selenium"
