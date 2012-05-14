from  web.webdriver_fragments import WebdriverFragments

class Page(WebdriverFragments):
    @property
    def is_the_current_page(self):
        page_title = self.browser.title()
        if re.search(self._page_title, page_title) is None:
            self.record_error()
            try:
                raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + page_title + "'")
            except Exception:
                raise Exception('Expected page title does not match actual page title.')
        else:
            return True
    def open(self):
        self.open_page('')


