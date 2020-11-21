import requests, sys

# Gets the contents of an image file to be sent to the
# machine learning model for classifying
def getImageFileData(locationOfImageFile):
    with open(locationOfImageFile, "rb") as f:
        data = f.read()
        if sys.version_info[0] < 3:
            # Python 2 approach to handling bytes
            return data.encode("base64")
        else:
            # Python 3 approach to handling bytes
            import base64
            return base64.b64encode(data).decode()


# This function will pass your image to the machine learning model
# and return the top result with the highest confidence
def classify(imagefile):
    key = "054d1e10-2702-11eb-a554-975a76eca2c24129ac52-5910-4c20-be43-4ec469bdce9e"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.post(url, json={ "data" : getImageFileData(imagefile) })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
