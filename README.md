# Scrape Lines with Keyword

This repository contains a Python script that reads lines from a text file (`692.txt`) and looks for a given keyword. If the line contains the keyword, the script further processes it to extract and save a specific segment into an output file (`692_output.txt`).

[![Demonstration Video on YouTube](http://img.youtube.com/vi/pyetHSV5Wn8/0.jpg)](https://www.youtube.com/watch?v=pyetHSV5Wn8&t=397s)  
> *Click on the image above to watch a brief demonstration of a similar approach on YouTube.*

---

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example](#example)
7. [Potential Edge Cases](#potential-edge-cases)
8. [License](#license)

---

## Description

**Scrape Lines with Keyword** is a straightforward tool designed for processing text logs or any line-based data. The script will:

1. Prompt the user for a **keyword**.  
2. Read each line of `692.txt`.  
3. If a line **contains** that keyword, the script splits the line on the **first two colons** (`:`).  
4. The text **after** the second colon is written to `692_output.txt`.

---

## Features

- **Keyword Search**: Filter only the lines you care about.  

- **Customizable Delimiter**: Currently uses `:`, but you can adapt the script to any delimiter.  

- **Minimal Dependencies**: Uses only Python’s built-in libraries.  

- **Simple & Flexible**: Edit the script to suit your exact requirements.

- **Easy to Use**: Requires minimal setup and provides clear prompts.

---

## Prerequisites

- **Python 3.6+** installed on your system.
- A text file named **`692.txt`** in the same directory as the script.

*(No external libraries are required.)*

---

## Installation

1. **Clone** or **download** this repository.
2. Confirm you have `692.txt` in the **same folder** as the script.
3. *(Optional)* Create and activate a virtual environment (recommended if you plan to extend the script).

---

## Usage

1. Open a terminal or command prompt in the repository’s directory.

2. Copy and paste the script below into a file (e.g., `scrape.py`):

3. Run the script (python scrape.py).

4. When prompted, type in the `keyword` you want to search for:

```python
Enter the keyword to search for: bilkent
```

5. The script will process `692.txt` and save results in `692_output.txt`.

## Example: 

### Input (`692.txt`):

```python
url:login:pass
```

### Keyword: `keyword`

### Output (`692_output.txt`):

```python
login:pass # for the intended keyword pattern lines.
```

## Potential Edge Cases

1. **Missing Input File**: If 692.txt is not in the same directory, the script will display an error message.

2. **Empty Lines**: Lines with no content after the second colon will be ignored.

3. **Keyword Not Found**: If no lines contain the keyword, the output file will be empty.

4. **Encoding Issues**: Files with unusual encodings might cause errors; the script uses UTF-8 with error handling to mitigate this.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.