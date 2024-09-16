import os
import subprocess

def read_terms(file_path):
    """Read terms from a markdown file, remove duplicates, and return a sorted list of terms."""
    terms = []
    in_yaml_header = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '---':
                in_yaml_header = not in_yaml_header  # Toggle the YAML header flag
                continue
            if not in_yaml_header and line:  # Only read terms if not in the YAML header
                terms.append(line)
    # Remove duplicates and return sorted terms
    return sorted(set(terms))

def escape_latex(term):
    """Escape special LaTeX characters in a term."""
    return term.replace('&', '\\&')

def create_markdown_table(terms, rows_per_table=49, columns=4):
    """Create LaTeX longtables from the sorted list of terms with fixed column widths and text wrapping."""
    column_width = '4.5cm'
    tables = []

    # Calculate the total number of rows
    total_rows = len(terms)

    # Create tables while filling columns across pages
    for table_index in range(0, total_rows, rows_per_table * columns):
        table = [
            '\\newpage',  # Start a new page before the table
            '\\begin{longtable}{|' + ' | '.join([f'p{{{column_width}}}' for _ in range(columns)]) + '|}',
            '\\hline'
        ]

        # Prepare the table rows
        for row in range(rows_per_table):
            row_terms = []
            for col in range(columns):
                # Calculate the index for the term
                index = (row + col * rows_per_table) + table_index
                if index < total_rows:
                    # Escape the term before adding it to the table
                    row_terms.append(escape_latex(terms[index]))
                else:
                    row_terms.append('')  # Fill empty cells
            table.append(' & '.join(row_terms) + ' \\\\ \\hline')  # Add row with horizontal line

        # End the longtable
        table.append('\\end{longtable}')
        tables.append('\n'.join(table))

    return '\n\n'.join(tables)  # Separate tables with a double newline

def write_markdown_file(output_path, content):
    """Write the markdown content to a file."""
    with open(output_path, 'w') as file:
        file.write(content)

def export_to_pdf(markdown_file, output_pdf):
    """Use Pandoc to convert the markdown file to PDF."""
    command = ['pandoc', markdown_file, '-o', output_pdf, '--pdf-engine=/Users/jacksonbe3/Library/TinyTeX/bin/universal-darwin/xelatex', '--standalone']
    try:
        subprocess.run(command, check=True)
        print(f"PDF exported successfully to {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while exporting to PDF: {e}")

def main():
    input_file = 'bonesWordBank.md'  # Change this to your input markdown file name
    output_markdown_file = 'output_table.md'  # Change this to your desired output file name
    output_pdf_file = 'bones_wordBank.pdf'  # Desired output PDF file name

    # Read terms, create table, and write to output markdown file
    terms = read_terms(input_file)
    markdown_table = create_markdown_table(terms)

    # Prepare the full markdown content with YAML header
    markdown_content = f"""---
geometry: "margin=.3in, letterpaper"
documentclass: article
header-includes:
  - \\usepackage{{booktabs}}
  - \\usepackage{{array}}
  - \\usepackage{{caption}}
  - \\usepackage{{longtable}}
output: 
  pdf_document:
    latex_engine: xelatex
---

{markdown_table}
"""
    write_markdown_file(output_markdown_file, markdown_content)

    # Export the markdown file to PDF
    export_to_pdf(output_markdown_file, output_pdf_file)

if __name__ == "__main__":
    main()