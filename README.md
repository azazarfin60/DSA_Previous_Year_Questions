# 📚 ECE 2103: Data Structures & Algorithms — Exam Study Repository

> **Department of Electrical & Computer Engineering, RUET**
> Semester Final Exam Preparation (2017–2024)

---

## 🗂️ Repository Structure

```
DSA_Exam/
├── questions/                  # Past exam papers (2017–2024), one file per year
├── answers/                    # Model answers for each year's paper
├── topicwise_answers/          # Answers reorganized by topic (BST, Graphs, Sorting, etc.)
├── notes/                      # Syllabus-derived deep study guides (16 topic files)
├── Jenny'sLecturesYT_Notes/    # 115 video-wise notes from Jenny's DSA YouTube playlist
├── Analysis_Report(2017-2024).md
├── Analysis_Report_OBE(2022-24).md
└── topic list.pdf              # Scanned course syllabus
```

## 📖 What's Inside

### 🔴 Exam Papers & Answers
- **`questions/`** — Digitized question papers from 2017 to 2024
- **`answers/`** — Complete model answers, year by year
- **`topicwise_answers/`** — Same answers reorganized into 20 topic files for targeted study

### 🟡 Study Notes
- **`notes/`** — 16 comprehensive topic guides synthesized from the course syllabus, covering definitions, pseudocode, C code, complexity analysis, and exam tips
- **`Jenny'sLecturesYT_Notes/`** — 115 video-wise study notes transcribed & synthesized from Jenny's Lectures DSA playlist, each with YouTube link, C code, trace examples, and Big-O analysis

### 🟢 Analysis
- **`Analysis_Report(2017-2024).md`** — Frequency analysis of all exam topics across 8 years
- **`Analysis_Report_OBE(2022-24).md`** — OBE-focused analysis for 2022–2024 papers

## 🔑 How to Use

1. **Quick review** → Start with `notes/00_index.md` or `Jenny'sLecturesYT_Notes/00_index.md`
2. **Topic-focused study** → Use `topicwise_answers/` to study all past exam questions on a single topic
3. **Full mock exam** → Pick a year from `questions/`, attempt it, then check `answers/`
4. **Predict next exam** → Read the `Analysis_Report` files to see which topics appear most frequently

## ⚙️ Pipeline (for regeneration)

The YouTube notes were generated via an automated pipeline:
1. `yt-dlp` → extract playlist metadata
2. `youtube-transcript` / `faster-whisper` (GPU) → fetch/generate transcripts
3. AI synthesis → structured Markdown notes

Pipeline artifacts (`raw_transcripts/`, `node_modules/`, etc.) are gitignored.

---

*Last updated: May 2026*
