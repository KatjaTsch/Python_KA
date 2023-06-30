import datetime
import os   
import json

class Note:
    def __init__(self, title: str, body: str, creation_date_time = None, modification_date_time=None) -> None:
        self.title = title
        self.body = body
        self.creation_date_time = creation_date_time if creation_date_time else str(datetime.datetime.now())
        self.modification_date_time = modification_date_time if modification_date_time else str(datetime.datetime.now())

    def __str__(self):
        return f"title: {self.title}\n" \
               f"create: {self.creation_date_time}\n" \
               f"modify: {self.modification_date_time}\n" \
               f"note: {self.body}\n" \

class NotesList:
    def __init__(self, path: os.path):
        self.notes = None
        self.idx = None
        self.path = path
        self.read_notes_from_file()

    def read_notes_from_file(self):
        self.notes = dict()
        self.idx = 0
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                notes_from_json = json.load(f)
                for idx, note in notes_from_json.items():
                    self.notes[int(idx)] = Note(note.get('title'), note.get('body'),
                                           note.get('creation_date_time'),
                                           note.get('modification_date_time'))
                self.idx = max(self.notes) + 1 if self.notes else 1

    def save_notes(self):
        with open(self.path, 'w') as f:
            json.dump(self.notes_to_dict(), f)

    def change_note(self, idx: int, note: Note):
        old_note = self.notes[idx]
        new_note = Note(note.title, note.body, old_note.creation_date_time, str(datetime.datetime.now()))
        self.notes[idx] = new_note

    def add_note(self, note: Note):
        self.notes[self.idx] = note
        self.idx += 1
        self.save_notes()

    def remove_note(self, idx: int):
        del self.notes[idx]
        self.save_notes()

    def get_note(self, idx):
        return self.notes[idx]

    def show_notes(self):
        for idx, note in self.notes.items():
            print(f"{'-' * 45}  ID: {idx}  {'-' * 45}")
            print(note)

    def notes_to_dict(self):
        return {idx: dict(title=note.title, body=note.body,
                          creation_date_time=note.creation_date_time,
                          modification_date_time=note.modification_date_time) for idx, note in self.notes.items()}

    def __len__(self):
        return len(self.notes)







# __init__(self, title: str, body: str, creation_date_time=None, modification_date_time=None) -> None:
#         self.title = title
#         self.body = body
#         self.creation_date_time = creation_date_time if creation_date_time else str(datetime.datetime.now())
#         self.modification_date_time = modification_date_time if modification_date_time else str(datetime.datetime.now())

# dt_now = datetime.datetime.now()


