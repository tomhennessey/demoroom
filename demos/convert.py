import glob
import pdftotext

files = glob.glob("./*.pdf")

for f in files:
    pdf = open(f, "rb")
    pdfText = pdftotext.PDF(pdf)
    out = open(f.replace(".pdf", ".txt"), "w")
    out.write("\n\n".join(pdfText))
    out.close()
    


