#!/usr/env/bin python
"""Make charts from Littlefield Simulation data."""

import csv
import os
import sys

import numpy
import matplotlib.pyplot as pyplot

import config


def read_csv():
    """Returns a list of dictionaries containing the CSV's data"""
    with open(config.production, 'rb') as f:
        reader = csv.DictReader(f)
        # Remove commas so that float() casts work
        return [{k:v.replace(',','') for k,v in row.items()} for row in reader]


def column(rows, name):
    """Returns a list of the data in the given column"""
    return [r[name] for r in rows]


def plot(rows, x='Day', y=[], filename='plot.png'):
    """Plots the named Y series against the X series, saved to the filename"""
    # Get our data columns
    x = column(rows, x)
    # Generating a tuple of the name and the data itself
    ys = [(name, column(rows, name)) for name in y]

    # Initialize the figure and subplot (the latter is so that we can adjust
    # the size latter)
    fig = pyplot.figure(figsize=(19.20, 10.80))
    ax = pyplot.subplot(111)

    # Draw our data
    for name, y  in ys:
        ax.plot(x, y, label=name)

    ax.grid(True)
    ax.set_xlim(xmax=float(x[-1])+1)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.95, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1,0.5))

    # Draw lines marking history events
    for day in config.history:
        ax.axvline(x=day, color='orange')

    pyplot.savefig(filename, bbox_inches='tight')


def plot_util(rows):
    names = (
        'Station 1 Util',
        'Station 2 Util',
        'Station 3 Util',
    )
    plot(rows, y=names, filename='utilization.png')


def plot_jobs(rows):
    names = (
        'Jobs Accepted',
        'Jobs Completed',
    )
    plot(rows, y=names, filename='jobs.png')


def plot_queues(rows):
    names = (
        'Station 1 Queue',
        'Station 2 Queue',
        'Station 3 Queue',
    )
    plot(rows, y=names, filename='queues.png')


def plot_jobs_and_util(rows):
    names = (
        'Jobs Accepted',
        'Station 1 Util',
        'Station 2 Util',
        'Station 3 Util',
        'Job Lead Time',
        'Jobs Completed',
    )
    plot(rows, y=names, filename='jobs_util.png')


def plot_singles(rows):
    for ds, name in config.datasets:
        filename = 'single_%s.png' % ds
        names = [name,]
        plot(rows, y=names, filename=filename)


def main():
    rows = read_csv()
    plot_util(rows)
    plot_jobs(rows)
    plot_queues(rows)
    plot_jobs_and_util(rows)
    plot_singles(rows)


if __name__ == "__main__":
    main()
