from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class Catalog(BaseModel):
    id: Optional[str] = Field(
        default=None,
        description="MongoDB ID - Se genera automáticamente desde el _id de MongoDB, no es necesario enviarlo en POST"
    )

    id_catalog_type: str = Field(
        description="ID del tipo de catálogo al que pertenece",
        examples=["507f1f77bcf86cd799439011"]
    )

    name: str = Field(
        description="Nombre del catálogo",
        min_length=1,
        max_length=100,
        examples=["Chocolates Premium", "Dulces Tradicionales"]
    )

    description: str = Field(
        description="Descripción detallada del catálogo",
        min_length=1,
        max_length=500,
        examples=["Colección especial de chocolates artesanales"]
    )

    cost: float = Field(
        description="Costo del catálogo",
        gt=0,
        examples=[150.50, 89.99]
    )

    discount: int = Field(
        description="Descuento en porcentaje (0-100)",
        ge=0,
        le=100,
        default=0,
        examples=[10, 25, 0]
    )

    active: bool = Field(
        default=True,
        description="Estado activo del catálogo"
    )
