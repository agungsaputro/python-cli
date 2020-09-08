import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#5
@cli.command(name="obfuscate")
@click.argument('sentence')
def obfuscate(sentence):
    sentence = list(sentence)
    text = ''.join(list(map(lambda char: f"&#{ord(char)};", sentence)))
    print(text)




if __name__ == "__main__":
    cli()