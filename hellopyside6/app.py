import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
try:
    from importlib import resources  # type: ignore
except ImportError:
    import importlib_resources as resources  # type: ignore


def main():
    print("hjer")

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    # engine.load(qml_file)
    with resources.open_binary("hellopyside6", "main.qml") as qml_file:
        engine.load(qml_file.name)
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
