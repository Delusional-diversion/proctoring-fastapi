from fastapi import FastAPI, Body
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
    print(data)
    print(type(data))
    return ({
        "success":"true"
    })

@app.post('/proctor')
def _proctorUser(
        data = Body(...)
):
    '''
    Send Base64 encoded image in each 5 second
    '''
    print(data)
    return ({
        "success":"true"
    })