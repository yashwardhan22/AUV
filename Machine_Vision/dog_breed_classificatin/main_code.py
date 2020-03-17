from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as k
import numpy as np
from keras.preprocessing import image


data_dir="Images"
img_size = 60

train_data_param=ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2)


training_data = train_data_param.flow_from_directory(
    data_dir,
    target_size=(img_size, img_size),
    color_mode="grayscale",
    batch_size=32,
    class_mode='categorical',
    shuffle=True,
    subset='training')


validation_data=train_data_param.flow_from_directory(
    data_dir,
    target_size=(img_size, img_size),
    color_mode="grayscale",
    batch_size=32,
    class_mode='categorical',
    shuffle=True,
    subset='validation')


if k.image_data_format() =='channels_first':
    input_shape = (1, img_size, img_size)
else:
    input_shape = (img_size, img_size, 1)



model = Sequential()

model.add(Conv2D(32,(3,3), input_shape=input_shape, padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Activation('relu'))
#model.add(Dropout(0.4))
#model.add(Conv2D(32,(3,3), input_shape=input_shape, padding='same'))
#model.add(Activation('relu'))
#model.add(Dropout(0.4))
#model.add(MaxPooling2D(pool_size=(2, 2)))

#model.add(Conv2D(64,(3,3)))
#model.add(Activation('relu'))
#model.add(Dropout(0.4))
model.add(Conv2D(64,(3,3), input_shape=input_shape, padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Activation('relu'))
#model.add(Dropout(0.4))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))
#model.add(Dense(64))

model.add(Conv2D(128,(3,3), padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Activation('relu'))
#model.add(Conv2D(32,(3,3)))
#model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

#model.add(Conv2D(64,(3,3)))
#model.add(Activation('relu'))
#model.add(Conv2D(64,(3,3)))
#model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(500))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(120))
model.add(Activation('softmax'))

#model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
#model.add(Activation('relu'))
#model.add(Conv2D(32, (3, 3)))
#model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))

#model.add(Conv2D(64, (3, 3), padding='same'))
#model.add(Activation('relu'))
#model.add(Conv2D(64, (3, 3)))
#model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))

model.summary()



model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


history=model.fit_generator(
            training_data,
            steps_per_epoch=1000,
            epochs=80,
            validation_data=validation_data,
            validation_steps=32,
            shuffle=True)

model.save_weights('second_try.h5')


img_pred = image.load_img('Images/n02116738-African_hunting_dog/n02116738_500.jpg', color_mode = "grayscale", target_size = (img_size, img_size))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred, axis = 0)


rslt = model.predict(img_pred)
print(rslt)


import matplotlib. pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
