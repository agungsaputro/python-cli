import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#4
@cli.command(name="palindrome")
@click.argument('sentence')
def palindrome(sentence):
    l, h = 0, len(sentence) - 1
    s = sentence.lower() 

    while (l <= h): 
    
        if (not(s[l] >= 'a' and s[l] <= 'z')): 
            l += 1
        elif (not(s[h] >= 'a' and s[h] <= 'z')): 
            h -= 1

        elif (s[l] == s[h]): 
            l += 1
            h -= 1
        else: 
            return print("NO")
    return print("YES")

if __name__ == "__main__":
    cli()