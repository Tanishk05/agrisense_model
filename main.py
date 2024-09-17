from flask import Flask, request
from flask_cors import CORS, cross_origin
import numpy as np
import io
from PIL import Image

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/predict', methods=["POST"])
@cross_origin()
def predict():
    if request.method == 'POST':
        data = request.get_data()
        
        start_index = data.find(b'\xff\xd8')  
        end_index = data.find(b'\xff\xd9') + 2  

        image_bytes = data[start_index:end_index]
        image = Image.open(io.BytesIO(image_bytes))
        image_array = np.array(image)
        
        print(image_array.shape)
        # some predictions are done
        
        disease = "Parelotamesia"
        
        return disease