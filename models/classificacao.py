import os
def main(modelo):

    if len(modelo) == 4:
        import three_breeds as model
    elif len(modelo) == 6:
        import five_breeds as model

    os.chdir("../imagens")
    for directory in modelo:
        os.chdir(directory)
        print(f"All bellow should be {directory}")
        for file in os.listdir(os.getcwd()):
            try:
                demo = model.classify(f"{file}")
                label = demo["class_name"]
                confidence = demo["confidence"]

                # change this to do something different with the result
                print(f"Name of the file: {file}")
                print("result: '%s' with %d%% confidence" % (label, confidence))
                print(20*"-")
            except:
                print(f"imagem {file} não abriu")
        os.chdir("../")
        print(20*"*")


modelo1 = ["yorkshire", "shih tzu", "poodle", "outros"]
modelo2 = ["yorkshire", "shih tzu", "poodle", "labrador", "pug", "outros"]

main(modelo2)
