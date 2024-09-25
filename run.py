import tkinter as tk
from tkinter import ttk
from googletrans import LANGUAGES, Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Penerjemah")

        # Set the character limit (you can change this value)
        self.character_limit = 50000

        self.create_widgets()

        # Bind the text input to the character count update function
        self.text_input.bind('<KeyRelease>', self.update_char_count)

    def create_widgets(self):
        self.label_from = ttk.Label(self.root, text="Dari Bahasa:")
        self.label_from.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.combo_from = ttk.Combobox(self.root, values=list(LANGUAGES.values()), state="readonly")
        self.combo_from.grid(row=0, column=1, padx=10, pady=10)
        self.combo_from.set("auto")

        self.label_to = ttk.Label(self.root, text="Ke Bahasa:")
        self.label_to.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.combo_to = ttk.Combobox(self.root, values=list(LANGUAGES.values()), state="readonly")
        self.combo_to.grid(row=2, column=1, padx=10, pady=10)
        self.combo_to.set("indonesian")

        self.label_input = ttk.Label(self.root, text="Teks:")
        self.label_input.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.text_input = tk.Text(self.root, height=5, wrap="word")
        self.text_input.grid(row=1, column=1, padx=10, pady=10)

        self.label_output = ttk.Label(self.root, text="Hasil Penerjemahan:")
        self.label_output.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.text_output = tk.Text(self.root, height=5, state="disabled", wrap="word")
        self.text_output.grid(row=3, column=1, padx=10, pady=10)

        self.translate_button = ttk.Button(self.root, text="Terjemahkan", command=self.translate_text)
        self.translate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.swap_button = ttk.Button(self.root, text="Tukar Bahasa", command=self.swap_languages)
        self.swap_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_char_count = ttk.Label(self.root, text="Jumlah Karakter: 0")
        self.label_char_count.grid(row=6, column=0, columnspan=2, pady=10)

        self.label_char_limit_warning = ttk.Label(self.root, text="", foreground="red")
        self.label_char_limit_warning.grid(row=7, column=0, columnspan=2, pady=10)

    def translate_text(self):
        text_to_translate = self.text_input.get("1.0", "end-1c")

        # Handle the case when the source language is "auto"
        if self.combo_from.get() == "auto":
            source_lang = "auto"
        else:
            source_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.combo_from.get())]

        target_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.combo_to.get())]

        translator = Translator()
        translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text

        self.text_output.config(state="normal")
        self.text_output.delete("1.0", "end")
        self.text_output.insert("1.0", translated_text)
        self.text_output.config(state="disabled")

        # Update character count label
        char_count = len(text_to_translate)
        self.label_char_count.config(text=f"Jumlah Karakter: {char_count}")

        # Clear character limit warning
        self.label_char_limit_warning.config(text="")

    def swap_languages(self):
        current_source_lang = self.combo_from.get()
        current_target_lang = self.combo_to.get()

        # Swap the languages in the comboboxes
        self.combo_from.set(current_target_lang)
        self.combo_to.set(current_source_lang)

    def update_char_count(self, event):
        # Update character count label when text changes
        text_to_translate = self.text_input.get("1.0", "end-1c")
        char_count = len(text_to_translate)
        self.label_char_count.config(text=f"Jumlah Karakter: {char_count}")

        # Check against the character limit
        if char_count > self.character_limit:
            warning_text = f"Melebihi batas karakter ({self.character_limit})"
            self.label_char_limit_warning.config(text=warning_text)
        else:
            self.label_char_limit_warning.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()


