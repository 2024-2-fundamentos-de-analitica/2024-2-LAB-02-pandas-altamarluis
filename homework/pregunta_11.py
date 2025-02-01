"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_11():
    data_frame = pd.read_csv("files/input/tbl1.tsv", delimiter="\t")
    grouped_data = data_frame.groupby('c0')['c4'].agg(lambda x: ','.join(map(str, sorted(x))))
    new_df = grouped_data.reset_index()
    return new_df