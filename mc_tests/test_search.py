# -*- coding: utf-8 -*-
from nose.tools import assert_true, assert_false
from nose.tools import assert_true, assert_false
from nose import with_setup
import time
from admin.settings_page import SettingsPage 
from admin.manage_page import ManagePage
from front.video_page import VideoPage
from front.search_page import SearchPage

class TestSearchVideos():
    test_feeds = { 'youtube user': {
                   'feed url': 'http://gdata.youtube.com/feeds/api/users/4001v63/uploads',
                   'feed name': '4001v63',
                   'feed author': '4001v63',
                   'feed source': 'Youtube User',
                   'approve all': True,
                    },
                  }
    search_terms = {'multi words with symbol': 'Duo Orre & Sinisalo',
                  'non-ascii-char': u'Elämäkerta',
                  'single word': 'Duo',
                  'numerical': '2009'
                  }
  
    def setup_func():
        """Make sure site settings are set to default (open submit permissions and link displayed).

        """
#        settings_page = SettingsPage()
#        settings_page.site_settings()
        t = TestSearchVideos()
        t.setup_videos(t.test_feeds)

    def setup_videos(self, testfeeds):
        manage_pg = ManagePage()
        manage_pg.open_manage_page()
        for k, v in testfeeds.iteritems():
            kwargs = v
            manage_pg.submit_feed(**kwargs)
        
    def teardown_func():
        "tear down test fixtures"
        

#    @with_setup(setup_func, teardown_func)     
    def test_video_search(self):
        for testcase in self.search_terms.iterkeys():
            yield self.verify_video_search, testcase

        
    def verify_video_search(self, testcase):
        search_pg = SearchPage()
        search_pg.search(self.search_terms[testcase])
        has_results, result = search_pg.has_results()
        assert_true(has_results, result)
        
        


        

    
        
