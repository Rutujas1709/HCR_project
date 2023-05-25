image_x, image_y = 64,64

from keras.models import load_model
classifier = load_model('Trained_model.h5')
classifier._make_predict_function()

def predictor(img):
       import numpy as np
       from keras.preprocessing import image
       test_image = image.load_img(img, target_size=(64, 64))
       test_image = image.img_to_array(test_image)
       test_image = np.expand_dims(test_image, axis = 0)
       result = classifier.predict(test_image)
       
       print(result)
       
       if result[0][0] == 1:
              return 'South'
       elif result[0][1] == 1:
              return 'fort'
       elif result[0][2] == 1:
              return 'family'
       elif result[0][3] == 1:
              return 'temple'
       elif result[0][4] == 1:
              return 'water'
       elif result[0][5] == 1:
              return 'wait'
       elif result[0][6] == 1:
              return 'display'
       elif result[0][7] == 1:
              return 'university'
       elif result[0][8] == 1:
              return 'exercise'
       elif result[0][9] == 1:
              return 'tree'                            