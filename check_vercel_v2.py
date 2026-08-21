import urllib.request, re
try:
    req = urllib.request.Request('https://www.silveryes.com/groundingbedding.html', headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as r:
        text = r.read().decode('utf-8')
    print('Vercel size:', len(text))
    print('Prev arrows:', text.count('gb-carousel-prev'))
    print('Next arrows:', text.count('gb-carousel-next'))
    print('flex-direction: column:', text.count('flex-direction: column'))
    print('window.goGB exposed:', text.count('window.goGB = goGB'))
    print('DEPLOYED')
except Exception as e:
    print('NOT DEPLOYED YET:', e)