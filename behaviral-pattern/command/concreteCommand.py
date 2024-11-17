from command import Command


class WriteCommand(Command):

    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        self.editor.delete(len(self.text))


class DeleteCommand(Command):
    def __init__(self, editor, length):
        self.editor = editor
        self.length = length

    def execute(self):
        self.deletedText = self.editor.getText()[-self.length:]
        self.editor.delete(self.length)

    def undo(self):
        self.editor.write(self.deletedText)
