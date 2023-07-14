from commands.command import Command

class CommandStack():
    def __init__(self) -> None:
        self.undoStack: list[Command] = []
        self.redoStack: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self.undoStack.append(command)
        # self.redoStack = [] 

    def undo(self) -> None:
        if len(self.undoStack) == 0:
            return
        lastCommand = self.undoStack[-1]
        lastCommand.undo()
        self.redoStack.append(lastCommand)
        self.undoStack.pop(-1)

    def redo(self) -> None:
        if len(self.redoStack) == 0:
            return
        lastUndo = self.redoStack[-1]
        lastUndo.redo()
        self.undoStack.append(lastUndo)
        self.redoStack.pop(-1)