from PySide6.QtWidgets import(
    QApplication,
    QWidget, 
    QDialog, 
    QPushButton, 
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QGridLayout,
    QFormLayout,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QMenu,  
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLCDNumber,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,  
    QTreeWidget,
    QTreeWidgetItem,    
    QListWidget,
    QHBoxLayout,
    QStackedLayout,
    QTabWidget,
    QToolBar,
    QStatusBar,
    QDialogButtonBox,
    QMessageBox,
)   
from PySide6.QtGui import QPixmap, QColor, QPalette, QAction, QFont, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize, QTimer, QObject, QEvent
from PySide6.QtUiTools import QUiLoader
import sys, time
from pathlib import Path
from random import randint

from Ui_MainWindow1 import Ui_MainWindow as Ui_MainWindow1

RES_DIR = Path(__file__).resolve().parent / "res"
UI_DIR = Path(__file__).resolve().parent / "ui"

def app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        button = QPushButton("Click me")
        button.setCheckable(True)
        button.toggled.connect(self.button_toggled)
        button.clicked.connect(self.button_clicked)

        self.setFixedSize(400, 400)
        self.setCentralWidget(button)

        self.windowTitleChanged.connect(self.on_title_changed)   

    def button_clicked(self):
        print("Button clicked")
        self.setWindowTitle("Button clicked")

    def button_toggled(self, checked):
        print(f"Button toggled: {checked}")

    def on_title_changed(self, title):
        print(f"Title changed: {title}")    
        self.setWindowTitle(title)

def app1(): 
    app = QApplication(sys.argv)
    window = MainWindow1()
    window.show()
    app.exec()

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        self.input = QLineEdit()
        self.label = QLabel()
        
        print(self.input.textChanged) # <PySide6.QtCore.SignalInstance textChanged(QString) at 0x0000028B7D3126F0>
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        self.setLayout(layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

def app2():
    app = QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    app.exec()

class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setText("Click the button")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("Left button pressed")
        elif event.button() == Qt.RightButton:
            self.label.setText("Right button pressed")
        elif event.button() == Qt.MiddleButton:
            self.label.setText("Middle button pressed")
        else:
            self.label.setText("Unknown button pressed")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("Left button released")
        elif event.button() == Qt.RightButton:
            self.label.setText("Right button released")
        elif event.button() == Qt.MiddleButton:
            self.label.setText("Middle button released")
        else:
            self.label.setText("Unknown button released")

    def mousedoubleclick(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("Left button double clicked")
        elif event.button() == Qt.RightButton:
            self.label.setText("Right button double clicked")
        elif event.button() == Qt.MiddleButton:
            self.label.setText("Middle button double clicked")
        else:
            self.label.setText("Unknown button double clicked")

def app3():
    app = QApplication(sys.argv)
    window = MainWindow3()
    window.show()
    app.exec()

class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.on_custom_context_menu_requested)

    def on_custom_context_menu_requested(self, pos):
        context_menu = QMenu(self)
        context_menu.addAction("Action 1", self.action1)
        context_menu.addAction("Action 2", self.action2)
        context_menu.addAction("Action 3", self.action3)
        context_menu.exec(self.mapToGlobal(pos))

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        context_menu.addAction("Action 1", self.action1)
        context_menu.addAction("Action 2", self.action2)
        context_menu.addAction("Action 3", self.action3)
        context_menu.exec(event.globalPos())

    def action1(self):
        print("Action 1")

    def action2(self):
        print("Action 2")

    def action3(self):
        print("Action 3")

def app4():
    app = QApplication(sys.argv)
    window = MainWindow4()
    window.show()
    app.exec()


class MainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for widget in widgets:
            layout.addWidget(widget())


        layout.itemAt(4).widget().valueChanged.connect(layout.itemAt(7).widget().display)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

def app5():
    app = QApplication(sys.argv)
    window = MainWindow5()
    window.show()
    app.exec()

class MainWindow6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        label1 = QLabel()
        label1.setText("Hello, World!")
        font = label1.font()
        font.setPointSize(60)
        label1.setFont(font)
        label1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        # label1.setWordWrap(True)
        label1.setStyleSheet("background-color: gray;")

        label2 = QLabel()
        label2.setText("This is a cat!")
        label2.setPixmap(QPixmap("./res/cat.webp")) 
        label2.setScaledContents(True)
        label2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label2.setStyleSheet("background-color: red;")
        
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

def app6():
    app = QApplication(sys.argv)
    window = MainWindow6()
    window.show()
    app.exec()

class MainWindow7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        checkbox = QCheckBox()
        checkbox.setText(f'This is a checkbox, state is: {"checked" if checkbox.isChecked() else "unchecked"}')
        checkbox.setChecked(True)
        checkbox.stateChanged.connect(lambda state: checkbox.setText(f'This is a checkbox, state is: {"checked" if state else "unchecked"}'))

        checkbox2 = QCheckBox()
        checkbox2.setText("This is a partially checked checkbox")
        checkbox2.setCheckState(Qt.CheckState.PartiallyChecked)

        tree = QTreeWidget()
        tree.setHeaderHidden(True)  # hide default header that shows "1"
        tree.setColumnCount(1)

        parent = QTreeWidgetItem(tree)
        parent.setText(0, "Documents")
        parent.setFlags(
            parent.flags()
            | Qt.ItemFlag.ItemIsUserCheckable
            | Qt.ItemFlag.ItemIsAutoTristate
        )
        parent.setCheckState(0, Qt.CheckState.Unchecked)

        child1 = QTreeWidgetItem(parent)
        child1.setText(0, "Report.docx")
        child1.setFlags(child1.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        child1.setCheckState(0, Qt.CheckState.Unchecked)

        child2 = QTreeWidgetItem(parent)
        child2.setText(0, "Notes.txt")
        child2.setFlags(child2.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        child2.setCheckState(0, Qt.CheckState.Checked)

        parent.setExpanded(True)

        layout = QVBoxLayout()
        layout.addWidget(checkbox)
        layout.addWidget(checkbox2)
        layout.addWidget(tree)
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

def app7():
    app = QApplication(sys.argv)
    window = MainWindow7()
    window.show()
    app.exec()

class MainWindow8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        combo = QComboBox()
        combo.addItems(["Item 1", "Item 2", "Item 3"])
        combo.currentTextChanged.connect(lambda text: print(f"Current text selected on combo: {text}"))
        combo.currentIndexChanged.connect(lambda index: print(f"Current index selected on combo: {index}"))

        combo2 = QComboBox()
        combo2.addItems(["egg", "milk", "bread"])
        combo2.setEditable(True)

        list = QListWidget()
        list.addItems(["One", "Two", "Three"])
        list.currentTextChanged.connect(lambda text: print(f"Current text selected on list: {text}"))
        list.currentItemChanged.connect(lambda item: print(f"Current item selected on list: {item}"))

        lineedit = QLineEdit()
        lineedit.setPlaceholderText("Enter your name")
        lineedit.setStyleSheet("background-color: darkgray;")

        lineedit2 = QLineEdit()
        lineedit2.setPlaceholderText("Enter your phone number")
        lineedit2.setInputMask("+86 000 0000 0000")
        lineedit2.setStyleSheet("background-color: darkgray;")

        spinbox = QSpinBox()
        spinbox.setRange(-10, 10)
        spinbox.setValue(0)
        spinbox.setPrefix("$")
        spinbox.setSuffix(" USD")
        spinbox.setSingleStep(2)
        spinbox.lineEdit().setReadOnly(True)
        # print(spinbox.lineEdit())

        layout = QVBoxLayout()
        layout.addWidget(combo)
        layout.addWidget(combo2)
        layout.addWidget(list)
        layout.addWidget(lineedit)
        layout.addWidget(lineedit2)
        layout.addWidget(spinbox)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

def app8():
    app = QApplication(sys.argv)
    window = MainWindow8()
    window.show()
    app.exec()

class MainWindow9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        slider1 = QSlider()
        slider1.setRange(0, 100)
        slider1.setValue(50)

        slider2 = QSlider()
        slider2.setRange(0, 100)
        slider2.setValue(50)
        slider2.setOrientation(Qt.Orientation.Horizontal)

        layout1 = QHBoxLayout()
        layout1.addWidget(slider1)
        layout1.addWidget(slider2)


        dial = QDial()
        dial.setRange(0, 100)
        dial.setValue(50)
        dial.valueChanged.connect(slider1.setValue)
        dial.valueChanged.connect(slider2.setValue)
        slider1.valueChanged.connect(dial.setValue)
        slider1.valueChanged.connect(slider2.setValue)
        slider2.valueChanged.connect(slider1.setValue)
        slider2.valueChanged.connect(dial.setValue)

        layout2 = QHBoxLayout()
        layout2.addWidget(dial)

        vlayout = QVBoxLayout()
        vlayout.addLayout(layout1)
        vlayout.addLayout(layout2)

        central_widget = QWidget()
        central_widget.setLayout(vlayout)

        self.setCentralWidget(central_widget)

def app9():
    app = QApplication(sys.argv)
    window = MainWindow9()
    window.show()
    app.exec()

class Color(QWidget):
    def __init__(self, color, size: tuple[int, int] | None = None):
        super().__init__()
        self.setAutoFillBackground(True)

        # Without a minimum size, Color collapses to ~0 width in a crowded
        # QHBoxLayout, so only QFormLayout (larger min size) remains visible.
        if size is not None:
            self.setFixedSize(size[0], size[1])
        else:
            self.setMinimumSize(60, 40)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow10(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.resize(1200, 400)

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("blue"))
        layout2.addWidget(Color("green"))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout4 = QGridLayout()
        layout4.addWidget(Color('red'), 0, 0)
        layout4.addWidget(Color('blue'), 0, 1)
        layout4.addWidget(Color('green'), 0, 2)
        layout4.addWidget(Color('yellow'), 1, 0)
        layout4.addWidget(Color('orange'), 1, 1)
        layout4.addWidget(Color('pink'), 1, 2)
        layout4.addWidget(Color('brown'), 2, 0)
        layout4.addWidget(Color('gray'), 2, 1)
        layout4.addWidget(Color('black'), 2, 2)

        # QStackedLayout shows only ONE widget at a time.
        # Without changing currentIndex, you only ever see the first page.
        stack_host = QWidget()
        layout5 = QStackedLayout(stack_host)
        layout5.addWidget(Color('red'))
        layout5.addWidget(Color('blue'))
        layout5.addWidget(Color('green'))
        layout5.addWidget(Color('yellow'))
        layout5.addWidget(Color('orange'))

        prev_btn = QPushButton("上一页")
        next_btn = QPushButton("下一页")
        page_label = QLabel(f"Stacked 第 {layout5.currentIndex() + 1}/{layout5.count()} 页")

        def go_prev():
            layout5.setCurrentIndex((layout5.currentIndex() - 1) % layout5.count())
            page_label.setText(f"Stacked 第 {layout5.currentIndex() + 1}/{layout5.count()} 页")

        def go_next():
            layout5.setCurrentIndex((layout5.currentIndex() + 1) % layout5.count())
            page_label.setText(f"Stacked 第 {layout5.currentIndex() + 1}/{layout5.count()} 页")

        prev_btn.clicked.connect(go_prev)
        next_btn.clicked.connect(go_next)

        stack_panel = QVBoxLayout()
        stack_panel.addWidget(page_label)
        stack_panel.addWidget(stack_host)
        btn_row = QHBoxLayout()
        btn_row.addWidget(prev_btn)
        btn_row.addWidget(next_btn)
        stack_panel.addLayout(btn_row)

        layout6 = QFormLayout()
        layout6.addRow("Name", QLineEdit())
        layout6.addRow("Age", QSpinBox())
        layout6.addRow("Email", QLineEdit())
        layout6.addRow("Phone", QLineEdit())
        layout6.addRow("Address", QLineEdit())
        layout6.addRow("City", QLineEdit())
        layout6.addRow("State", QLineEdit())
        layout6.addRow("Zip", QLineEdit())

        layout7 = QHBoxLayout()
        layout7_1 = QVBoxLayout()
        layout7_2 = QStackedLayout()

        label_sample = QLabel("tab sample")
        # addWidget(widget, stretch) — stretch>0 means this item absorbs
        # extra height. Label grows tall but text stays small, so the gap
        # under "tab sample" looks much larger than between buttons.
        layout7_1.addWidget(label_sample)
        btn_red = QPushButton("Red")
        layout7_1.addWidget(btn_red)
        btn_red.clicked.connect(lambda: layout7_2.setCurrentIndex(0))
        btn_blue = QPushButton("Blue")
        layout7_1.addWidget(btn_blue)
        btn_blue.clicked.connect(lambda: layout7_2.setCurrentIndex(1))
        btn_green = QPushButton("Green")
        layout7_1.addWidget(btn_green)
        btn_green.clicked.connect(lambda: layout7_2.setCurrentIndex(2))
        layout7_1.addStretch()  # leftover space goes to the bottom, not between items

        layout7_2.addWidget(Color('red'))
        layout7_2.addWidget(Color('blue'))
        layout7_2.addWidget(Color('green'))
        layout7.addLayout(layout7_1)
        layout7.addLayout(layout7_2)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        # tabs.setTabPosition(QTabWidget.TabPosition.North)
        # tabs.setDocumentMode(True)
        tabs.setMovable(True)
        tabs.addTab(Color('red'), 'Red')
        tabs.addTab(Color('blue'), 'Blue')
        tabs.addTab(Color('green'), 'Green')

        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(10)
        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)
        layout1.addLayout(stack_panel)
        layout1.addLayout(layout6)
        layout1.addLayout(layout7)
        layout1.addWidget(tabs)

        central_widget = QWidget()
        central_widget.setLayout(layout1)

        self.setCentralWidget(central_widget)

def app10():
    app = QApplication(sys.argv)
    window = MainWindow10()
    window.show()
    app.exec()

class MainWindow11(QMainWindow):

    class ButtonEventFilter(QObject):
        def __init__(self, parent, watched):
            super().__init__(parent)
            self.window = parent
            self.watched = watched

        def eventFilter(self, obj, event):
            if obj is self.watched and event.type() == QEvent.Type.Leave:
                self.window.on_leave_btn_action()
            return super().eventFilter(obj, event)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        self.label = QLabel()
        self.label.setFont(QFont("Digital-7", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_update_timer)
        self.timer.start(1000)

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.btn_action = QAction(QIcon(str(RES_DIR / "pause.png")), "&Pause", self)
        # self.btn_action.setStatusTip("Pause the timer") # will override status bar
        self.btn_action.setShortcut(QKeySequence("Ctrl+P"))
        self.btn_action.triggered.connect(self.on_pause_timer)
        self.btn_action.hovered.connect(self.on_hover_btn_action)


        toolbar.addAction(self.btn_action)

        btn_widget = toolbar.widgetForAction(self.btn_action)
        btn_widget.installEventFilter(self.ButtonEventFilter(self, btn_widget))

        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Widgets Sample:"))
        toolbar.addWidget(QDateTimeEdit())
        toolbar.addWidget(QDial())

        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        self.statusBar().addWidget(QLabel("Status Bar"))
        self.statusBar().addWidget(QPushButton("Click me"))
        self.statusBar().addWidget(QDateTimeEdit())
        self.statusBar().addWidget(QDial())

        menu = self.menuBar()
        tools_menu = menu.addMenu("&Tools")
        tools_menu.addAction(self.btn_action)
        # cant not add widgets to menu
        tools_menu.addSeparator()
        sub_menu = tools_menu.addMenu("SubMenu")
        tools_menu.addAction("Exit", self.close)
        
        sub_menu.addAction("SubMenu 1", lambda: print("SubMenu 1"))
        sub_menu.addAction("SubMenu 2", lambda: print("SubMenu 2"))
        sub_menu.addAction("SubMenu 3", lambda: print("SubMenu 3"))

        self.on_update_timer()

    def on_update_timer(self):  
        self.label.setText(time.strftime("%H:%M:%S"))

    def on_hover_btn_action(self):
        label = self.statusBar().findChildren(QLabel)[0]
        if self.timer.isActive():
            label.setText("Pause the timer")
        else:
            label.setText("Resume the timer")
    
    def on_leave_btn_action(self):
        label = self.statusBar().findChildren(QLabel)[0]
        label.setText("Status Bar")

    def on_pause_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn_action.setIcon(QIcon(str(RES_DIR / "resume.png")))
            self.btn_action.setText("Resume")
            # self.btn_action.setStatusTip("Resume the timer")
        else:
            self.timer.start()
            self.btn_action.setIcon(QIcon(str(RES_DIR / "pause.png")))
            self.btn_action.setText("Pause")
            # self.btn_action.setStatusTip("Pause the timer")

def app11():
    app = QApplication(sys.argv)
    window = MainWindow11()
    window.show()
    app.exec()

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        # Pass parent to QDialog so it stays a top-level window
        # (owned/centered by parent). Do NOT call setParent() — that
        # embeds the dialog as a normal child widget and it won't pop up.
        super().__init__(parent)

        self.setWindowTitle("Dialog")

        QBtn = (QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow12(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        layout = QHBoxLayout()

        button = QPushButton("Click me for a dialog")
        button.clicked.connect(self.on_click_button)

        button2 = QPushButton("Click me for a message box")
        button2.clicked.connect(self.on_click_button2)
        
        button3 = QPushButton("Click me for a critical message box")
        button3.clicked.connect(self.on_click_button3)

        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def on_click_button(self):
        dialog = CustomDialog(self)
        dialog.setWindowTitle("Dialog")
        # dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        if dialog.exec():
            print("Success!")
        else:
            print("Cancel!")

    def on_click_button2(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("I have a question")
        msgBox.setText("Do you want to save your changes?")
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
        result = msgBox.exec()
        if result == QMessageBox.StandardButton.Save:
            print("Save!")
        elif result == QMessageBox.StandardButton.Discard:
            print("Discard!")    
        else:
            print("Cancel!")  

    def on_click_button3(self):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )
        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")

def app12():
    app = QApplication(sys.argv)
    window = MainWindow12()
    window.show()
    app.exec()

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow13(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.w2 = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.button2 = QPushButton("Push for Window2")
        self.button2.clicked.connect(self.show_new_window2)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_new_window(self, checked):
        # in a fraction of a second, local variable w will go out of scope
        # w = AnotherWindow()
        # w.show()

        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None  # Drop the reference. The object will be destroyed if no other references exist.
            
    def show_new_window2(self, checked):
        if self.w2.isVisible():
            self.w2.hide()
        else:
            self.w2.show()

def app13():
    app = QApplication(sys.argv)
    window = MainWindow13()
    window.show()
    app.exec()

def app14():
    app = QApplication(sys.argv)
    loader = QUiLoader()
    # pyside6-uic mainwindow.ui -o MainWindow.py
    window = loader.load("./ui/MainWindowDesigner1.ui", None)
    window.show()
    app.exec()

class MainWindow15(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def app15():
    app = QApplication(sys.argv)
    window = MainWindow15()
    window.show()
    app.exec()

def main():
    app15()  

if __name__ == "__main__":
    main()