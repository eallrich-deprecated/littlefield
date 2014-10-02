#!/usr/env/bin python
"""Handles authenticating to Littlefield"""

import requests

from config import credentials, proxy

class LoginError(RuntimeError):
    pass

def login():
    """Returns the auth cookie"""
    auth_url = 'http://ops.responsive.net/Littlefield/CheckAccess'

    r = requests.post(auth_url, data=credentials, proxies=proxy)
    if r.status_code == 200:
        return r.cookies
    else:
        raise LoginError("Status %r. Text: %s" % (r.status_code, r.text))

