import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', encoding='utf-8') as f:
    gb = f.read()
idx = gb.find('id="fittedCarousel"')
end = gb.find('id="flatCarousel"')
seg = gb[idx:end]
dots_idx = seg.find('gb-carousel-dots')
print('groundingbedding dots:')
print(repr(seg[dots_idx:dots_idx+400]))

print()
# pu-earthing-mat local
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    pu = f.read()
idx2 = pu.find('id="puSheetCarousel"')
end2 = pu.find('id="puDeskCarousel"')
seg2 = pu[idx2:end2]
dots_idx2 = seg2.find('gb-carousel-dots')
print('pu-earthing-mat dots:')
print(repr(seg2[dots_idx2:dots_idx2+400]))