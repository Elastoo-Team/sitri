Sitri - powerful settings & configs for python
============================================================

Installation
----------------

.. code:: bash

   poetry add sitri

or

.. code:: bash

   pip3 install sitri

Basics with SystemProvider
--------------------------

.. code:: python

   from sitri.providers.contrib import SystemConfigProvider
   from sitri import Sitri

   conf = Sitri(
       config_provider=SystemConfigProvider(prefix="basics"),
   )

System provider use system environment for get config data. For unique -
sitri lookup to “namespace” by prefix.

Example:

*In console:*

.. code:: bash

   export BASICS_NAME=Huey

*In code:*

.. code:: python

   name = conf.get_config("name")

   print(name)  # output: Huey


Contents
==========================

Practice
----------------

.. toctree::
   :maxdepth: 3

   getting_started

   advanced_usage

API Reference
-------------

.. toctree::
   :maxdepth: 3

   api



Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
