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
try:
   import thread as _thread
except ImportError:
   import dummy_thread as _thread

# defaults
# you may want to alter these so you don't have to specify command line args
_threads = 5 # set to 1 or above; number of simaltanious downloads
_first = 0 # 0 = not set
_last = 0 # 0 = not set
_verbose = 0 # 0 = off, 1 = on
_quiet = 0 # 0 = show errors, 1 = supress errors
_outDir = './'
_format = 'ogg' # ogg or mp3

# parse parameters
def main(argv):
   try:
      opts, args = getopt.getopt(argv,"d:t:f:l:o:F:vqh",["download=", "threads=",
      "first=", "last=", "out=","format=","verbose","quiet","help"])
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
      # removed rss support because it wouldn't actually help
      # ftp listing is more accurate for releases anyway
      #elif opt in ("-r","--rss"):
      #   global _rss
      #   _rss = arg
      elif opt in ("-v","--verbose"):
         global _verbose
         _verbose = 1
      elif opt in ("-q","--quiet"):
         global _quiet
         _quiet = 1
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
