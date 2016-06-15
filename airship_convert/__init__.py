#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import json
import glob
import os

from jinja2 import Environment, PackageLoader
import pypandoc

from airship_convert.release import __author__, __version__


def parse(path):
    with open(path) as fr:
        return json.load(fr)


def main(path, out):
    # Search every subdirectory for note.json
    paths = glob.glob(os.path.join(path, "*", "note.json"))

    env = Environment(loader=PackageLoader("airship_convert", "templates"))
    template = env.get_template("markdown/base.md")
    rendered = template.render({"files": [parse(path) for path in paths]})

    pypandoc.convert(
        source=rendered, to="html",
        format="markdown-blank_before_header",
        outputfile=out, extra_args=("-s", "--highlight-style=tango")
    )

