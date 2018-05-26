# -*- coding: utf-8 -*-
"""
Created on Sat May 26 06:49:12 2018

@author: Srikrishna.Sadula
"""

from nose import *
import NAME
def setup():
    print ("SETUP!")
def teardown():
    print ("TEAR DOWN!")
def test_basic():
    print ("I RAN!")