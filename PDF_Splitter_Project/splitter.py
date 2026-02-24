from pypdf import PdfReader, PdfWriter
import os

def split_pdf(input_pdf, chunk_size):
    if not os.path.exists(input_pdf):
        print("❌ File not found.")
        return

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    if chunk_size <= 0:
        print("❌ Chunk size must be greater than 0.")
        return

    print(f"\n📄 Total Pages: {total_pages}")
    print(f"🔪 Splitting into chunks of {chunk_size} pages...\n")

    base_name = os.path.splitext(input_pdf)[0]

    for start in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        end = min(start + chunk_size, total_pages)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_filename = f"{base_name}_{start+1}-{end}.pdf"

        with open(output_filename, "wb") as f:
            writer.write(f)

        print(f"✅ Created: {output_filename}")

    print("\n🎉 Splitting Complete!")

if __name__ == "__main__":
    input_pdf = input("Enter full PDF path or filename: ").strip()
    chunk_size = int(input("Enter pages per split: "))
    split_pdf(input_pdf, chunk_size)