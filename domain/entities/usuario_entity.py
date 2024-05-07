from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.entities.base_entity import BaseEntity


@dataclass
class UsuarioEntity(BaseEntity):
    tipo_de_usuario: Optional[int] = None
    login: Optional[str] = None
    email: Optional[str] = None
    celular: Optional[str] = None
    password1: Optional[str] = None
    password2: Optional[str] = None
    ativo: Optional[bool] = True
    criacao: Optional[datetime] = None
    alteracao: Optional[datetime] = None