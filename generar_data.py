import pandas as pd
import numpy as np
import os

np.random.seed(42)

n_registros = 5000

tiendas = ['Tienda_01', 'Tienda_02', 'Tienda_03', 'Tienda_04']
productos = ['Bebidas', 'Snacks', 'Cigarros', 'Comida Rápida', 'Abarrotes']
turnos = ['Mañana', 'Tarde', 'Noche']

data = {
    'fecha': pd.date_range(start='2024-01-01', periods=n_registros, freq='H'),
    'tienda': np.random.choice(tiendas, n_registros),
    'producto': np.random.choice(productos, n_registros),
    'turno': np.random.choice(turnos, n_registros),
    'unidades_vendidas': np.random.poisson(lam=4, size=n_registros),
    'precio_unitario': np.round(np.random.uniform(2.5, 12.0, n_registros), 2)
}

df = pd.DataFrame(data)
df['venta_total'] = df['unidades_vendidas'] * df['precio_unitario']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(BASE_DIR, 'ventas_tienda_conveniencia.csv')
df.to_csv(ruta_csv, index=False)

print(f"Archivo creado en: {ruta_csv}")
