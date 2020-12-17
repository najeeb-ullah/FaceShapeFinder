from flask import Flask,request, jsonify
import faceDetector

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def check():

    return "hello world"

@app.route('/check' , methods=['GET'])
def getimage():
    req_body = request.get_json()
    print("the request = " , request)
    image_url = req_body['url']
    response = jsonify(result = faceDetector.get_face_shap(image_url))
    print(response)
    return response



if __name__ == '__main__':
    app.run()
