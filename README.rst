Hatem's Resume
==============

This repo contains the source files for my resume. You can find compiled
versions in PDF, HTML, or even .doc versions on http//nassrat.ca ... feel free
to contact me if you can't locate any of the pre-compiled versions or if having
trouble compiling this version.

Compiling
---------

.. code-block:: shell

    make -C resume/ # to print usage
    make -C resume/ pdf cpdf html # example

Dependencies
------------

On debian or compatible, install the following dependencies::

    sudo aptitutde install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended tth
