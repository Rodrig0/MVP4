import numpy as np
import pickle
import joblib

class Model:

    @staticmethod
    def carrega_modelo(path, scaler=None):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        if scaler is not None:
            model.scaler = scaler
        return model
    
    def preditor(model, form):
        """Realiza a predição de um passeiro com base no modelo treinado
        """
        X_input = np.array([form.pclass, 
                            form.age, 
                            form.sibsp, 
                            form.parch, 
                            form.fare, 
                            form.sex, 
                            form.embarkedc, 
                            form.embarkedq,
                            form.embarkeds
                        ])

        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        X_input_scaled = model.scaler.transform(X_input)
        result = model.predict(X_input_scaled.reshape(1, -1))
        return int(result[0])