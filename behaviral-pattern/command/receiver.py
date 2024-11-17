class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def delete(self, length):
        self.text = self.text[:-length]

    def getText(self):
        return self.text
