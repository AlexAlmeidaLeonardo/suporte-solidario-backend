from enum import Enum

class TipoUsuario(Enum):
    CLIENTE = 1
    COLABORADOR = 2
    AMBOS = 3
    MASTER = 99