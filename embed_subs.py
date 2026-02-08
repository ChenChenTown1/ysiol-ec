#!/usr/bin/env python3
import os, subprocess, glob

def embed_subtitle(video, srt):
    video_base = os.path.splitext(video)[0]
    output = f"{video_base}_subtitled.mp4"
    
    cmd = [
        'ffmpeg', '-i', video,
        '-vf', f"subtitles={srt}:force_style='Alignment=2,Fontsize=24,MarginV=40'",
        '-c:a', 'copy', '-y', output
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f'Success: {os.path.basename(video)} -> {os.path.basename(output)}')
        return True
    except subprocess.CalledProcessError as e:
        print(f'Failed: {os.path.basename(video)} - {e.stderr[:200]}')
        return False

def main():
    fixed_srts = glob.glob('**/*_fixed.srt', recursive=True)
    
    if not fixed_srts:
        print('No _fixed.srt files found')
        return
    
    print(f'Found {len(fixed_srts)} _fixed.srt files')
    
    success = 0
    for srt in fixed_srts:
        srt_name = os.path.basename(srt).replace('_fixed.srt', '')
        srt_dir = os.path.dirname(srt)
        
        videos = glob.glob(os.path.join(srt_dir, '*.mp4')) + glob.glob(os.path.join(srt_dir, '*.MP4'))
        
        matched = False
        for video in videos:
            video_name = os.path.basename(video).lower()
            srt_base = srt_name.lower()
            
            if srt_base in video_name or video_name.replace('.mp4', '') in srt_base:
                print(f'Matching: {os.path.basename(srt)} -> {os.path.basename(video)}')
                if embed_subtitle(video, srt):
                    success += 1
                matched = True
                break
        
        if not matched:
            print(f'No MP4 match for: {os.path.basename(srt)}')
    
    print(f'Completed: {success}/{len(fixed_srts)}')

if __name__ == '__main__':
    main()
