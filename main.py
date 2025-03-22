import sys
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QInputDialog, QMessageBox, QListWidget)
from PyQt5.QtGui import QFont  

class Note:
    def __init__(self, title, content, date, Id):
        self.title = title
        self.content = content
        self.date = int(date)
        self.Id = int(Id)

class Notebook:
    def __init__(self):
        self.notes = []
        self.load_notes()
    
    def add_note(self, title, content, date, Id):
        if any(note.Id == Id for note in self.notes):
            raise ValueError("Bu ID zaten kullanılıyor!")
        new_note = Note(title, content, date, Id)
        self.notes.append(new_note)
        self.save_notes()

    def list_notes(self):
        return [(note.Id, note.title, note.date, note.content) for note in self.notes]

    def update_note(self, Id, new_title, new_content, new_date):
        for note in self.notes:
            if note.Id == Id:
                note.title = new_title
                note.content = new_content
                note.date = int(new_date)
                self.save_notes()
                return True
        return False
    
    def delete_note(self, Id):
        self.notes = [note for note in self.notes if note.Id != Id]
        self.save_notes()
    
    def save_notes(self):
        with open('notes.json', 'w') as file:
            json_notes = [note.__dict__ for note in self.notes]
            json.dump(json_notes, file)

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                json_notes = json.load(file)
                self.notes = [Note(**note) for note in json_notes]
        except FileNotFoundError:
            self.notes = []

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notebook = Notebook()
        self.setWindowTitle("Simple Notebook")
        self.setGeometry(100, 100, 400, 300)

        
        anime_font = QFont("Comic Sans MS", 14)
        

        
        widget = QWidget()
        layout = QVBoxLayout()

        
        self.note_list = QListWidget()
        self.note_list.setStyleSheet("background-color: #FFB6C1; color: #FDF5E6;")
        self.note_list.setFont(anime_font)  # Yazı tipini uygula
        layout.addWidget(self.note_list)

        
        add_button = QPushButton("Add Note")
        list_button = QPushButton("List Notes")
        update_button = QPushButton("Update Note")
        delete_button = QPushButton("Delete Note")
        exit_button = QPushButton("Exit")

        
        button_style = """
            QPushButton {
                background-color: #FFB6C1;  /* Tatlı pembe */
                color: #FFFACD;            /* Pastel sarı */
                border: 1px solid #FFFACD;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #FF9999;
            }
        """
        add_button.setStyleSheet(button_style)
        list_button.setStyleSheet(button_style)
        update_button.setStyleSheet(button_style)
        delete_button.setStyleSheet(button_style)
        exit_button.setStyleSheet(button_style)

        
        add_button.setFont(anime_font)
        list_button.setFont(anime_font)
        update_button.setFont(anime_font)
        delete_button.setFont(anime_font)
        exit_button.setFont(anime_font)

        
        add_button.clicked.connect(self.add_note_gui)
        list_button.clicked.connect(self.refresh_list)
        update_button.clicked.connect(self.update_note_gui)
        delete_button.clicked.connect(self.delete_note_gui)
        exit_button.clicked.connect(self.close)

        
        layout.addWidget(add_button)
        layout.addWidget(list_button)
        layout.addWidget(update_button)
        layout.addWidget(delete_button)
        layout.addWidget(exit_button)

        
        widget.setStyleSheet("background-color: #C8A2C8;")
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.refresh_list()

    def add_note_gui(self):
        try:
            title, ok = QInputDialog.getText(self, "Input", "Başlık giriniz:")
            if not ok: return
            content, ok = QInputDialog.getText(self, "Input", "Konuyu giriniz:")
            if not ok: return
            date, ok = QInputDialog.getInt(self, "Input", "Tarihi giriniz:")
            if not ok: return
            Id, ok = QInputDialog.getInt(self, "Input", "ID Kimliğinizi giriniz:")
            if not ok: return
            self.notebook.add_note(title, content, date, Id)
            self.refresh_list()
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))

    def refresh_list(self):
        self.note_list.clear()
        for note in self.notebook.list_notes():
            self.note_list.addItem(f"ID: {note[0]} | Title: {note[1]} | Date: {note[2]}")

    def update_note_gui(self):
        Id, ok = QInputDialog.getInt(self, "Input", "Güncellenecek notun kimliğini giriniz:")
        if not ok: return
        new_title, ok = QInputDialog.getText(self, "Input", "Yeni başlık giriniz: ")
        if not ok: return
        new_content, ok = QInputDialog.getText(self, "Input", "Yeni içerik giriniz: ")
        if not ok: return
        new_date, ok = QInputDialog.getInt(self, "Input", "Yeni tarihi giriniz: ")
        if not ok: return
        if self.notebook.update_note(Id, new_title, new_content, new_date):
            self.refresh_list()
        else:
            QMessageBox.critical(self, "Error", "NOT BULUNAMIYOR.")

    def delete_note_gui(self):
        Id, ok = QInputDialog.getInt(self, "Input", "Silinecek notun kimliğini girin:")
        if ok:
            self.notebook.delete_note(Id)
            self.refresh_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())