from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from base_entity import BaseEntity

@dataclass
class AtendimentoMensagemEntity(BaseEntity):
    id_atendimento: Optional[int] = None
    criacao: Optional[datetime] = None
    alteracao: Optional[datetime] = None
    is_cliente: Optional[bool] = None
    mensagem: Optional[str] = None
    id_em_resposta: Optional[int] = None