from pathlib import Path

from parsers.text_parser import parse_text
from parsers.pdf_parser import parse_pdf
from parsers.docx_parser import parse_docx
from parsers.pptx_parser import parse_pptx
from parsers.xlsx_parser import parse_xlsx

class Indexer:

    def parse_file(
        self,
        file_path
    ):

        ext = Path(
            file_path
        ).suffix.lower()

        if ext in [".txt",".md",".py",".cpp",".java"]:
            return parse_text(file_path)

        elif ext == ".pdf":
            return parse_pdf(file_path)

        elif ext == ".docx":
            return parse_docx(file_path)

        elif ext == ".pptx":
            return parse_pptx(file_path)

        elif ext == ".xlsx":
            return parse_xlsx(file_path)

        return ""