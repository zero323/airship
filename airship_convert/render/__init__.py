#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

from jinja2 import Environment, PackageLoader
import pypandoc

from airship_convert.zeppelin import parse


def render_template(paths, out):
    env = Environment(loader=PackageLoader("airship_convert", "templates"))
    template = env.get_template("markdown/base.md")
    rendered = template.render({"files": [parse(path) for path in paths]})

    pypandoc.convert(
        source=rendered, to="html",
        format="markdown-blank_before_header",
        outputfile=out, extra_args=("-s", "--highlight-style=tango")
    )
