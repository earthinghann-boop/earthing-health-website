import os
root = r'C:\Users\18574\Desktop\EARTHING\image'
targets = [
    'Conductive-Keyboard-Foot-Mat-Sleep-Earthed-Plug-Cable-1-Full-Keyboard-Desk-Closeup-Web-1500.jpg',
    'earthing-and-grounding-mat-68-x-25-cm-5342316.webp',
    '61cObI19fpL._AC_.jpg',
    '81v9WvyxERL._AC_SX679_.jpg'
]
for target in targets:
    print(f'=== {target} ===')
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        if target in filenames:
            full = os.path.join(dirpath, target)
            sz = os.path.getsize(full)
            print(f'  {sz//1024:>6}KB  {full}')
            found.append(full)
    if not found:
        print('  NOT FOUND ANYWHERE')
    print()