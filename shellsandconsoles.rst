Shells and Consoles: Windows into your Computer
================================================

We'll do a lot of work in a *console* which is a 
view of your computer you may not yet be familiar
with.

A *console* lets you issue *commands* that
manipulate your computer directly. The consoles
we will use are normally applications that you
can run from your normal programs menu. 

Look for a program with a name like:

* Konsole (KDE Linux)
* Gnome-Terminal (Gnome Linux)
* X-Term (Generic Linux, such as a Raspberry Pi)
* Terminal (OS-X)
* Windows Subsystem for Linux (WSL Ubuntu on Windows 10)

which, when run will connect you to a program
called a *shell* which is responsible for:

* listening to the commands you type
* trying to run those commands
* letting you see the results of the command

Your shell prompt should look something like this::

  example@397026a860f1:~$

Your console may have a blinking square, or a solid
white square just after the `$` character. You may
have a more involved shell prompt that tells you more 
information, but generally it will include:

* your linux username `example` here
* the machine you are running on `@397026a860f1` here
* your current directory `~` here (which means *your home directory*)
* the `$` character, which traditionally is used as the prompt on linux

As you work on the command line, you'll type commands
and hit the *Enter* key to tell the shell to execute
the commands. The shell may print out an error if it
doesn't know the command, or it may spend a long time
running the command, or it may just immediately spit
out the result of the command.

Exploring the Computer
-----------------------

Most computer *operating systems* use the idea of 
*directories* (sometimes called folders) and *files*.
These together are the *filesystem*.

Some *operating systems*, such as Linux or OS-X 
have a single tree of directories and files that
starts at the `/` directory (called the root directory).
Others, such as Windows, have a separate tree for 
every piece of storage (disks, usb keys) plugged into 
the machine.

Looking Around 
...............

Your *shell* (running in your *console*) keeps track
of *where* you are in the filesystem. We saw above
that many shells will display this as part of their
*prompt*.

You can ask the computer **where am I**::

  example@397026a860f1:~$ pwd
  /home/example

Which says, if you start at the root directory 
which is named `/` go to the sub-directory named
`home` and then to the sub-directory named `example`
which is where your console (shell) normally starts
when you open a console.

So why didn't pwd say `~` when we asked? `~` is a
shorthand meaning `my home directory`, which is
something that your administrator can set to a 
different location.

Let's ask **what is here**::

  example@397026a860f1:~$ ls -l
  total 0

Which tells us there are currently no files or directories 
in this home directory.

The `-l` part was what is called a *flag* that changes
how the `ls` command works. If we had called the ls command
*without* that flag, we would have seen::

  example@397026a860f1:~$ ls
  example@397026a860f1:~$

The flag here means *long* listing which includes a count
of the number of *things* the directory listing includes::

  example@397026a860f1:~$ ls -l ..
  total 4
  drwxr-xr-x 2 example example 4096 Apr 30 21:19 example

Here we added what's called an *argument*, a
thing on which to act. The special name
`..` means *the parent directory* of the 
current directory. So our command here means
"give me a long listing of the parent of this directory".

Moving Around
..............

We can change where we are in the shell with the command `cd` (change directory):

If we want to **go up a directory**::

  example@397026a860f1:~$ pwd
  /home/example
  example@397026a860f1:~$ cd ..
  example@397026a860f1:/home$ pwd
  /home
  example@397026a860f1:/home$ ls
  example
  example@397026a860f1:/home$ cd ..
  example@397026a860f1:/$ pwd
  /
  example@397026a860f1:/$ ls
  bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
  example@397026a860f1:/$ cd ~
  example@397026a860f1:~$

Here we've walked up from `/home/example` all
the way to the *root* directory `/` of the machine. We can see that this directory seems
to have a lot of directories inside of it,
one of which is the `home` directory.
We then jump right back to our home directory
by doing `cd ~`.

Moving Things Around
......................

You can create your own directories and files
in your home directory.

Let's **create a folder**::

  example@397026a860f1:~$ mkdir school-work
  example@397026a860f1:~$ ls
  school-work
  example@397026a860f1:~$ cd school-work/
  example@397026a860f1:~/school-work$

Let's create a file to move around:

  example@397026a860f1:~/school-work$ touch a-special-file.txt
  example@397026a860f1:~/school-work$ ls
  a-special-file.txt

Oh, but the file is in the wrong place, we want it in a folder just for this project:

  example@397026a860f1:~/school-work$ mkdir this-project
  example@397026a860f1:~/school-work$ mv a-special-file.txt this-project/
  example@397026a860f1:~/school-work$ ls
  this-project
  example@397026a860f1:~/school-work$ ls this-project/
  a-special-file.txt

After this, we've created a structure
that looks like this::

  /
  `-- home
      `-- example
          `-- school-work
              `-- this-project
                  `-- a-special-file.txt


Some Hints
-----------

* If you start a program and it doesn't come back, hitting `<ctrl-c>`
  (that is, holding down the ctrl key while you tap the c key)
  will generally stop a program
* If you want to know how to use a program, the program `man` will
  generally give you information about how to use a common program
* Most programs also can provide their own help if you pass `--help` to them
* The program `echo` will echo what you type
* You can put the output of a command into a file with::


    $ echo "A cat is cool" > somefile.txt

* There are thousands of commands
  available in Linux, either already installed,
  or installable by pulling in 
  new software
* A *command* is a piece of software, it is a reusable piece of code that can be called from the shell
* A *flag* is an optional argument you may add to a command to change how it behaves, normally it has a `-` character for short flags or a `--` for longer flag names.

Now that we can get around in the *shell*
let's move onto :doc:`starting python <startpython>`