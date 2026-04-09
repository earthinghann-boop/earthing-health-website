import io
import asyncio
from pathlib import Path
from PIL import Image as PILImage

PDF_OUT = Path(r"C:\Users\18574\Desktop\Earthing_Catalog_HD.pdf")

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

PAGE_W = 210 * mm
PAGE_H = 297 * mm
MARGIN = 10 * mm
VIEWPORT_W = 1280
VIEWPORT_H = 800
SCROLL_STEP = 700
SCALE = 2  # 2x resolution for crisp images

async def main():
    print("Launching Chromium (HD 2x)...")
    from playwright.async_api import async_playwright
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
        )
        context = await browser.new_context(
            viewport={'width': VIEWPORT_W, 'height': VIEWPORT_H},
            device_scale_factor=SCALE,
        )
        page = await context.new_page()
        page.set_default_timeout(30000)
        
        print("Loading page...")
        await page.goto("http://localhost:8080/index.html", wait_until="networkidle")
        await page.wait_for_timeout(5000)
        
        total_height = await page.evaluate("document.body.scrollHeight")
        print(f"Total: {total_height}px, scale={SCALE}x")
        
        screenshots = []
        y = 0
        while y < total_height:
            await page.evaluate(f"window.scrollTo(0, {y})")
            await page.wait_for_timeout(2500)
            img_bytes = await page.screenshot(type="png")
            img = PILImage.open(io.BytesIO(img_bytes)).convert("RGB")
            screenshots.append(img)
            print(f"  y={y}: {img.size}")
            y += SCROLL_STEP
        
        await browser.close()
    
    print("Building HD PDF...")
    c = canvas.Canvas(str(PDF_OUT), pagesize=(PAGE_W, PAGE_H))
    img_w_mm = PAGE_W - 2 * MARGIN
    
    for i, img in enumerate(screenshots):
        orig_w, orig_h = img.size
        # Scale to fit page width
        scale = img_w_mm / (orig_w / 72 * 25.4)
        rendered_h = orig_h / 72 * 25.4 * mm * scale / img_w_mm * img_w_mm
        
        if i > 0:
            c.showPage()
        
        c.drawImage(ImageReader(img), MARGIN, PAGE_H - MARGIN - rendered_h, width=img_w_mm, height=rendered_h)
        
        if (i + 1) % 3 == 0:
            print(f"  Page {i+1}/{len(screenshots)}")
    
    c.save()
    size_mb = PDF_OUT.stat().st_size / 1024 / 1024
    print(f"Done! {size_mb:.1f} MB")


if __name__ == "__main__":
    asyncio.run(main())
