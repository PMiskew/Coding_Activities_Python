
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='25dd403977044f108b994b4fb8a5c7c0')

# get the general model
model = app.models.get("Textures & Patterns")

# predict with the model
print(model.predict_by_url(url='https://samples.clarifai.com/model-gallery/images/textures-patterns-001.jpg'))
file = open('data.txt',"w")
file.write(model.predict_by_url(url='https://samples.clarifai.com/model-gallery/images/textures-patterns-001.jpg'));
file.close();