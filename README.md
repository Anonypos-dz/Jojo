# Jojo — Minimalist HTML Generator

Jojo is a Python script that allows you to easily create HTML pages in a structured way.  
It provides methods to add headings, paragraphs, tables, and more while keeping the code clean and readable.

## 📦 Installation

No installation required.  
Simply download `jojo.py` and import it into your Python project.

## 🧰 Usage Example

```python
from jojo import Jojo as jj

# Create a page with a title
page = jj("My First Page")

# Add an H1 heading
page.head_add_element("h1", "Welcome to my page")

# Add a paragraph
page.body_add_element("p", "This is an example paragraph.")

# Add a table
page.add_table(
    rows=[
        ["Name", "Age", "City"],
        ["Alice", "30", "Paris"],
        ["Bob", "25", "Lyon"]
    ],
    table_attributes="class='table'"
)

# Get the HTML code
html_code = page.get_page()
print(html_code)
