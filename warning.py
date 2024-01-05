class WarningNotification:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def write_warning_to_db(self):
        pass