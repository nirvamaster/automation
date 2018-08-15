import PyPDF2

#FIRST: OPEN and READ PDF file
##Enter the path before the name of the file (e.g. C:\Users\...\Desktop)
print("Welcome to PDF Analyzer")
print("Add The PDF filename")
pdf_name = input()
pdf_file = open(pdf_name, 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()

print("This document contains " + str(number_of_pages) + " pages.")
print("How many pages would you like to analyze?")
limit_pages = input()
print("What is your first keyword?")
keyword_1 = input()
print("What is your second keyword?")
keyword_2 = input()
print("What is your third keyword?")
keyword_3 = input()
print("The text conversion is starting...")

page = read_pdf.getPage(0)
page_content = page.extractText()
number_of_pages = limit_pages
#SECOND: Loop the text of the PDF and match text and page number in same dictionary
i = 0
page_content_total = []
while i < int(number_of_pages):
    page_content_final = {}
    page_nbr = read_pdf.getPage(i)

    #FIRST: EXTRACT from TEXT
    page_content = page_nbr.extractText()
    page_number = read_pdf.getPageNumber(page_nbr)

    #SECOND: ADD to VAR
    page_content_final["Content"] = page_content
    page_content_final["Page"] = page_number

    page_content_total.append(page_content_final)
    i = i + 1

print("All pages have been extracted.")

#print(page_content_total)
print("The analysis is starting...")
# Define keyords to look for in the PDF
key_words = {keyword_1, keyword_2, keyword_3}
final_output = []

# Loop the different keywords
for k in key_words:
    unique_output = {}
    total_responses = []
    # Loop the different pages
    n = 1
    for d in page_content_total:
        response = {}
        content = d["Content"]
        number = d["Page"]
        #print(content)
        if content.find(k) != -1:
            response = number + 1
        n = n + 1
        total_responses.append(response)

    # Add to variables
    unique_output['Keyword'] = k
    unique_output['Page'] =  total_responses
    final_output.append(unique_output)

print("The analysis is finished.")

for f in final_output:
    print("Analysis for " + f['Keyword'] + ":")
    print(f['Page'])
