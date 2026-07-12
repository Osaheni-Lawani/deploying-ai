from config import MAX_HISTORY


class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(self, user_message, assistant_message):

        self.history.append(
            {
                "user": user_message,
                "assistant": assistant_message
            }
        )

        # Keep only recent conversations
        self.history = self.history[-MAX_HISTORY:]


    def get_history(self):

        return self.history


    def clear(self):

        self.history = []
