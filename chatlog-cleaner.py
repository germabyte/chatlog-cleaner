import tkinter as tk
from tkinter import filedialog, messagebox
import os

def clean_content(text):
    """
    Clean the .md file content by removing all '#### You:' sections 
    and preserving only '#### ChatGPT:' sections and their following content.
    
    Also updated to handle chat2markdown.py output, which may include lines like:
      > **User:** content
      **ChatGPT:** content
      **Assistant:** content
    
    The logic remains the same: user sections are skipped, ChatGPT/Assistant 
    sections are preserved.
    """
    lines = text.split('\n')
    cleaned_lines = []
    current_section = None  # 'you', 'chatgpt', or None
    
    for line in lines:
        stripped = line.strip()
        
        # --- Original logic for conversation from ChatGPT Playground format ---
        if stripped.startswith("#### You:"):
            current_section = 'you'
            continue
        elif stripped.startswith("#### ChatGPT:"):
            current_section = 'chatgpt'
            cleaned_lines.append(line)
            continue
        
        # --- NEW: Additional logic for chat2markdown.py output ---
        #   > **User:** or **User:**
        if stripped.startswith("> **User:**") or stripped.startswith("**User:**"):
            current_section = 'you'
            continue
        
        #   **ChatGPT:** or **Assistant:**
        if stripped.startswith("**ChatGPT:**") or stripped.startswith("**Assistant:**"):
            current_section = 'chatgpt'
            cleaned_lines.append(line)
            continue
        # --- END of NEW logic ---
        
        # If currently in chatgpt section, keep lines; otherwise skip.
        if current_section == 'chatgpt':
            cleaned_lines.append(line)
        # If in 'you' section or no section, do not append lines
    
    # Remove trailing newlines
    final_text = '\n'.join(cleaned_lines).strip() + '\n'
    return final_text

class ChatCleanerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ChatGPT Cleaner")
        self.file_paths = []
        self.cleaned_contents = {}
        
        # Frame for buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)
        
        self.select_button = tk.Button(button_frame, text="Select .md Files", command=self.select_files)
        self.select_button.grid(row=0, column=0, padx=5)
        
        self.clean_button = tk.Button(button_frame, text="Clean Content", command=self.clean_selected_files)
        self.clean_button.grid(row=0, column=1, padx=5)
        
        self.save_button = tk.Button(button_frame, text="Save Cleaned Files", command=self.save_files, state='disabled')
        self.save_button.grid(row=0, column=2, padx=5)
        
        # Instructions
        instr_label = tk.Label(self.master, text="Preview of Cleaned Content:")
        instr_label.pack(pady=5)
        
        # Text preview area
        self.text_preview = tk.Text(self.master, wrap='word', width=100, height=30)
        self.text_preview.pack(padx=10, pady=10)
        
        # Vertical scrollbar for text preview
        scroll_y = tk.Scrollbar(self.master, command=self.text_preview.yview)
        self.text_preview.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    def select_files(self):
        file_types = [("Markdown files", "*.md")]
        paths = filedialog.askopenfilenames(title="Select .md Files", filetypes=file_types)
        if paths:
            self.file_paths = paths
            self.text_preview.delete(1.0, tk.END)
            self.cleaned_contents = {}
            self.save_button.config(state='disabled')
            
            # Show selected files (unprocessed) in preview for clarity
            preview_header = "Selected files:\n" + "\n".join(self.file_paths) + "\n\n"
            self.text_preview.insert(tk.END, preview_header)

    def clean_selected_files(self):
        if not self.file_paths:
            messagebox.showwarning("No Files Selected", "Please select at least one .md file first.")
            return
        self.cleaned_contents = {}
        self.text_preview.delete(1.0, tk.END)
        
        for path in self.file_paths:
            try:
                with open(path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                cleaned = clean_content(content)
                self.cleaned_contents[path] = cleaned
            except Exception as e:
                self.cleaned_contents[path] = f"Error cleaning file {path}: {str(e)}"
        
        # Display cleaned contents
        for path in self.file_paths:
            self.text_preview.insert(tk.END, f"--- Cleaned content for {os.path.basename(path)} ---\n")
            self.text_preview.insert(tk.END, self.cleaned_contents[path])
            self.text_preview.insert(tk.END, "\n\n")
        
        # Enable save button now that we have cleaned content
        self.save_button.config(state='normal')

    def save_files(self):
        if not self.cleaned_contents:
            messagebox.showwarning("Nothing to Save", "No cleaned content found. Please clean files first.")
            return
        
        out_dir = filedialog.askdirectory(title="Select Directory to Save Cleaned Files")
        if not out_dir:
            return  # User cancelled
        
        for path, content in self.cleaned_contents.items():
            base_name = os.path.basename(path)
            root, ext = os.path.splitext(base_name)
            cleaned_name = f"{root}_cleaned{ext}"
            out_path = os.path.join(out_dir, cleaned_name)
            try:
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save {cleaned_name}: {str(e)}")
        
        messagebox.showinfo("Success", "Cleaned files saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatCleanerGUI(root)
    root.mainloop()
