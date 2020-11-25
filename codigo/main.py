import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 16)
HEIGHT = 350
WIDTH = 500

WIDTH_CANVAS, HEIGHT_CANVAS = 200, 200
BUTTON_SELECT_HEIGHT = 70 + HEIGHT_CANVAS

class Screen(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{WIDTH}x{HEIGHT}+400+300")
        self.title("Projeto Machine Learning")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ModelOne, ModelTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def select_image(self):
        image = filedialog.askopenfilename(initialdir="../imagens/apresentacao",
                                           filetypes=(("Jpg files", "*.jpg"), ("Png files", "*.png"),
                                                      ("All Files", "*.*")))
        # print(image)
        return image

    def make_prediction(self, image, window):
        if window == 1:
            import three_breeds as model
        if window == 2:
            import five_breeds as model
        demo = model.classify(image)
        label = demo["class_name"]
        confidence = demo["confidence"]

        if confidence < model.threshold:
            return "Não consegui identificar a imagem"
        return label

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_label = tk.Label(self, text="Projeto Machine Learning", font=LARGE_FONT)
        title_label.place(x=WIDTH/2, y=20, anchor="center")

        x = 180
        y = 200
        button = tk.Button(self, text="3 raças",
                           command=lambda: controller.show_frame(ModelOne))
        button.place(x=x, y=y, anchor="center")

        button2 = tk.Button(self, text="5 raças",
                            command=lambda: controller.show_frame(ModelTwo))
        button2.place(x=WIDTH - x, y=y, anchor="center")



class ModelOne(tk.Frame):

    window = 1
    def __init__(self, parent, controller):
        def prediction():
            image = controller.select_image()
            classificacao = controller.make_prediction(image, self.window)

            blank = tk.Label(self,text = " "*100)
            blank.place(x=WIDTH/2, y=BUTTON_SELECT_HEIGHT + 30, anchor="center")

            result = tk.Label(self, text=classificacao, fg="red")
            result.place(x=WIDTH/2, y=BUTTON_SELECT_HEIGHT + 30, anchor="center")

            image_resized = Image.open(image)
            image_resized = image_resized.resize((HEIGHT_CANVAS, WIDTH_CANVAS), Image.ANTIALIAS)
            image_tkinter = ImageTk.PhotoImage(image_resized)
            image_canvas = tk.Label(self, image=image_tkinter)
            image_canvas.image = image_tkinter
            image_canvas.place(x=WIDTH/2, y=HEIGHT_CANVAS/2 + 40, anchor="center")

        tk.Frame.__init__(self, parent)
        self.title()

        place_holder = tk.Canvas(self, width=WIDTH_CANVAS, height=HEIGHT_CANVAS, bg="grey")
        place_holder.place(x=WIDTH/2, y=HEIGHT_CANVAS/2 + 40, anchor="center")

        request = tk.Label(place_holder, text="Selecione a sua imagem", bg="grey")
        request.place(x=WIDTH_CANVAS/2, y=HEIGHT_CANVAS/2, anchor="center")

        button_select = tk.Button(self, text="Selecionar Imagem",
                            command=prediction)
        button_select.place(x=WIDTH/2, y=BUTTON_SELECT_HEIGHT, anchor="center")

        button_back = tk.Button(self, text="Voltar", command=lambda: controller.show_frame(StartPage))
        button_back.place(x=0, y=HEIGHT-30)

    def title(self):
        label = tk.Label(self, text="Yorkshire, Poodle e Shih Tzu", font=LARGE_FONT)
        label.place(x=WIDTH/2, y=20, anchor="center")

class ModelTwo(ModelOne):
    window = 2
    def __init__(self, parent, controller):
        ModelOne.__init__(self, parent, controller)

    def title(self):
        label = tk.Label(self, text="Yorkshire, Poodle, Shih Tzu, Labrador e Pug", font=LARGE_FONT)
        label.place(x=WIDTH/2, y=20, anchor="center")


app = Screen()
app.mainloop()