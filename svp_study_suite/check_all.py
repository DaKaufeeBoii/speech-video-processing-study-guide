# -*- coding: utf-8 -*-
import os, re

def check():
    print("=== CHECKING SUITE FILES ===")
    base = "svp_study_suite"
    
    # 1. Check Diagrams
    svg_dir = os.path.join(base, "diagrams")
    svgs = [f for f in os.listdir(svg_dir) if f.endswith(".svg")]
    print(f"Total SVGs in {svg_dir}: {len(svgs)} / 40")
    
    # 2. Check Study Guide
    md_file = os.path.join(base, "Speech_and_Video_Processing_Complete_Study_Guide.md")
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    print(f"Study Guide Size: {len(md_text):,} chars | File size: {os.path.getsize(md_file):,} bytes")
    q_headers_md = re.findall(r"^## (MID[12]-Q\d+)", md_text, re.MULTILINE)
    print(f"Total Question Headers in MD: {len(q_headers_md)} / 40")
    
    # 3. Check Handbook HTML
    hb_file = os.path.join(base, "speech_video_processing_handbook.html")
    with open(hb_file, "r", encoding="utf-8") as f:
        hb_text = f.read()
    print(f"Handbook HTML Size: {len(hb_text):,} chars | File size: {os.path.getsize(hb_file):,} bytes")
    q_cards_hb = re.findall(r'id="(MID[12]-Q\d+)"', hb_text)
    print(f"Total Question Sections in Handbook: {len(q_cards_hb)} / 40")
    print(f"Embedded SVGs in Handbook: {hb_text.count('<svg ')}")
    
    # 4. Check Speedrun Trainer HTML
    sr_file = os.path.join(base, "speedrun_trainer.html")
    with open(sr_file, "r", encoding="utf-8") as f:
        sr_text = f.read()
    print(f"Speedrun HTML Size: {len(sr_text):,} chars | File size: {os.path.getsize(sr_file):,} bytes")
    import json
    sr_count = 0
    for line in sr_text.splitlines():
        if line.startswith("const RAW_QUESTIONS = "):
            json_str = line[len("const RAW_QUESTIONS = "):].strip()
            if json_str.endswith(";"):
                json_str = json_str[:-1]
            data = json.loads(json_str)
            sr_count = len(data)
            break
    print(f"Total Question Cards in Speedrun Trainer JSON: {sr_count} / 40")
    
    # 5. Check CSS and JS assets
    for asset in ["style.css", "audio.js", "app.js"]:
        ap = os.path.join(base, asset)
        print(f"Asset {asset}: Exists={os.path.exists(ap)}, Size={os.path.getsize(ap):,} bytes")
        
    print("=== ALL VERIFICATION CHECKS COMPLETE ===")

if __name__ == "__main__":
    check()
