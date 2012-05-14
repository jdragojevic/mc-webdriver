

# ===================================
# =    LOG IN AS FACEBOOK USER      =
# ===================================

# This subroutine logs in to MC site as a Facebook user with <email>-<password> credentials
# The user becomes known to the system as <username>

def LogInAsFacebookUser(self,sel,username,email,password):
    sel.open(testvars.MCTestVariables["LoginPage"])
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
    sel.window_maximize()
    time.sleep(1)
    tabFacebook = "link=Facebook"
    print "Checking that Facebook tab on Login page exists..."
    if sel.is_element_present(tabFacebook)==False:
        self.fail("Facebook tab not found")
    else:
        print "OK"
        sel.click(tabFacebook)
        time.sleep(7)
        buttonFacebookLogin = "css=div#login_tab_facebook.inactive div.left a"
        if sel.is_element_present(buttonFacebookLogin)==False:
            mclib.AppendErrorMessage(self,sel,"Could not find Login with Facebook button")
        else:
            print "Clicking Log in to Facebook button..."
            sel.click(buttonFacebookLogin)
            time.sleep(5)
        # Enter Facebook user's email address
            if sel.is_element_present("css=input#email.inputtext")==False:
                mclib.AppendErrorMessage(self,sel,"Entry field for Facebook user's EMAIL not found")
            else:
                print "Entering the Facebook user credentials"
                sel.type("css=input#email.inputtext", email)
        # Enter Facebook user's password
            if sel.is_element_present("css=input#pass.inputpassword")==False:
                mclib.AppendErrorMessage(self,sel,"Entry field for Facebook user's password not found")
            else:
                sel.type("css=input#pass.inputpassword", password)
            # Click Login button
            if sel.is_element_present("css=div#login_button_inline label.uiButton input")==False:
                mclib.AppendErrorMessage(self,sel,"Login button on Facebook user's credentials entry form not found")
            else:
                sel.click("css=div#login_button_inline label.uiButton input")
                sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                print "Done"
                # Should be at Home page and logged in now
                # Check that "Logout <username>" link is present at the bottom of the page
                print "Checking that user "+username+" is logged on"
                linkLogout = "link=Logout "+username
                mclib.wait_for_element_present(self, sel, linkLogout)
                #if sel.is_element_present(linkLogout)==False:
                #    mclib.AppendErrorMessage(self,sel,"'Logout "+username+"' link on Home page not found")
                # Navigating to user profile to check the user's account parameters
                print "Checking the user's profile"
                linkYourProfile = "link=Your Profile"
                if sel.is_element_present(linkYourProfile)==False:
                    mclib.AppendErrorMessage(self,sel,"'Your profile' link on Home page not found")
                else:
                    sel.click("link=Your Profile")
                    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                    print "Checking Facebook user's name on Profile page..."
                    if sel.is_element_present("id_name")==False:
                        mclib.AppendErrorMessage(self,sel,"User Name field on Profile page not found")
                    else:
                        if sel.get_value("id_name")!=username:
                            mclib.AppendErrorMessage(self,sel,"Unexpected user name found")
                            print "Expected user name: "+username
                            print "- Actual user name: "+sel.get_value("id_name")
                        else:
                            print "OK"




# ===================================
# =    LOG IN TO FACEBOOK SITE      =
# ===================================

# This subroutine logs in to Facebook with the use of PCF test account

def LogInToFacebook(self,sel):
    sel.open("http://www.facebook.com")
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
    sel.window_maximize()
    time.sleep(1)
    sel.type("id=email", testvars.MCTestVariables["FBLogin"])
    sel.type("id=pass", testvars.MCTestVariables["FBPassword"])
    sel.click("css=.title:contains('Please Sign In')")

    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])

