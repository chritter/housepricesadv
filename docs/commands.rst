Commands
========

The Makefile contains the central entry points for common tasks related to this project.

Syncing data to S3
^^^^^^^^^^^^^^^^^^

Recursively sync files in `data/` up to `s3://houseprices/data/`.

.. code:: bash

    make sync_data_to_s3


Recursively sync files from `s3://houseprices/data/` to `data/`:

.. code:: bash

    make sync_data_from_s3

Download data from Kaggle
^^^^^^^^^^^^^^^^^^^^^^^^^

Download the data from Kaggle:

.. code:: bash

    kaggle competitions download -c house-prices-advanced-regression-techniques