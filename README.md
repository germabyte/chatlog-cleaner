# ChatGPT Cleaner

## 1. Introduction and Purpose

### 🧩 Introduction  
**ChatGPT Cleaner** is a simple desktop application designed to clean `.md` files exported from ChatGPT conversations. It removes all user messages while preserving only the AI-generated responses.

### ❓ Purpose & Problem Statement  
When exporting conversations from ChatGPT or tools like `chat2markdown.py`, the output includes both user and assistant messages. For users who wish to keep only the assistant's responses (for documentation, publishing, or archiving), manually editing these logs can be tedious.

### 🎯 Value Proposition  
This tool streamlines that process by automatically:
- Removing user messages.
- Preserving only ChatGPT or Assistant messages.
- Providing a visual preview and save feature.
- Supporting batch processing of multiple `.md` files at once.

---

## 2. Dependencies (Required Software/Libraries)

### ✅ Required:
| Dependency | Description | Installation |
|------------|-------------|--------------|
| **Python** (version 3.x) | Required to run the program. Python is the language this script is written in. | [Download Python from the official website](https://www.python.org/downloads/) |
| **tkinter** | Used to create the graphical user interface (GUI). Included by default with most Python distributions. | No action required if using standard Python. |

> ✅ **No other third-party libraries or installations are required.**

---

## 3. Getting Started (Installation & Execution)

### 📥 Step-by-Step Instructions

1. **Download the Repository**
   - Click the green `<> Code` button on GitHub.
   - Select `Download ZIP`.
   - Extract the ZIP file to a folder of your choice.

2. **Run the Application**
   - Make sure Python is installed on your system.
   - Open your terminal or command prompt:
     - **Windows:** Press `Win + R`, type `cmd`, press Enter.
     - **macOS/Linux:** Use Spotlight/Search to open "Terminal".
   - Navigate to the extracted folder:
     ```bash
     cd path/to/extracted-folder
     ```
   - Launch the program using:
     ```bash
     python chatlog-cleaner.py
     ```

   > A window will open with buttons to select, clean, preview, and save cleaned chat logs.

---

## 4. User Guide (How to Effectively Use the Program)

### 🖱️ How to Use the GUI

1. **Click "Select .md Files"**
   - Browse and select one or more markdown files exported from ChatGPT or `chat2markdown.py`.

2. **Click "Clean Content"**
   - The program will process the selected files.
   - All user messages (`"#### You:"`, `"**User:**"`, etc.) are removed.
   - ChatGPT responses (`"#### ChatGPT:"`, `"**ChatGPT:**"`, `"**Assistant:**"`) are retained.

3. **Preview Cleaned Output**
   - The main text box will show the cleaned version of each file.

4. **Click "Save Cleaned Files"**
   - Choose a folder to save the cleaned `.md` files.
   - Cleaned versions will be named with `_cleaned` appended to the original filename.

---

## 5. Use Cases and Real-World Examples

### ✅ Use Case 1: Blog Post Preparation  
**Scenario:** A user wants to publish ChatGPT responses in a blog post without showing their original prompts.  
**Input:** Markdown file with alternating `#### You:` and `#### ChatGPT:` sections.  
**Output:** A file that includes only the `#### ChatGPT:` responses, ready for blog formatting.

---

### ✅ Use Case 2: Academic Research Documentation  
**Scenario:** A researcher uses ChatGPT for generating summaries and needs clean logs for their appendix.  
**Input:** File using `**User:**` and `**ChatGPT:**` from `chat2markdown.py`.  
**Output:** Only the assistant responses remain, making the file suitable for referencing in reports.

---

### ✅ Use Case 3: Personal Journal Archive  
**Scenario:** A user keeps a personal AI conversation journal and wants to reflect on AI insights without seeing their own inputs.  
**Input:** Exported markdown file from ChatGPT Playground.  
**Output:** A cleaned, assistant-only log stored in a personal archive.

---

## 6. Disclaimer & Important Notices

- The repository and its contents may be updated at any time without notice.  
- Such updates may render parts of this README file obsolete.  
- No commitment is made to maintain or update this README to reflect future changes.  
- The provided code is delivered "as-is," and no guarantees—explicit or implied—are made regarding functionality, reliability, compatibility, or correctness.
