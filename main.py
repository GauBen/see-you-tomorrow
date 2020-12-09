"""
Un petit teaser pour le hackathon.

Si vous arrivez à lancer ce teaser, alors vous êtes prêts pour demain !
tkinter n'est pas à connaître, c'est seulement pour l'affichage du jeu.
"""

import tkinter
from tkinter import ttk


class Animation:
    """Anime un petit magicien qui marche."""

    def __init__(self, root: tkinter.Tk):
        """Initialise la fenêtre de tkinter."""
        self.root = root
        self.root.title("Hackathon n7")
        self.frames = [
            tkinter.PhotoImage(file="./red-e1.png"),
            tkinter.PhotoImage(file="./red-e2.png"),
        ]
        self.root.iconphoto(True, self.frames[0])

        ttk.Label(self.root, text="See you tomorrow...", font=("", 16, "")).grid(
            row=0, column=0, padx=32, pady=16
        )
        self.canvas = tkinter.Canvas(self.root, width=96, height=96)
        self.canvas.grid(row=1, column=0)
        self.i = 0
        self.frame = self.canvas.create_image(48, 48, image=self.frames[self.i])
        ttk.Button(self.root, text="Jouer !", command=self.play).grid(
            row=2, column=0, padx=16, pady=16
        )

    def mainloop(self):
        """Lance l'animation."""

        def update():
            """Met à jour l'image tous les 250 ms."""
            self.canvas.delete(self.frame)
            self.i = 1 - self.i
            self.frame = self.canvas.create_image(48, 48, image=self.frames[self.i])

            self.root.after(250, update)

        update()
        self.root.mainloop()

    def play(self):
        """Affiche un petit message dans la console."""
        print("Bientôt ! :)")


if __name__ == "__main__":
    root = tkinter.Tk()
    Animation(root).mainloop()
