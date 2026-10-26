from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.schemas import ClienteCreate

router = APIRouter(prefix='/clientes', tags=['Clientes'])

@router.get('/')
def listar_clientes():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM clientes')
            return cur.fetchall()
    finally:
        conn.close()

@router.post('/', status_code=201)
def crear_cliente(cliente: ClienteCreate):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # correo duplicado -> 409
            cur.execute('SELECT id FROM clientes WHERE email = %s', (cliente.email,))
            if cur.fetchone():
                raise HTTPException(status_code=409, detail='El correo ya está registrado')
            cur.execute(
                'INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)',
                (cliente.nombre, cliente.email, cliente.telefono),
            )
        conn.commit()
        return {'id': cur.lastrowid, **cliente.model_dump()}
    finally:
        conn.close()
