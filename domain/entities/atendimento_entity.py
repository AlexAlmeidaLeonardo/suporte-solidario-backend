from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from base_entity import BaseEntity

@dataclass
class AtendimentoEntity(BaseEntity):
    id_solicitacao: Optional[int] = None
    id_colaborador: Optional[int] = None
    atendido_em: Optional[datetime] = datetime.now()
    confirmado_em: Optional[datetime] = None
    finalizado_em: Optional[datetime] = None
    avaliacao: Optional[int] = None