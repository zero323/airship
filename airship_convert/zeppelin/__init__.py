#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import json


def parse(path):
    with open(path) as fr:
        return json.load(fr)
