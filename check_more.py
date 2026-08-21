"""Look inside subdirs"""
import os
shirt = r'C:\Users\18574\Desktop\EARTHING\image\衬衫'
lounge = r"C:\Users\18574\Desktop\EARTHING\image\服装\Ma's 宝拉3件 已修"

print('=== 衬衫 ===')
for d in os.listdir(shirt):
    full = os.path.join(shirt, d)
    if os.path.isdir(full):
        print(f'\n--- {d} ---')
        for f in os.listdir(full):
            print(f'  {f}')

print('\n\n=== Ma\'s 宝拉3件 已修 ===')
if os.path.exists(lounge):
    for f in os.listdir(lounge):
        print(f'  {f}')
else:
    print('not exists')
