import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
from ClibboardWatcher import ClipboardWatcher
from notifypy import Notify

def main():
    app = QApplication(sys.argv)

    # Check if system tray is available
    if not QSystemTrayIcon.isSystemTrayAvailable():
        print("System tray is not available")
        return

    # Create a system tray icon
    tray_icon = QSystemTrayIcon(QIcon("follow.png"))  # Replace with your icon path

    # Create a menu for the tray icon
    menu = QMenu()

    # Add "Open" action
    open_action = QAction("Open", tray_icon)
    menu.addAction(open_action)
    open_action.triggered.connect(open_triggered)

    # Add "Settings" action
    settings_action = QAction("Settings", tray_icon)
    menu.addAction(settings_action)
    settings_action.triggered.connect(settings_triggered)

    # Add "Quit" action
    quit_action = QAction("Quit", tray_icon)
    menu.addAction(quit_action)
    quit_action.triggered.connect(app.quit)

    # Set the menu to the tray icon and show it
    tray_icon.setContextMenu(menu)
    tray_icon.show()

    watcher = define_watcher()

    sys.exit(app.exec())

def define_watcher():
    if sys.platform == "darwin":
        return ClipboardWatcher(on_clipboard_change_mac)
    else:
        clipboard = app.clipboard()
        clipboard.dataChanged.connect(on_clipboard_change)
        return None

def on_clipboard_change_win(content):
    clipboard = QApplication.clipboard()
    if clipboard.mimeData().hasText():
        text = clipboard.text()
        on_clipboard_change(text)

def on_clipboard_change_mac(content):
    on_clipboard_change(content)

def on_clipboard_change(content):
    print(f"Clipboard changed: {content}")
    notification = Notify()
    notification.title = " "
    notification.message = content
    notification.send()

def open_triggered():
    print("Open clicked")

def settings_triggered():
    print("Settings clicked")

if __name__ == "__main__":
    main()
