# 🎬 Jenny's Lectures — Video-Wise DSA Notes

**115 structured study notes**, one per video, from the [Data Structures & Algorithms playlist](https://www.youtube.com/playlist?list=PLdo5W4Nhv31bbKJzrsKfMpo_grxuLl8LU) by Jenny's Lectures.

## How These Were Made

1. **67 videos** had YouTube captions → fetched via `youtube-transcript` (Node.js)
2. **48 videos** had captions disabled → audio downloaded via `yt-dlp`, transcribed locally using `faster-whisper` (Whisper large-v3-turbo) on GPU
3. All 115 transcripts were synthesized into exam-focused Markdown notes

## Structure

See [`00_index.md`](00_index.md) for the full hierarchical index.

### Sections
| Section | Topic | Notes |
|---------|-------|-------|
| 0 | Foundations | 2 |
| 1 | Arrays | 6 |
| 2 | Linked Lists | 19 |
| 3 | Stack & Expressions | 13 |
| 4 | Queue & Deque | 8 |
| 5 | Trees (BT, BST, AVL, RBT, Splay, B-Tree, B+) | 31 |
| 6 | Graphs | 15 |
| 7 | Searching & Sorting | 14 |
| 8 | Hashing | 3 |
| 9 | Greedy (Huffman) | 2 |
| **Total** | | **115** |

## Format

Every note includes:
- 📺 YouTube link to the original video
- 📌 Executive summary
- 💻 C code with inline comments
- 📐 Step-by-step traces with tables/diagrams
- ⏱️ Time & Space complexity
- 💡 Exam-ready takeaways
