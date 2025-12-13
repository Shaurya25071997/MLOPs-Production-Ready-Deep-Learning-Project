import tensorflow as tf
import numpy as np
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = tf.keras.models.load_model(
            os.path.join("model", "model.h5")
        )

        img = tf.keras.utils.load_img(
            self.filename,
            target_size=(224, 224)
        )

        img = tf.keras.utils.img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        preds = model.predict(img)
        result = np.argmax(preds, axis=1)[0]

        if result == 1:
            return [{"image": "Healthy"}]
        else:
            return [{"image": "Coccidiosis"}]
