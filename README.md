# simple_archive

optional arguments:<br>
  -h, --help (Show this help message and exit)<br>
  -s SOURCE, --source SOURCE (Source directory.)<br>
  -a ARCHIVE, --archive ARCHIVE (Archive directory.)<br>
  -d DAYS, --days DAYS  (Days old.)<br>
  -r REGEX, --regex REGEX (Regular expression. Default = ".*")<br><br>

Examples:<br><br>

Archive all files older than 90 days.<br>
./archive_files.py -s /Users/larry/Desktop/stuff -a /Users/larry/storage -d 90<br><br> 

Archive all .png .jpg .gif files older than 90 days.<br>
./archive_files.py -s /Users/larry/Desktop/stuff -a /Users/larry/storage -d 90 -r '.png$|.jpg$|.gif$'<br><br>

