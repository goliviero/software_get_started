================================
Some bash examples and use cases
================================


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


Searching in files
------------------

.. code:: sh

   $ find . -type f -exec grep -l "wordtofind" {} \;
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

.. code:: sh

   $ find . -type f -exec grep -l "localhost:8000" {} \; | xargs sed -i 's/localhost:8000/localhost:8080/g'
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
