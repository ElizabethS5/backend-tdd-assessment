#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "ElizabethS5"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("text", help='text to be manipulated')
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    return parser


def main():
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args()
    uppercase = args.upper
    lowercase = args.lower
    titlecase = args.title
    text = args.text

    if uppercase:
        text = text.upper()
    if lowercase:
        text = text.lower()
    if titlecase:
        text = text.title()
    print(text)
    return text


if __name__ == '__main__':
    main()
