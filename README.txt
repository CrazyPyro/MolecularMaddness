MolecularMaddness
===============

Entry in PyWeek #14  <http://www.pyweek.org/14/>
URL: https://github.com/CrazyPyro/MolecularMaddness
Team: CrazyPyro12
Members: CrazyPyro
License: see LICENSE.txt


Running the Game
----------------

On Windows or Mac OS X, locate the "run_game.pyw" file and double-click it.

Othewise open a terminal / console and "cd" to the game directory and run:

  python2 run_game.py


How to Play the Game
--------------------

2D puzzle game. Move molecules to thwart a mad scientist's evil plans.



Development notes 
-----------------

Creating a source distribution with::

   python setup.py sdist

You may also generate Windows executables and OS X applications::

   python setup.py py2exe
   python setup.py py2app

Upload files to PyWeek with::

   python pyweek_upload.py

Upload to the Python Package Index with::

   python setup.py register
   python setup.py sdist upload

