"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Eight

This program establishes an FTP connection to a remote server.
"""

from ftplib import FTP
import ftplib

SERVER = 'ftp.gnu.org'
FILENAME = 'README'
BLOCK_SIZE = 1024

try:
    print("Connecting to: ", SERVER)
    ftp = FTP(SERVER)
    print("Welcome message: ", ftp.getwelcome())

    print("Logging in as anonymous user.")
    ftp.login()

except ftplib.all_errors as e:
    print(str(e))

else:
    print("Current working directory: ", ftp.pwd())
    print("Directory listing:")
    ftp.retrlines('LIST')

    print("Downloading ", FILENAME)
    localfile = open(FILENAME, 'wb')
    ftp.retrbinary('RETR ' + FILENAME, localfile.write, BLOCK_SIZE)

    print("Closing connection...")
    ftp.quit()
    localfile.close()

""" PROGRAM RUN
Connecting to:  ftp.gnu.org
Welcome message:  220 GNU FTP server ready.
Logging in as anonymous user.
Current working directory:  /
Directory listing:
lrwxrwxrwx    1 0        0               8 Aug 20  2004 CRYPTO.README -> .message
-rw-r--r--    1 0        0           17864 Oct 23  2003 MISSING-FILES
-rw-r--r--    1 0        0            4178 Aug 13  2003 MISSING-FILES.README
-rw-r--r--    1 0        0            2509 Oct 13  2017 README
-rw-r--r--    1 0        0          405121 Oct 23  2003 before-2003-08-01.md5sums.asc
-rw-rw-r--    1 0        3003       259362 Nov 25 11:25 find.txt.gz
drwxrwxr-x  319 0        3003        12288 Nov 16 22:31 gnu
drwxrwxr-x    3 0        3003         4096 Mar 10  2011 gnu+linux-distros
-rw-rw-r--    1 0        3003       476020 Nov 25 11:25 ls-lrRt.txt.gz
drwxr-xr-x    3 0        0            4096 Apr 20  2005 mirrors
lrwxrwxrwx    1 0        0              11 Apr 15  2004 non-gnu -> gnu/non-gnu
drwxr-xr-x   90 0        0            4096 Mar 31  2015 old-gnu
lrwxrwxrwx    1 0        0               1 Aug 05  2003 pub -> .
drwxr-xr-x    2 0        0            4096 Nov 08  2007 savannah
drwxr-xr-x    2 0        0            4096 Aug 02  2003 third-party
drwxr-xr-x    2 0        0            4096 Apr 07  2009 tmp
drwxr-xr-x    2 0        0            4096 May 07  2013 video
-rw-r--r--    1 0        0            1344 Oct 13  2017 welcome.msg
Downloading  README
Closing connection...

Process finished with exit code 0
"""
