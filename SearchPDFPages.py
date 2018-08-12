import PyPDF2

#FIRST: OPEN and READ PDF file
##Enter the path before the name of the file (e.g. C:\Users\...\Desktop)
pdf_file = open('document.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()


#SECOND: Loop the text of the PDF and match text and page number in same dictionnary
i = 0
page_content_total = []
for p in page:
    page_content_final = {}
    page = read_pdf.getPage(i)
    
    #FIRST: EXTRACT from TEXT
    page_content = page.extractText()
    page_number = read_pdf.getPageNumber(page)
    
    #SECOND: ADD to VAR
    page_content_final["Content"] = page_content
    page_content_final["Page"] = page_number
 
    page_content_total.append(page_content_final)
    i = i + 1
    
#print(page_content_total)

# Define keyords to look for in the PDF
key_words = {"test1", "test2", "test3"}
final_output = []

# Loop the different keywords
for k in key_words:
    unique_output = {}
    total_responses = []
    # Loop the different pages
    for d in page_content_total:
        response = {}
        content = d["Content"]
        number = d["Page"]
        #print(content)
        if content.find(k) != -1:
            response = number + 1
        else:
            response = "N/A"
        total_responses.append(response)  
            
    # Add to variables       
    unique_output['Keyword'] = k
    unique_output['Page'] =  total_responses
    final_output.append(unique_output)

print(final_output)
    
