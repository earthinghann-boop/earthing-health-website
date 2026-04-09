import pdfplumber
with pdfplumber.open(r'C:\Users\18574\Desktop\Earthing_Product_Catalog_WeChat.pdf') as pdf:
    print(f'Pages: {len(pdf.pages)}')
    total_imgs = 0
    for i, page in enumerate(pdf.pages):
        imgs = page.images
        total_imgs += len(imgs)
        if imgs:
            print(f'  Page {i+1}: {len(imgs)} images')
    print(f'Total images in PDF: {total_imgs}')
