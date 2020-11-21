import requests, sys, os

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
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.post(url, json={ "data" : getImageFileData(imagefile) })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to the name of the image file you want to classify
path = "../imagens"
count = 0
imagens_falhas = []
progress = 0
for racas in os.listdir(path):
    for cachorro in os.listdir(path+f"/{racas}"):
        try:
            demo = classify(path+f"/{racas}/{cachorro}")

            label = demo["class_name"]
            confidence = demo["confidence"]


            # CHANGE THIS to do something different with the result
            # print ("result: '%s' with %d%% confidence" % (label, confidence))
        except:
            print("nao pegou")
            count += 1
            imagens_falhas.append(cachorro)
        finally:
            progress += 1
            print(f"images calculated: {progress}")
print(f"{count} imagens sem pegar")
print(imagens_falhas.sort())
# data = [{'37.jpg'}, {'25.jpg'}, {'02.jpg'}, {'03.jpg'}, {'05.jpg'}, {'06.jpg'}, {'01.jpg'}, {'57.jpg'}, {'105.jpg'}, {'126.jpg'}, {'128.jpg'}, {'104.jpg'}, {'173.jpg'}, {'156.jpg'}, {'179.jpg'}, {'188.jpg'}, {'160.jpg'}, {'152.jpg'}, {'163.jpg'}, {'169.jpg'}, {'175.jpg'}, {'171.jpg'}, {'183.jpg'}, {'155.jpg'}, {'199.jpg'}, {'167.jpg'}, {'184.jpg'}, {'207.jpg'}, {'227.jpg'}, {'235.jpg'}, {'209.jpg'}, {'203.jpg'}, {'219.jpg'}, {'245.jpg'}, {'230.jpg'}, {'246.jpg'}, {'208.jpg'}, {'202.jpg'}, {'248.jpg'}, {'231.jpg'}, {'250.jpg'}, {'214.jpg'}, {'216.jpg'}, {'236.jpg'}, {'204.jpg'}, {'298.jpg'}, {'271.jpg'}, {'284.jpg'}, {'295.jpg'}, {'286.jpg'}, {'293.jpg'}, {'274.jpg'}, {'260.jpg'}, {'267.jpg'}, {'269.jpg'}, {'278.jpg'}, {'265.jpg'}, {'263.jpg'}, {'264.jpg'}, {'280.jpg'}, {'302.jpg'}, {'255.jpg'}, {'258.jpg'}, {'285.jpg'}, {'270.jpg'}, {'300.jpg'}, {'273.jpg'}, {'261.jpg'}, {'275.jpg'}, {'252.jpg'}, {'299.jpg'}, {'281.jpg'}, {'257.jpg'}, {'262.jpg'}, {'277.jpg'}, {'297.jpg'}, {'294.jpg'}, {'291.jpg'}, {'272.jpg'}, {'301.jpg'}, {'296.jpg'}, {'282.jpg'}, {'268.jpg'}, {'256.jpg'}, {'254.jpg'}, {'292.jpg'}, {'253.jpg'}, {'276.jpg'}, {'289.jpg'}]
# data = [int(str(i)[2:-6]) for i in data]
# data.sort()
# print(data)
#
# with open("fotos_grandes.txt","w") as f:
#     for num in data:
#         f.write(str(num) + "\n")