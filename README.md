# Detecting_Missing_Video_Frames-HurryApp_Hackathon_Candidate_Quiz
Solution 

This repository contains the solution for the HurryApp Hackathon 3 Candidate Quiz
```python
def find_missing_ranges(frames: list[int]) -> dict:
    if not frames:
        return {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0
        }

    max_frame = 0
    seen_frames = set()
    for frame in frames:
        if frame > max_frame:
            max_frame = frame
        seen_frames.add(frame)

    gaps = []
    longest_gap = []
    missing_count = 0
    max_gap_len = 0
    
    current_frame = 1
    while current_frame <= max_frame:
        if current_frame not in seen_frames:
            gap_start = current_frame
            
            while current_frame <= max_frame and current_frame not in seen_frames:
                current_frame += 1
            
            gap_end = current_frame - 1
            
            current_gap = [gap_start, gap_end]
            gaps.append(current_gap)
            
            current_gap_len = gap_end - gap_start + 1
            missing_count += current_gap_len
            
            if current_gap_len > max_gap_len:
                max_gap_len = current_gap_len
                longest_gap = current_gap
        else:
            current_frame += 1
            
    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }

```
### Edge Cases Covered By My Test

1. **Empty list** – no frames provided
2. **No missing frames** – all frames are sequential and present
3. **Sequence not starting at 1** – frames start from a number higher than 1
4. **Only one frame received** – a single frame in the list
5. **All frames missing except the last** – only the last frame is present, all prior frames missing


## How to Run

The solution is a standard Python script. You can run it directly:

```bash
python solution.py
