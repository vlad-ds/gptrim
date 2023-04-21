gptrim
======

gptrim is a Python library designed to help you trim text inputs, making
it easier to fit more content within GPT’s context window. By
tokenizing, stemming, and removing spaces, this library prepares your
text inputs for efficient processing with GPT models.

Installation
------------

.. code:: commandline

   pip install gptrim

Usage
-----

.. code:: python

   from gptrim import trim

   text = "This is an example sentence to demonstrate gptrim usage."
   trimmed_text = trim(text)
   print(trimmed_text)
