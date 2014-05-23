# -*- coding: utf-8 -*-

from nose.tools import assert_true, assert_false
from nose import with_setup

from admin.settings_page import SettingsPage 
from front.user_nav import NavPage
from front.submit_page import SubmitPage

class TestSubmitVideos():
    
    test_videos = { 'youtube': {
                        'url': 'http://www.youtube.com/watch?v=WqJineyEszo',
                        'form': 'scraped',
                        'title': 'Stop looking at my mom',
                        'search': 'X Factor audition',
                        'source': 'clowntownhonkhonk',
                        },
##                    'vimeo': {
##                        'url': 'http://vimeo.com/26487510',
##                        'title': u'Con la música a otra parte',
##                        'form': None,
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
            pass

    def setup_func():
        """Make sure site settings are set to default (open submit permissions and link displayed).

        """
        settings_page = SettingsPage()
        settings_page.site_settings()
#        t = TestSubmitVideos()
#        t.delete_videos(t.test_videos)
        
    def teardown_func():
        "tear down test fixtures"
        

    @with_setup(setup_func, teardown_func)     
    def test_video_submit(self):
        """Submit a video.

        """                
        for tc, vid_url in self.test_videos.iteritems():
            yield self.verify_video_submit, tc

    def test_submit_duplicate_video(self):
        """Submit a duplicate video.

        """
        pass


    def verify_video_submit(self, testcase):
        submit_pg = SubmitPage()
        kwargs = self.test_videos[testcase]
        video_page_url = submit_pg.submit_a_valid_video(**kwargs)
        
        
        
      


    
    
        