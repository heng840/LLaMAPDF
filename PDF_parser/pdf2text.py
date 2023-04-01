import PyPDF2
import sys


def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python pdf2text.py <pdf_file_path>")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    extracted_text = pdf_to_text(pdf_file_path)

    print(extracted_text)


if __name__ == "__main__":
    main()
