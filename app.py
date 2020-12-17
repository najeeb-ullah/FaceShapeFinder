from flask import Flask,request, jsonify
import faceDetector

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def check():

    return "hello world"

@app.route('/check' , methods=['GET'])
def getimage():
    reqURl = request.args.get("url" )
   
    response = jsonify(result = faceDetector.get_face_shap(reqURl))
    #print(response)
    return response



if __name__ == '__main__':
    app.run()
