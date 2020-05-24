#!/usr/bin/python
import sys
import json
import random
import argparse
import pkg_resources

DATA_PATH = pkg_resources.resource_filename('imbored', 'data/')

def display_fact():
    with open(DATA_PATH + 'facts.json') as f:
        data = json.load(f)
        fact_num = random.randint(0, len(data)-1)
        print(data[fact_num]['fact'][0])

def display_quote():
    with open(DATA_PATH + 'quotes.json') as f:
        data = json.load(f)
        quote_num = random.randint(0, len(data)-1)
        print(data[quote_num]['quote']['quote'])
        print("Author: ", data[quote_num]['quote']['author'])

def display_joke():
    file_num = random.randint(1, 11)
    with open(DATA_PATH + 'jokes_' + str(file_num) + '.json') as f:
        data = json.load(f)
        joke_num = random.randint(0, len(data)-1)
        print(data[joke_num]['joke'])

def display_random():
    num = random.randint(1, 3)
    if num == 1: display_fact()
    elif num == 2: display_quote()
    else: display_joke()

def main():
    print("\n\nWelcome to imbored!")
    print("You could also try: 'imbored fact', 'imbored joke' or 'imbored quote'.\n\n")

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        display_random()
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() in ["f", "fact"]:
            display_fact()
        elif sys.argv[1].lower() in ["q", "quote"]:
            display_quote()
        elif sys.argv[1].lower() in ["j", "joke"]:
            display_joke()
        else:
            display_random()
    print("\n")

if __name__ == "__main__":
    main()