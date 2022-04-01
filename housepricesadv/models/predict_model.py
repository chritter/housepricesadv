import pandas as pd


class Predictor:
    """
    The Predictor class allows for the application of the models.
    """
    
    def __init__(self) -> None:
        pass

    def predict(self, X: pd.DataFrame, y: pd.Series) -> pd.Series:
        """
        _summary_

        Parameters
        ----------
        X : pd.DataFrame
            _description_
        y : pd.Series
            _description_

        Returns
        -------
        pd.Series
            _description_
        """
        return pd.Series(data=0, index=X.index)

