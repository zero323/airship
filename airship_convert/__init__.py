#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import
import glob
import os
import argparse

from airship_convert.release import __author__, __version__
from airship_convert.render import render_template


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    render = subparsers.add_parser("render")
    render.add_argument("--path", required=True)
    render.add_argument("--out", default="out.html")

    args = parser.parse_args()

    # Search every subdirectory for note.json
    paths = glob.glob(os.path.join(args.path, "*", "note.json"))
    render_template(paths, args.out)







