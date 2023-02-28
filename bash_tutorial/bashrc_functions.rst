=========================
Bashrc functions examples
=========================

:Authors: Guillaume Oliviéro
:Date:    2023-02-27
:Contact: oliviero@cenbg.in2p3.fr

.. contents:: Table of Contents

Introduction
============

The .bashrc file is a shell script  that is executed every time a user
opens a new shell. To edit it, open it using your favorite text-editor
(a.k.a emacs) ``emacs ~/.bashrc``.

We can now add  every alias or every function we  can imagine and want
persistent  when we  open  a new  shell.  I'm  giving  you few  useful
examples I am using in my own  ``.bashrc`` file. You can dig on github
or stackoverflow to find other useful (or not) bash commands.

Just add them at the end of the file

Aliases
=======

More aliases for listing files:

.. code:: sh

   alias ll='ls -alF'
   alias la='ls -A'
   alias l='ls -CF'
..

To add yellow color for some files (.root, .brio and .bin):

.. code:: sh

   export LS_COLORS="$LS_COLORS:*.root=33;1:*.brio=33;1:*.bin=31;1"
..


To expand paths in the shell after a ${} variable

.. code:: sh

   shopt -s direxpand
..


Functions
=========


To automatically update and upgrade your linux system:

.. code:: sh

   function do_linux_update()
   {
     echo "NOTICE: Updating, upgrading and cleaning linux !" >&2
     sudo apt autoremove
     sudo apt update
     sudo apt upgrade
     sudo apt autoremove
     sudo apt clean
     sudo -k
     echo "NOTICE: Linux was updated, upgraded and cleaned !" >&2
     return;
   }
   export -f do_linux_update
..

To remove all tilde files recursively. It can be dangerous if for some
reason you want to keep some backup tilde files.

.. code:: sh

   function remove_tilde()
   {
     echo "Removing tilde files '*~'..."
     `rm_tilde`
     if [ $? -ne 1 ];
     then
     echo "INFO : Tilde files were removed successfully !"
     fi
   }
..

To launch emacs as a daemon:

.. code:: sh

   function launch_emacs()
   {
    emacs --daemon
    echo "NOTICE: Emacs daemon is now setup"
    echo ""
    echo "***********"
    echo "WARNING: TO RESTORE ALL SAVED BUFFERS, DO : M-X ret : sk-desktop in the first emacs daemon !"
    echo "***********"
   }
..

To extract any compressed file:

.. code:: sh

   extract() {
    if [ -f $1 ] ; then
	    case $1 in
            *.tar.bz2)   tar xvf $1    ;;
            *.tar.gz)    tar xvf $1    ;;
            *.bz2)       bunzip2 $1    ;;
            *.rar)       unrar x $1    ;;
            *.gz)        gunzip $1     ;;
            *.tar)       tar xvf $1    ;;
            *.tbz2)      tar xvf $1    ;;
            *.tgz)       tar xvf $1    ;;
            *.zip)       unzip $1      ;;
            *.Z)         uncompress $1 ;;
            *.7z)        7z x $1       ;;
            *)           echo "don't know how to extract '$1'..." ;;
	    esac
    else
	    echo "'$1' is not a valid file!"
    fi
   }
..

To reset your paths and empty the variable you set previously:

.. code:: sh

function do_reset_paths_and_variables()
{
    # Reset the software variables we set previously :
    GEANT4_INSTALL_DIR=''
    ROOT_INSTALL_DIR=''
    CLHEP_INSTALL_DIR=''

    # Reset ${PATH} and ${LD_LIBRARY_PATH} variables
    source /etc/environment
    export PATH=/home/sheatz/bin:/home/sheatz/.local/bin:${PATH}
    export LD_LIBRARY_PATH=''
}
export -f do_reset_paths_and_variables
..
