# ⚡ AI Power Tools Directory & Multi-Tab Video Explorer

A comprehensive Python application providing in-depth analysis, single-paragraph operational breakdowns, and embedded YouTube tutorial videos for **9 cutting-edge AI tools**.

---

## 🛠️ The 9 Featured AI Tools

| # | Tool Name | Category | Official URL | YouTube Tutorial ID |
|---|---|---|---|---|
| **1** | **Google NotebookLM** | Research & Knowledge Synthesis | [notebooklm.google.com](https://notebooklm.google.com/) | `uSVBfyHBiDU` |
| **2** | **Google Stitch** | AI-Native UI/UX & Frontend Prototyping | [stitch.withgoogle.com](https://stitch.withgoogle.com/) | `o6Gr7X9erF8` |
| **3** | **Google AI Studio** | Developer Playground & LLM API | [aistudio.google.com](https://aistudio.google.com/) | `AcNOi-PUTL4` |
| **4** | **Wispr Flow** | Voice Dictation & Speech-to-Text | [wisprflow.ai](https://wisprflow.ai/) | `x6XJIbRksgI` |
| **5** | **Claude AI** | Conversational AI & Reasoning | [claude.ai](https://claude.ai/) | `r2vYObllqJU` |
| **6** | **Julius AI** | Data Science & Computational Analytics | [julius.ai](https://julius.ai/) | `pzf0ZtgX0fs` |
| **7** | **Higgsfield AI** | Cinematic AI Video & World Models | [higgsfield.ai](https://higgsfield.ai/) | `3W1VhiKLNp4` |
| **8** | **Claude Skills** | Agentic Framework & Reusable Skills | [claude.com/skills](https://claude.com/skills) | `w7_yWjYyxjE` |
| **9** | **ElevenLabs** | AI Voice Synthesis & Voice Cloning | [elevenlabs.io](https://elevenlabs.io/) | `yDTbAxJ3sKI` |

---

## 🚀 How to Run the Application

The application is written in **100% pure standard library Python** with **zero external dependencies** required.

### Option 1: Modern Interactive Web Application (Recommended)
Starts the local multi-threaded HTTP server on port 5000 and automatically launches your browser:
```powershell
python app.py
```
Or use the launcher:
```powershell
python run.py
```
Or on Windows:
```cmd
start.bat
```
* **Web UI URL:** `http://127.0.0.1:5000`
* **Features:**
  * Multi-tab navigation with dedicated tabs for each tool.
  * Embedded responsive YouTube video players.
  * Live search and category filters.
  * Dark / Light mode toggle.
  * One-click clipboard copy for all descriptions.
  * Comparison matrix table.
  * Full JSON REST API at `http://127.0.0.1:5000/api/tools`.

---

### Option 2: Native Desktop GUI Application (Tkinter)
Runs a native desktop window with a tabbed container (`ttk.Notebook`), feature checklists, and direct video launcher buttons:
```powershell
python gui_app.py
```
Or via the launcher:
```powershell
python run.py --gui
```

---

### Option 3: Command Line Interface (CLI)
Interact with the tools database directly in your PowerShell terminal:
```powershell
# Interactive menu:
python cli.py

# Quick commands:
python cli.py list
python cli.py show notebooklm
python cli.py search voice
python cli.py open stitch
python cli.py video elevenlabs
```

---

## 🧪 Running Unit & Integration Tests

Run the complete 10-test test suite:
```powershell
python -m unittest test_app.py
```

---

## 📂 Project Architecture

```
c:\antigravity\aitoolpython\
├── app.py           # Multi-threaded HTTP Web server & REST API
├── gui_app.py       # Native desktop GUI application using Tkinter
├── cli.py           # Command-line interface for terminal usage
├── run.py           # Master application launcher
├── start.bat        # Windows one-click batch launcher
├── tools_data.py    # Python module containing complete tool metadata
├── tools.json       # JSON data store of all 9 tools
├── index.html       # Responsive multi-tab Web UI with YouTube embeds
├── test_app.py      # Automated unit and integration test suite
└── README.md        # Documentation and reference guide
```
