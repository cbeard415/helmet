import os
import subprocess

source_dir = "/Users/t/Desktop/Helmet low "
target_dir = "/Users/t/Desktop/2026 website/Helmet local files/helmet"
ffmpeg_bin = os.path.expanduser("~/Library/Python/3.13/bin/static_ffmpeg")

source_files = [f for f in os.listdir(source_dir) if f.endswith('.mp4')]

for src in source_files:
    target_name = src.replace(" dusuk", "")
    t_path = os.path.join(target_dir, target_name)
    s_path = os.path.join(source_dir, src)
    
    print(f"Optimizing: {src} -> {target_name}")
    subprocess.run([ffmpeg_bin, "-i", s_path, "-c", "copy", "-movflags", "+faststart", "-y", t_path], 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Batch optimization complete.")
