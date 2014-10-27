#!/usr/env/bin python
"""Handles authenticating to Littlefield"""

import requests

from config import credentials, proxy, headers

class LoginError(RuntimeError):
    pass


def cache_cookie(func):
    result = {}
    def wrapped():
        if 'cookies' not in result:
            result['cookies'] = func()
        return result['cookies']
    return wrapped


@cache_cookie
def login():
    """Returns the auth cookie"""
    auth_url = 'http://ops.responsive.net/Littlefield/CheckAccess'

    r = requests.post(auth_url, data=credentials, proxies=proxy, headers=headers)
    if r.status_code == 200:
        return r.cookies
    else:
        raise LoginError("Status %r. Text: %s" % (r.status_code, r.text))

