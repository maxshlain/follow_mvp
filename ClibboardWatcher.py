from PySide6.QtCore import QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication

class ClipboardWatcher:
    def __init__(self, callback):
        self._callback = callback
        self._clip = QApplication.clipboard()
        self._recent_value = self._clip.text()
        self._timer = QTimer()
        self._timer.timeout.connect(self._on_timeout)
        self._timer.start(1000)  # check every second

    def _on_timeout(self):
        tmp_value = self._clip.text()
        if tmp_value != self._recent_value:
            self._recent_value = tmp_value
            self._callback(self._recent_value)

# def my_callback(content):
#     print(f'Clipboard changed: {content}')

# app = QApplication([])
# clip_watcher = ClipboardWatcher(my_callback)
# app.exec()
