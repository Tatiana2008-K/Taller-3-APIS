from fastapi import APIRouter

router = APIRouter(prefix='/pedidos', tags=['Pedidos'])

@router.get('/')
def listar_pedidos():
    return {'mensaje': 'Lista de pedidos'}
