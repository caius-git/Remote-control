# Remote-control
Remote control software project

# PROJECT PAGE: https://caiusinfo.data.blog/

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
- If the host is not listening, the client will retry every 5 minutes
- Rest of the functionality can be read on the man pages down below

Keep an eye out for any new releases, I typically release them after adding some important
functionality to the program. 

## ABOUT THE SCREENSHOT FUNCTION

Since adding the screenshot function, the program will no longer work unless the target has 
installed the necessary dependencies. This can be avoided by compiling the program into an .exe
using pyinstaller, though notice that the machine you compile it on also needs to have
the necessary dependencies or it still won't work. This is explained in further detail on the project page.


## KNOWN BUGS

- Keylogger function can't be stopped after it started unless connection is terminated with "quit" command



## Man pages


Commands:

- Most system commands should work. Be careful when opening certain files (.txt etc) as the program can get stuck until the client closes said file.
- screenshot (home path). Takes a screenshot. Home path is optional, it'll use the current working directory without it and names the screenshot "screenshot.png". Be careful about overwriting important files.
- opensite (url) opens any website on the target machine, using the default web browser.
- upload (home path) (target path) . Alternatively you can only use the home path and it will upload the file to the current working directory.
- download (target path) (home path(optional)). Again, you can just use the target path and it'll use the default working directory.
- keylogger . By far the most complex command, which is why it'll deserve its own section.
- Quit . Stops the program on both ends and is the only way to terminate an existing keylogger session currently.

### Keylogger

Starting the keylogger:

**keylogger start** (IMPORTANT: CANNOT BE SHUT DOWN AFTER STARTING AS OF RIGHT NOW)

Default keylogger delivery method is through files, not email. To download the file, please use:

**keylogger download** . If the file doesn't exist yet, the keylogger hasn't captured anything.

To delete the keylogger file from the target machine, use:

**keylogger delete**

To change the keylogger delivery method:

**keylogger method (method**) . Valid methods are file/email. 

To change the frequency at which the keylogger updates, please use:

**keylogger timer (time between updates in seconds)**. Default timer is 15 seconds, it is recommended to change this if you're using email. 


Email credentials:

**keylogger email (username) (password)** . These are required in order to use the email mode.Note that depending on your email you'll have to allow less secure apps as well (gmail is an example). 
