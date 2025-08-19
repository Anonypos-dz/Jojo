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

# Add an elements to the head
page.head_add_element(name="link",attributes="rel='stylesheet' herf='style.css'")
page.head_add_element(name="link",attributes="rel='icon' herf='icon.ico'")

# Add a paragraph
page.body_add_element(name="p", content="This is an example paragraph.",attributes="id='hi' onclick='alert(0)'")

# Add a table
page.add_table(
    rows=[
        ["Name", "Age", "City"],
        ["Alice", "30", "NY"],
        ["Bob", "25", "Paris"]
    ],
    table_attributes="class='table'"
)

# Get the HTML code
html_code = page.get_page()
print(html_code)
