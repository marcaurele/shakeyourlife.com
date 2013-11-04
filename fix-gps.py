#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os, sys, re, shutil

def edit_file(filename):
	input = open(filename, encoding='utf-8')

	summary = ''

	# Searching for the summary
	for line in input:
		m = re.search('(?<=message\:\").{40}', line)
		if m:
			sys.stdout.write(m.group(0)+'\n')
			summary = m.group(0)

	input.close()

	# Writing the new summary in the file
	input = open(filename, encoding='utf-8')
	output = open(filename+'-temp', 'w', encoding='utf-8')
	i=0
	for line in input:
		output.write(line)
		if i == 4:
			output.write('Summary: ' + summary + '...\n')
		i+=1

	input.close()
	output.close()

	# Move temp file to old gps file
	shutil.move(filename+'-temp', filename)


directory = sys.argv[1]

for file in os.listdir(directory):
	gf = re.search('\.md', file)
	if gf:
		sys.stdout.write(file + '\n')
		edit_file(directory + file)



