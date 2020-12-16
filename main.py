import math

from matplotlib.pyplot import imshow
from PIL import Image, ImageDraw
import face_recognition

import urllib.request

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("munim.jpeg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)


print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)

# Show the picture
pil_image.show()



#Load image
# image = face_recognition.load_image_file("munim.jpeg")
#get landmarks of image
landmarks = face_recognition.api._raw_face_landmarks(image)
points = [(p.x, p.y) for p in landmarks[0].parts()]
#for forehead
forehead_left, forehead_right = points[0], points[16]
print("Forehead ",forehead_left,forehead_right)

forehead_X=math.pow(forehead_left[0]-forehead_right[0],2)
forehead_y=math.pow(forehead_left[1]-forehead_right[1],2)
forehead=math.sqrt(forehead_X+forehead_y)
print("Forehead width = ",forehead)
forehead=math.floor(forehead/15)
print("Forehead width = ",forehead)

#for cheeks measurements
cheek_left, cheek_right = points[2], points[14]
print("Cheeks ",cheek_left,cheek_right)

cheek_X=math.pow(cheek_left[0]-cheek_right[0],2)
cheek_y=math.pow(cheek_left[1]-cheek_right[1],2)
cheek=math.sqrt(cheek_X+cheek_y)
cheek=math.floor(cheek/15)
print("Cheeks length = ",cheek)

#for jawline
jawline_upper, jawline_lower = points[12], points[8]
# jawline_upper, jawline_lower = points[3], points[13]

print("Jawline ",jawline_upper,jawline_lower)

jawline_X=math.pow(jawline_upper[0]-jawline_lower[0],2)
jawline_y=math.pow(jawline_upper[1]-jawline_lower[1],2)
jawline=math.sqrt(jawline_X+jawline_y)
jawline=jawline*2
jawline=math.floor(jawline/15)
print("Jawline length = ",jawline)

#for face length

face_upper, face_lower = points[21], points[7]
print("face ",face_upper,face_lower)

face_X=math.pow(face_upper[0]-face_lower[0],2)
face_y=math.pow(face_upper[1]-face_lower[1],2)
face=math.sqrt(face_X+face_y)
face=math.floor((face/15))
if face<=10:
    face=face+1
elif 20>=face>10:
    face=face+2
elif 30>=face>20:
    face=face+3
elif 40>=face>30:
    face=face+4
else:
    face=face+5

print("face length = ",face)


shape="Null"

if face>cheek and forehead<cheek:
    shape="oval"
    print("Your FaceShape is Oval")
elif face>cheek and cheek==forehead:
    shape="Rectangle"
    print("Your Face Shape is ",shape)
elif forehead<cheek and jawline>face:
    shape = "Round"
    print("Your Face Shape is ",shape)
elif face>cheek>forehead:
    shape = "Diamond"
    print("Your Face Shape is ",shape)
elif forehead == face:
    shape = "square"
    print("Your Face Shape is ",shape)
elif forehead>cheek:
    shape="Triangle"
    print("Your Face Shape is ",shape)


print("end_________________")


