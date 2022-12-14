#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'CdnNS Application Gateway (CdnNs/WdidcNet)'


def is_waf(self):
    schemes = [
        self.matchContent(r'cdnnswaf application gateway')
    ]
    if any(i for i in schemes):
        return True
    return False