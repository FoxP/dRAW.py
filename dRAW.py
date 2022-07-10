#!/usr/bin/env python
# -*- coding: utf-8 -*-

#	##### BEGIN GPL LICENSE BLOCK #####
#
#	This program is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License
#	as published by the Free Software Foundation; either version 2
#	of the License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software Foundation,
#	Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#	##### END GPL LICENSE BLOCK #####

#	Name :
#				dRAW.py
#	Author :
#				▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄▄▄▄▄▄
#				█ ▄▄▄ █ ██ ▀▄ █ ▄▄▄ █
#				█ ███ █ ▄▀ ▀▄ █ ███ █
#				█▄▄▄▄▄█ █ ▄▀█ █▄▄▄▄▄█
#				▄▄ ▄  ▄▄▀██▀▀ ▄▄▄ ▄▄
#				 ▀█▄█▄▄▄█▀▀ ▄▄▀█ █▄▀█
#				 █ █▀▄▄▄▀██▀▄ █▄▄█ ▀█
#				▄▄▄▄▄▄▄ █▄█▀ ▄ ██ ▄█
#				█ ▄▄▄ █  █▀█▀ ▄▀▀  ▄▀
#				█ ███ █ ▀▄  ▄▀▀▄▄▀█▀█
#				█▄▄▄▄▄█ ███▀▄▀ ▀██ ▄

# DEPENDENCIES

import os
import sys
import argparse

# CONFIGURATION

# Example :
# Delete .dng file if no .jpg file (with same name) exists
RAW_EXTENSION = "dng"
JPG_EXTENSION = "jpg"
RAW_DIRECTORY_PATH = r"shared/Pictures/Raw"
JPG_DIRECTORY_PATH = r"shared/DCIM/Camera"

PROGRAM_NAME = "dRAW.py"
PROGRAM_VERSION = "1.0"

# Command-line interface
argParser = argparse.ArgumentParser(description=PROGRAM_NAME + " " + PROGRAM_VERSION)
argParser.add_argument('--dry-run', action='store_true', help='dry-run mode, do not delete anything')
args = vars(argParser.parse_args())

# MAIN PROGRAM

# Check if RAW and JPG directory paths exist
if not os.path.isdir(RAW_DIRECTORY_PATH):
	sys.exit("'RAW_DIRECTORY_PATH' does not exist : " + RAW_DIRECTORY_PATH)
if not os.path.isdir(JPG_DIRECTORY_PATH):
	sys.exit("'JPG_DIRECTORY_PATH' does not exist : " + JPG_DIRECTORY_PATH)

count_deleted = 0
count_kept = 0
count_error = 0

# Iterate over files from 'RAW_DIRECTORY_PATH'
for RAW_file_name in os.listdir(RAW_DIRECTORY_PATH):
	# RAW file path
	RAW_file_path = os.path.join(RAW_DIRECTORY_PATH, RAW_file_name)
	# JPG file path
	JPG_file_path = os.path.join(JPG_DIRECTORY_PATH, os.path.splitext(RAW_file_name)[0] + "." + JPG_EXTENSION)

	# Check if file (not a directory)
	if os.path.isfile(RAW_file_path):
		# Check if JPG file with same name exists
		if not os.path.exists(JPG_file_path):
			# --dry-run argument passed
			if args['dry_run']:
				# Do not delete anything
				print("TO DELETE : " + RAW_file_path)
				count_deleted += 1
			else:
				try:
				# Delete RAW file
					os.remove(RAW_file_path)
				except:
					print("ERROR DELETING : " + RAW_file_path)
					count_error += 1
				else:
					print("DELETED : " + RAW_file_path)
					count_deleted += 1
		else:
			if args['dry_run']:
				print("TO KEEP : " + RAW_file_path)
			else:
				print("KEPT : " + RAW_file_path)
			count_kept += 1

if args['dry_run']:
	print("SUMMARY : " + str(count_deleted) + " TO DELETE, " + str(count_kept) + " TO KEEP, " + str(count_deleted + count_kept) + " TOTAL")
else:
	print("SUMMARY : " + str(count_deleted) + " DELETED, " + str(count_kept) + " KEPT, " + str(count_error) + " DELETION ERROR, " + str(count_deleted + count_kept + count_error) + " TOTAL")