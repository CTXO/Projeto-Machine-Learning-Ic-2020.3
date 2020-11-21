import os

pictures_missed = {}
pictures_right = {}
def main(modelo):
    if len(modelo) == 4:
        import three_breeds as model
    elif len(modelo) == 6:
        import five_breeds as model

    os.chdir("../imagens")
    for directory in modelo:
        acertos = 0

        os.chdir(directory)

        pictures = os.listdir(os.getcwd())
        total_pictures = len(pictures)
        print(f"All bellow should be {directory}")
        for file in pictures:
            # try:
            print(f"{file}")
            demo = model.classify(f"{file}")
            label = demo["class_name"]
            confidence = demo["confidence"]
            answer = directory
            if label.lower() == answer:
                acertos += 1
                pictures_right[directory] = (file, str(confidence) + "%")
            else:
                pictures_missed[directory] = (file, label, str(confidence)+"%")

            # except:
            #     print(f"imagem {file} não abriu")
        print()
        porcentagem = acertos / total_pictures
        print(f"Porcentadem de acerto em {directory}: {porcentagem:.2f}")
        os.chdir("../")
        print(20*"*")

    print(f"Pictures got right: {pictures_right}")
    print(f"Pictures missed: {pictures_missed}")



modelo1 = ["yorkshire", "shih tzu", "poodle", "outros"]
modelo2 = ["yorkshire", "shih tzu", "poodle", "labrador", "pug", "outros"]

main(modelo2)


