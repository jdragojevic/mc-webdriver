import imaplib
import time
import re
from webdriver_fragments import WebdriverFragments

class Google(WebdriverFragments):
    
    def activate_mc_user_account(self, email, password, url):
        """Activates a new Miro Community user's gmail account.

        Returns the activation url.a
        """
        print "Checking email for activation link"
        mailUser = email
        mailPassword = password
        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        mail.login(mailUser, mailPassword)
        mail.select('Inbox')
        result, data = mail.uid('search', None, '(HEADER Subject "Finish Signing Up at")')
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        lines = raw_email.split('\n')
        for line in lines:
            if line.startswith(url):
                activationURL = line
                break
        else:
            print 'failed to find link'
        return activationURL


        


# ===================================
# =      LOG IN AS GOOGLE USER      =
# ===================================

# This subroutine logs in to MC site as a Google user with <email>-<password> credentials

def LogInAsGoogleUser(self,sel,email,password):
    sel.open(testvars.MCTestVariables["LoginPage"])
    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
    sel.window_maximize()
    time.sleep(1)
    tabGoogle = "link=Google"
    print "Checking that Google tab on Login page exists..."
    if sel.is_element_present(tabGoogle)==False:
        self.fail("Google tab not found")
    else:
        print "OK"
        sel.click(tabGoogle)
        time.sleep(7)
        buttonSignIn = "css=div#login_tab_google.inactive div.left form p input.button"
        if sel.is_text_present("Sign in with your Google Account")==False or sel.is_element_present(buttonSignIn)==False:
            mclib.AppendErrorMessage(self,sel,"Could not find Sign In button")
        else:
            sel.click(buttonSignIn)
            sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
            if sel.is_element_present("css=input#Email")==False:
                mclib.AppendErrorMessage(self,sel,"Edit box for Google email not found")
            else:
                sel.type("css=input#Email",email)
                sel.type("css=input#Passwd",password)
                sel.click("css=input#signIn.g-button")
                sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                if sel.is_element_present("css=input#approve_button.lsobtn"):
                    sel.click("css=input#approve_button.lsobtn")
                    time.sleep(5)
                # Navigating to user profile to check the user's account parameters
                print "Checking the user's profile"
                linkYourProfile = "link=Your Profile"
                if sel.is_element_present(linkYourProfile)==False:
                    mclib.AppendErrorMessage(self,sel,"'Your profile' link on Home page not found")
                else:
                    sel.click("link=Your Profile")
                    sel.wait_for_page_to_load(testvars.MCTestVariables["TimeOut"])
                    if sel.get_value("id_email")!=email:
                        mclib.AppendErrorMessage(self,sel,"Unexpected user email encountered in User Profile")
                        print "Expected email: "+email
                        print "- Actual email: "+sel.get_value("id_email")
                    print "Checking Google user's name on Profile page..."
                    if sel.is_element_present("id_username")==False:
                        mclib.AppendErrorMessage(self,sel,"User Name field on Profile page not found")
                    else:
                        print "Google user has signed in and is known in the system as "+sel.get_value("id_username")





