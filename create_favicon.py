import os
try:
    from PIL import Image
except ImportError:
    import sys
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image

def make_favicon():
    # Open the logo
    img_path = 'logo-white.png'
    if not os.path.exists(img_path):
        print(f"Error: {img_path} not found.")
        return
        
    img = Image.open(img_path)
    
    # Use the brand dark background #0E0E10
    bg_color = (14, 14, 16, 255)
    
    # Create background image
    bg = Image.new('RGBA', img.size, bg_color)
    
    # Paste the original logo over the background using alpha mask
    bg.paste(img, (0, 0), img)
    
    # Save as favicon.png
    bg.save('favicon.png', 'PNG')
    print("Success: Generated favicon.png with solid brand-dark background.")

if __name__ == '__main__':
    make_favicon()
