with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-blanket.html', encoding='utf-8') as f:
    html = f.read()

# Show full Natural Grounding section
start = html.find('<!-- Natural Grounding -->')
end = html.find('<!-- Footer CTA -->')
print(html[start:end])
