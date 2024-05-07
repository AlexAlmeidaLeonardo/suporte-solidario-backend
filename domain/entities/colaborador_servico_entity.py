from dataclasses import dataclass
from typing import Optional
from base_entity import BaseEntity

@dataclass
class ColaboradorServicoEntity(BaseEntity):
    id_colaborador: Optional[int] = None
    id_servico: Optional[int] = None