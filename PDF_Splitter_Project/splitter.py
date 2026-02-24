from pypdf import PdfReader, PdfWriter
import os

def split_pdf(input_pdf, chunk_size):
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

        print(f"Created: {output_filename}")

if __name__ == "__main__":
    input_pdf = input("Enter PDF filename (with .pdf): ")
    chunk_size = int(input("Enter pages per split: "))
    split_pdf(input_pdf, chunk_size)