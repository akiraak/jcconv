#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
   jcconv, Japanese Characters CONVerter, interconvert hiragana, katakana, half-width kana.
   This module also treat 'half/wide number', 'half/wide alphabet'.
   
   IMPOTANT: In current version, this works only with utf-8 encoding.


   Simple example of usage is followings

       >>> from jcconv import *
       >>> print hira2kata('あいうえお')   # hiragana to katakana
       アイウエオ
       >>> print kata2hira('カタカナ')     # katakana to hiragana
       かたかな
       >>> print half2hira('ﾊﾝｶｸｶﾀｶﾅ')      # half-width kana to hiragana
       はんかくかたかな       
       >>> print half2wide('hello jcconv') # half-width alphabet to wide-width
       ｈｅｌｌｏ ｊｃｃｏｎｖ
       >>> print wide2half('ＷＩＤＥ')     # wide-width alphabet to half-width
       wide
"""

__author__  = "Matsumoto Taichi (taichino@gmail.com)"
__version__ = "0.1.6"
__license__ = "MIT License"

from jcconv import *
