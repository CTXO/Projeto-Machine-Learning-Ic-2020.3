import os, sys
MODELO1 = ["yorkshire", "shih_tzu", "poodle", "outros"]
MODELO2 = ["yorkshire", "shih_tzu", "poodle", "labrador", "pug", "outros"]

# sys.stdout = open("out2.txt","w")
def main(modelo):
    #Dicts
    pictures_missed = {}
    pictures_right = {}
    accuracy = {}

    #Choosing wich API to usw
    if len(modelo) == 4:
        import three_breeds as model
    elif len(modelo) == 6:
        import five_breeds as model

    os.chdir("../imagens")

    # Iterating through breeds
    for directory in modelo:
        acertos = 0

        os.chdir(directory)

        pictures_missed[directory] = []
        pictures_right[directory] = []

        pictures = os.listdir(os.getcwd())
        total_pictures = len(pictures)
        for file in pictures:
            # Using ML API
            demo = model.classify(f"{file}")
            label = demo["class_name"]
            confidence = demo["confidence"]

            answer = directory

            if label.lower() == answer:
                acertos += 1
                pictures_right[directory].append({"file": file, "prediction": label, "confidence": str(confidence) + "%"})
            else:
                pictures_missed[directory].append({"file": file, "prediction": label, "confidence": str(confidence) + "%"})


        porcentagem = acertos/total_pictures * 100
        accuracy[directory] = str(porcentagem) + "%"
        os.chdir("../")

    return ({"acertos": pictures_right, "erros": pictures_missed}, accuracy)


db = {}
acc = {}

db["modelo_1"], acc["modelo_1"] = main(MODELO1)
db["modelo_2"], acc["modelo_2"] = main(MODELO2)

print(f"Data Base = {db}")
print(f"Accuracy = {acc}")



