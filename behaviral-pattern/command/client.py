from receiver import TextEditor
from invoker import TextEditorInvoker
from concreteCommand import WriteCommand, DeleteCommand

editor = TextEditor()
invoker = TextEditorInvoker()

writeCommand1 = WriteCommand(editor, "Hello, ")
writeCommand2 = WriteCommand(editor, "world!")
deleteCommand = DeleteCommand(editor, 6)

invoker.executeCommand(writeCommand1)
invoker.executeCommand(writeCommand2)
print(editor.getText())

invoker.executeCommand(deleteCommand)
print(editor.getText())

invoker.undo()
print(editor.getText())

invoker.undo()
print(editor.getText())