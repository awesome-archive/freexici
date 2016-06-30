================
freexici
================


What is freexici module for?
------------------------------------

This module is made to scrape and generate random & usable web proxies.


Usage Example
-------------

.. code:: python

    >>> from freexici import freexici
    >>> proxy = freexici.randomProxy(many=1)
    >>> for p in proxy:
    ...     print p
    http://183.54.227.194:9797
    >>> proxies = freexici.randomProxy(many=5)
    >>> for proxy in proxies:
    ...     print proxy
    https://185.28.193.95:8080
    http://177.135.176.138:3128
    http://123.201.219.14:8080
    http://125.71.198.124:8998
    http://14.23.109.2:3128
    >>>


Installation
------------

Use pip:

.. code:: shell

    $ pip install -U freexici


Documentation
-------------

Documentation is available at https://github.com/brunobell/freexici/blob/master/README.rst


Contribution
============

Use github to submit bug,fix or wish request: https://github.com/brunobell/freexici/issues

