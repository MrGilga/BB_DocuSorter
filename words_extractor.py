# %%
import regex as re
import PyPDF2

def extract_text_from_pdf(pdf_file: str) -> [str]:
    reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        if content:
            pdf_text.append(content)
    return pdf_text

extracted_text = extract_text_from_pdf("pdfexample.pdf")
invoice_count = 0

# Searching for the word 'invoice' in each page's text
for text in extracted_text:
    # text is processed as lowercase and regex is used to find all occurrences
    found_invoices = re.findall(r'\binvoice\b', text.lower())
    invoice_count += len(found_invoices)

print(f"Total number of invoices: {invoice_count}")
print(f"Total number of pages: {len(extracted_text)}")

print(extracted_text)
# %%
