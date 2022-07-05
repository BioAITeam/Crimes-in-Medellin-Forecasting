import pandas as pd
import io
import requests
from pandas.api.types import is_datetime64_any_dtype as is_datetime

cols = ['dataframe', 'col_num', 'tipo', 'nombre', 'total', 'registros','num_categorias', 'categorias_unicas', 'desc_info']
max_categories = 200


def get_df_from_url(url: str):
    content = requests.get(url).content
    return pd.read_csv(io.StringIO(content.decode('utf-8')), sep=";")


def concat_df_info(df: pd.DataFrame, name: str, data):
    return data.append(get_df_info(df, name))


def get_df_info(df: pd.DataFrame, name: str):
    df_info = pd.DataFrame(columns=cols)
    for i, col in enumerate(df.columns):
        dict_col = {'dataframe': name, 'col_num': i + 1, 'nombre': col, 'total': df.shape[0]}

        column = df[col]
        dict_col['registros'] = column.count()
        # Parsea la fecha a datetime
        if 'fecha' in col.lower():
            column = pd.to_datetime(column)

        # Guarda el tipo de dato de la columna
        type = column.dtype
        dict_col['tipo'] = str(type)

        # Guarda la informacion de la columna
        dict_col['desc_info'] = series_to_str(column.describe().fillna(0))

        # Si es fecha cuenta los valores por año
        if is_datetime(type):
            dict_col['tipo'] = 'fecha'
            dict_col['categorias_unicas'] = series_to_str(column.groupby(column.dt.year).count())
            dict_col['num_categorias'] = len(column.dt.year.unique())
        else:
            dict_col['num_categorias'] = len(column.drop_duplicates())
            if dict_col['num_categorias'] < max_categories:
                dict_col['categorias_unicas'] = series_to_str(df.groupby(col)[col].count())
            else: dict_col['categorias_unicas'] = f"mas de {max_categories}"
        df_info = df_info.append(dict_col, ignore_index=True)
    return df_info


def series_to_str(series: pd.Series):
    col_str = ''
    for i, x in series.items():
        col_str += f"{i}: {x}, "
    return col_str
