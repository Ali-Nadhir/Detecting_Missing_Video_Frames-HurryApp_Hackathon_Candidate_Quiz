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

if __name__ == '__main__':

print("--- 1. PDF Example ---")
frames_input = [1, 2, 3, 5, 6, 10, 11, 16]
result = find_missing_ranges(frames_input)
print(f"Input: {frames_input}\nResult: {result}\n")

print("--- 2. Edge Case: Empty List ---")
frames_input = []
result = find_missing_ranges(frames_input)
print(f"Input: {frames_input}\nResult: {result}\n")

print("--- 3. Edge Case: No Missing Frames ---")
frames_input = [1, 2, 3, 4, 5]
result = find_missing_ranges(frames_input)
print(f"Input: {frames_input}\nResult: {result}\n")

print("--- 4. Edge Case: Sequence Not Starting at 1 ---")
frames_input = [4, 5, 6, 10]
result = find_missing_ranges(frames_input)
print(f"Input: {frames_input}\nResult: {result}\n")

print("--- 5. Edge Case: Only One Frame Received ---")
frames_input = [8]
result = find_missing_ranges(frames_input)
print(f"Input: {frames_input}\nResult: {result}\n")

print("--- 6. Edge Case: All Frames Missing Except the Last ---")
frames_input = [100]
result = find_missing_ranges(frames_input)
print(f"Input: {frames_input}\nResult: {result}\n")