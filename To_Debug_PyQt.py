# To check if something was wrong when the app crashed and no information was given through the output.
if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QtWidgets.QApplication([])
    window = MyWindow(*args)
    window.show()
    sys.exit(app.exec())
