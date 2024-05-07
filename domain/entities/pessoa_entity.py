from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from domain.entities.base_entity import BaseEntity

@dataclass
class PessoaEntity(BaseEntity):
    id_usuario: Optional[int] = None
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    cpf: Optional[str] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[int] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    ddd_telefone: Optional[str] = None
    telefone: Optional[str] = None
    ddd_celular: Optional[str] = None
    celular: Optional[str] = None
    email: Optional[str] = None
    ativo: Optional[bool] = None
    possui_coordenadas_gps: Optional[bool] = None
    criacao: Optional[datetime] = None
    alteracao: Optional[datetime] = None
    inativacao: Optional[datetime] = None