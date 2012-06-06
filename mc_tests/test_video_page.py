# -*- coding: utf-8 -*-

from nose.tools import assert_true, assert_false
from nose import with_setup
import time
from admin.settings_page import SettingsPage 
from admin.manage_page import ManagePage
from front.search_page import SearchPage
from front.video_page import VideoPage

class TestVideoPage():
    test_feeds = { 'youtube user': {
                   'feed url': 'http://www.youtube.com/user/clowntownhonkhonk',
                   'feed name': 'clowntownhonkhonk',
                   'feed author': 'clowntownhonkhonk',
                   'feed source': 'Youtube User',
                   'approve all': True,
                    },
                  }
    test_videos = {'youtube user': {
                    'title': 'X Factor Audition - Stop Looking At My Mom',
                    'search': 'stop looking at my mom rap', #term that returns a unique result
                    'tags': ['competition', 'mom', 'music', 'rap'],
                    'description': 'Brian Bradley sings his original song Stop Looking',
                    'source': 'clowntownhonkhonk',
                    },
                   }

    def add_feeds(self, testdata):
            manage_pg = ManagePage()
            manage_pg.open_manage_page()
            kwargs = testdata['youtube user']
            manage_pg.submit_feed(**kwargs)



    def setup_func():
        """Make sure site settings are set to default (open submit permissions and link displayed).

        """
        t = TestVideoPage()
        t.add_feeds(t.test_feeds)
        
    def teardown_func():
        "tear down test fixtures"
        

    @with_setup(setup_func, teardown_func)     
    def test_video_page_layout(self):
        for video_source in self.test_videos.iterkeys():
            yield self.verify_video_page, video_source


    def verify_video_page(self, testcase):
        search_pg = SearchPage()
        search_pg.on_searchable_page()
        kwargs = self.test_videos[testcase]
        search_pg.search(kwargs['search'])
        del kwargs['search']
        page_url = search_pg.click_first_result()
        video_pg = VideoPage()
        video_metadata = video_pg.check_video_details(**kwargs)
        for results in video_metadata:
            assert_false(results)

            

      


    
    
        
