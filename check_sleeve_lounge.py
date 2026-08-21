"""Find sleeve_shirt and loungewear actual paths"""
import os

# Check shirt directory
shirt_dir = r'C:\Users\18574\Desktop\EARTHING\image\衬衫'
if os.path.exists(shirt_dir):
    print('=== 衬衫 directory ===')
    for f in os.listdir(shirt_dir):
        print(f'  {f}')

# Check loungewear possible dirs
candidates = [
    r'C:\Users\18574\Desktop\EARTHING\image\服装',
    r'C:\Users\18574\Desktop\EARTHING\image\模特床',
]
for d in candidates:
    if os.path.exists(d):
        print(f'\n=== {d} ===')
        for f in os.listdir(d):
            print(f'  {f}')
