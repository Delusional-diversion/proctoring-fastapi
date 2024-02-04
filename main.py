from fastapi import FastAPI, Body, HTTPException
from proctoring import proctor
from recognition import verifyFaces

app = FastAPI()


@app.get("/")
def first_example():
    """
    FG Example First Fast API Example
    """
    return {"GFG Example": "FastAPI"}

@app.post('/verifypfp')
def _verifyProfilePicture(
        data = Body(...)
):
    # print(data)
    # print(type(data))
    try:
        img1 = data["image1"]
        img2 = data["image2"]
        status = verifyFaces(img1,img2)
        return ({
            "success":status
        })  
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@app.post('/proctor')
def _proctorUser(
        data = Body(...)
):
    '''
    Send Base64 encoded image in each 5 second
    '''
    try:
        original = data["original"]
        captured = data["captured"]
        status = proctor(original,captured)
        return ({
            "status":status
        })  
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))