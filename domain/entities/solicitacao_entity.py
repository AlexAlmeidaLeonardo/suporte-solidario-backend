from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from base_entity import BaseEntity

@dataclass
class SolicitacaoEntity(BaseEntity):
    id_cliente: Optional[int] = None
    id_servico: Optional[int] = None
    data: Optional[datetime] = None
    detalhes: Optional[str] = None
    data_servico: Optional[datetime] = None
    em_aberto: Optional[bool] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[int] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None