#!/usr/bin/env python3
import os, sys

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.srt') and not file.endswith('_fixed.srt'):
            srt_path = os.path.join(root, file)
            out_path = os.path.join(root, file.replace('.srt', '_fixed.srt'))
            
            try:
                with open(srt_path, 'rb') as f:
                    text = f.read().decode('utf-8', errors='ignore')
                
                text = text.replace('\r\n', '\n').replace('\r', '\n')
                blocks = [b for b in text.split('\n\n') if b.strip()]
                subs = []
                
                for b in blocks:
                    lines = [l.strip() for l in b.split('\n') if l.strip()]
                    if len(lines) >= 3 and lines[0].isdigit() and '-->' in lines[1]:
                        start, end = lines[1].split('-->', 1)
                        subs.append([start.strip(), end.strip(), ' '.join(lines[2:])])
                
                for i in range(len(subs)-1):
                    subs[i][1] = subs[i+1][0]
                
                with open(out_path, 'w', encoding='utf-8') as f:
                    for idx, (start, end, txt) in enumerate(subs, 1):
                        f.write(f'{idx}\n{start} --> {end}\n{txt}\n\n')
                
                print(f'Fixed: {srt_path} -> {len(subs)} subtitles')
            except Exception as e:
                print(f'Error: {srt_path}: {e}')
