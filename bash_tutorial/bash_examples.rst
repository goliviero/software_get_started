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
