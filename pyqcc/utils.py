import pandas as pd

def qcc_groups(df: pd.DataFrame, values_col: str, group_col: str) -> pd.DataFrame:
    """
    Transpose data based on grouping dimension.\n
    Width is based on largest group size with NaN filling any blanks.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to be transposed. Minimum 2 columns.
    values_col : str
        Column name within df for values.
    group_col : str
        Column name within df for grouping dimension.
    
    Returns
    -------
    pd.DataFrame
        2d array of values.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f'Expected pandas DataFrame, got {type(df)}.')
    
    df = df[[values_col, group_col]]
    df = (df.groupby(group_col)[values_col]
              .apply(lambda df: df.reset_index(drop=True))
              .unstack()
              .reset_index()
            )
    df = df.iloc[:, 1:] # drop first col
    df = df.rename(
        columns={x:y for x,y in zip(df.columns, range(1, len(df.columns) + 1))}
    )
    return df