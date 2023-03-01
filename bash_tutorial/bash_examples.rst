=================================================
Bash simple commands, some examples and use cases
=================================================

:Authors: Guillaume Oliviéro
:Date:    2023-01-26
:Contact: oliviero@cenbg.in2p3.fr

.. contents:: Table of Contents

Bash simple common commands
===========================

``RTFM``  (``Read The  Fucking Manual``),  the manual  for each  linux
command is available under ``man`` command. Example with ``ssh``:

.. code:: sh

   $ man ssh
..

It is pretty explicit and it's listing **ALL** options with examples.

One fun alternative is the ``tldr`` package. It stands for ``too long;
didn't   read``   which   is   a   common   expression   on   internet
forums. According to the command ``$ tldr tldr``, it display simple help
pages for command-line  tools from the tldr-pages  project. Install it
first and then try it on a dedicated command:

.. code:: sh

   $ sudo apt  install tldr

   # Example with the ssh command:
   $ tldr ssh

  ssh

  Secure Shell is a protocol used to securely log onto remote systems.
  It can be used for logging or executing commands on a remote server.
  More information: https://man.openbsd.org/ssh.

  - Connect to a remote server:
    ssh username@remote_host

  - Connect to a remote server with a specific identity (private key):
    ssh -i path/to/key_file username@remote_host

    # and so on....
..


Bash examples and use cases
===========================

Directory and file handling
---------------------------

.. code:: sh

   $ ls -l .
   dir1
   dir2
   dir3
   dir4
   dir5
..

If you want for example copy dir1 dir2 and dir3 but not dir4 and dir5,
instead of  doing it manually  one by one, you  can use an  inline for
loop bash command like this:


.. code:: sh

   $ for i in {1..3}; do scp -r ./dir${i} other_place/. ; done
..

``ì`` is the incremental variable. It shoul be protecred when used and
that's why we are using the braces ``{ }``.


Searching in dir/files
----------------------

One of the most useful command is ``grep``. You can search for a given
string recursively with the following command and it will show you all
the files where  the given string is. It find  patterns in files using
regular expressions.  The ``-i`` option is to ignore case distinctions
and ``-r`` option is to read all files under each directory. Note that
you should always  use ``" "`` caracters to be  sure it is interpreted
as a string, and the whitespaces or symbols are well interpreted.

.. code:: sh

   $ grep -ri "string_to_search"
..

Similar  function can  be to  use  find if  you  want to  search in  a
specific type of files.  As you can  see you can combine find and grep
command using ``-exec``.

.. code:: sh

   $ find . -type f -exec grep -l "wordtofind" {} \;
..

An other example where  it can search for a pattern in  a set of files
using find,  pipe ``|``, xargs  and grep  commands. In bash  there are
several methods to do the exact same thing and each one has advantages
and inconvenients.

.. code:: sh

   $ find . -name "*py" | xargs grep "import sys"
..


Print the Elapsed Time of Code Execution
----------------------------------------

.. code:: sh

   #!/bin/bash

   start_time=$(date +%s)

   # your code here

   end_time=$(date +%s)

   echo "Time elapsed: $(($end_time - $start_time)) seconds"
..

Search and Replace Strings in Files
-----------------------------------

Find a given string and replace it with an other string in a file

.. code:: sh

   $ find . -type f -exec grep -l "localhost:8000" {} \; | xargs sed -i 's/localhost:8000/localhost:8080/g'
..

Find a given string in a given file and delete the line containing the string:

.. code:: sh

   $ grep -rl 'string' file.txt | xargs sed -i '/string/d' file.txt
..

Delete Specific Files
---------------------

This command deletes all empty files ending with .log:

.. code:: sh

   $ find . -type f -name "*.log" -exec rm {} \;
..

To delete all files older than 25 days, run this command:

.. code:: sh

   $ find . -type f -mtime +25 -exec rm {} \;
..

Download and upload files from remote server
--------------------------------------------

For example: CCIN2P3

Use this command to download a file from a server and save it locally:

.. code:: sh

   $ scp username@server:path/to/file destination_path
..

Copy a local directory to a remote server:

.. code:: sh

   $ scp -r /local/dir username@server:/remote/dir
..

This command uploads a local file to a server under a new filename:

.. code:: sh

   $ scp file.txt username@server:/remote/dir/newfilename.txt
..

Copy Files Between Two Remote Servers:

.. code:: sh

   $ scp user1@server1:/dir1/file.txt user2@server2:/dir2
..
