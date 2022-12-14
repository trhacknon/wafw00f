#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'MaxCDN (MaxCDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-CDN', r'maxcdn'))
    ]
    if any(i for i in schemes):
        return True
    return False