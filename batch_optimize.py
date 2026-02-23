import os
import subprocess
import difflib

source_dir = "/Users/t/Desktop/Helmet_Low_size_videos"
target_dir = "/Users/t/Desktop/2026 website/Helmet local files/helmet"
ffmpeg_bin = os.path.expanduser("~/Library/Python/3.13/bin/static_ffmpeg")

source_files = [f for f in os.listdir(source_dir) if f.endswith('.mp4') and f != "43th 4th low.mp4"]
target_files = [f for f in os.listdir(target_dir) if f.endswith('.mp4')]

for src in source_files:
    # Find closest match in target dir (excluding " low")
    base_src = src.replace(" low", "")
    closest_matches = difflib.get_close_matches(base_src, target_files, n=1, cutoff=0.6)
    
    if closest_matches:
        target_name = closest_matches[0]
        t_path = os.path.join(target_dir, target_name)
        s_path = os.path.join(source_dir, src)
        
        print(f"Optimizing: {src} -> {target_name}")
        # To overwrite safely and quickly without re-encoding:
        subprocess.run([ffmpeg_bin, "-i", s_path, "-c", "copy", "-movflags", "+faststart", "-y", t_path], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"Could not find match for {src}")

print("Batch optimization complete.")
