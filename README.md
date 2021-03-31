# Remote-control
Remote control software project



Most of the documentation is done at caiusinfo.data.blog, which is the project page. 
The blog posts go over all the project work being done.
If you're interested in the methods and processes beyond the code, please visit the project page. 
Project posts get released weekly, though changes come to github as they are made.

## As of 12.3.2021, the program is capable of:

- Executing commands remotely
- Establishing an encrypted connection between the server and the client
- Being undetected by Windows Defender (other antivirus not tested yet)
- Able to download/upload files to and from target
- Taking screenshots

Keep an eye out for any new releases, I typically release them after adding some important
functionality to the program. 

## ABOUT THE SCREENSHOT FUNCTION

Since adding the screenshot function, the program will no longer work unless the target has 
installed the necessary dependencies. This can be avoided by compiling the program into an .exe
using pyinstaller, though notice that the machine you compile it on also needs to have
the necessary dependencies or it still won't work. This is explained in further detail on the project page.


## KNOWN BUGS

- Keylogger function can't be stopped after it started unless connection is terminated with "quit" command
- Invalid email error is not instant
