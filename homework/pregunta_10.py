"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_10():
    data_frame = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    result = data_frame.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()
    result = result.set_index('c1')
    return result