import json
import os

class Database:
    def __init__(self):
        """Initialize the database with users and messages."""
        self.db_file = "database.json"
        self.data = {"users": [], "messages": []}
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                self.data = json.load(f)

    def save(self):
        """Save the database to a JSON file."""
        with open(self.db_file, "w") as f:
            json.dump(self.data, f)

    def add_user(self, chat_id):
        """Add a user to the database if not already present."""
        if chat_id not in self.data["users"]:
            self.data["users"].append(chat_id)
            self.save()

    def add_message(self, message):
        """Add a message to the database if not already present."""
        if message not in self.data["messages"]:
            self.data["messages"].append(message)
            self.save()

    def get_users(self):
        """Retrieve the list of users."""
        return self.data["users"]

    def get_messages(self):
        """Retrieve the list of messages."""
        return self.data["messages"]