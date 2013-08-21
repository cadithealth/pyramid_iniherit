================================
INI File Inheritance for Pyramid
================================

The `pyramid-iniherit` package enables pyramid configuration INI file
inheritance via the "iniherit" package. See iniherit_ for
documentation on how to use INI file inheritance.

Installation
============

.. code-block:: shell

  $ pip install pyramid-iniherit


Usage
=====

To be able to use ``%inherit``-enabled INI files, do the following:

* Use ``i-pserve`` instead of ``pserve`` (same goes for pshell,
  proutes, pviews, ptweens, prequest, pscheduler, and alembic).

* Add this line **before** you import any pyramid, paster, or other
  server application module (such as in your WSGI loader):

  .. code-block:: python

    # add support for inherited INI files
    import pyramid_iniherit.install


That's it!


.. _iniherit: https://github.com/cadithealth/iniherit
