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
    _MESSAGE = 'div.message'
    _DUP_MESSAGES = ['A video with that url has already been submitted. You can moderate it here.',
                     'It appears that we already have a copy of that video here']

    #DIRECT LINK FORM FIELDS
    _NAME = 'input#id_name'
    _WEBSITE = 'input#website_url'
    _THUMB_FILE = 'input#id_thumbnail_file'
    _THUMB_URL = 'input#id_thumbnail'
    _DESCRIPTION = 'textarea#description'

    #EMBED FORM FIELDS
    _TAGS = 'input#id_tags'    

    #VIDEO SUBMITTED OR DUPLICATED LINK
    _SUBMITTED_VID_LINK = 'div.message a'


    def submit_a_valid_video(self, **kwargs):
        print "Submitting a valid video"
        url = kwargs['url']
        form = kwargs['form']
        self.open_page(self._URL)
        self._submit_video(url)
        
        if form == 'duplicate':
            return self._duplicate()
        else:
            form_action = "_".join(["", form, "form"])
            getattr(self, form_action) (**kwargs)
            self._submit_form()
            return self._submitted_video()
   
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
        print "I got the scraped video form"
        print kwargs
        
    def _tag_form(self, **kwargs):
        print "I got the tagged video form"
        tags = kwargs.get('tags', None)
        if tags == None:
            pass
        elif  isinstance(tags, basestring):
            self.type_by_css(self._TAGS, tags)
        else:
            for tag in tags:
                self.type_by_css(self._TAGS, ", ".join(tags))

    def _direct_form(self, **kwargs):
        print "I got the direct submission form"
        try:
            assert "direct" in self.current_url()
        except:
            raise AssertionError("Expected the direct form, got this" + self.current_url())

        
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
                

    def _submitted_video(self):
        self.wait_for_element_present(self._SUBMITTED_VID_LINK)
        video_link = self.get_element_attribute(self._SUBMITTED_VID_LINK, 'href')
        return video_link

    def _duplicate(self):
        message = self.get_text_by_css(self._MESSAGE)
        for mess in self._DUP_MESSAGES:
            if mess in message:
                print "Duplicate video detected"
                return self._submitted_video()
    
    def _submit_form(self):
        self.click_by_css(self._SUBMIT)

        
    
        
        
                
        
