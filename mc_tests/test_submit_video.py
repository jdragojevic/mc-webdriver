# -*- coding: utf-8 -*-

from nose.tools import assert_true, assert_false
from nose import with_setup
import time
from admin.settings_page import SettingsPage 
from admin.bulk_edit_page import BulkEditPage
from front.user_nav import NavPage
from front.submit_page import SubmitPage
from front.video_page import VideoPage

class TestSubmitVideos():
    
    test_videos = { 'youtube': {
                        'url': 'http://www.youtube.com/watch?v=WqJineyEszo',
                        'form': 'scraped',
                        'title': 'X Factor Audition - Stop Looking At My Mom',
                        'search': 'stop looking at my mom rap', #term that returns a unique result
                        'tags': ['competition', 'mom', 'music', 'rap'],
                        'description': 'Brian Bradley sings his original song Stop Looking',
                        'source': 'clowntownhonkhonk',
                    },
                   
##                    'vimeo': {
##                        'url': 'http://vimeo.com/26487510',
####                        'title': u'Con la música a otra parte',
##                        'form': 'embed',
##                        
##                        },
##                    'blip': {
##                        'url': 'http://blip.tv/djvibetv/dj-roots-booh-drum-and-bass-sessions-vol-2-213741'
##                         'form': 'embed'                    
##                        'title': 'Dj Roots - Booh! Drum and Bass Sessions Vol.2'
##                        }
            #        'mp4':'',
            #        'form': 'direct'
            #        'ogg':'',
                    
                    }

    def delete_videos(self, testdata):
        for source, metadata in testdata.iteritems():
            bulk_pg = BulkEditPage()
            bulk_pg.open_bulk_page()
            bulk_pg.search_and_bulk_delete(metadata.get('search', 'title'))

    def setup_func():
        """Make sure site settings are set to default (open submit permissions and link displayed).

        """
#        settings_page = SettingsPage()
#        settings_page.site_settings()
        t = TestSubmitVideos()
        t.delete_videos(t.test_videos)
        
    def teardown_func():
        "tear down test fixtures"
        

    @with_setup(setup_func, teardown_func)     
    def test_video_submit(self):
        for testcase in self.test_videos.iterkeys():
            yield self.verify_video_submit, testcase

    def test_video_submit_duplicate(self):
        for testcase, vals in self.test_videos.iteritems():
            self.test_videos[testcase + 'duplicate'] = self.test_videos[testcase]
            self.test_videos[testcase + 'duplicate']['form'] = 'duplicate'
            yield self.verify_video_submit, testcase
            self.test_videos.pop(testcase + 'duplicate')
              

    def verify_video_submit(self, testcase):
        submit_pg = SubmitPage()
        kwargs = self.test_videos[testcase]
        video_page_url = submit_pg.submit_a_valid_video(**kwargs)
        video_pg = VideoPage()
        video_pg.open_page(video_page_url)
        video_metadata = video_pg.check_video_details(**kwargs)
        for results in video_metadata:
            assert_false(results)
        


    
    
        
