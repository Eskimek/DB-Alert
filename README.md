# DecibelWatcher
[![DBalert Light](https://github.com/Eskimek/AI-message-by-discord-user/blob/main/assets/logo2lightmode.png#gh-light-mode-only)](https://github.com/Eskimek/AI-message-by-discord-user)
[![DBalert Dark](https://github.com/Eskimek/AI-message-by-discord-user/blob/main/assets/logo1.png#gh-dark-mode-only)](https://github.com/Eskimek/AI-message-by-discord-user)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)](LICENSE)

A tiny noise detector that listens through your default microphone and shows a popup if the volume exceeds 80 dB.
---

## 💡 What It Does
- Constantly listens via the system microphone
- Calculates real-time audio level in decibels
- Triggers a popup if volume exceeds a defined threshold (default: 80 dB)
- Has a cooldown to avoid spam popups
---
## How to Use
1. Install dependencies:

```bash
pip install pyaudio numpy
```

2. Run the script:

```bash
python DBdetector.py
```

---

## Auto Start on Windows
To run the script automatically on system startup:

1. Create a file named `start_detector.vbs` with the following content:

```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "pythonw.exe \"C:\\Full\\Path\\To\\DBdetector.py\"", 0
```
(Or just download from my repo)
2. Press `Win + R`, type `shell:startup` and hit Enter.
3. Move the `.vbs` file (or its shortcut) into that folder.

Done - it will silently run every time your PC starts.

---

## Notes
- Requires a working microphone.
- You can adjust the `THRESHOLD_DB` and `COOLDOWN_SECONDS` in the script.

---

## 📞 Contact
discord: **eskimek**
