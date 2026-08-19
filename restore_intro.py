#!/usr/bin/env python3
path = 'earthing-fitted-sheet.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = '<!-- Product Introduction (removed per user request) -->'
new = '''<!-- Product Introduction -->
    <section class="section section-white">
        <div class="container">
            <div class="intro-grid">
                <div class="intro-image">
                    <div class="intro-carousel">
                        <img src="images/earthing-fitted/overview-1.jpg" alt="Earthing Fitted Sheet" class="intro-carousel-img active">
                        <img src="images/earthing-fitted/overview-2.jpg" alt="Earthing Fitted Sheet" class="intro-carousel-img">
                        <img src="images/earthing-fitted/overview-3.jpg" alt="Earthing Fitted Sheet" class="intro-carousel-img">
                        <img src="images/earthing-fitted/overview-4.jpg" alt="Earthing Fitted Sheet" class="intro-carousel-img">
                        <div class="intro-carousel-dots">
                            <span class="intro-dot active" onclick="goFittedIntroSlide(0)"></span>
                            <span class="intro-dot" onclick="goFittedIntroSlide(1)"></span>
                            <span class="intro-dot" onclick="goFittedIntroSlide(2)"></span>
                            <span class="intro-dot" onclick="goFittedIntroSlide(3)"></span>
                        </div>
                    </div>
                </div>
                <div class="intro-content">
                    <span class="section-label">Product Overview</span>
                    <h2>Premium Earthing Fitted Sheet Manufacturer</h2>
                    <p>EcoBridge earthing fitted sheets are engineered for a secure, comfortable mattress fit while delivering reliable grounding performance through high-quality conductive silver fibers woven into premium fabrics.</p>
                    <p>Designed for global distributors, wellness brands, retailers, and private label businesses, our grounding fitted sheets combine cutting-edge conductive textile technology with exceptional comfort \u2014 so your customers sleep better while staying grounded.</p>
                    <p>With a decade of manufacturing expertise, state-of-the-art production facilities, and rigorous quality control, EcoBridge delivers earthing products that meet the highest international standards.</p>
                    <a href="get-price.html" class="btn btn-primary" style="margin-top:10px;">Request Wholesale Quote</a>
                </div>
            </div>
        </div>
    </section>'''

n = content.count(old)
print(f'Occurrences of placeholder: {n}')
content = content.replace(old, new, 1)

# Restore the JS IIFE
old_js = '// Intro carousel removed (HTML section deleted)'
new_js = '''// Intro carousel (4 images)
        (function() {
            const slides = document.querySelectorAll('.intro-carousel-img');
            const dots = document.querySelectorAll('.intro-dot');
            let current = 0;
            let timer;

            function go(n) {
                current = (n + slides.length) % slides.length;
                slides.forEach(function(s) { s.classList.remove('active'); });
                dots.forEach(function(d) { d.classList.remove('active'); });
                slides[current].classList.add('active');
                dots[current].classList.add('active');
            }

            function start() {
                stop();
                timer = setInterval(function() { go(current + 1); }, 3500);
            }

            function stop() {
                if (timer) clearInterval(timer);
            }

            window.goFittedIntroSlide = function(n) {
                go(n);
                start();
            };

            const container = document.querySelector('.intro-carousel');
            if (container) {
                container.addEventListener('mouseenter', stop);
                container.addEventListener('mouseleave', start);
            }

            start();
        })()'''
content = content.replace(old_js, new_js, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(path, 'r', encoding='utf-8') as f:
    verify = f.read()
import re
print(f'goFittedIntroSlide refs: {len(re.findall("goFittedIntroSlide", verify))}')
print(f'intro-carousel-img tags: {len(re.findall("intro-carousel-img", verify))}')
print(f'Product Introduction section: {"Product Overview" in verify}')
print(f'File size: {len(verify)}')