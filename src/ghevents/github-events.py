#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
# This function returns data from url as a dictionary
	data = requests.get(url).text
	return json.loads(data)

def print_events(events, n=5):
# This function prints the type and repo name for n events
	for x in events[:n]:
    		event = x['type'] + ' :: ' + x['repo']['name']
    		print(event)

def main():
	print(GHUSER)
	print(url)
	list = retrieve_events(url)
	print_events(list)

if __name__ == "__main__":
    main()

