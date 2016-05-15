# -*- coding: utf-8 -*-
"""
Created on Sat May 03 03:24:27 2016

@author: Laksh
@handle: techedlaksh
@website: www.laksharora.com
"""

import os
import urllib
url = "https://www.indiegogo.com/private_api/explore?filter_category=Technology&filter_funding=&filter_percent_funded=&filter_quick=popular_all&filter_status=&per_page=12&pg_num=1"
site = urllib.urlopen(url)
jdata = site.read()
print jdata