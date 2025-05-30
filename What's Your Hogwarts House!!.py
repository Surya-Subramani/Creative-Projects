import tkinter as tk
from tkinter import ttk
import random

# Character and house data
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley", "Luna Lovegood",
    "Draco Malfoy", "Sirius Black", "Bellatrix Lestrange", "Neville Longbottom",
    "Severus Snape", "Ginny Weasley", "Minerva McGonagall", "Cedric Diggory",
    "Cho Chang", "Newt Scamander", "Nymphadora Tonks", "Tom Riddle"
]

character_quotes = {
    "Harry Potter": "I don’t go looking for trouble. Trouble usually finds me.",
    "Hermione Granger": "Books! And cleverness! There are more important things—friendship and bravery.",
    "Ron Weasley": "Why spiders? Why couldn’t it be follow the butterflies?",
    "Luna Lovegood": "You're just as sane as I am.",
    "Draco Malfoy": "My father will hear about this!",
    "Sirius Black": "We've all got both light and dark inside us.",
    "Bellatrix Lestrange": "I killed Sirius Black!",
    "Neville Longbottom": "It takes a great deal of bravery to stand up to your enemies… and your friends.",
    "Severus Snape": "Always.",
    "Ginny Weasley": "Anything’s possible if you’ve got enough nerve.",
    "Minerva McGonagall": "Have a biscuit, Potter.",
    "Cedric Diggory": "Remember Cedric Diggory.",
    "Cho Chang": "It’s not how you fall, it’s how you get back up.",
    "Newt Scamander": "Worrying means you suffer twice.",
    "Nymphadora Tonks": "Don’t call me Nymphadora!",
    "Tom Riddle": "Greatness inspires envy, envy engenders spite."
}

house_quotes = {
    "Gryffindor": "🏆 You have the daring of a dragon and a heart of fire.",
    "Hufflepuff": "🌙 You’re loyal, kind, and quietly unbreakable.",
    "Ravenclaw": "📘 Wit and curiosity are youkr guiding stars.",
    "Slytherin": "🧪 You value cunning, ambition, and magical mastery."
}

# Dark theme colors
bg_color = "#1a1a1a"
text_color = "#f8f8f2"
button_colors = ["#6a1b9a", "#283593", "#00695c", "#c62828"]  # Dark purple, navy, green, red

# Quiz questions
questions = [
    {"question": "Which Fantastic Beast would you choose as a companion?",
     "options": {"Niffler": "Hufflepuff", "Bowtruckle": "Ravenclaw", "Occamy": "Slytherin", "Thunderbird": "Gryffindor"}},
    {"question": "Which Hogwarts professor intrigues you the most?",
     "options": {"McGonagall": "Gryffindor", "Dumbledore": "Ravenclaw", "Snape": "Hufflepuff", "Slughorn": "Slytherin"}},
    {"question": "Choose a spell to master:",
     "options": {"Patronus Charm": "Hufflepuff", "Lumos": "Ravenclaw", "Expelliarmus": "Gryffindor", "Stupefy": "Slytherin"}},
    {"question": "Pick your favorite magical snack:",
     "options": {"Treacle Tart": "Ravenclaw", "Fizzing Whizbees": "Hufflepuff", "Licorice Wands": "Slytherin", "Pumpkin Pasties": "Gryffindor"}},
    {"question": "Who's your favorite Marauder?",
     "options": {"James": "Gryffindor", "Remus": "Ravenclaw", "Sirius": "Slytherin", "Peter": "Hufflepuff"}},
    {"question": "Choose your favorite Weasley:",
     "options": {"Fred & George": "Gryffindor", "Ginny": "Ravenclaw", "Bill": "Slytherin", "Molly": "Hufflepuff"}},
    {"question": "Pick your favorite book from the series:",
     "options": {"Goblet of Fire": "Gryffindor", "Prisoner of Azkaban": "Ravenclaw", "Order of the Phoenix": "Slytherin", "Philosopher’s Stone": "Hufflepuff"}},
    {"question": "Which object would you keep forever?",
     "options": {"Golden Snitch": "Gryffindor", "Time Turner": "Ravenclaw", "Nimbus 2000": "Hufflepuff", "Godric’s Sword": "Slytherin"}},
    {"question": "Choose your magical pet:",
     "options": {"Phoenix": "Gryffindor", "Hippogriff": "Ravenclaw", "Unicorn": "Hufflepuff", "Nagini": "Slytherin"}},
    {"question": "Who would you bring back?",
     "options": {"Dumbledore": "Ravenclaw", "Sirius Black": "Gryffindor", "Cedric": "Hufflepuff", "Dobby & Hedwig": "Slytherin"}}
]

class WizardQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Wizarding World Personality Quiz ✨")
        self.root.geometry("850x600")
        self.root.configure(bg=bg_color)

        self.q_index = 0
        self.scores = {house: 0 for house in houses}

        self.title = tk.Label(root, text="Which Wizarding World Paths Align With Yours?",
                              font=("Georgia", 20, "bold"), bg=bg_color, fg=text_color)
        self.title.pack(pady=10)

        self.progress = ttk.Progressbar(root, length=700, mode='determinate', maximum=len(questions))
        self.progress.pack(pady=10)

        self.q_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=800, bg=bg_color, fg=text_color)
        self.q_label.pack(pady=20)

        self.options_frame = tk.Frame(root, bg=bg_color)
        self.options_frame.pack()

        self.show_question()

    def show_question(self):
        current = questions[self.q_index]
        self.q_label.config(text=current["question"])
        self.progress["value"] = self.q_index

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for i, (text, house) in enumerate(current["options"].items()):
            btn = tk.Button(
                self.options_frame, text=text, width=60, pady=8,
                bg=button_colors[i % len(button_colors)], fg="white",
                font=("Verdana", 11, "bold"),
                command=lambda h=house: self.record_answer(h)
            )
            btn.pack(pady=6)

    def record_answer(self, house):
        self.scores[house] += 1
        self.q_index += 1

        if self.q_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        top_house = max(self.scores, key=self.scores.get)
        character = random.choice(characters)
        quote = character_quotes.get(character, "A unique soul in the wizarding world.")
        house_catchphrase = house_quotes.get(top_house, "")

        result = tk.Toplevel(self.root)
        result.title("🔮 Your Magical Match")
        result.geometry("600x500")
        result.configure(bg="#212121")

        tk.Label(result, text="✨ You've been matched with...", font=("Helvetica", 18, "bold"),
                 bg="#212121", fg="#fbc02d").pack(pady=10)
        tk.Label(result, text=f"🏰 House: {top_house}", font=("Helvetica", 20, "bold"),
                 bg="#212121", fg="#ffab00").pack(pady=5)
        tk.Label(result, text=house_catchphrase, font=("Helvetica", 12, "italic"),
                 wraplength=500, bg="#212121", fg="#ffffff").pack(pady=10)

        tk.Label(result, text=f"🧙 Character: {character}", font=("Helvetica", 20, "bold"),
                 bg="#212121", fg="#80cbc4").pack(pady=10)
        tk.Label(result, text=f'"{quote}"', font=("Helvetica", 12, "italic"),
                 wraplength=500, bg="#212121", fg="#eeeeee").pack(pady=10)

        tk.Button(result, text="🔁 Try Again", bg="#3949ab", fg="white",
                  font=("Helvetica", 12, "bold"), command=self.root.destroy).pack(pady=25)

if __name__ == "__main__":
    root = tk.Tk()
    app = WizardQuiz(root)
    root.mainloop()

