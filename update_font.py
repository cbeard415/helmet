
path = '/Users/t/Desktop/2026 website/Helmet local files/helmet/index.html'
with open(path, 'r') as f:
    content = f.read()

# Replace existing h3 class with added serif and italic
new_content = content.replace('class="text-[22px] font-light"', 'class="text-[22px] font-light serif italic"')

with open(path, 'w') as f:
    f.write(new_content)
