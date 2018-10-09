from enum import Enum


class Status(Enum):
    REGISTERED = 'Cadastrado'
    AVAILABLE = 'Disponível'
    RESERVED = 'Reservado'
    DONATED = 'Doado'


class Categoria(Enum):
    CLOTHING = 'Vestuário'
    FURNITURE = 'Móveis'
    ELETRO = 'Eletrônicos/Eletrodomésticos'
    FOOD = 'Alimentos'
    HOUSEHOLD = 'Utensílios Domésticos'
    BOOK_OFFICE = 'Livraria/Papelaria'
    VOLUNTEER_WORK = 'Trabalho Voluntário'
