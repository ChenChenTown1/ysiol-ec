#!/usr/bin/env python3
import os, subprocess, glob

def embed_all():
    mp4_files = glob.glob('**/*.mp4', recursive=True)
    srt_files = glob.glob('**/*_fixed.srt', recursive=True)
    
    if not mp4_files:
        print('No MP4 files found')
        return
    
    if not srt_files:
        print('No _fixed.srt files found')
        return
    
    print(f'Found {len(mp4_files)} MP4 files, {len(srt_files)} SRT files\n')
    
    success = 0
    for mp4 in mp4_files:
        mp4_name = os.path.basename(mp4).replace('.mp4', '').lower()
        
        matching_srt = None
        for srt in srt_files:
            srt_name = os.path.basename(srt).replace('_fixed.srt', '').lower()
            if mp4_name in srt_name or srt_name in mp4_name:
                matching_srt = srt
                break
        
        if matching_srt:
            output = mp4.replace('.mp4', '_subtitled.mp4')
            
            cmd = [
                'ffmpeg', '-i', mp4,
                '-vf', f"subtitles='{matching_srt}':force_style='Alignment=2,Fontsize=24,MarginV=40'",
                '-c:a', 'copy', '-y', output
            ]
            
            print(f'Processing: {os.path.basename(mp4)}')
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f'Success: {os.path.basename(output)}\n')
                    success += 1
                else:
                    print(f'Failed\n')
            except:
                print(f'Error\n')
    
    print(f'Completed: {success}/{len(mp4_files)}')

if __name__ == '__main__':
    embed_all()
