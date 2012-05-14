def LogInAsTwitterUser(self,sel,username,password):
    sel.open(testvars.MCTestVariables["LoginPage"])
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
    sel.window_maximize()
    time.sleep(1)
    tabTwitter = "link=Twitter"
    print "Checking that Twitter tab on Login page exists..."
    if sel.is_element_present(tabTwitter)==False:
        self.fail("Twitter tab not found")
    else:
        print "OK"
        sel.click(tabTwitter)
        time.sleep(7)
        buttonTwitterLogin = "css=div#login_tab_twitter.inactive div.left a"
        if sel.is_element_present(buttonTwitterLogin)==False:
            mclib.AppendErrorMessage(self,sel,"Could not find Sign in with Twitter button")
        else:
            print "Clicking Sign in to Twitter button..."
            sel.click(buttonTwitterLogin)
            time.sleep(5)
        # Enter Twitter username address
            if sel.is_element_present("css=input#username_or_email.text")==False:
                mclib.AppendErrorMessage(self,sel,"Entry field for Twitter user's USERNAME not found")
            else:
                print "Entering the Twitter user credentials"
                sel.type("css=input#username_or_email.text", username)
        # Enter Twitter user's password
            if sel.is_element_present("css=input#password.password")==False:
                mclib.AppendErrorMessage(self,sel,"Entry field for Twitter user's password not found")
            else:
                sel.type("css=input#password.password", password)
            # Click Login button
            if sel.is_element_present("css=input#allow.submit")==False:
                mclib.AppendErrorMessage(self,sel,"Login button on Twitter user's credentials entry form not found")
            else:
                sel.click("css=input#allow.submit")
                sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                print "Done"
                time.sleep(15)
                # Should be at Home page and logged in now
                # Check that "Logout <username>" link is present at the bottom of the page
                print "Checking that user "+username+" is logged on"
                linkLogout = "link=Logout "+username
                mclib.wait_for_element_present(self, sel, linkLogout)

#                if sel.is_element_present(linkLogout)==False:
#                    mclib.AppendErrorMessage(self,sel,"'Logout "+username+"' link on Home page not found")
                # Navigating to user profile to check the user's account parameters
                print "Checking the user's profile"
                linkYourProfile = "link=Your Profile"
                if sel.is_element_present(linkYourProfile)==False:
                    mclib.AppendErrorMessage(self,sel,"'Your profile' link on Home page not found")
                else:
                    sel.click("link=Your Profile")
                    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                    print "Checking Twitter user's name on Profile page..."
                    if sel.is_element_present("css=div.form_box input#id_username")==False:
                        mclib.AppendErrorMessage(self,sel,"User Name field on Profile page not found")
                    else:
                        if sel.get_value("css=div.form_box input#id_username")!=username:
                            mclib.AppendErrorMessage(self,sel,"Unexpected user name found")
                            print "Expected user name: "+username
                            print "- Actual user name: "+sel.get_value("css=div.form_box input#id_username")
                        else:
                            print "OK"




# ===================================
# =     LOG IN TO TWITTER SITE      =
# ===================================

# This subroutine logs in to Twitter with the use of PCF test account

def LogInToTwitter(self,sel):
    sel.open("http://www.twitter.com")
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
    sel.window_maximize()
    time.sleep(1)
#    sel.click("css=div.username > span.holder")
#    sel.type("css=div.username > span.holder", testvars.MCTestVariables["TwitterLogin"])
#    sel.type("css=div.password > span.holder", testvars.MCTestVariables["TwitterPassword"])
    sel.type("css=div.username > input", testvars.MCTestVariables["TwitterLogin"])
    sel.type("css=div.password > input", testvars.MCTestVariables["TwitterPassword"])
    sel.click("css=div.front-signin > form.signin > fieldset.subchck > button.submit.button")
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
