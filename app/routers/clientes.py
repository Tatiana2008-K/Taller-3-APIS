#importa apirouter oara crear rutas agrupadas, http es poara manejar errores HTTP
from fastapi import APIRouter, HTTPException
#importar la excepcion que se genra cuando se viola, una restriccion de integridad en MySQL
from pymysql.err import IntegrityError
#importar la funcion 
from app.database import conectar
from app.schemas import ClienteCrear, ClienteRespuesta, PedidoCliente

router = APIRouter(prefix='/clientes', tags=['Clientes'])

@router.get('', response_model=list[ClienteRespuesta])
def listar():
    with conectar() as db:
        with db.cursor() as cur:
            cur.execute('SELECT * FROM clientes ORDER BY id')
            return cur.fetchall()

@router.get('/{cliente_id}', response_model=ClienteRespuesta)
def obtener(cliente_id: int):
    with conectar() as db:
        with db.cursor() as cur:
            cur.execute('SELECT * FROM clientes WHERE id=%s', (cliente_id,))
            cliente = cur.fetchone()
    if cliente is None:
        raise HTTPException(404, 'Cliente no encontrado')
    return cliente

#RETO (A) = IMPLEMENTAR EL GET PARA VER TODOS LOS PEDISO Y ORDENADOS POR FECHA
@router.get('/{cliente_id}/pedidos', response_model=list[PedidoCliente])
def pedidos_cliente(cliente_id: int):
    with conectar() as db:
        with db.cursor() as cur:
            cur.execute( '''
            SELECT p.id, p.fecha, p.estado, p.total 
            FROM pedidos p 
            INNER JOIN clientes c ON p.cliente_id = c.id 
            WHERE c.id = %s 
            ORDER BY p.fecha
            ''',
            (cliente_id,)
            )
            pedidos = cur.fetchall()
            return pedidos
        
@router.post('', response_model=ClienteRespuesta, status_code=201)
def crear(datos: ClienteCrear):
    try:
        with conectar() as db:
            with db.cursor() as cur:
                cur.execute('INSERT INTO clientes (nombre,correo) VALUES (%s,%s)', (datos.nombre, str(datos.correo)))
                nuevo_id = cur.lastrowid
                cur.execute('SELECT * FROM clientes WHERE id=%s', (nuevo_id,))
                return cur.fetchone()
    except IntegrityError as exc:
        raise HTTPException(409, 'Correo ya registrado') from exc
