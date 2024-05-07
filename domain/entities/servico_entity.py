from dataclasses import dataclass
from typing import Optional
from base_entity import BaseEntity

@dataclass
class ServicoEntity(BaseEntity):
    id_categoria: Optional[int] = None
    descricao: Optional[str] = None