High Park and Annette Coder's Club
===========================================

.. topic:: First Up! While you wait, Find Python

    * Get logged into your TDSB account

      * See Daniel or Betty-Lynn **immediately** if you need a password reset or don't have an account

    * Get Python started
    
      * |startbutton| Start Button | type "py" | Choose "Idle" or "Pyscripter 2.7" or "Python"

      * If you don't see it, choose another machine but *log out* first

    * Now ignore those computers! We have sandwiches to build after we say "Hi!"

.. |startbutton| image:: images/windowsstart.png
                 :alt: Windows Start Button

Who are You?
------------

* What do you want to learn?

* What do you want to do?

* What have you done already?

* Do you have any questions?

Sandwich Bot
------------

Our first challenge is to get the sandwich bot to make a sandwich.
This is the most important thing any robot can be taught to accomplish.

Reviewing the Sandwich Bot
--------------------------

What worked when we were programming the bot?
How did the robot make decisions?
How did we get the robot to finish the task?

Why Python?
-----------

* Relatively straightforward to learn and use
* Free and open source
* Useful in many domains

  * System tasks
  * Web and database programming
  * Bioinformatics (BioPython)
  * Data analysis and visualization

* Large global community

System Setup
------------

* You will need a `Python <http://www.python.org/download>`_ interpreter 
  (Python 2.7 for the current version of these tutorials)
  
  * Academic users may wish to use the `Enthought Python Distribution <http://www.enthought.com/products/getepd.php>`_
    but we do not use any special features of this distribution in this lesson 

* You will need a copy of this `project distribution <download.tar.gz>`_ 
  (the exercises and sample data files are included in the archive)
  
  * save and extract the ``download.tar.gz`` file into a new directory
  
    * ``mkdir python-lesson``
    * ``wget http://142.1.253.67/download.tar.gz``
    * ``tar -zxvf download.tar.gz``

  * the ``workshop`` directory contains a local copy of this site
  * the ``exercises`` directory contains the exercise and source-code samples 
    you will need to complete the session
  
* You will need a ``bash`` or similar shell

  * On windows you may wish to install the `Cygwin <http://cygwin.com/install.html>`_
    environment to obtain a copy of bash (and potentially Python)
  * On Linux or Mac OSX you should already have bash available
  
* test that you can run the exercise scripts (in the ``exercises`` folder)

    .. code-block:

        $ cd exercises 
        $ ./basicexercise.py
        $ # OR
        $ python basicexercise.py

  * Windows 
  
    * filename/extension on Windows
    * PATHEXT on Windows
    * cygwin setup


Contents
--------

.. toctree::
   :maxdepth: 2
   
   lessonplan
   links
   instructors
   todo
   readme

..
    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

