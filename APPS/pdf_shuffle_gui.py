import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import random
import os
import shutil

# 니 맥 기준 기본 폴더
DEFAULT_DIR = "/Users/wondongsoo/Downloads"

class PDFShufflerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Page Shuffler")
        self.root.geometry("420x200")

        self.pdf_path = None

        # 파일 선택 버튼
        self.btn_select = tk.Button(root, text="PDF 파일 선택", command=self.select_file)
        self.btn_select.pack(pady=10)

        # 선택된 파일 표시
        self.label_file = tk.Label(root, text="선택된 파일: 없음", wraplength=380)
        self.label_file.pack(pady=5)

        # 백업 여부 체크박스
        self.backup_var = tk.BooleanVar(value=True)
        self.chk_backup = tk.Checkbutton(root, text="원본 백업 파일 만들기 (.backup.pdf)", variable=self.backup_var)
        self.chk_backup.pack(pady=5)

        # 셔플 버튼
        self.btn_shuffle = tk.Button(root, text="페이지 셔플해서 저장 (덮어쓰기)", command=self.shuffle_and_save)
        self.btn_shuffle.pack(pady=10)

    def select_file(self):
        path = filedialog.askopenfilename(
            title="PDF 파일 선택",
            filetypes=[("PDF Files", "*.pdf")],
            initialdir=DEFAULT_DIR
        )
        if path:
            self.pdf_path = path
            self.label_file.config(text=f"선택된 파일: {os.path.basename(path)}")

    def shuffle_and_save(self):
        if not self.pdf_path:
            messagebox.showwarning("경고", "먼저 PDF 파일을 선택해라.")
            return

        try:
            input_pdf = self.pdf_path
            folder = os.path.dirname(input_pdf)
            filename = os.path.basename(input_pdf)

            # 백업
            if self.backup_var.get():
                backup_path = os.path.join(folder, filename.replace(".pdf", ".backup.pdf"))
                shutil.copy2(input_pdf, backup_path)

            reader = PdfReader(input_pdf)
            writer = PdfWriter()

            pages = list(range(len(reader.pages)))
            random.shuffle(pages)

            for p in pages:
                writer.add_page(reader.pages[p])

            # 같은 파일 이름으로 덮어쓰기
            with open(input_pdf, "wb") as f:
                writer.write(f)

            messagebox.showinfo("완료", f"셔플 완료!\n파일: {filename}")

        except Exception as e:
            messagebox.showerror("에러", f"문제 생김:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFShufflerApp(root)
    root.mainloop()