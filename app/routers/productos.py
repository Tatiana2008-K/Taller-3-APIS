from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.schemas import ProductoCreate

router = APIRouter(prefix='/productos', tags=['Productos'])

@router.get('/')
def listar_productos():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM productos')
            return cur.fetchall()
    finally:
        conn.close()

@router.post('/', status_code=201)
def crear_producto(producto: ProductoCreate):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                'INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)',
                (producto.nombre, producto.precio, producto.stock),
            )
        conn.commit()
        return {'id': cur.lastrowid, **producto.model_dump()}
    finally:
        conn.close()
