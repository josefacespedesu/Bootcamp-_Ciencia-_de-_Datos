import pandas as pd
# 2) Cargar el CSV con punto y coma
df_pedidos = pd.read_csv("pedidos.csv", sep=",")
print("CSV cargado:", df_pedidos.shape)
df_pedidos.head()
dfs_excel = pd.read_excel("Clientes.xlsx", sheet_name=None)
print("Hojas en Excel:", list(dfs_excel.keys()))
# Acceder a una hoja
df_clientes = dfs_excel["clientes"]
df_clientes.head()

# Acceder a una hoja
df_empleados = dfs_excel["empleados"]
df_empleados.head()
# mirar las columnas de todos los df
df_clientes.columns, df_empleados.columns, df_pedidos.columns
# 1) Pedidos + Clientes (por IdCliente)
df_final = df_pedidos.merge(
    df_clientes,
    on="IdCliente",
    how="left"
)

# 2) + Empleados (por IdEmpleado)
df_final = df_final.merge(
    df_empleados,
    on="IdEmpleado",
    how="left"
)

df_final.head()
df_final.columns
df_final = df_final.rename(columns={
    "Cargo_x": "CargoEnvio",
    "Cargo_y": "CargoEmpleado"
})
df_final.head()
df_final.columns
# eliminamos: "Longitud","Latitud" 
df_final = df_final.drop(columns=["Longitud","Latitud"], errors="ignore")
# finalmente nuestro df:
df_final.head()
# 6) Guardar consolidado a CSV
df_final.to_csv(
    "consolidado.csv",
    index=False,
    encoding="utf-8-sig"
)
print("Archivo guardado")