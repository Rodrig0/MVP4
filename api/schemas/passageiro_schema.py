from pydantic import BaseModel
from typing import Optional, List
from model.passageiro import Passageiro
import json
import numpy as np

class PassageiroSchema(BaseModel):
    """ Define como um novo passageiro a ser inserido deve ser representado
    """
    name: str = "Paulo"
    pclass: int = 2
    age: int = 35
    sibsp: int = 0
    parch: int = 0
    fare: float = 25.00
    sex: int = 1
    embarkedc: int = 0
    embarkedq: int = 1
    embarkeds: int = 0
    
class PassageiroViewSchema(BaseModel):
    """Define como um passageiro será retornado
    """
    id: int = 1
    name: str = "Paulo"
    pclass: int = 2
    age: int = 35
    sibsp: int = 0
    parch: int = 0
    fare: float = 25.00
    sex: int = 1
    embarkedc: int = 0
    embarkedq: int = 1
    embarkeds: int = 0
    outcome: int = None
    
class PassageiroBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do passageiro.
    """
    name: str = "Paulo"

class ListaPassageirosSchema(BaseModel):
    """Define como uma lista de passageiros será representada
    """
    passageiros: List[PassageiroSchema]

    
class PassageiroDelSchema(BaseModel):
    """Define como um passageiro para deleção será representado
    """
    name: str = "Paulo"
    
# Apresenta apenas os dados de um passageiro    
def apresenta_passageiro(passageiro: Passageiro):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassageiroViewSchema.
    """
    return {
        "id": passageiro.id,
        "name": passageiro.name,
        "pclass": passageiro.pclass,
        "age": passageiro.age,
        "sibsp": passageiro.sibsp,
        "parch": passageiro.parch,
        "fare": passageiro.fare,
        "sex": passageiro.sex,
        "embarkedc": passageiro.embarkedc,
        "embarkedq": passageiro.embarkedq,
        "embarkeds": passageiro.embarkeds,
        "outcome": passageiro.outcome
    }
    
# Apresenta uma lista de passageiros
def apresenta_passageiros(passageiros: List[Passageiro]):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassageiroViewSchema.
    """
    result = []
    for passageiro in passageiros:
        result.append({
            "id": passageiro.id,
            "name": passageiro.name,
            "pclass": passageiro.pclass,
            "age": passageiro.age,
            "sibsp": passageiro.sibsp,
            "parch": passageiro.parch,
            "fare": passageiro.fare,
            "sex": passageiro.sex,
            "embarkedc": passageiro.embarkedc,
            "embarkedq": passageiro.embarkedq,
            "embarkeds": passageiro.embarkeds,
            "outcome": passageiro.outcome
        })

    return {"passageiros": result}

