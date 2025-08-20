<p align="center">
  <br/>
  <br/>
  <picture>
    <img alt="mdfy teaser" src="https://raw.githubusercontent.com/argonism/mdfy/main/mdfy.png" style="max-width: 100%;">
  </picture>
</p>

<p align="center">
    <img alt="test" src="https://img.shields.io/github/actions/workflow/status/argonism/mdfy/test_for_pr.yml?logo=pytest&label=test&color=green">
    <img alt="latest version" src="https://img.shields.io/github/v/tag/argonism/mdfy?logo=pypi&logoColor=white&label=latest%20version">
    <a href='https://mdfy.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/mdfy/badge/?version=latest' alt='Documentation Status' /></a>
    <a href="https://pepy.tech/projects/mdfy"><img src="https://static.pepy.tech/badge/mdfy" alt="PyPI Downloads"></a>
</p>

# mdfy

mdfy is a Python library that makes creating markdown documents as simple as writing Python code. Generate reports, documentation, and structured content with an intuitive, object-oriented API.

## 🚀 Quick Start

### Installation

```shell
pip install mdfy
```

### Usage

```python
from mdfy import Mdfier, MdHeader, MdText, MdTable
# Create markdown content
content = [
    MdHeader("My Report"),
    MdText("This quarter's sales were [excellent:bold]!"),
    MdTable([
        {"Product": "Laptop", "Sales": 1200, "Growth": "+15%"},
        {"Product": "Phone", "Sales": 800, "Growth": "+8%"}
    ])
]
# Generate markdown file
Mdfier("report.md").write(content)
```

## 📖 Documentation

| Resource | Description |
|----------|-------------|
| [**Getting Started**](https://mdfy.readthedocs.io/en/latest/getting_started.html) | Step-by-step tutorial for beginners |
| [**User Guide**](https://mdfy.readthedocs.io/en/latest/user_guide.html) | Complete feature documentation |
| [**Examples**](https://mdfy.readthedocs.io/en/latest/examples.html) | Real-world usage examples |
| [**API Reference**](https://mdfy.readthedocs.io/en/latest/mdfy.html) | Complete API documentation |

### Basic Features

| Feature | Description |
|---------|-------------|
| **Text styling** | Format text with bold, italic, and more - even in the middle of text |
| **Headers** | Multiple levels for document structure |
| **Links** | Internal and external linking |
| **Lists** | Ordered and unordered with nesting support |
| **Tables** | From dictionaries and lists with formatting |
| **Images** | With alt text and titles |
| **Code blocks** | With syntax highlighting |
| **Quotes** | For emphasis and citations |
| **Horizontal rules** | For section separation |
| **Table of Contents** | Automatic generation from headers |

### Basic Usage

```python
import mdfy as m

# Create content
content = [
    m.header("My Report"),
    m.text("This quarter's sales were [excellent:bold]!"),
    m.table(
        [
            {"Product": "Laptop", "Sales": 1200, "Growth": "+15%"},
            {"Product": "Phone", "Sales": 800, "Growth": "+8%"},
        ]
    ),
]

# Generate markdown file
m.Mdfier.from_filepath("report.md").write(content)
```

**Output:**
```markdown
# My Report

This quarter's sales were [excellent:bold]!

| Product | Sales | Growth |
| --- | --- | --- |
| Laptop | 1200 | +15% |
| Phone | 800 | +8% |
```

## 🎨 Core Elements

**Headers & Text**
```python
MdHeader("Title", level=1)                    # # Title
MdText("[Bold:bold] and [italic:italic]")     # **Bold** and *italic*
```

**Data & Lists**
```python
MdTable(data, precision=2)                    # Convert dicts/lists to tables
MdList(items, numbered=True)                  # • Bullet or 1. Numbered lists
```

**Code & More**
```python
MdCode("print('hello')", syntax="python")     # Syntax-highlighted code blocks
```

You can use a shortened syntax for convenience:

```python
import mdfy as m
# Create a header
header = m.header("My Report", level=1)        # # My Report
text = m.text("This quarter's sales were [excellent:bold]!")
table = m.table([
    {"Product": "Laptop", "Sales": 1200, "Growth": "+15%"},
    {"Product": "Phone", "Sales": 800, "Growth": "+8%"}
])
```

## 💡 Real-world Examples

### Dynamic Reports

```python
import mdfy as m

def generate_sales_report(sales_data):
    total = sum(item['amount'] for item in sales_data)
    return [
        m.header("Sales Report"),
        m.text(f"Total Revenue: [${total:,}:bold]"),
        m.table(sales_data, precision=2)
    ]

m.Mdfier.from_filepath("sales.md").write(generate_sales_report(quarterly_data))
```

### Data Analysis
```python
# Convert pandas DataFrame to markdown table
df_summary = df.describe()
table = MdTable(df_summary.to_dict(), precision=3)

# Create analysis report
analysis = [
    MdHeader("Data Analysis Report"),
    MdText("Dataset contains [1,000:bold] records with [95%:bold] completeness."),
    MdTable(df_summary.to_dict(), precision=3)
]
```


## 🔧 Advanced Features

- **Nested Content**: Organize content hierarchically
- **Custom Formatting**: Flexible text styling with `[text:style]` syntax
- **Table Customization**: Headers, row labels, precision control, transposition
- **Independent Elements**: Each element can be used standalone
- **Type Safety**: Full type hints for better IDE support
- ""Table of Contents**: Automatically generated from headers

## 🤝 Contributing

We welcome contributions! Here's how to get started:

```shell
# Development setup
git clone https://github.com/argonism/mdfy.git
cd mdfy
uv sync --all-groups

# Run tests
python -m pytest
```

**Areas we'd love help with:**
- 🐛 Bug reports and fixes
- 📚 Documentation improvements
- ✨ New element types
- 🎨 Styling and formatting features


## 📜 License

This project is licensed under the MIT License.
