# -*- coding: utf-8 -*-
import logging
from pathlib import Path
import click
from dotenv import find_dotenv, load_dotenv
from sklearn import model_selection
import pandas as pd


def create_fold_file(file_in, file_out, n_splits=5, stratify=None):
    """
    takes training file (e.g. train.csv) and produces new file
    with additional column kfold, indicating the validation folds!

    Parameters
    ----------
    file_in : _type_
        _description_
    file_out : _type_
        _description_
    n_splits : int, optional
        _description_, by default 5
    stratify : _type_, optional
        _description_, by default None

    Examples
    --------
    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    """
    
    train = pd.read_csv(file_in,
                    keep_default_na=False, na_values=[""])
    
    # ensure training data is shuffled, do this outside/before of the folders
    train = train.sample(frac=1, random_state=42).reset_index(drop=True)
    
    if stratify:
        folder = model_selection.StratifiedKFold(n_splits=n_splits)
    else:
        folder = model_selection.KFold(n_splits=n_splits)
        
    for n_fold, (_, valid_idx) in enumerate(folder.split(X=train, y=stratify)):
        train.loc[valid_idx, "kfold"] = n_fold
    train['kfold'] = train['kfold'].astype(int)
 
    #fname = Path(file_in).stem
    # suffix = Path(file_in).suffix

    train.to_csv(file_out, index=False)


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    
    Parameters
    ----------
    input_filepath : _type_
        _description_
    output_filepath : _type_
        _description_
    """
    
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    
    create_fold_file(input_filepath, output_filepath,
                     n_splits=5, stratify=None)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
