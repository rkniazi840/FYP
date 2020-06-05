import web
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model


# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img

def loadmodel():
    model = load_model("notes_model.h5")
    return model

def predict_Image(imgpath="",img=""):
    classes = ["Pepper__bell___Bacterial_spott","Pepper__bell___healthy","Potato___Early_blight","Potato___Late_blightt","Tomato_Bacterial_spot","Tomato_Late_blite"]
    model = loadmodel()
    values = None
    if(imgpath == ""):
        values = model.predict(img)
    else:
        values = model.predict(load_image(imgpath))
    values = values.tolist()[0]
    new_values = [x for x in values]
    new_values.sort(reverse=True)
    index = [x for x in range(0,len(values)) if new_values[0] == values[x]][0]
    return classes[index]

urls = (
    '/', 'index',
    '/imagepredict', 'imagepredict'
)

class index:
    def GET(self):
        return "Hello, world Index!"

class imagepredict:
    def POST(self):
        
        #return predict_Image(self.data["img"])
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
