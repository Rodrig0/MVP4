from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from  model import Base

# colunas = Pclass, Age, SibSp, Parch, Fare, BinarySex, Embarked_C, Embarked_Q, Embarked_S, Outcome

class Passageiro(Base):
    __tablename__ = 'passageiros'
    
    id = Column(Integer, primary_key=True)
    name = Column("Name", String(50))
    pclass= Column("Pclass", Integer)
    age = Column("Age", Integer)
    sibsp = Column("SibSp", Integer, nullable=True)
    parch = Column("Parch", Integer, nullable=True)
    fare = Column("Fare", Float)
    sex = Column("BinarySex", Integer, nullable=True)
    embarkedc = Column("Embarked_C", Integer, nullable=True)
    embarkeds = Column("Embarked_Q", Integer, nullable=True)
    embarkedq = Column("Embarked_S", Integer, nullable=True)
    outcome = Column("Survived", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, pclass:int, age:int, sibsp:int, name:str, parch:int,
                 fare:float, sex:int, embarkedc:int, 
                 embarkedq:int, embarkeds:int, outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Passageiro

        Arguments:
        name: nome do passageiro
            pclass: classe do navio em que o passageiro estava
            age: idade do passageiro
            sibsp: número de irmãos/cônjuges a bordo
            parch: número de pais/filhos a bordo
            fare: valor da tarifa paga
            sex: sexo do passageiro
            embarkedc: embarque no porto de Cherbourg
            embarkedq: embarque no porto de Queenstown
            embarkeds: embarque no porto de Southampton
            outcome: sobreviveu ou não sobreviveu
            data_insercao: data de quando o passageiro foi inserido à base
        """
        self.name = name
        self.pclass = pclass
        self.age = age
        self.sibsp = sibsp
        self.parch = parch
        self.fare = fare
        self.sex = sex
        self.embarkedc = embarkedc
        self.embarkedq = embarkedq
        self.embarkeds = embarkeds
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao