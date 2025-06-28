# 🧠 Txt to JSONL Converter for Conversation Data

Welcome! 👋 This Python script takes multiple `.txt` files containing structured conversation logs and turns them into a machine-learning-ready `.jsonl` file. It's perfect for preparing datasets for fine-tuning language models like ChatGPT! 🤖📚

---

## 📁 Project Structure

```
📂 YourProject
 ┣ 📂 Input               # Place your .txt conversation files here
 ┣ 📂 Output              # The converted JSONL file will be saved here
 ┣ 📄 script.py           # The main Python script (shared above)
 ┣ 📄 README.md           # This file
```

---

## 🧾 Input Format

Each text file in the `Input` folder should follow this pattern:

- A back-and-forth dialogue between **Chedy** and an **Unknown Speaker**
- Speaker names are clearly marked: `Chedy` or `Unknown Speaker`
- A new speaker block starts with either speaker's name
- Blank lines inside a speaker’s turn are allowed (and handled)
- The line `Transcribed by https://otter.ai` (if present) is ignored

### ✍️ Example:

```
Unknown Speaker
I'm sitting on the couch in my living room. It's about this time of day

Chedy
And she snapped at you. Is it true? Listen carefully...
```

---

## 📤 Output Format

The script creates a `.jsonl` file in this format (line-delimited JSON):

```json
{"prompt": "Unknown Speaker: I'm sitting on the couch in my living room. It's about this time of day.", "completion": "Chedy: And she snapped at you. Is it true? Listen carefully..."}
```

This format is **perfect for training ChatGPT models** using prompt-completion pairs! 🧠⚙️

---

## ⚙️ How to Use

1. ✅ **Prepare your `.txt` files**: Place them all into the `Input` folder.
2. ▶️ **Run the script**:

```bash
python script.py
```

3. 📂 Your JSONL output will be saved as:

```
Output/session_data.jsonl
```

---

## 💡 Features

✨ Handles:
- Multiple `.txt` files at once
- UTF-8 encoding
- Empty lines within blocks
- Extra whitespace
- Removal of transcription footer lines

---

## 🛠️ Requirements

This script uses **only built-in Python libraries**:
- `os`
- `json`

Just run it with Python 3.6+!

---

## ❤️ Author

Created with care for data preparation by **you** ✨  
Feel free to contribute, fork, or open issues!

---

## 🚀 Example Use Case

Want to fine-tune a model with real-world conversations?  
This tool lets you convert natural conversations into training-ready data — fast!

---

## 📬 Feedback & Contributions

Suggestions? Found a bug?  
Feel free to open an Issue or a Pull Request! 🚀

---

## 🧪 Coming Soon

- CLI arguments for custom folders and filenames
- Web UI for easier usage
- Additional speaker roles & metadata support

---

📝 _Let's turn messy human conversation into structured training data — one block at a time!_
