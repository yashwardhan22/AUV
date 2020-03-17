from keras.models import model_from_json
import numpy as np

class CNN_Model(object):
    out_list = ["ANGRY", "DISGUST", "FEAR", "HAPPY", "SAD", "SURPRISE", "NEUTRAL"]

    def __init__(self, model_json_file, model_weights_file):
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)
        print("\nModel loaded from disk")
        self.loaded_model.summary()

    def predict_result(self, img):
        self.result = self.loaded_model.predict(img)
        return CNN_Model.out_list[np.argmax(self.result)], str( np.int(np.amax(self.result)*100) )

#, np.array_str(np.amax(self.result))


if __name__ == '__main__':
    pass
