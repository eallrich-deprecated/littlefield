#!/usr/env/bin python
"""Access configuration to Littlefield Simulation instances."""

credentials = {
    'institution': 'university, perhaps?',
    'id':          'who art thou?',
    'password':    'open sesame!',
}

# If you need to connect through a proxy, use this form instead:
# proxy = {'http': 'http://proxy.example.com:8080'}
proxy = {}

# Any custom HTTP headers to send with the request. Leave blank to use the defaults.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3',
}

# File for storing ranking data
rankings = 'rankings.csv'

# File for storing production data
production = 'production.csv'

datasets = (
    # (Dataset name, Column heading), ...
    ('JOBIN',  'Jobs Accepted'),
    ('JOBQ',   'Jobs Waiting for Kits'),
    ('INV',    'Kits Inventory'),
    ('S1Q',    'Station 1 Queue'),
    ('S1UTIL', 'Station 1 Util'),
    ('S2Q',    'Station 2 Queue'),
    ('S2UTIL', 'Station 2 Util'),
    ('S3Q',    'Station 3 Queue'),
    ('S3UTIL', 'Station 3 Util'),
    ('CASH',   'Cash ($1000)'),
    ('JOBOUT', 'Jobs Completed'),
    ('JOBT',   'Job Lead Time'),
    ('JOBREV', 'Revenue Per Job'),
)

# These datasets are affected by the choice of oder contract. By Default, only
# the first 'set' of data is retrieved for each name. When multiple contracts
# are available, contracts other than the default appear under their own 'sets'
# and require special handling.
multisets = (
    'JOBOUT',
    'JOBT',
    'JOBREV',
)

# As you perform actions, update this tuple with the days of events
# E.g. history = (55, 71, 91, 211, 213)
history = ()
