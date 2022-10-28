# dwm status bar

This project comprises a series of scripts that show information on the status
bar. It is meant to be used with suckless‘ dynamic window manager (dwm).

## Features

It shows cpu and ram usage, used space in disk (using the path "/"), battery
level, battery changing status and current date and time. The battery only shows
up on laptops.

## Install

In order to use dwm status bar, you need to install the dependencies. Provided
you have python and (GNU) make, you can run the command:
```
sudo make install
```
Then, create a symbolic link with the command:
```
sudo make link
```
If you just cloned this repository, you can run both with:
```
sudo make
```
Although it is customary to create a virtual environment in most python
projects, in this case it is necessary to install the dependencies system wide.

To uninstall dwm status bar, run:
```
sudo make unlink
```

## Usage

You can run the script at anytime with the command:
```
dwm-status-bar
```
If you want the script to execute on startup (which you probably do), paste the
following snippet on your `.profile` (or whatever startup script you might be
using):
```
if [ "${XDG_SESSION_TYPE}" = x11 ]; then
	dwm-status-bar &
fi
```
To turn off the script, you can use the command:
```
dwm-status-bar close
```

## Configuring

The status bar can be configured using the following envirionment variables:
```
STATUS_BAR_NOTIFY=true
STATUS_BAR_NOTIFICATION_TIME=10
```
The first one controls wether it will send a message through the notification
daemon when the process terminates. It accepts the values "true" and "false".  
The second one sets the duration of the notification, in seconds.  
The defaults are the same as stated in the example above.

## Disclaimer

This project is a work in progress. It started from my personal need to put
useful information on the bar. If you have any doubts or if you found an error,
feel free to open an issue.
