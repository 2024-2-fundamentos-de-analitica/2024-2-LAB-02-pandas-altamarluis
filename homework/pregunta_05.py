"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_05():
    data_frame = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    max_values_per_group = data_frame.groupby('c1')['c2'].max()
    return max_values_per_group
