from abc import ABC, abstractmethod

from src.utils.SimpleKeyboard import SimpleKeyboard


class IEditorInterface(ABC):
    @abstractmethod
    def forward_frames(self, n: int) -> None:
        pass

    @abstractmethod
    def cut(self, cam: int) -> None:
        pass


class Resolve(IEditorInterface):
    def forward_frames(self, n: int) -> None:
        SimpleKeyboard.press_numpad(f"+{n}enter")

    def cut(self, cam: int) -> None:
        allowed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if cam not in allowed:
            raise ValueError(f"Invalid camera number {cam}")

        key = str(cam)
        SimpleKeyboard.press(key)