import pandas as pd
import numpy as np


data = {'Producto': ['Pan', 'Jabón', 'Arroz', 'Cerveza', 'Galletas'],
        'Ventas': [80, 250, 600, 50, 300]}
ventas = pd.DataFrame(data)

def asignar_categoria(ventas):
    if ventas <= 100:
        return 'Baja'
    elif ventas <= 500:
        return 'Media'
    else:
        return 'Alta'

ventas['Categoría'] = ventas['Ventas'].apply(asignar_categoria)

total_ventas_categoria = ventas.groupby('Categoría')['Ventas'].sum()

def aplicar_descuento(df, porcentaje_descuento):
    df['Ventas'] = df['Ventas'] * (1 - porcentaje_descuento)


porcentaje_descuento = 0.1 
aplicar_descuento(ventas, porcentaje_descuento)


print("Ventas con categorías:")
print(ventas)
print("Total de ventas por categoría:")
print(total_ventas_categoria)