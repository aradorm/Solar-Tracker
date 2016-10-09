# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:18:12 2016

@author: ARADORM-HOME
"""

import ephem


location=ephem.Observer() #observer - heliostat\collector location
location.lon = '34:48:12.0'
location.lat = '31:15:13.9'
location.elevation = 0
location.date = '2016/8/18'
sun=ephem.Sun(location)
alt=sun.alt
az=sun.az
print (alt, az)
  