from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import  CORSMiddleware
from detectDocument import get_corners

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = origins,
    allow_headers = origins
)


@app.post('/upload_image')
def upload_image(image: UploadFile):
    with open('image_2.jpg', 'wb') as out_file:
        content = image.file.read()  # async read
        out_file.write(content)

    print(1)
    return {
       'data' :  get_corners(imagePath= 'image_2.jpg')
    }