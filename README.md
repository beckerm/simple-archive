# simple_archive

optional arguments:
  -h, --help (Show this help message and exit)
  -s SOURCE, --source SOURCE (Source directory.)
  -a ARCHIVE, --archive ARCHIVE (Archive directory.)
  -d DAYS, --days DAYS  (Days old.)
  -r REGEX, --regex REGEX (Regular expression. Default = ".*")

Examples:

Archive all files older than 90 days.
./archive_files.py -s /Users/larry/Desktop/stuff -a /Users/larry/storage -d 90 

Archive all .png .jpg .gif files older than 90 days.
./archive_files.py -s /Users/larry/Desktop/stuff -a /Users/larry/storage -d 90 -r '.png$|.jpg$|.gif$'

