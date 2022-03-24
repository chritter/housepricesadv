Commands
========

The Makefile contains the central entry points for common tasks related to this project.

Syncing data to S3
^^^^^^^^^^^^^^^^^^

* `make sync_data_to_s3` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://houseproices/data/`.
* `make sync_data_from_s3` will use `aws s3 sync` to recursively sync files from `s3://houseproices/data/` to `data/`.


Download data from Kaggle
^^^^^^^^^^^^^^^^^^^^^^^^^

* `kaggle competitions download -c house-prices-advanced-regression-techniques` will download the data from Kaggle.