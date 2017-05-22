#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:20:39 2017

@author: ujjwal
"""

import os
import urllib
import sys
import tarfile
import re


if (len(sys.argv) > 1 ):
    downloadUrl = sys.argv[1]
else:
    raise ValueError('provide url in argument')
    
dirname = re.match('[\w\d]*\.', downloadUrl.split('/')[-1]).group(0)
if not os.path.isdir('./'+ dirname):
    os.mkdir('./'+ dirname)

os.chdir('./'+ dirname)
filename, headers = urllib.request.urlretrieve(downloadUrl)
tarObj = tarfile.open(filename)
tarObj.extractall(path="./")
tarObj.close()
                


    

 