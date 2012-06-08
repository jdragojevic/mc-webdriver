#!/usr/bin/env python
import time
from page import Page
from user_nav import NavPage

class SearchPage(NavPage):
    """Search Page - lists the results of a search.

    """

    _SEARCH_RESULT_THUMB = 'ul.media-grid li.media-item figure.thumb a'
    _SEARCH_RESULT_TITLE = 'a.title-link'
    _SEARCH_RESULT_TIMESTAMP = 'a.timestamp-link'
    _SEARCH_HEADER = 'header.page-header h1'
    _RSS = 'a.rss'

    def on_searchable_page(self):
        if not self.is_element_present(self.SEARCH_BOX):
            self.open()

    def search(self, term):
        self.on_searchable_page()
        self.clear_text(self.SEARCH_BOX)
        self.type_by_css(self.SEARCH_BOX, term)
        self.click_by_css(self.SEARCH_SUBMIT)

    def has_results(self):
        results =  self._search_results()
        if results['titles'] > 0:
            return True, results
        else:
            return False, results
        
        

    
    def click_first_result(self):
        vid_page = self.get_element_attribute(self._SEARCH_RESULT_THUMB, 'href')
        self.click_by_css(self._SEARCH_RESULT_THUMB)
        return vid_page
        
    def _search_results(self):
        result = {}
        thumbs = self.count_elements_present(self._SEARCH_RESULT_THUMB)
        titles = self.count_elements_present(self._SEARCH_RESULT_TITLE)
        times = self.count_elements_present(self._SEARCH_RESULT_TIMESTAMP)
        result = {'thumbs': thumbs,
                  'titles': titles,
                  'times': times,
                  }
        return result

        
