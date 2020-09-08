import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#3
@cli.command(name="mean")
@click.argument("number", type=click.INT, nargs=-1)
def mean(number):
    l = list(number)
    print(statistics.mean(l))

@cli.command(name="median")
@click.argument("number", type=click.INT, nargs=-1)
def median(number):
    l = list(number)
    print(statistics.median(l))

@cli.command(name="mode")
@click.argument("number", type=click.INT, nargs=-1)
def mode(number):
    l = list(number)
    print(statistics.mode(l))

@cli.command(name="fmean")
@click.argument("number", type=click.INT, nargs=-1)
def fmean(number):
    l = list(number)
    print(statistics.fmean(l))

if __name__ == "__main__":
    cli()
