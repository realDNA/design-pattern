class TextEditorInvoker:
    def __init__(self):
        self.history = []

    def executeCommand(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
