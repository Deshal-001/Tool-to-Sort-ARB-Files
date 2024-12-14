# Sort ARB Files Tool

## Overview
This tool helps organize `.arb` (Application Resource Bundle) files used in Flutter projects for localization. It reads an `.arb` file, sorts the translation keys alphabetically (keeping the `@@locale` key at the top), and writes the sorted data back to a new or existing `.arb` file.

By converting the script to an executable, it can be easily shared with team members to simplify the management of localization files.

---

## Features
- Reads user-specified `.arb` files.
- Sorts keys alphabetically for better organization.
- Preserves the `@@locale` key at the top for metadata consistency.
- Outputs the sorted `.arb` file to a new or existing file path.
- Can be converted into a standalone executable for ease of use.

---

## Requirements
- Python 3.x
- Libraries:
  - `json`
  - `PyInstaller` (optional for creating an executable)

---

## How to Use

### 1. Running the Script
1. Save the script as `sort_arb.py`.
2. Run the script:
   ```bash
   python sort_arb.py
   ```
3. Follow the prompts to provide the input `.arb` file path and the desired output file path.

### 2. Convert to Executable (Optional)
To make the script easier to use, create an executable with PyInstaller:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Generate the executable:
   ```bash
   pyinstaller --onefile sort_arb.py
   ```
3. The executable will be available in the `dist` directory.

---

## Why Use This Tool?
- **Improved Readability:** Makes `.arb` files easier to navigate and maintain.
- **Consistency:** Ensures all localization files follow the same structure.
- **Error Prevention:** Reduces the risk of duplicate or missing keys.
- **Team-Friendly:** Share the executable version with non-technical team members.

---

## Example
### Input `.arb` File:
```json
{
  "greeting": "Hello",
  "farewell": "Goodbye",
  "@@locale": "en"
}
```

### Sorted Output `.arb` File:
```json
{
  "@@locale": "en",
  "farewell": "Goodbye",
  "greeting": "Hello"
}
```
