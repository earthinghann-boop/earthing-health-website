"""Check all emf-wearing images and current page state"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
EAR = r'C:\Users\18574\Desktop\EARTHING'

sets = {
    'shawl': (os.path.join(EAR, r'image\披风'),
              ['Se7cbd550064b47f888c7b4974d51601f3.png',
               'S06e25cff543f45c88009f3e87b2065d5T.png',
               'Sf5c8285e1ac243498f3abfe333293b79M.png',
               'S34f66e3f88124b7cbe04dbac7842bf39k.png',
               'Sef778ae1471f45d09eb20f3a12c88947M.png']),
    'fishman_cap': (os.path.join(EAR, r'image\cap\fishman cap'),
                    ['黑女帽.png', '白男帽.png',
                     'ChatGPT Image 2026年7月22日 11_35_23.png',
                     '623380f3d0390f2533c6291042bbc525.jpg']),
    'beanie': (os.path.join(EAR, r'image\cap\Beanie\beanie自己拍\原图'),
               ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']),
    'hood': (os.path.join(EAR, r'image\cap\Hood'),
             ['81EIqkla9fL._AC_SY550_.jpg',
              '71d3opedxoL._AC_SX569_.jpg',
              '81NfzfaURvL._AC_SY879_.png',
              '81I4OTpEPxL._AC_SY879_.jpg',
              '91s4ZovQPML._AC_SY879_.jpg']),
    'baseball_cap': (os.path.join(EAR, r'image\cap\鸭舌帽'),
                     ['鸭舌帽侧面.png', '鸭舌帽正面.png',
                      'ScreenShot_2026-08-21_142810_822.png']),
    'curtain': (os.path.join(EAR, r'image\curtain'),
                os.listdir(os.path.join(EAR, r'image\curtain')) if os.path.exists(os.path.join(EAR, r'image\curtain')) else []),
    'socks': (os.path.join(EAR, r'image\袜子'),
              ['H84bbddc4af784b4bb35458d6d82a91523.png',
               'H876cb02d80334a00ae58c60ad6fb1ac8B.png',
               'H7838b2b13cee469d93b110f19f4234317.png',
               'Sed54d91371084fc2bc6fff86eb6fec5fK.png']),
    'eye_mask': (os.path.join(EAR, r'image\眼罩'),
                 ['微信图片_20260722104525_11983_15.png',
                  '全部颜色.png',
                  '微信图片_20260722104348_11979_15.jpg']),
    'sleeve_shirt': (os.path.join(EAR, r'image\衬衫'),
                     ['342.jpg','346.jpg','124.jpg','122.jpg']),
    'loungewear': (os.path.join(EAR, r'image\服装\Ma\'s 宝拉3件 已修'),
                   ['2277 - 副本.jpg', '2283 - 副本.jpg']),
    'loungewear2': (os.path.join(EAR, r'image\模特床'),
                    ['DSC08124.JPG', 'DSC08100.JPG']),
    'boxer': (os.path.join(EAR, r'image\服装\1.30马特\1'),
              ['1725.jpg','1729.jpg','1743.jpg','1748.jpg']),
}

print('=== Image existence check ===\n')
for name, (dir_, files) in sets.items():
    if not isinstance(files, list):
        continue
    print(f'--- {name} (in {dir_}) ---')
    if not os.path.exists(dir_):
        print(f'  DIR NOT EXISTS: {dir_}')
        continue
    for f in files:
        p = os.path.join(dir_, f)
        if os.path.exists(p):
            try:
                img = Image.open(p)
                print(f'  OK  {f}: {img.size} {os.path.getsize(p):,}b')
            except Exception as e:
                print(f'  ERR {f}: {e}')
        else:
            print(f'  MISSING: {f}')
    print()
