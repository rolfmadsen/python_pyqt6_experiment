# Database Analysis Tool

## Overview

This PyQt application, "Database Analysis Tool," is designed for System Analysis. It allows users to select specific systems and perform data processing tasks related to system relationships and object interactions.

## Features

- **System Selection**: Choose from predefined systems for analysis.
- **Data Processing Options**: Select different types of data processing jobs related to system landscapes and object relationships.
- **Internationalization**: Support for English and Danish languages.

## Getting Started

### Prerequisites

- Python 3.x
- PyQt6

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git [clone github.com/rolfmadsen/python_pyqt6_experiment]
   cd [python_pyqt6_experiment]
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Execute the main script to start the application:

```bash
python main.py
```

## Internationalization (i18n)

This application supports internationalization and is currently available in English and Danish.

### Updating Translations

To update translations:

1. **Generate POT file**:
   ```bash
   xgettext --from-code=UTF-8 -d databaseanalysis -o locales/databaseanalysis.pot main.py
   ```

2. **Create/Update PO files**:
   ```bash
   msginit -l da -o locales/da/LC_MESSAGES/databaseanalysis.po -i locales/databaseanalysis.pot
   msgmerge -U locales/da/LC_MESSAGES/databaseanalysis.po locales/databaseanalysis.pot
   ```

3. **Compile PO files to MO files**:
   ```bash
   msgfmt locales/da/LC_MESSAGES/databaseanalysis.po -o locales/da/LC_MESSAGES/databaseanalysis.mo
   ```

### Testing Translations

Uncomment the line in `main.py` to force the application to use the Danish locale:

```python
os.environ['LANGUAGE'] = 'da_DK'
```

## License

GPL-3.0 license