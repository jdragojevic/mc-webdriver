#!/usr/bin/env python

from page import Page
class SubmitPage(Page):
    """
     Submit Video Page
     
    """
    _URL = 'submit_video/'
    _INPUT_URL = 'input#id_url'
    _ERROR = 'ul.errorlist li'
    _SUBMIT = 'footer.form-actions > button'

    #DIRECT LINK FORM FIELDS
    _NAME = 'input#id_name'
    _WEBSITE = 'input#website_url'
    _THUMB_FILE = 'input#id_thumbnail_file'
    _THUMB_URL = 'input#id_thumbnail'
    _DESCRIPTION = 'textarea#description'

    #EMBED FORM FIELDS
    _TAGS = 'input#id_tags'    

    #THANKS
    _THANKS = 'div.message.success'

    _SUBMITTED_VID_LINK = 'a#next'


    def submit_a_valid_video(self, **kwargs):
        print "I want to submit a video"
        url = kwargs['url']
        form = kwargs['form']
        self.open_page(self._URL)
        self._submit_video(url)
        form_action = "_".join(["", form, "form"])
        getattr(self, form_action) (**kwargs)
        
        if form == 'embed':
            self._tag_form(kwargs['tags'])
        elif form == 'direct':
            self._direct_form(**kwargs)
   
    def _error_message(self):
        if self.is_element_visible(self._ERROR):
            return True

    def _error_message_text(self):
        if self.is_element_visible(self._ERROR):
            return self.get_text_by_css(self._ERROR)

    def _submit_video(self, url):
        self.type_by_css(self._INPUT_URL, url)
        self.click_by_css(self._SUBMIT)

    def _scraped_form(self, **kwargs):
        print "I am on the scraped video form"
        print kwargs
        self.click_by_css(self._SUBMIT)

    def _tag_form(self, **kwargs):
        tags = kwargs.get('tags', None)
        if tags == None:
            pass
        elif  isinstance(tags, basestring):
            self.type_by_css(self._TAGS, tags)
        else:
            for tag in tags:
                self.type_by_css(self._TAGS, ", ".join(tags))
        self._submit_form()

    def _direct_form(self, **kwargs):
        try:
            assert "direct" in self.current_url
        except:
            raise AssertionError("Expected the direct form, got this" + self.current_url)

        
        form_fields = {'title': None,
                    'website': None,
                    'thumb_file': None,
                    'thumb_url': None,
                    'description': None,
                    }

        form_fields.update(kwargs)
        for k, v in form_fields.iteritems():
            if v:
                field = "_"+str(k).upper()
                self.type_by_css(getattr(self, field), v)
                
        self._submit_form()

    def _thanks(self):
        video_link = self.get_attr(self._SUBMITTED_VID_LINK, 'href')
        print video_link
        return video_link

    
        
        
                
        
