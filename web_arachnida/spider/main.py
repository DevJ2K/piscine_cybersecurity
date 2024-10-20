#!/usr/bin/python3
import requests
import argparse

def spider(url: str):
	pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog='spider',
		description='What the program does',
		epilog='Text at the bottom of help')

	parser.add_argument('filename')           # positional argument
	parser.add_argument('-c', '--count')      # option that takes a value
	parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

	args = parser.parse_args()
	print(args.filename, args.count, args.verbose)
	# print("Hello !")
