============
Git tutorial
============

:Authors: Guillaume Oliviéro
:Date:    2023-02-17
:Contact: oliviero@cenbg.in2p3.fr

.. contents:: Table of Contents

Goal of the tutorial
====================

- Set-up git SSH keys for cloning and push
- Learn the git flow
- Learn how to use properly a git repository
- Understand the branching concepts


Introduction
============

What is git?
------------

``Oh  baby, don't  loose me.  Don't  loose me.  No more``.   Git is  a
powerful and free versioning system usually used for coordinating work
among  programmers  collaboratively   developing  source  code  during
software development.


Why using git?
--------------

- Backup and save your work
- Powerful version system if you want to roll back
- Most used collaborative tool for code
- You can use  it for your codes, manuals BUT  also your presentations
  AND your thesis ;)


Set-up SSH keys
===============

You must follow this small github documentation guide:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key

Bash commands

.. code:: sh

   $ ssh-keygen -t ed25519 -C "your_email@example.com"

   $ eval "$(ssh-agent -s)"

   $ open ~/.ssh/config

   $ touch ~/.ssh/config # if the config file doesn't exist

   $ ssh-add --apple-use-keychain ~/.ssh/id_ed25519
..

Now instead of using HTTPS to clone a repository OR each time you want
to commit something, it will be done through SSH keys.


Git step-by-step
================

Step 1: Creating your first repository on the github interface
--------------------------------------------------------------


.. figure:: img/step_1_repo.png
   :width: 1800

   Under your account, click on Repositories and New

.. figure:: img/step_1_create_repo.png
   :width: 1800

   Give a name  and a short description to your  repository.  Tick the
   ``Add  a README  file`` box  and choose  a convenient  License. GNU
   General Public License can be chosen

Step 2: Cloning your repository
-------------------------------

Cloning your new repository into your ``/home/user/~``:

.. code:: sh

   $ cd ~
   $ git clone https://github.com/YOURUSERNAME/git-test-repo.git
   # Replace username and the name of your new git repo, mine is under goliviero/git-test-repo.git
   $ cd git-test-repo/
..

.. figure:: img/step_2_clone_ssh.png
   :width: 1800

   Cloning using SSH keys

Step 3: Stage new files
-----------------------

Creating a src directory:

.. code:: sh

   $ mkdir src/
..

Creating an empty cxx program:

.. code:: sh

   $ touch src/test.cxx
..

See the status of your repository:

.. code:: sh

   $ git status
..

.. figure:: img/step_3_git_status.png
   :width: 1200

   Git status initial before stage and commit

For now, the file is only existing  locally. We want to add your first
CPP program to  your repository. First, we will  ``stage`` (track) the
file we want:

.. code:: sh

   $ git add src/test.cxx
..

See the status again of your repository:

.. code:: sh

   $ git status
..


.. figure:: img/step_3_git_status_staged.png
   :width: 1200

   Git status after ``git add`` while staged



Step 4: Commit new staged files
-------------------------------

After  stagging your  file, we  want to  commit your  new file  to the
branch we are working on. For now, we are on the ``main`` branch.

.. code:: sh

   $ git commit -m "Add a test cpp program to my repository"
..

.. figure:: img/step_4_git_status_commit.png
   :width: 1200

   Git status after ``git commit`` and before the push


The ``-m`` option allows you to do an inline commit message. Otherwise
it  will open  an editor  inside the  terminal but  you can  give more
details about your commit.

HOW TO RIGHT A GOOD COMMIT MESSAGE - few recommandations:
.........................................................

- Keep it short
- Use the imperative mood
- Add a short title
- Add a body (explain WHAT the change is, but especially WHY the change was needed)

- Good examples:

  - `Enable Logging Globally`
  - `Add Account Delete Route`
       `Needed for account deletion workflow on frontend`

- Bad examples:

  - `debugging`
  - `update`
  - `I've added a delete route to the accounts controller`


Step 5: Push files remotely
---------------------------

Once stagged and commit, we want to push the file to the online remote
repository:

.. code:: sh

   $ git push
..


.. figure:: img/step_5_git_push.png
   :width: 1000

   Git push on the ``main`` branch

Your file has been pushed to your ``main`` branch.

Step 6: Create a new branch and push it
---------------------------------------

Git  branches  are  effectively  a  pointer  to  a  snapshot  of  your
changes. When you want to add a new feature or fix a bug—no matter how
big or how  small—you spawn a new branch to  encapsulate your changes.
A branch  in Git  is simply  a lightweight movable  pointer to  one of
these  commits.  The default  branch  name  in  Git is  ``master``  or
``main``.

.. figure:: img/step_6_git_branch_drawing.png
   :width: 1800

First we start from our ``main`` branch:

.. figure:: img/step_6_git_branch_main.png
   :width: 1600

   Make sure the starting point is the main branch in most cases

Creating a  new branch for a  dedicated feature. Here we  will add two
empty classes in our src/ directory.

First we have to create the new branch ``feature_add_classes``.

.. code:: sh

   $ git checkout -b feature_add_classes
..

the ``-b``  option allow us to  create a branch and  switch (i.e ``git
checkout``) directly on it.

.. figure:: img/step_6_git_branch_checkout_feature.png
   :width: 1800

   Switching to the new feature branch just created


Then create  the two empty classes  named ``foo`` and ``bar``  on this
new branch.

.. code:: sh

   $ cd src
   $ touch foo.cpp foo.hpp bar.cpp bar.hpp
..

Stage  all  the  files  at  once   in  the  src  directory  on  branch
``feature_add_classes``:

.. code:: sh

   $ git add *
..

.. figure:: img/step_6_git_add_star.png
   :width: 1000

   Stage all new files at once with ``git add *``

Before   commit,   check   we   are  in   the   right   branch   (i.e:
feature_add_classes):

.. code:: sh

   $ git branch
..

.. figure:: img/step_6_git_check_branch.png
   :width: 1200

   Checking we are on the good branch before commit and push


Commit the  two classes to  the ``feature_add_classes`` branch  with a
good and explicit commit message:

.. code:: sh

   $ git commit -m "Add two empty classes named foo and bar"
..

First push to the upstream branch. If you try to just:

.. code:: sh

   $ git push
..

You'll see a fatal error message:

.. figure:: img/step_6_git_push_branch_remote_error.png
   :width: 1600

   Push error message because the current local branch as no upstream branch

The current  branch ``feature_add_classes``  is only existing  on your
local machine and  has no ``upstream`` branch remotely. We  should set the
``remote`` as ``upstream`` using:

.. code:: sh

   $ git push --set-upstream origin feature_add_classes
..

.. figure:: img/step_6_git_push_branch_remote_push.png
   :width: 1700

   Commit and push the new branch complete

For the next pushes on this branch it  will be set so you can just use
``$ git push``.

BRANCH NAMING CONVENTIONS:  as for the commits, you  should be concise
and explicit about what you want to do with a branch. You can indicate
if you want to  add a new feature with the  prefix ``feature-``, fix a
bug with ``bugfix-``  prefix, test with ``test-`` and so  on. Then you
should describe briefly the purpose.


Step 7: Open a merge/pull request
---------------------------------

Opening a merge request through the git interface.

.. figure:: img/step_7_mr_page.png
   :width: 1700

   Git interface  for the repository.  Click on Pull Requests  and you
   will open the interface where you can easily open one

.. figure:: img/step_7_mr_page_2.png
   :width: 1700

   Interface to create a new Pull Request

.. figure:: img/step_7_mr_creation.png
   :width: 1700

   Choose the feature branch you want to merge into the main branch

.. figure:: img/step_7_mr_creation_message.png
   :width: 1700

   Describe what your changes will do to the code

.. figure:: img/step_7_mr_creation_success.png
   :width: 1700

   The  merge request  is  now  open and  someone  else  (or you)  can
   crosshcheck  your  changes  and  then  accept  or  not  your  merge
   request. It is  a space of discussion where someone  can ask you to
   do some modifications and so on.

.. figure:: img/step_7_mr_creation_success_2.png
   :width: 1700

   Accepted merge request (``Merged``)


Note 1: merge request and pull request are the same thing.

Note  2: we  can do  it with  the  command line  but it  is much  less
convenient. I'll let you look online for this.

Step 8: Pull and update your repository
---------------------------------------

Pull the changes in your main local branch from remote

.. figure:: img/step_8_git_checkout.png
   :width: 1200

   Checkout  the  ``main`` branch  after  the  ``feature`` branch  was
   merged into the ``main`` on the remote git interface

.. code:: sh

   $ git pull --all
..

The ``--all`` option allows you to pull  the commits as well as all of
the branches from the remote.

The changes you made on the feature  branch are now on the main branch
and the 2 new classes ``foo`` and ``bar`` are available.

Step 9: Delete your branch localy and remotely
----------------------------------------------

Deleting the branch you worked on (i.e ``feature_add_classes``  branch).

You can delete it through the  git interface after accepting the merge
request.

But  you can  also delete  it  manually and  push this  from local  to
remote.  First of  all, git  won't let  you remove  the branch  you're
sitting on so you must make sure to checkout a branch that you are NOT
deleting:

.. code:: sh

   $ git checkout main
..

Delete the branch locally:

.. code:: sh

   $ git branch -d feature_add_classes
..

.. figure:: img/step_9_delete_branch.png
   :width: 1700

   Deleting localy the ``feature`` branch

Then propagate it remotely:

.. code:: sh

   $ git push origin --delete feature_add_classes
..

.. figure:: img/step_9_delete_branch_remote.png
   :width: 1700

   Deleting remotely the ``feature`` branch



and see the result on your git repository interface:

.. figure:: img/step_9_delete_branch_interface.png
   :width: 1700

   Git  repository interface  without  the feature  branch because  we
   deleted it


Useful git commands
===================

In this section I will provide some useful git commands.

Reset a commit not pushed to remote:

.. code:: sh

   $ git reset HEAD~1
..

Reset the last  commit pushed to remote:

.. code:: sh

   $ git revert HEAD
..

Git has the  ability to tag specific points in  a repository’s history
as being important.  Typically, people  use this functionality to mark
release  points (v1.0,  v2.0 and  so on).   List all  the tags  of the
repository:

.. code:: sh

   $ git tag -l
..

Create a new annotated tag (``-a`` option) with a tagging message (``-m`` option):

.. code:: sh

   $ git tag -a v2.0 -m "my version 2.0"
..

Add some your email, name and some aliases to your ``~/.gitconfig``:

.. code:: sh

   $ emacs ~/.gitconfig

   # Once in your gitconfig file you can put this basic gitconfig file:

   [alias]
     co = checkout
     br = branch
     ci = commit
     st = status

   [user]
     email = youremail@yourdomain.com
     name  = yourusername
..

Resources
=========

- Official git scm (source code mirror) documentation: https://git-scm.com/book/en/v2
- Git - the simple guide: https://rogerdudler.github.io/git-guide/
