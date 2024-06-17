# %%
from typing import List # only needed for versions before python 3.9
import regex as re
import PyPDF2

def extract_text_from_pdf(pdf_file: str) -> List[str]:
    reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        if content:
            pdf_text.append(content)
    return pdf_text

extracted_text = extract_text_from_pdf("pdfexample.pdf")
words_list = []
invoice_count = 0

for text in extracted_text:
    # clean_text = only keep alphanumeric characters and the euro/dollar symbol
    clean_text = re.sub(r'[^a-zA-Z0-9\s€$]', '', text)
    lower_text = clean_text.lower()
    words = lower_text.split()
    words_list.extend(words)
    found_invoices = re.findall(r'\binvoice\b', lower_text)
    invoice_count += len(found_invoices)

print(f"Total number of invoices: {invoice_count}")
print(f"Total number of pages: {len(extracted_text)}")

print(words_list)
# %%
