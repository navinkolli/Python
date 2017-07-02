# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 02:17:38 2017

@author: navin
"""

import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
#daily_engagement = read_csv('/datasets/ud170/udacity-students/daily_engagement.csv')
#project_submissions = read_csv('/datasets/ud170/udacity-students/project_submissions.csv')
unique_students= set()
for enrollment in enrollments: 
    unique_students.add(enrollment['account_key'])
print(len(unique_students))
#results = [int(i) for i in enrollments[]]
#print(results)
for enrollment in enrollments:
    student=enrollment['account_key']
    if student not in unique_students:
        print (enrollment)
        break