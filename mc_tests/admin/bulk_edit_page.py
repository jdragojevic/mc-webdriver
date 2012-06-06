#!/usr/bin/env python
from admin_nav import AdminNav


class BulkEditPage(AdminNav):
    """Describes elements and functions for the Admin Settings page.

    """


    _URL = 'admin/bulk_edit/'

    _FILTER = 'select.behave'  #Filters are name = category, author, filter

    _SEARCH = 'input[name="q"]'
    _SUBMIT_SEARCH = 'button.med_button[type="submit"]'

    _BULK_EDIT = 'select#bulk_action_selector'
    _BULK_EDIT_APPLY = 'div.bulkedit_controls button'

    #BULK EDIT FORM
    _TITLE_EDIT = 'li.title_edit input'
    _THUMB_EDIT = 'li.thumb_edit input'
    _DATE_EDIT = 'li.date_edit input'
    _DESCRIPTION_EDIT =  'li.description_edit input'
    _TAGS_EDIT = 'li.tags_edit'
    _CATEGORIES_EDIT = 'li.categories_edit'
    _USERS_EDIT = 'li.users_edit'
    _SUBMIT_BULK_FORM = 'div#massedit button'
    _CLOSE_BULK_FORM = 'div#massedit div.close'


    #VIDEOS TABLE
    _SELECT_ALL = 'th.checkbox input#toggle_all'
    _VIDEO_TITLE = 'tbody tr td:nth-child(2) span'
    

    def _bulk_edit_action(self, action):
        """Choose one of the bulk edit options.

        actions = Bulk Actions, Edit, Delete, Approve, Unapprove, Feature, Unfeature
        """
        if self._items_in_table() == True:
            self.select_option_by_text(self._BULK_EDIT, action)
            self.click_by_css(self._BULK_EDIT_APPLY)
        else:
            print 'no items in the table'
 
    def _search(self, term):
        self.type_by_css(self._SEARCH, term)
        self.click_by_css(self._SUBMIT_SEARCH)
     
    def _select_all_visible(self):
        print 'selecting all visible items'
        self.click_by_css(self._SELECT_ALL)
 
    def _items_in_table(self):
        return self.is_element_present(self._VIDEO_TITLE)
       
    def _filter_view(self, filter, option):
        pass
        #Show All Categories - category default
        #Show All Users - user default
        #Current Videos - video default
        #Featured Videos
        #Rejected Videos
        #Featured Videos
        #Unapproved Videos
        #Videos without Attribution
        #Videos without Category


    
    def open_bulk_page(self):
        self.open_admin_page(self._URL)

    def search_and_bulk_delete(self, term):
        self._search(term)
        self._select_all_visible()
        self._bulk_edit_action("Delete")
         
