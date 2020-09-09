import click
from src._1_string import lower, upper, capitalize
from src._2_arithmatic import add,subtract,multiply,divide
from src._3_statistics import mean, median, mode , fmean
from src._4_palindrome import palindrome
from src._5_obfuscator import obfuscate
from src._6_random_string import random_string
from src._7_ip_private import get_ip
from src._8_ip_public import get_public_ip
from src._9_sum import sum_number


@click.group()
def cli():
    pass

#1
cli.add_command(lower)
cli.add_command(upper)
cli.add_command(capitalize)

#2
cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)

#3
cli.add_command(mean)
cli.add_command(median)
cli.add_command(mode)
cli.add_command(fmean)

#4
cli.add_command(palindrome)

#5
cli.add_command(obfuscate)

#6
cli.add_command(random_string)

#7
cli.add_command(get_ip)

#8
cli.add_command(get_public_ip)

#9
cli.add_command(sum_number)


if __name__ == "__main__":
    cli()
