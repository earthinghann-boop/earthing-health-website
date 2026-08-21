import os
root = r'C:\Users\18574\Desktop\EARTHING\image'
dirs_of_interest = ['PU垫','PU垫图片','绿边台垫','台垫2530','台垫26x68','台垫4060','鼠标垫彩色','橙垫']
for d in dirs_of_interest:
    full = os.path.join(root, d)
    print('===', d, '===')
    if os.path.isdir(full):
        for f in sorted(os.listdir(full)):
            if f.lower().endswith(('.jpg','.png','.jpeg','.webp')):
                p = os.path.join(full, f)
                try:
                    sz = os.path.getsize(p)
                    print(f'  {sz:>9} {f}')
                except:
                    print('  ERR', f)
    print()