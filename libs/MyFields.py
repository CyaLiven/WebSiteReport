#-*- coding:utf-8 -*-
__author__ = 'aliven.cen'

from wtforms.fields import TextField
from wtforms.widgets.core import TextArea

class TextAreaField(TextField):
    widget = TextArea()

    def __init__(self, width=100, high=100, *args, **kwargs):
        self.width = width
        self.high = high
        super(TextAreaField,self).__init__(*args, **kwargs)

    def __call__(self, **kwargs):
       kwargs['style'] = 'width: %spx; height: %spx;' %(self.width, self.high)
       return self.widget(self, **kwargs)

