import json
from PyQt5.QtWidgets import QMessageBox

class DataManager:
    def __init__(self, parent=None):
        self.parent = parent
        self.tasks = []
        self.records = {}
        self.load_data()

    def save_data(self):
        # Save data in JSON format
        data = {
            "tasks": self.tasks,
            "records": self.records
        }
        try:
            with open("study_progress_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            self.show_error_message(f"Failed to save data: {e}")

    def load_data(self):
        # Load data from JSON file
        try:
            with open("study_progress_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = data.get("tasks", [])
                self.records = data.get("records", {})
        except FileNotFoundError:
            # Do nothing if file not found
            pass
        except Exception as e:
            self.show_error_message(f"Failed to load data: {e}")

    def show_error_message(self, message):
        if self.parent:
            QMessageBox.critical(self.parent, "Error", message)