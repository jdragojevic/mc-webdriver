#!/usr/bin/env python
import time

from front.page import Page
from front.login import Login

class AdminNav(Page):
    """
     Unisubs page contains common web elements found across
     all Universal Subtitles pages. Every new page class is derived from
     UnisubsPage so that every child class can have access to common web 
     elements and methods that pertain to those elements.
    """

    _URL = '/admin/'
     
    def open_admin_page(self, url=None):
        if not url:
            url = self._URL
        self.open_page(url)
        l =  Login()
        if l.overlay_present():
            l.login(user=self.ADMIN_USER, passw=self.ADMIN_PASSW)
        
