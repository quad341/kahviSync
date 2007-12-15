#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
kahvisync.py

Simple python script to sync kahvi collective releases to a certain directory.
Supports several options and multi-threaded downloads by default.

by James Wordelman <quad341@gmail.com>
"""

import sys
from ftplib import FTP

# parse parameters
def main(argv):
   try:
      opts, args = getopt.getopt(argv,"d:t:f:l:o:F:vh",["download=", "threads=",
      "first=", "last=", "out=","format=","verbose","help"])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-d","--download"):
         # this is either a single download or the spawn of itself
         getRelease(arg)
         sys.exit()
      elif opt in ("-t","--threads"):
         global _threads
         _threads = arg
      elif opt in ("-f","--first"):
         global _first
         _first = arg
      elif opt in ("-l","--last"):
         global _last
         _last = arg
      elif opt in ("-r","--rss"):
         global _rss
         _rss = arg
      elif opt in ("-v","--verbose"):
         global _verbose
         _verbose = 1
      elif opt in ("-h","--help"):
         fullUsage()
         sys.exit()
      elif opt in ("-o","--out"):
         global _outDir
         _outDir = arg
      elif opt in ("-F","--format"):
         if arg in ("mp3","ogg"):
            global _format
            _formt = arg
         else:
            usage()
            sys.exit(2)

def usage():
   print "Usage: %s [-d|--download releaseNumber] [-t|--threads threadCount]
   [-f|--first releaseNumber] [-l|--last releaseNumber] [-v|--verbose] [-o|--out
   outDir] [-F|--format mp3|ogg]"

def fullUsage():
   usage()
   print "releaseNumber \t The number of the release as a number (such as 1 or
   202"
   print "threadCount \t The number of simaltanious connections for downloading"

def getRelease(releaseNumber):
   # we must find the release from the ftp directory and download the file
# vim: set sw=3 tw=80 :
