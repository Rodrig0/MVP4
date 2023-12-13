import joblib
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Passageiro, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
passageiro_tag = Tag(name="Passageiro", description="Adição, visualização, remoção e predição de passageiros sobreviventes ou não do Titanic")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de passageiros
@app.get('/passageiros', tags=[passageiro_tag],
         responses={"200": PassageiroViewSchema, "404": ErrorSchema})
def get_passageiros():
    """Lista todos os passageiros cadastrados na base
    Retorna uma lista de passageiros cadastrados na base.
    
    Args:
        nome (str): nome do passageiro
        
    Returns:
        list: lista de passageiros cadastrados na base
    """
    session = Session()
    
    # Buscando todos os passageiros
    passageiros = session.query(Passageiro).all()
    
    if not passageiros:
        logger.warning("Não há passageiros cadastrados na base :/")
        return {"message": "Não há passageiros cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d passageiros encontrados" % len(passageiros))
        return apresenta_passageiros(passageiros), 200


# Rota de adição de passageiro
@app.post('/passageiro', tags=[passageiro_tag],
          responses={"200": PassageiroViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PassageiroSchema):
    """Adiciona um novo passageiro à base de dados
    Retorna uma representação dos passageiros e situação de sobrevivência associados.
    
    Args:
        name (str): nome do passageiro
        pclass (int): classe do navio em que o passageiro estava: Pclass
        age (int): idade do passageiro (anos): Age
        sibsp (int): número de irmãos/cônjuges a bordo: SibSp
        parch (int): número de pais/filhos a bordo: Parch
        fare (float): valor da tarifa paga ($): Fare
        sex (int): sexo do passageiro: BinarySexy
        embarkedc (int): embarque no porto de Cherbourg: Embarked_C
        embarkedq (int): embarque no porto de Queenstown: Embarked_Q
        embarkeds (int): embarque no porto de Southampton: Embarked_S
        
    Returns:
        dict: representação do passageiro e situação de sobrevivência associado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/classificador.pkl'
    scaler = joblib.load('ml_model/scaler.joblib')
    modelo = Model.carrega_modelo(ml_path, scaler)
    
    passageiro = Passageiro(
        name=form.name.strip(),
        pclass=form.pclass,
        age=form.age,
        sibsp=form.sibsp,
        parch=form.parch,
        fare=form.fare,
        sex=form.sex,
        embarkedc=form.embarkedc,
        embarkedq=form.embarkedq,
        embarkeds=form.embarkeds,
        outcome=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando passageiro de nome: '{passageiro.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se passageiro já existe na base
        if session.query(Passageiro).filter(Passageiro.name == form.name).first():
            error_msg = "Passageiro já existente na base :/"
            logger.warning(f"Erro ao adicionar passageiro '{passageiro.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando passageiro
        session.add(passageiro)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado passageiro de nome: '{passageiro.name}'")
        return apresenta_passageiro(passageiro), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo passageiro :/"
        logger.warning(f"Erro ao adicionar passageiro '{passageiro.name}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de passageiro por nome
@app.get('/passageiro', tags=[passageiro_tag],
         responses={"200": PassageiroViewSchema, "404": ErrorSchema})
def get_passageiro(query: PassageiroBuscaSchema):    
    """Faz a busca por um passageiro cadastrado na base a partir do nome

    Args:
        nome (str): nome do passageiro
        
    Returns:
        dict: representação do passageiro e situação de sobrevivência associado
    """
    
    passageiro_nome = query.name
    logger.debug(f"Coletando dados sobre o passageiro #{passageiro_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    passageiro = session.query(Passageiro).filter(Passageiro.name == passageiro_nome).first()
    
    if not passageiro:
        # se o passageiro não foi encontrado
        error_msg = f"Passageiro {passageiro_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar passageiro '{passageiro_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Passageiro encontrado: '{passageiro.name}'")
        # retorna a representação do passageiro
        return apresenta_passageiro(passageiro), 200
   
    
# Rota de remoção de passageiro por nome
@app.delete('/passageiro', tags=[passageiro_tag],
            responses={"200": PassageiroViewSchema, "404": ErrorSchema})
def delete_passageiro(query: PassageiroBuscaSchema):
    """Remove um passageiro cadastrado na base a partir do nome

    Args:
        nome (str): nome do passageiro
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    passageiro_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre o passageiro #{passageiro_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando passageiro
    passageiro = session.query(Passageiro).filter(Passageiro.name == passageiro_nome).first()
    
    if not passageiro:
        error_msg = "Passageiro não encontrado na base :/"
        logger.warning(f"Erro ao deletar passageiro '{passageiro_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(passageiro)
        session.commit()
        logger.debug(f"Deletado passageiro #{passageiro_nome}")
        return {"message": f"Passageiro {passageiro_nome} removido com sucesso!"}, 200