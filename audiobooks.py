print('hello world pour la enieme fois...')
import pyttsx3,PyPDF2


pdfreader = PyPDF2.PdfFileReader(open('book1.pdf', 'rb'))
speaker = pyttsx3.init()
allpages = ""
#firstpage = pdfreader.getPage(7).extractText()
#lastpage = pdfreader.getPage(256).extractText()
#allpages = firstpage + lastpage


for page_num in range(0,10):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    allpages = allpages + clean_text
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(allpages, 'story.mp3')
speaker.runAndWait()

speaker.stop()
