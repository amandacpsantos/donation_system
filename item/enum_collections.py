from enum import Enum


class Gender(Enum):
    DESPINIVEL = 'Disponivel'
    INDISPONIVEL = 'Indisponível'
    EM_DOACAO = 'Em Doação'
    DOADO = 'Doado'


class Race(Enum):
    VESTUARIO = 'Vestuário'
    FINANCEIRO = 'Financeiro'
    MOVEIS = 'Moveis'
