# -*- coding: utf-8 -*-

from nose.tools import assert_true, assert_false
from nose import with_setup
import time
from admin.settings_page import SettingsPage 
from admin.manage_page import ManagePage
from front.search_page import SearchPage
from front.video_page import VideoPage

class TestSubmitVideoFeeds():
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


    def setup_func():
        """Make sure site settings are set to default (open submit permissions and link displayed).

        """
        pass
#        t = TestSubmitVideoFeeds()
#        t.delete_feeds(t.test_feeds)
        
    def teardown_func():
        "tear down test fixtures"
        

    @with_setup(setup_func, teardown_func)     
    def test_add_video_feed(self):
        for video_source in self.test_feeds.iterkeys():
            yield self.add_feeds, video_source

    def test_feed_video_page(self):
        for video_source in self.test_videos.iterkeys():
            yield self.verify_video_page, video_source


    def add_feeds(self, testcase):
            manage_pg = ManagePage()
            manage_pg.open_manage_page()
            kwargs = self.test_feeds[testcase]
            manage_pg.submit_feed(**kwargs)


    def verify_video_page(self, testcase):
        search_pg = SearchPage()
        search_pg.on_searchable_page()
        kwargs = self.test_videos[testcase]
        search_pg.search(kwargs['search'])
        page_url = search_pg.click_first_result()
        video_pg = VideoPage()
        video_metadata = video_pg.check_video_details(**kwargs)
        for results in video_metadata:
            assert_false(results)

            

      


    
    
        
