#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    config.py
    ~~~~~

    Basic configuration for your Open Journal instance

    :created: 2013-02-26 18:04:13 -0800
    :license: BSD. See LICENSE.
"""
import os
import ConfigParser
cwd = os.path.dirname(__file__)
config = ConfigParser.ConfigParser()
try:
    config.read(os.path.join(cwd, 'config.cfg'))
    NAME = config.get('site', 'name')
except Exception as e:
    raise Exception("Need a valid config.cfg file, got error: %s" % e)
