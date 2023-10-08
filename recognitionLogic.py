#Código para integrar el dataset de los gatos y el reconocimiento.
import tensorflow as tf
from tensorflow.python.keras import layers, models
from tensorflow.python.keras.models import load_model
import os

class CatRecognitionTrainer:
    def __init__(self, x_shape:int ,y_shape:int):
        self.model = models.Sequential()
        self.input_shape = (x_shape,y_shape,3)
    
    def build_model(self):
        #Primera capa 
        self.model.add(layers.Conv2D(32, 
                                     (3,3), 
                                     activation='relu', 
                                     input_shape= self.input_shape))
        self.model.add(layers.MaxPooling2D((2,2)))
        #Segunda capa
        self.model.add(layers.Conv2D(64, (3,3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        #Tercera capa
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(1, activation='sigmoid'))
    def compile_model(self):
        self.model.compile(optimizer='adam',
                           loss='binary_crossentropy',
                           metrics=['accuracy'])
    
    def summary(self):
        self.model.summary()
    
    def train_model(self, train_data, train_labels, epochs, batch_size):
        self.model.compile_model()
        self.model.fit(train_data, train_labels, epochs,batch_size)
    
    def save_model(self):
        self.model.save('./model_train/cat_model.h5')
    
    def load_model(self):
        model = load_model('./model_train/cat_model.h5')
        return model
    
    def check(self):
        if os.path.isfile('./model_train/cat_model.h5'):
            return True
        else:
            return False