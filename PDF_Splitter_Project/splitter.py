import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from pypdf import PdfReader, PdfWriter


def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        file_entry.delete(0, "end")
        file_entry.insert(0, file_path)


def split_pdf():
    input_pdf = file_entry.get()
    chunk_size = chunk_entry.get()

    if not os.path.exists(input_pdf):
        messagebox.showerror("Error", "File not found!")
        return

    if not chunk_size.isdigit() or int(chunk_size) <= 0:
        messagebox.showerror("Error", "Enter valid chunk size!")
        return

    chunk_size = int(chunk_size)

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    base_name = os.path.splitext(input_pdf)[0]

    for start in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        end = min(start + chunk_size, total_pages)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_filename = f"{base_name}_{start+1}-{end}.pdf"

        with open(output_filename, "wb") as f:
            writer.write(f)

    messagebox.showinfo("Success", "PDF split successfully!")


# GUI Setup
root = Tk()
root.title("PDF Splitter Tool")
root.geometry("450x200")

Label(root, text="Select PDF File:").pack(pady=5)

file_entry = Entry(root, width=50)
file_entry.pack()

Button(root, text="Browse", command=browse_file).pack(pady=5)

Label(root, text="Pages per Split:").pack(pady=5)

chunk_entry = Entry(root)
chunk_entry.pack()

Button(root, text="Split PDF", command=split_pdf).pack(pady=10)

root.mainloop()