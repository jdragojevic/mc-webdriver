#!/usr/bin/env python
import time
from page import Page

class LoginOverlay(Page):
    """
     Overlay that displays when the user chooses to login.
     Contains, site, signin, facebook, openinstall, and google options.
     
    """
    _CLOSE = "div#overlay a.close"
    _ERROR = "ul.errorlist"
    _FORGOT_PASS_ERROR = "div a[href='/accounts/password/reset/']"
    _TABS = {'site':
                {"css": ".login_tab_user",
                 "text": "Login/Sign Up"},
             
             'signup':
                {"css": ".login_tab_user",
                 "text": "Login/Sign Up"},

            'facebook':
                {"css": ".login_tab_facebook",
                 "text": "Facebook"}
            }
    #SITE LOGIN FORM
    _SITE_USERNAME = 'div.left input#id_username'
    _SITE_PASSWORD = 'div.left input#id_password'
    _LOGIN = 'div.left input.button'

    #SITE SIGNUP FORM
    _SIGNUP_USERNAME = 'div.right input#id_username'
    _SIGNUP_EMAIL = 'div.right input#id_email'
    _SIGNUP_PASSWORD1 = 'div.right input#id_password1'
    _SIGNUP_PASSWORD2 = 'div.right input#id_password2'
    _SIGNUP_SUBMIT = 'div.right input.button'

    def site(self, *args):
        user, passw, _, success = args
        print args
        self.type_by_css(self._SITE_USERNAME, user)
        self.type_by_css(self._SITE_PASSWORD, passw)
        self.click_by_css(self._LOGIN)
        print success
        if not success == True:
            self.login_error(success)
        else:
            self.overlay_gone()


    def login_error(self, error):
        
        if error == 'bad password':
            assert self.is_element_present(self._FORGOT_PASS_ERROR), \
            'Invalid user or pass message not displayed'
        elif error == 'blank value':
            self.wait_for_element_present(self._ERROR)
            assert self.verify_text_present(self._ERROR, "This field is required."), \
            'Field required message not displayed'
        elif error == 'account inactive':
            self.wait_for_element_present(self._ERROR)
            assert self.verify_text_present(self._ERROR, "This account is inactive."), \
            'Account inactive message not displayed'
        else:
            assert False, "expected an error, but not this one"
        time.sleep(2)
        self.click_by_css(self._CLOSE)
                
            
    def signup(self, *args):
        user, passw, email, success = args
        self.type_by_css(self._SIGNUP_USERNAME, user)
        self.type_by_css(self._SIGNUP_EMAIL, email)
        self.type_by_css(self._SIGNUP_PASSWORD1, passw)
        self.type_by_css(self._SIGNUP_PASSWORD2, passw)
        self.click_by_css(self._SIGNUP_SUBMIT)
        if success:
            self.overlay_gone()
              
    def facebook(self, *args):
        user, passw, _ = args
        print user
        print passw
        

    def openinstall(self, *args):
        user, passw, _ = args
        print user
        print passw

    def google(self, *args):
        user, passw, _ = args
        print user
        print passw
        
    def choose_login_tab(self, tab):
        self.click_by_css(self._TABS[tab]['css'])
        
    def login(self, user, passw, tab, email, success):
        self.wait_for_element_present(self._TABS['site']['css'])
        if not tab.startswith('s'):
            self.choose_login_tab(tab)
        getattr(self, tab) (user, passw, email, success)

    def overlay_gone(self):
        self.wait_for_element_not_visible(self._TABS['site']['css'])
        



