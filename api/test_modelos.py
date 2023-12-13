from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = 'database/titanic_golden.csv'
colunas = ['pclass', 'age', 'sibsp', 'parche', 'fare', 'sex', 'embarkedc', 'embarkeds', 'embarkedq', 'class']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo SVM a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_svm():  
    # Importando o modelo SVM
    svm_path = 'ml_model/classificador.pkl'
    modelo_svm = modelo.carrega_modelo(svm_path)

    # Obtendo as métricas do Modelo SVM
    acuracia_svm = avaliador.avaliar(modelo_svm, X, Y)
    
    # Testando as métricas do modelo SVM
    assert acuracia_svm >= 0.80
    
    
 
