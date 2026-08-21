var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var orig = h;

// Build Available Colors section (single image, centered, like grounding-blanket style)
var colorsSection = "\n    <section class=\"gb-category-section\" id=\"available-colors\" style=\"background: #f8f5f0;\">\n        <div class=\"container\">\n            <div class=\"gb-category-header\" style=\"text-align: center; margin-bottom: 32px;\">\n                <h2 style=\"font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; color: #1a2e3a; font-weight: 500; margin: 0 0 16px;\">Available Colors</h2>\n                <p style=\"color: #4a5a65; max-width: 640px; margin: 0 auto; line-height: 1.7;\">Choose from our classic grounding bedding palette. Each color is woven with the same silver fiber technology — soft, breathable, and ready to ground you to earth's potential.</p>\n            </div>\n            <div style=\"text-align: center; padding: 24px 0 40px;\">\n                <img src=\"images/products/groundingbedding/colors/colors.jpg\" alt=\"Available Bedding Colors\" style=\"max-width: 900px; width: 100%; height: auto; display: block; margin: 0 auto; border-radius: 12px; box-shadow: 0 12px 40px rgba(0,0,0,0.08);\">\n            </div>\n            <div style=\"text-align: center; padding: 0 0 32px;\">\n                <a href=\"get-price.html\" class=\"btn btn-primary\" style=\"background: #1a2e3a; color: #fff; padding: 12px 28px; border-radius: 100px; text-decoration: none; display: inline-block;\">Request Color Samples</a>\n            </div>\n        </div>\n    </section>\n";

// Find insertion point: end of hero </section>, before first <section class="gb-category-section" id="fitted-sheet"
var heroCloseIdx = h.indexOf('</section>', h.indexOf('collection-hero'));
console.log('hero close at:', heroCloseIdx);
var firstProdSectionIdx = h.indexOf('<section class="gb-category-section" id="fitted-sheet"');
console.log('first product section at:', firstProdSectionIdx);

if (heroCloseIdx === -1 || firstProdSectionIdx === -1) {
    console.log('ERROR: anchors not found');
    process.exit(1);
}

// Insert colorsSection between hero close and first product section
var insertPos = heroCloseIdx + '</section>'.length;
var newH = h.slice(0, insertPos) + colorsSection + h.slice(insertPos);

fs.writeFileSync('groundingbedding.html', newH, 'utf8');
console.log('\nInserted Available Colors section.');
console.log('New size:', newH.length, '(was', orig.length, ', +', newH.length - orig.length, ')');

// Verify
console.log('\n=== Verification ===');
var hasCG = newH.indexOf("font-family: 'Cormorant Garamond'") !== -1;
console.log('h2 with Cormorant Garamond:', hasCG);
var hasColors = newH.indexOf('Available Colors') !== -1;
console.log('Available Colors text:', hasColors);
var sectionCount = (newH.match(/class="gb-category-section"/g) || []).length;
console.log('Section count now:', sectionCount, '(was 5, expect 6)');
var hasImg = newH.indexOf('groundingbedding/colors/colors.jpg') !== -1;
console.log('colors.jpg ref:', hasImg);
var hasId = newH.indexOf('id="available-colors"') !== -1;
console.log('available-colors id:', hasId);