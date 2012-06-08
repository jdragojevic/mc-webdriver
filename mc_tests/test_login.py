from nose.tools import assert_true, assert_false
from nose import with_setup
from front.user_nav import NavPage 


class TestLoginPage():
    
    login_data = {'valid login': {
                     'user': 'seleniumTestUser',
                     'passw': 'selenium'},
                 'bad password': {
                     'user': 'seleniumTestUser',
                     'passw': 'junk'},
                 'blank value': {
                     'user': 'seleniumTestUser',
                     'passw': ''},
                  }

    def setup_func():
        """The seleniumTestUser account must exist.

        """
        pass
#        t = TestVideoPage()
#        t.delete_feeds(t.test_feeds)
                  
    def teardown_func():
        "tear down test fixtures"
        

    @with_setup(setup_func, teardown_func)     
    def test_login(self):
        for testcase in self.login_data.iterkeys():
            yield self.login, testcase
    
    def login(self, testcase):
        mc = NavPage()
        mc.open()
        kwargs = self.login_data[testcase]
        if testcase == 'valid login':
            kwargs['success'] = True
            assert_true(mc.login(**kwargs))
        else:
            kwargs['success'] = testcase
            assert_false(mc.login(**kwargs))
    
        
