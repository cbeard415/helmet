import os
import subprocess
import json

directory = "/Users/t/Desktop/2026 website/Helmet local files/helmet"
ffprobe_bin = os.path.expanduser("~/Library/Python/3.13/bin/static_ffprobe")

videos = [f for f in os.listdir(directory) if f.endswith('.mp4')]
report = []

for video in videos:
    path = os.path.join(directory, video)
    size_mb = os.path.getsize(path) / (1024 * 1024)
    
    # Check if faststart is enabled by seeing if moov comes before mdat
    try:
        result = subprocess.run([ffprobe_bin, "-v", "trace", "-i", path], 
                                capture_output=True, text=True, stderr=subprocess.STDOUT)
        
        output = result.stdout
        moov_idx = output.find("type:'moov'")
        mdat_idx = output.find("type:'mdat'")
        
        is_optimized = moov_idx != -1 and mdat_idx != -1 and moov_idx < mdat_idx
        status = "Yes (Fast Start)" if is_optimized else "NO (NOT OPTIMIZED)"
        
        report.append({"name": video, "size_mb": round(size_mb, 1), "optimized": status})
    except Exception as e:
        report.append({"name": video, "size_mb": round(size_mb, 1), "optimized": "Error checking"})

report_sorted = sorted(report, key=lambda x: x['size_mb'], reverse=True)

with open(os.path.join(directory, "video_report.txt"), "w") as f:
    f.write("HELMET MEDIA - VIDEO OPTIMIZATION REPORT\n")
    f.write("="*50 + "\n\n")
    for item in report_sorted:
        f.write(f"Video: {item['name']}\n")
        f.write(f"Size : {item['size_mb']} MB\n")
        f.write(f"Web Optimized (iOS Safari Compatible): {item['optimized']}\n")
        f.write("-" * 50 + "\n")
