
from nose.tools import assert_true, assert_false
from nose import with_setup

#from front.user_nav import NavPage 


class TestListingPages():

    def setup_func():
        """Listing tests require a number of videos, some of which are featured and others that are popular.

        If we are running local, we can setup with local fixtures, otherwise need to do it on test site.
        """
        print 'setting up test data'


    def teardown_func():
        "tear down test fixtures"
        

    @with_setup(setup_func, teardown_func)     
    def test_page_listings(self):
        """Test listing pages layout and content.'

        """
        listing_pages = ['new','featured','popular']
        test_cases = ['rss_feed', 'pagination']
                    
        for page in listing_pages:
            for tc in test_cases:
                yield self.verify_listing_page, page, tc

    def verify_listing_page(self, page, tc):
        print tc, page
        getattr(self, tc) (page)
      
    def rss_feed(self, listing):
        """Check for the rss link and verify feed exists.

        """
        assert False, 'this needs to be implemented'

    def thumbs(self, listing):
        """Verify videos listed have thumbnails."""
        assert False, 'this needs to be implemented'

    def title(self, listing):
        """Verify videos listed have titles that are links to vid page.

        """
        assert False, 'this needs to be implemented'

    def published(self, listing):
        """Verify videos display published date (if configurd)."""
        assert False, 'this needs to be implemented'

    def author(self, listing):
        """Verify author link (if exists).

        """
        assert False, 'this needs to be implemented'

    def overlay(self, listing):
        """Verify author link (if exists).

        """
        assert False, 'this needs to be implemented'    
    
        
