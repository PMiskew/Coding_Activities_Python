
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='8ace5602350c4aa1a770bdf44b5c145c')

file = open("results.txt","w")

model = app.models.get('travel-v1.0')
image = ClImage(url='https://clarifai.com/cms-assets/20180308185817/travel.jpg')
results = model.predict([image])
file.write(str(results))
print(results['outputs'][0]['data'][0])
file.close()