import tkinter as tk
from tkinter import ttk
import random

# Personality to Pokémon mapping
pokemon_personality_map = {
    "Bold": ["Charizard", "Blastoise", "Machamp", "Gyarados", "Arcanine"],
    "Calm": ["Lapras", "Vaporeon", "Butterfree", "Slowbro", "Exeggutor"],
    "Playful": ["Pikachu", "Jigglypuff", "Clefairy", "Meowth", "Mew"],
    "Wise": ["Alakazam", "Kadabra", "Mr. Mime", "Hypno", "Slowking"],
    "Loyal": ["Bulbasaur", "Squirtle", "Charmander", "Eevee", "Ninetales"],
    "Mischievous": ["Gengar", "Haunter", "Koffing", "Ditto", "Drowzee"]
}

pokemon_catchphrases = {
    "Charizard": "You light up the sky with your fiery spirit!",
    "Blastoise": "Cool under pressure — that’s you!",
    "Machamp": "Powerhouse with a heart of gold!",
    "Gyarados": "You’ve got intensity and strength to spare!",
    "Arcanine": "Loyal, brave, and fast as fire!",
    "Lapras": "Gentle soul, wise mind, and strong heart.",
    "Vaporeon": "You flow gracefully through life’s challenges.",
    "Butterfree": "Bright, breezy, and full of peace.",
    "Slowbro": "Slow? Maybe. But also calm and collected.",
    "Exeggutor": "A walking garden of deep thoughts!",
    "Pikachu": "You bring joy wherever you go!",
    "Jigglypuff": "Adorable, musical, and always ready to shine!",
    "Clefairy": "A whimsical heart with playful energy.",
    "Meowth": "Clever, charming, and just a little sneaky.",
    "Mew": "You’re bubbly and curious to the core!",
    "Alakazam": "A brilliant mind in a sharp body!",
    "Kadabra": "You dazzle others with your intellect.",
    "Mr. Mime": "Unique and clever — just like your style!",
    "Hypno": "Mysterious and insightful. Others follow your lead.",
    "Slowking": "The wise king of calm minds!",
    "Bulbasaur": "Steady, loyal, and surprisingly strong.",
    "Squirtle": "Reliable and cool in any situation.",
    "Charmander": "Small spark, huge heart!",
    "Eevee": "Adaptable, lovable, and full of surprises.",
    "Ninetales": "Elegant and mystical — you turn heads.",
    "Gengar": "Mischief is your middle name!",
    "Haunter": "Spooky, fun, and always entertaining.",
    "Koffing": "Life of the party (even if it’s a bit stinky).",
    "Ditto": "You fit in anywhere — the ultimate chameleon!",
    "Drowzee": "You dream big, think deep, and move softly."
}

questions = [
    {
        "question": "What sounds like a perfect weekend?",
        "options": {
            "Climbing a mountain": "Bold",
            "Lounging at the beach": "Calm",
            "Going to a party": "Playful",
            "Reading in a library": "Wise",
            "Volunteering": "Loyal",
            "Pulling a prank": "Mischievous"
        }
    },
    {
        "question": "Pick a favorite season:",
        "options": {
            "Summer": "Playful",
            "Winter": "Wise",
            "Spring": "Loyal",
            "Autumn": "Calm",
            "Stormy": "Bold",
            "Foggy": "Mischievous"
        }
    },
    {
        "question": "Choose a hobby:",
        "options": {
            "Skydiving": "Bold",
            "Painting": "Calm",
            "Dancing": "Playful",
            "Puzzle solving": "Wise",
            "Gardening": "Loyal",
            "Magic tricks": "Mischievous"
        }
    },
    {
        "question": "What’s your superpower?",
        "options": {
            "Super strength": "Bold",
            "Telepathy": "Wise",
            "Invisibility": "Mischievous",
            "Healing": "Loyal",
            "Water control": "Calm",
            "Teleportation": "Playful"
        }
    },
    {
        "question": "Which snack do you crave?",
        "options": {
            "Spicy noodles": "Bold",
            "Herbal tea": "Calm",
            "Cotton candy": "Playful",
            "Dark chocolate": "Wise",
            "Bento box": "Loyal",
            "Sour gummies": "Mischievous"
        }
    },
    {
        "question": "Pick a spirit animal:",
        "options": {
            "Lion": "Bold",
            "Dolphin": "Calm",
            "Monkey": "Playful",
            "Owl": "Wise",
            "Dog": "Loyal",
            "Fox": "Mischievous"
        }
    },
    {
        "question": "What's your favorite music genre?",
        "options": {
            "Rock": "Bold",
            "Classical": "Wise",
            "Pop": "Playful",
            "Lo-fi": "Calm",
            "Folk": "Loyal",
            "Techno": "Mischievous"
        }
    },
    {
        "question": "Pick a color:",
        "options": {
            "Red": "Bold",
            "Blue": "Calm",
            "Yellow": "Playful",
            "Purple": "Wise",
            "Green": "Loyal",
            "Black": "Mischievous"
        }
    },
    {
        "question": "You're at a party. You are:",
        "options": {
            "The daring one doing backflips": "Bold",
            "Chill in a cozy corner": "Calm",
            "The one dancing on the table": "Playful",
            "Chatting about weird facts": "Wise",
            "Helping set up and clean": "Loyal",
            "Starting a game of hide and seek": "Mischievous"
        }
    },
    {
        "question": "What do your friends say about you?",
        "options": {
            "You never back down": "Bold",
            "You give the best advice": "Wise",
            "You’re fun and energetic": "Playful",
            "You’re easy to talk to": "Calm",
            "You’re always there when needed": "Loyal",
            "You always make them laugh": "Mischievous"
        }
    }
]

button_colors = {
    "Bold": "#FF6B6B",
    "Calm": "#4DD0E1",
    "Playful": "#FFD54F",
    "Wise": "#9575CD",
    "Loyal": "#81C784",
    "Mischievous": "#BA68C8"
}

class PokemonQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Pokémon Personality Quiz ✨")
        self.root.geometry("700x550")
        self.root.configure(bg="#f5f5f5")

        self.question_index = 0
        self.scores = {ptype: 0 for ptype in pokemon_personality_map}

        self.title_label = tk.Label(
            root, text="🌟 Which Kanto Pokémon Are You? 🌟",
            font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333"
        )
        self.title_label.pack(pady=10)

        self.progress = ttk.Progressbar(root, length=600, mode='determinate')
        self.progress.pack(pady=10)
        self.progress["maximum"] = len(questions)

        self.question_label = tk.Label(
            root, text="", font=("Helvetica", 16), wraplength=650, bg="#f5f5f5"
        )
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(root, bg="#f5f5f5")
        self.options_frame.pack()

        self.show_question()

    def show_question(self):
        q_data = questions[self.question_index]
        self.question_label.config(text=q_data["question"])
        self.progress["value"] = self.question_index

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for text, personality in q_data["options"].items():
            color = button_colors[personality]
            btn = tk.Button(
                self.options_frame, text=text,
                bg=color, fg="black", font=("Helvetica", 12),
                width=50, pady=5,
                command=lambda p=personality: self.record_answer(p)
            )
            btn.pack(pady=5)

    def record_answer(self, personality):
        self.scores[personality] += 1
        self.question_index += 1

        if self.question_index < len(questions):
            self.show_question()
        else:
            self.progress["value"] = len(questions)
            self.show_result()

    def show_result(self):
        top_personality = max(self.scores, key=self.scores.get)
        pokemon = random.choice(pokemon_personality_map[top_personality])
        phrase = pokemon_catchphrases.get(pokemon, "")
        cheeky_quotes = {
            "Bold": "🔥 You fear nothing — and it shows!",
            "Calm": "🌊 Unbothered. Moisturized. Thriving.",
            "Playful": "🎉 You're the party no one wants to leave!",
            "Wise": "🧠 You probably solve puzzles for fun, huh?",
            "Loyal": "🫶 You're the friend every team needs!",
            "Mischievous": "😏 You’d prank your boss and get away with it."
        }
        quote = cheeky_quotes[top_personality]
        color = button_colors[top_personality]

        result_window = tk.Toplevel(self.root)
        result_window.title("🎉 Your Pokémon Match 🎉")
        result_window.geometry("500x400")
        result_window.configure(bg=color)

        tk.Label(
            result_window, text=f"You're most like...",
            font=("Helvetica", 18, "bold"), bg=color, fg="white"
        ).pack(pady=20)

        tk.Label(
            result_window, text=pokemon,
            font=("Helvetica", 28, "bold"), bg=color, fg="white"
        ).pack(pady=10)

        tk.Label(
            result_window, text=f"{phrase}",
            font=("Helvetica", 14, "italic"), bg=color, fg="white", wraplength=450
        ).pack(pady=10)

        tk.Label(
            result_window, text=f"({quote})",
            font=("Helvetica", 12), bg=color, fg="#eee", wraplength=450
        ).pack(pady=10)

        tk.Button(
            result_window, text="Thanks for playing!",
            font=("Helvetica", 12, "bold"), bg="#ffffff", fg="#333",
            command=self.root.destroy
        ).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonQuiz(root)
    root.mainloop()
