#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import json
import argparse
import glob
import os

from jinja2 import Environment, PackageLoader

from airship_convert.release import __author__, __version__


def parse(path):
    with open(path) as fr:
        return json.load(fr)


def main(path, out):
    # Search every subdirectory for note.json
    paths = glob.glob(os.path.join(path, "*", "note.json"))

    env = Environment(loader=PackageLoader("airship_convert", "templates"))
    template = env.get_template("base.html")

    with open(out, "w") as fw:
        fw.write(template.render({"files": [parse(path) for path in paths]}))

