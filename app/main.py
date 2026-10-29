#importa la clase FastAPI y los routers de cada módulo
from fastapi import FastAPI  
from app.routers import clientes, productos, pedidos
# crea la aplicacion principal de fastAPI, aparece el nombre de la documentacion, version de la API, descripcion general del proyecto
app = FastAPI(title='Taller 3 ADSO - Tienda', version='3.0', description='API relacional: clientes, productos, pedidos y detalles')
#esto registra el router de clientes en la aplicacion, permite acceder a las rutas relacionadas con clientes
app.include_router(clientes.router)
#registra el router de productos, contiene los endpoints oara gestionar los productos 
app.include_router(productos.router)
#regustra el router de pedidos, contiene las rutas para crear y consultra pedidos
app.include_router(pedidos.router)

#define una ruta GET para la raíz de la aplicacion
@app.get('/', tags=['Inicio'])
def inicio():
    return {'mensaje': 'API tienda ADSO', 'documentacion': '/docs'}
