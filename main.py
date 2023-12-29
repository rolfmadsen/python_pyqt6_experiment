# Create and activate a virtual envirtonment
"""
python3 -m venv venv
source venv/bin/activate
"""

# Install required packages
"""
pip install -r requirements.txt
pip freeze > requirements.txt # add new packages to requirements.txt
"""

# Translate (i18n) english system text strings
"""
## Create POT file with the text strings marked with _() in the main.py file
xgettext --from-code=UTF-8 -d databaseanalysis -o locales/databaseanalysis.pot main.py

## Create PO files from the POT file
msginit -l da -o locales/da/LC_MESSAGES/databaseanalysis.po -i locales/databaseanalysis.pot
## Update PO files and merge changes without removing existing translations
msgmerge -U locales/da/LC_MESSAGES/databaseanalysis.po locales/databaseanalysis.pot

Now translate the english text strings in the .po file

## Compile .po files to .mo files
msgfmt locales/da/LC_MESSAGES/databaseanalysis.po -o locales/da/LC_MESSAGES/databaseanalysis.mo
"""

import sys
import gettext
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QCheckBox, QPushButton, QMessageBox
from PyQt6.QtCore import pyqtSlot
from enum import Enum

# Set environment variable for locale to test danish translation in english language Operation System
#os.environ['LANGUAGE'] = 'da_DK'

# Setup gettext and locale
locale_dir = './locales'
gettext.bindtextdomain('databaseanalysis', locale_dir)
gettext.textdomain('databaseanalysis')
_ = gettext.gettext


class SelectedSystem(Enum):
    SYS1 = _("System 1")
    SYS2 = _("System 2")
    SYS3 = _("System 3")

class DatabaseAnalysis(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(_("University of Copenhagen - System Analysis"))

        layout = QVBoxLayout()
        self.comboBox = QComboBox()
        for selected_system in SelectedSystem:
            self.comboBox.addItem(selected_system.name, selected_system.value)
        layout.addWidget(self.comboBox)

        # Checkboxes for data processing jobs
        self.job1CheckBox = QCheckBox(_("System landscape of all system relations"))
        self.job2CheckBox = QCheckBox(_("System landscape of systems with relations to the selected system"))
        self.job3CheckBox = QCheckBox(_("Relationships between objects in systems referring to objects and their column names in the selected system"))
        layout.addWidget(self.job1CheckBox)
        layout.addWidget(self.job2CheckBox)
        layout.addWidget(self.job3CheckBox)

        # Submit button
        self.submitButton = QPushButton(_("Submit"))
        self.submitButton.clicked.connect(self.onSubmit)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    @pyqtSlot()
    def onSubmit(self):
        if not any([self.job1CheckBox.isChecked(), self.job2CheckBox.isChecked(), self.job3CheckBox.isChecked()]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(_("Please select at least one option for data processing and output"))
            msg.setWindowTitle(_("Selection Required"))
            msg.exec()
            return
        
        self.close()

        selected_system = self.comboBox.currentText()
        print(f"Selected system: {selected_system}")

        # Data processing logic goes here
        if self.job1CheckBox.isChecked():
            # Perform job 1
            print("Checked job 1")
            pass
        if self.job2CheckBox.isChecked():
            # Perform job 2
            print("Checked job 2")
            pass
        if self.job3CheckBox.isChecked():
            # Perform job 3
            print("Checked job 3")
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DatabaseAnalysis()
    window.show()
    sys.exit(app.exec())