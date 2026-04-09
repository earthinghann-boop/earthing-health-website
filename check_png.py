import pdfplumber
from PIL import Image

with pdfplumber.open(r'C:\Users\18574\Desktop\Earthing_Catalog_Final.pdf') as pdf:
    print(f'Pages: {len(pdf.pages)}')
    p = pdf.pages[0]
    img = p.to_image(resolution=72).original
    print(f'Page 1 size: {img.size}')
    # Check pixel colors to see if images are there
    import numpy as np
    arr = np.array(img)
    # Check if there are non-white pixels (content)
    non_white = np.sum(arr < 240)
    print(f'Non-white pixels: {non_white}')
    if non_white > 10000:
        print('Page has visible content/images!')
    # Save preview
    thumb = img.resize((500, int(500 * img.size[1] / img.size[0])))
    thumb.save(r'C:\Users\18574\Desktop\preview_p1.png')
    print('Preview: C:\\Users\\18574\\Desktop\\preview_p1.png')
