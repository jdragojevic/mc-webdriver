def LogInAsOpenIDUser(self,sel,username,password):
    sel.open(testvars.MCTestVariables["LoginPage"])
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
    sel.window_maximize()
    time.sleep(1)
    tabOpenID = "link=OpenID"
    print "Checking that OpenID tab on Login page exists..."
    if sel.is_element_present(tabOpenID)==False:
        self.fail("OpenID tab not found")
    else:
        print "OK"
        sel.click(tabOpenID)
        time.sleep(7)
        inputOpenID = "css=input.openid"
        if sel.is_element_present(inputOpenID)==False:
            mclib.AppendErrorMessage(self,sel,"Could not find the input field for OpenID")
        else:
            sel.type(inputOpenID,username+'.myopenid.com')
            sel.click("css=div#login_tab_openid.inactive div.left form p input.button")
            sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
            if sel.is_element_present("css=input#password")==False:
                mclib.AppendErrorMessage(self,sel,"Edit box for OpenID password not found")
            else:
                sel.type("css=input#password",password)
                sel.click("css=input#signin_button")
                sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                if sel.is_element_present("css=button#continue-button"):
                    sel.click("css=button#continue-button")
                    time.sleep(5)
                # Navigating to user profile to check the user's account parameters
                print "Checking the user's profile"
                linkYourProfile = "link=Your Profile"
                if sel.is_element_present(linkYourProfile)==False:
                    mclib.AppendErrorMessage(self,sel,"'Your profile' link on Home page not found")
                else:
                    sel.click("link=Your Profile")
                    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                    print "Checking OpenID user's name on Profile page..."
                    if sel.is_element_present("id_username")==False:
                        mclib.AppendErrorMessage(self,sel,"User Name field on Profile page not found")
                    else:
                        print "OpenID user has signed in and is known in the system as "+sel.get_value("id_username")
