import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

@cli.command(name="lower")
@click.argument('sentence')
def lower(sentence):
    print(sentence.lower())

@cli.command(name="upper")
@click.argument('sentence')
def upper(sentence):
    print(sentence.upper())

@cli.command(name="capitalize")
@click.argument('sentence')
def capitalize(sentence):
    lst = [word[0].upper() + word[1:] for word in sentence.split()]
    word = " ".join(lst)
    print(word)

if __name__ == "__main__":
    cli()
