from pydantic import BaseModel, EmailStr, Field

class ClienteCreate(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str | None = None

class ProductoCreate(BaseModel):
    nombre: str
    precio: float = Field(gt=0)  # precio negativo -> 422
    stock: int = Field(ge=0)
