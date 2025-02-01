"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_12():
    data_frame = pd.read_csv('files/input/tbl2.tsv', sep='\t')
    data_frame['c5'] = data_frame['c5a'].astype(str) + ':' + data_frame['c5b'].astype(str)
    result = data_frame.groupby('c0')['c5'].apply(lambda x: ','.join(map(str, sorted(x)))).reset_index()
    return result