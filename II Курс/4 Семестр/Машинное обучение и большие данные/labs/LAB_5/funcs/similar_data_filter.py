import pandas as pd
import numpy as np

def filter_similar_rows(
    df: pd.DataFrame,
    threshold: float = 0.03,
    id_column: str = None,
    ignore_columns: list = None
) -> pd.DataFrame:
    """
    Удаляет строки, где числовые значения отличаются меньше чем на threshold от разброса.
    
    Параметры:
    ----------
    df : pd.DataFrame
        Входной датафрейм (может содержать категориальные столбцы).
    threshold : float, default=0.03
        Порог фильтрации (например, 0.03 = 3% от разброса значений).
    id_column : str, optional
        Столбец-идентификатор (если нужно явно указать, какие столбцы не учитывать).
    ignore_columns : list, optional
        Список столбцов, которые следует игнорировать при анализе (например, категориальные).
        
    Возвращает:
    -----------
    pd.DataFrame
        Отфильтрованный датафрейм.
    """
    df_filtered = df.copy()

    numeric_cols = df_filtered.select_dtypes(include=[np.number]).columns.tolist()

    if ignore_columns:
        numeric_cols = [col for col in numeric_cols if col not in ignore_columns]
    if id_column and id_column in numeric_cols:
        numeric_cols.remove(id_column)

    if not numeric_cols:
        print("Предупреждение: Нет числовых столбцов для анализа.")
        return df_filtered

    ranges = df_filtered[numeric_cols].max() - df_filtered[numeric_cols].min()
    thresholds = ranges * threshold

    mask = pd.Series(True, index=df_filtered.index)

    for col in numeric_cols:
        diff = df_filtered[col].diff().abs()
        diff.iloc[0] = np.inf
        mask &= (diff > thresholds[col])
    
    df_filtered = df_filtered[mask]
    
    return df_filtered.reset_index(drop=True)
