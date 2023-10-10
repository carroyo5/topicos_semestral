from keras import layers, models
from keras.preprocessing.image import ImageDataGenerator, DirectoryIterator
import os
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

class CatRecognition:
    def __init__(self, x_shape: int, y_shape: int, num_classes: int):
        self.model = models.Sequential()
        self.input_shape = (x_shape, y_shape, 3)
        self.num_classes = num_classes

    def build_model(self):
        # Primera capa
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=self.input_shape))
        self.model.add(layers.MaxPooling2D((2, 2)))
        
        # Segunda capa
        self.model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))

        # Tercera capa
        self.model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))

        # Cuarta capa
        self.model.add(layers.Conv2D(256, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))

        # Quinta capa
        self.model.add(layers.Conv2D(256, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(256, activation='relu'))
        self.model.add(layers.Dense(self.num_classes, activation='softmax'))
 

    def load_dataset(self, batch_size):
        dataset_path = './dataset'
        train_path = os.path.join(dataset_path, 'train')
        test_path = os.path.join(dataset_path, 'test')
        image_size = (128, 128)

        train_datagen = ImageDataGenerator(
            rescale=1.0 / 255.0,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            shear_range=0.2,
            zoom_range=0.2,
            fill_mode="nearest",
        )

        test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

        train_generator = train_datagen.flow_from_directory(
            train_path,
            target_size=image_size,
            batch_size=batch_size,
            class_mode="categorical",  
        )
        self.test_generator = test_datagen.flow_from_directory(
            test_path,
            target_size=image_size,
            batch_size=batch_size,
            class_mode="categorical", 
        )
        return train_generator, self.test_generator

    def compile_model(self):
        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def summary(self):
        self.model.summary()

    def train_model(self, train_generator, test_generator, epochs):
        history = self.model.fit(train_generator,
                                 epochs=epochs,
                                 validation_data=test_generator)
        return history

    def save_model(self):
        self.model.save('./model_train/cat_model.h5')

    def load_model(self):
        model = models.load_model('./model_train/cat_model.h5')
        return model

    def check(self):
        if os.path.isfile('./model_train/cat_model.h5'):
            return True
        else:
            return False

if __name__ == "__main__":
    parameters = CatRecognition(128, 128, num_classes=7)
    parameters.build_model()
    parameters.compile_model()
    train_gen, test_gen = parameters.load_dataset(batch_size=32)
    print(type(test_gen))
    parameters.summary()
    history = parameters.train_model(train_gen, test_gen, epochs=17)
    test_loss, test_accuracy = parameters.model.evaluate(test_gen)
    print(f'Precisión en el conjunto de prueba: {test_accuracy * 100:.2f}%')
    parameters.save_model()