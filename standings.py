import csv
import time

from BeautifulSoup import BeautifulSoup as soup
import requests

import auth
import config


class StandingsError(RuntimeError):
    pass


def download():
    url = "http://ops.responsive.net/Littlefield/Standing"
    cookies = auth.login()

    r = requests.get(url, cookies=cookies, proxies=config.proxy)
    if r.status_code == 200:
        return r.text
    else:
        message = "Got status %r when retrieving rankings. Text: %s" % (r.status_code, r.text)
        raise StandingsError(message)


def latest():
    raw = download()
    html = soup(raw)
    data = []

    # Iterate over all the rows, but the first one is just the headers: skip it
    for row in html.body.findAll('tr')[1:]:
        # We don't need the 'rank' column
        _, name, cash = [c.text for c in row.findAll('td')]
        cash = float(cash.replace(',', '')) # Treat numbers as numbers!
        data.append([name, cash])

    return data


def existing(data):
    """If historical data exists, return it. Else, start making history!"""
    # See if we need to read in existing data first
    try:
        with open(config.rankings, 'rb') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            history = [row for row in reader]
    except IOError: # No existing data? Create the structures!
        headers = ['Time',]
        headers.extend([name for name,_ in data])
        history = []
    return (headers, history)


def main():
    current = latest()
    headers, history = existing(current)

    # Put the latest data into the expected format, including current timestamp
    now = int(time.time())
    row = {'Time': now,}
    row.update({name: cash for name, cash in current})
    history.append(row)

    with open(config.rankings, 'wb') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(history)

if __name__ == "__main__":
    main()

