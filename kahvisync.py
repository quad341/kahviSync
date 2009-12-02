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
_temp_dir = '/tmp'
_cache_dir = True

# internal variables
_host = 'ftp://ftp.scene.org/'
_ftpdir = 'pub/music/groups/kahvicollective/'

_files = []

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
   202\n"
   print "threadCount \t The number of simaltanious connections for downloading\n"
   print "format is a preference; if only one exists, it will be downloaded"

def getFTPInDir():
   global _host, _ftpdir
   ftp = FTP(_host)
   ftp.login()
   ftp.cwd(_ftpdir)
   return ftp

def getFileList():
   global _cache_dir
   data = []
   if _cache_dir:
      global _files
      data = _files
   # just return if we have a cache of something and are using it
   if len(data) > 0:
      return data
   ftp = getFTPInDir()
   ftp.dir(data.append)
   if _cache_dir:
      _files = data
   return data

def getRelease(releaseNumber):
   # we must find the release from the ftp directory and download the file
   # for threading support, we are spawning a new ftp connection to get the file
   # first figure out what full file name is for the number
   #   ex file:kahvi277_acrilic_colors-yves_klein_blue_(mp3).zip
   for file in getFileList():
      pass
   global _tmpdir
   ftp = getFTPInDir()
# vim: set sw=3 tw=80 :
