import pyttsx3
import PyPDF2
import os


def pdf_to_speech(pdf_file):
    # Remove 'file://' prefix if present
    if pdf_file.startswith("file:///"):
        pdf_file = pdf_file[8:]

    # Ensure the path is normalized for the operating system
    pdf_file = os.path.normpath(pdf_file)

    try:
        # Initialize PDF Reader
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

            # Initialize text-to-speech engine
            engine = pyttsx3.init()

            # Read text from each page and convert to speech
            print("Converting PDF to speech...")
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                if text:
                    print(f"Reading page {page_num + 1}/{num_pages}")
                    engine.say(text)
                else:
                    print(f"Page {page_num + 1} is empty or not readable.")

            # Run the speech engine
            engine.runAndWait()
    except FileNotFoundError:
        print(f"Error: File '{pdf_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace 'sample.pdf' with the path to your PDF file
    pdf_file = input("Enter the path to the PDF file: ")
    pdf_to_speech(pdf_file)