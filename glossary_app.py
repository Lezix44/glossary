import tkinter as tk
from tkinter import ttk

GLOSSARY = {
    "Державні інформаційні ресурси": {
        "uk": "Інформаційні ресурси, що належать державі та використовуються органами влади.",
        "en": "Information resources owned by the state and used by public authorities."
    },
    "Об’єкт інформаційної діяльності": {
        "uk": "Інформація або процеси, щодо яких здійснюється інформаційна діяльність.",
        "en": "Information or processes that are the subject of information activity."
    },
    "Система технічного захисту інформації": {
        "uk": "Сукупність організаційних та технічних заходів захисту інформації.",
        "en": "A set of organizational and technical measures for information protection."
    },
    "Протидія технічним розвідкам": {
        "uk": "Заходи щодо запобігання несанкціонованому отриманню інформації.",
        "en": "Measures to prevent unauthorized technical intelligence gathering."
    },
    "Засіб криптографічного захисту інформації": {
        "uk": "Програмний або апаратний засіб для шифрування інформації.",
        "en": "A software or hardware tool for cryptographic information protection."
    },
    "Засіб спеціального зв’язку": {
        "uk": "Технічний засіб захищеної передачі інформації.",
        "en": "A technical means for secure information transmission."
    },
    "Спеціальний зв’язок": {
        "uk": "Система захищеного зв’язку для державних потреб.",
        "en": "A secure communication system for state needs."
    },
    "Документ": {
        "uk": "Матеріальний носій інформації з реквізитами.",
        "en": "A material carrier of information with requisites."
    },
    "Суб’єкт владних повноважень": {
        "uk": "Орган або посадова особа, що здійснює владні повноваження.",
        "en": "An authority or official exercising public powers."
    },
    "Відкрита інформація": {
        "uk": "Інформація з вільним доступом.",
        "en": "Information with free access."
    },
    "Конфіденційна, таємна та службова інформація": {
        "uk": "Інформація з обмеженим доступом відповідно до законодавства.",
        "en": "Information with restricted access under the law."
    },
    "Державна таємниця": {
        "uk": "Інформація, що охороняється державою.",
        "en": "Information protected by the state."
    },
    "Гриф секретності": {
        "uk": "Позначка рівня секретності інформації.",
        "en": "A marking indicating the secrecy level."
    },
    "Блокування інформації в системі": {
        "uk": "Обмеження доступу до інформації в інформаційній системі.",
        "en": "Restriction of access to information in an information system."
    },
    "База персональних даних": {
        "uk": "Іменована сукупність упорядкованих персональних даних.",
        "en": "A named set of organized personal data."
    },
    "Публічна інформація": {
        "uk": "Інформація, що знаходиться у володінні суб’єктів владних повноважень.",
        "en": "Information held by public authorities."
    }
}

class GlossaryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Інтерактивний глосарій")
        self.geometry("750x450")

        self.lang = tk.StringVar(value="uk")

        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Radiobutton(frame, text="Українська", variable=self.lang, value="uk").pack(anchor="w")
        ttk.Radiobutton(frame, text="English", variable=self.lang, value="en").pack(anchor="w")

        self.listbox = tk.Listbox(frame)
        for term in GLOSSARY:
            self.listbox.insert(tk.END, term)
        self.listbox.pack(fill="both", expand=True, pady=5)

        self.text = tk.Text(frame, height=6, wrap="word")
        self.text.pack(fill="x")

        self.listbox.bind("<<ListboxSelect>>", self.show_definition)

    def show_definition(self, event):
        if not self.listbox.curselection():
            return
        term = self.listbox.get(self.listbox.curselection())
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, GLOSSARY[term][self.lang.get()])

if __name__ == "__main__":
    app = GlossaryApp()
    app.mainloop()
