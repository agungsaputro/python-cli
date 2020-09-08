import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#3
@cli.command(name="Mean")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.mean(l))

@cli.command(name="Median")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.median(l))

@cli.command(name="Mode")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.mode(l))

@cli.command(name="Fmean")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.fmean(l))

if __name__ == "__main__":
    cli()
