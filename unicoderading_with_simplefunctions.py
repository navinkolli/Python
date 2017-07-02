# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:37:19 2017

@author: navin
"""

import unicodecsv
engagement_filename = 'daily_engagement.csv'
submissions_filename = 'project_submissions.csv'
def read_file(file_name):
   with open(file_name,'rb') as f:
       reader=unicodecsv.DictReader(f)
       return list(reader)
#daily_engagement = []     # Replace this with your code
#project_submissions = []  # Replace this with your code
enroll=read_file(engagement_filename)
getfile=read_file(submissions_filename)
print (enroll[0])
print(getfile[0])
