#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
from jinja2 import Environment, FileSystemLoader, ModuleLoader
import json
import argparse
import glob
import os


def parse(path):
    with open(path) as fr:
        return json.load(fr)


def main(path, out, template):
    # Search every subdirectory for note.json
    paths = glob.glob(os.path.join(path, "*", "note.json"))
    with open(out, "w") as fw:
        fw.write(template.render({"files": [parse(path) for path in paths]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    parser.add_argument("--out", default="out.html")
    args = parser.parse_args()

    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

    env = Environment(loader=FileSystemLoader(os.path.join(
        PROJECT_PATH,  "templates"
    )))

    main(args.path, args.out, env.get_template("base.html"))


