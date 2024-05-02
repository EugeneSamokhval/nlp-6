from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets
import logging
import interface
import sys  # sys нужен для передачи argv в QApplication
import nlp
import datetime
import re
logger = logging.getLogger(__name__)


def get_date():
    return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")


class ChatApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ChatApp, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_request)
        model = QStandardItemModel()
        model.setObjectName('MyModel')
        model.appendRow(QStandardItem(
            'Assistant: I\'m your personal real estate assistant. How can i help you?'))
        self.columnView.setModel(model)

    def send_request(self):
        model = self.columnView.model()
        user_message = self.plainTextEdit.toPlainText()
        logger.info(
            f'Sending request: {user_message} Time:{get_date()}'.strip(
                '<|im_start|>').strip('<|im_end|>'))
        self.plainTextEdit.setPlainText('')
        model: QStandardItemModel
        model.appendRow(QStandardItem(f'User:{user_message}'))
        responce = nlp.process_text(user_message).replace('\n', '')
        pattern = r'(.*)(<\|im_start\|>assistant)'
        some_text = re.findall(pattern, responce, re.MULTILINE)[0][0]
        responce = responce.replace(some_text, '')
        responce = responce.replace(
            '<|im_end|>', '').replace('<|im_start|>', '').removeprefix('assistant')
        if responce:
            answer = f'Assistant:\n{responce}'
            model.appendRow(QStandardItem(answer))
            logger.info(
                f"Request solved. Responce: {responce} Time:{get_date()}")
        else:
            model.appendRow(QStandardItem(
                'Error:\nError ocured during responce generation'))
            logger.error(
                f'Error during processing request Time:{get_date()}')
        self.columnView.setModel(model)


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info(
        f'Started Time:{datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")}')
    app = QtWidgets.QApplication(sys.argv)
    window = ChatApp()
    window.show()
    app.exec_()
    logger.info(
        f'Finished Time:{datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")}')


if __name__ == '__main__':
    main()
