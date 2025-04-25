class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes(self, keyword):
        return [note for note in self.notes if keyword.lower() in note.lower()]
