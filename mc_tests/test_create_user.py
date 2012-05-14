try:
    from django.test import LiveServerTestCase
except:
   pass
import time
from nose.tools import assert_true, assert_false
from front.user_nav import NavPage
from web.google import Google

def test_register_user_activate_login():
    """Sign up a new user, activate account and login.

    """
    kwargs = {'user': 'testuser'+str(time.time()),
                  'passw': 'test.pass',
                  'email': 'pculture.qa@gmail.com',
                  'kind': 'signup',
                  }
    mc = NavPage()
    mc.open()
    mc.login(**kwargs)
    kwargs['kind'] = 'site'
    kwargs['success'] = 'account inactive'
    mc.login(**kwargs)
    g = Google()
    activate_url = g.activate_mc_user_account('pculture.qa@gmail.com', 'Univers@lSubtitles', mc.base_url)
    mc.open_page(activate_url)
    kwargs['success'] = True
    assert_true mc.login(**kwargs), 'Login failed with new user account'

def test_create_user_admin_ui():
    pass

def test_make_user_an_admin():
    pass


class SubUI(TestCase):
    def test_create_user(self):
        pass

    def test_activate_user(self):
        pass

    def test_create_user_mismatch_password(self):
        pass

    def test_create_user_invalid_email(self):
        pass

    def test_create_user_short_username(self):
        pass

    def test_create_user_long_username(self):
        pass

    def test_create_admin(self):
        pass

    def test_change_user_privilages(self):
        pass
    

    
