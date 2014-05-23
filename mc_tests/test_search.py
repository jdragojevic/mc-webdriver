from nose.tools import assert_true, assert_false
from front.user_nav import NavPage 


def test_site_login():
    test_data = [
                 ['janet', 'janet', True],
                 ['jane', 'junk', 'bad password'],
                 ['janet', '', 'blank value']
                 ]
    for user, passw, rez in test_data:
        yield login, user, passw, rez
    

        
def login(user, passw, expected_result):
    mc = NavPage()
    mc.open()
    if expected_result == True:
        assert_true(mc.login(user, passw, success=expected_result))
    else:
        assert_false(mc.login(user, passw, success=expected_result))
    
        
