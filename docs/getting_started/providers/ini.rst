
Prepare
*******
**Just Relax**

Usage
******

.. hint::
    test.ini:

    .. code-block:: ini

            [section1]
            var1=s1v1
            var2=s1v2

            [section2]
            var1=s2v1
            var2=s2v2


.. code-block:: python

    from sitri.contrib.ini import IniConfigProvider


    conf = IniConfigProvider(
        ini_path="./test.ini",
    )

    print(conf.get("var1", "section1"))
    # Output: s1v1

    print(conf.get("var2", "section2"))
    # Output: s2v2
