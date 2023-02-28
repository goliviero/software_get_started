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

Just append them to the file.

Aliases
=======

More aliases for listing files:

.. code:: sh

   alias ll='ls -alF'
   alias la='ls -A'
   alias l='ls -CF'
..

Expand paths in the shell after a ${} variable:

.. code:: sh

   shopt -s direxpand
..

Connect through an SSH connection to a remote server more easily:

.. code:: sh

   alias remote_server="ssh -Y username@server"
..

SSHFS (Secure shell  file system) is a filesystem client  to mount and
interact  with directories  and files  located on  a remote  server or
workstation over a  normal ssh connection. It is  very convenient when
you want to work on a remote server  but interact with it as if it was
on  your  local machine.   You  must  have  a (really)  good  internet
connection for this usage otherwise  you will encounter some lags. One
example alias command to put in your bashrc:

.. code:: sh

   alias remote_scratch="sshfs -o reconnect,ServerAliveInterval=1  username@server:/location/ /home/username/Desktop/remote_scratch_home"

   # Then we can export a new local variable to make it more convenient:
   export REMOTE_SCRATCH_PATH="/home/username/Desktop/remote_scratch_home"
..

``Warning:  remote_scratch_home  must  be  an  already  created  empty
directory created BEFORE you do the sshfs command.``

Look for a process running (or not):

.. code:: sh

   alias process="ps -ax | grep -i"
   # usage : $ process firefox
..

Kill a process with a given PID (Process ID):

.. code:: sh

   alias kill="kill -9 $@"
   # usage : $ kill 3190
..

Exported variables
==================

The base directory of all my software (convenient path variable):

.. code:: sh

   export SW_WORK_DIR="/home/username/software"
..

If you  want to  change the color  when you ``ls``  in the  shell, see
`this link  <https://linuxhint.com/ls_colors_bash/>`_. For example,add
yellow color for some files (.root, .brio and .bin):

.. code:: sh

   export LS_COLORS="$LS_COLORS:*.root=33;1:*.brio=33;1:*.bin=31;1"
..


Functions
=========

Automatically update and upgrade your linux system:

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

Remove all  tilde files recursively. It  can be dangerous if  for some
reason you want to keep some backup tilde files:

.. code:: sh

   function remove_tilde_test()
   {
          echo "Removing tilde files '*~'..."
          `find . -name  "*~" -exec rm -rf {} \;`
          if [ $? -ne 1 ];
          then
          echo "INFO : Tilde files were removed successfully !"
          fi
   }
..

Launch emacs as  a daemon (once per session, it  will be persistent in
other shells):

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

Extract any compressed file:

.. code:: sh

   function extract()
   {
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
            *)           echo "Don't know how to extract '$1'..." ;;
	    esac
    else
	    echo "'$1' is not a valid file!"
    fi
   }
   export -f extract
..

Reset your paths and empty the variables you set previously:

.. code:: sh

   function do_reset_paths_and_variables()
   {
          # Reset the software variables we set previously :
          GEANT4_INSTALL_DIR=''
          ROOT_INSTALL_DIR=''
          CLHEP_INSTALL_DIR=''

          # Reset ${PATH} and ${LD_LIBRARY_PATH} variables
          source /etc/environment
          export PATH=/home/username/bin:/home/username/.local/bin:${PATH}
          export LD_LIBRARY_PATH=''
   }
   export -f do_reset_paths_and_variables
..

Mount the remote scratch using the alias defined above:

.. code:: sh

   function mount_remote_scratch()
   {
          remote_scratch
          echo "NOTICE: REMOTE_SCRATCH is mounted !" >&2
   }
..

Unmount the remote scratch:

.. code:: sh

   function umount_nemo_scratch()
   {
          fusermount -uz /home/username/Desktop/remote_scratch_home/
          echo "NOTICE: REMOTE_SCRATCH is unmounted !" >&2
   }
..

Setting up an environment: Source and export specific software in the shell
---------------------------------------------------------------------------

I'll give you a  full example of my physics base setup  when I want to
use some  software like  CLHEP, ROOT  and Geant4.  I  begin to  set up
these bricks and then add more and more specific software depending of
geant4  or ROOT  with  other functions  **AFTER**  sourcing first  the
``base`` softwares. This order is very important otherwise you'll face
some very weird issues.

.. code:: sh

   # The physics setup function:
   function do_base_physics_setup()
   {
          echo "[info] do_base_physics_setup: loading CLHEP GEANT4.10 ROOT6.20 and BxDecay0, will update PATH and LD_LIBRARY_PATH variables !" >&2

          # Add CLHEP to the PATH
          IF [ -n "${CLHEP_INSTALL_DIR}" ]; then
              echo "[warning] do_base_physics_setup: CLHEP is already setup, PATH was not updated !" >&2
              return 1
          fi
          export CLHEP_INSTALL_DIR="${SW_WORK_DIR}/common/CLHEP-install"
          export PATH=${CLHEP_INSTALL_DIR}/bin:${PATH}
          export LD_LIBRARY_PATH=${CLHEP_INSTALL_DIR}/lib:${LD_LIBRARY_PATH}
          echo "[info] do_base_physics_setup: CLHEP (v2.4.1.0) is now setup !" >&2

          # Add Geant4 to the PATH
          if [ -n "${GEANT4_INSTALL_DIR}" ]; then
              echo "[warning] do_base_physics_setup: Geant4 is already setup, PATH was not updated !" >&2
	          return 1
          fi
          export GEANT4_INSTALL_DIR="${SW_WORK_DIR}/common/geant4.9.6.p04/install"
          export GEANT4_ROOT=${GEANT4_INSTALL_DIR}
          source ${GEANT4_INSTALL_DIR}/bin/geant4.sh
          echo "[info] do_base_physics_setup: Geant4 (v4.9.6.p04) is now setup !" >&2

          # Add ROOT to the PATH
          if [ -n "${ROOT_INSTALL_DIR}" ]; then
              echo "[warning] do_base_physics_setup: ROOT is already setup, PATH was not updated !" >&2
              return 1
          fi
          export ROOT_INSTALL_DIR="${SW_WORK_DIR}/common/root-6.20.08-install"
          source ${ROOT_INSTALL_DIR}/bin/thisroot.sh
          echo "[info] do_base_physics_setup: ROOT  (v6.20.08) with PYTHON3 is now setup !" >&2
          echo "[info] do_base_physics_setup: PATH and LD_LIBRARY_PATH variables have been updated." >&2
          echo "[info] do_base_physics_setup: PATH=${PATH}" >&2
          echo "[info] do_base_physics_setup: LD_LIBRARY_PATH=${LD_LIBRARY_PATH}" >&2
          echo "[info] do_base_physics_setup: Exiting function... !" >&2
          return;
   }
   export -f do_base_physics_setup
..

As you can  see I am always  using relative paths based  on my generic
${SW_WORK_DIR}  variable.  It  means   that  I  can  copy-paste  these
functions in an other environment if I have the same software tree.


Once  this base  is setup,  I can  load the  next software  I want  to
use. Here I'll load Bayeux software with this function:

.. code:: sh

   # The Bayeux setup function:
   function do_bayeux_setup()
   {
          do_base_physics_setup # Automatically load the dependencies needed by Bayeux

          # Add Bxdecay0 to the PATH
          if [ -n "${BXDECAY0_INSTALL_DIR}" ]; then
              echo "[warning] do_bayeux_setup: BXDECAY0 is already setup, PATH was not updated !" >&2
	          return 1
          fi
          export BXDECAY0_INSTALL_DIR="${SW_WORK_DIR}/snemo/bxdecay0/install"
          export PATH=${BXDECAY0_INSTALL_DIR}/bin:${PATH}
          echo "[info] do_bayeux_setup: BXDECAY0 is now setup !" >&2


          if [ -n "${BAYEUX_INSTALL_DIR}" ]; then
              echo "[warning] do_bayeux_setup: Bayeux develop is already setup !" >&2
	          return 1
          fi
          export BAYEUX_INSTALL_DIR=${SW_WORK_DIR}/snemo/Bayeux-dev/install
          export PATH=${BAYEUX_INSTALL_DIR}/bin:${PATH}

          echo "[info] do_bayeux_setup: Bayeux develop is now setup !" >&2

          # Load SNRS setup to install Falaise
          if [ -n "${SNRS_INSTALL_DIR}" ]; then
              echo "[warning] do_bayeux_setup: SNRS develop is already setup !" >&2
	          return 1
          fi
          export SNRS_INSTALL_DIR=${SW_WORK_DIR}/snemo/SNRS/install
          export PATH=${SNRS_INSTALL_DIR}/bin:${PATH}
          echo "[info] do_bayeux_setup: SNRS is now setup !" >&2

          echo "[info] do_bayeux_setup: PATH and LD_LIBRARY_PATH variables have been updated." >&2
          echo "[info] do_bayeux_setup: PATH=${PATH}" >&2
          echo "[info] do_bayeux_setup: LD_LIBRARY_PATH=${LD_LIBRARY_PATH}" >&2
          echo "[info] do_bayeux_setup: Exiting function... !" >&2
          return;
   }
   export -f do_bayeux_setup
..

And then  I can  load Falaise  with this function  which is  the final
brick we are using in SuperNEMO:

.. code:: sh

   # The Falaise setup function:
   function do_falaise_setup()
   {
          do_bayeux_setup # Automatically load the Bayeux dependency
          if [ -n "${FALAISE_INSTALL_DIR}" ]; then
              echo "[warning] do_falaise_setup: Falaise develop is already setup !" >&2
              return 1
          fi
          export FALAISE_INSTALL_DIR=${SW_WORK_DIR}/snemo/Falaise-dev/install
          export PATH=${FALAISE_INSTALL_DIR}/bin:${PATH}

          echo "[info] do_falaise_setup: Falaise develop is now setup !" >&2

          echo "[info] do_falaise_setup: PATH and LD_LIBRARY_PATH variables have been updated." >&2
          echo "[info] do_falaise_setup: PATH=${PATH}" >&2
          echo "[info] do_falaise_setup: LD_LIBRARY_PATH=${LD_LIBRARY_PATH}" >&2
          echo "[info] do_falaise_setup: Exiting function... !" >&2
          return;
   }
   export -f do_falaise_setup
..

As you can  see, in Falaise setup functions calls  Bayeux function and
Bayeux function  calls the Base physics  setup. It means that  you can
only type  ``do_falaise_setup`` and everything  will be loaded  in the
good order.  It  can be useful to do  that **OR** to not do  it if you
want to really control which software you are loading. These functions
can be independant bricks if you remove the recursive calls.
