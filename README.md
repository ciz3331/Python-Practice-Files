# Python Practice Files

*Written in 2024 while working through the book.*

This repository contains small Python programs I wrote while reading the book:
*"Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming."*
They're simple, self-contained exercises — nothing here requires special software beyond
what's listed below.

You don't need to know how to program to look through these files or run them. This guide
walks through everything step by step, written for someone with no coding background.

A heads-up if you try running these: most of these programs don't ask you to type anything
— they just print output straight to the screen when run, so it may not be obvious what a
program is actually demonstrating just from watching it run. To help with that, each `.py`
file has comments near the top (either the original exercise instructions, or a short
explanation I wrote of what the code does) — open the file in Notepad first to get that
context before running it.

---

## What You'll Need

Just **one thing**: **Python** itself.

---

## Step 1: Install Python

1. Go to the official Python download page:
   [python.org/downloads](https://www.python.org/downloads/)
2. Download the **Windows installer** for the latest Python version.
3. Run the downloaded installer.
4. On the very first screen of the installer, look near the bottom for a
   checkbox labeled **"Add python.exe to PATH"** (or similar). **Check
   this box** — it saves you from doing Step 2 manually.
5. Click **Install Now** and let the installer finish.

---

## Step 2: Confirm Python Is Set Up Correctly

1. Open the **Command Prompt** (press the Windows key, type `cmd`, and hit
   Enter).
2. Type the following and press Enter:
   ```
   python --version
   ```
3. If it prints a version number (e.g. `Python 3.13.2`), you're all set —
   skip to Step 3.
4. If instead you see an error like `'python' is not recognized...`, the
   PATH checkbox wasn't checked during install. Here's how to add it
   manually:

   4.a Press the Windows key, type **env**, and open
      **"Edit the system environment variables."**
   4.b Click the **"Environment Variables..."** button.
   4.c Under **"System variables,"** find and select the variable named
      **Path**, then click **"Edit..."**
   4.d Click **"New"** and add the path to your Python install folder. It
      will look something like:
      ```
      C:\Users\YourName\AppData\Local\Programs\Python\Python313\
      ```
      Then click **"New"** again and also add the `Scripts` folder inside
      it:
      ```
      C:\Users\YourName\AppData\Local\Programs\Python\Python313\Scripts\
      ```
   4.e Click **OK** on all open windows to save.
   4.f Close and reopen Command Prompt, then re-run `python --version` to
      confirm it works now.

---

## Step 3: Viewing the Code

Every file in this repository ending in `.py` is a plain text file — you
can open and read it with **Notepad** (or any basic text editor):

1. Right-click the `.py` file you want to view.
2. Choose **"Open with"** → **Notepad**.

You'll be able to read the code and any comments explaining what it does,
even without programming knowledge.

---

## Step 4: Running a Program

Unlike some languages, Python doesn't need a separate "build/compile" step
— you can run a `.py` file directly.

1. Download or clone this repository to your computer.
2. If you used the green **"Code"** button on GitHub and chose
   **"Download ZIP,"** the repository will download as a single
   compressed `.zip` file. You'll need to **extract/unzip it first**
   before you can use it — right-click the downloaded `.zip` file and
   choose **"Extract All..."**, then pick a location to save the
   extracted folder. Command Prompt can't run files that are still
   inside a `.zip`.
3. Open **Command Prompt**.
4. Most exercise files live together in one folder. There's also another
   2 folders inside containing extra exercises from later chapters of the
   book — it works the same way, you'll just `cd` (change directory) into
   that folder separately when you want to run something from it. For
   example:
   ```
   cd C:\Users\YourName\Downloads\python-practice-files
   ```
5. Only run the `.py` files that have a number in their name (like
   `1_program.py`) — those are the actual exercises. Some folders also
   contain `.py` files without a number (e.g. plain module/helper files)
   — these aren't meant to be run directly; they're imported and used by
   the numbered exercise files.
6. The chapter 9-10 folder names the exercise files differently (e.g.
   `module_1.py` instead of a leading number like `1_program.py`) — these
   are still the files meant to be run. This naming is intentional, since
   Python module names can't start with a digit if they're meant to be
   imported by another file.
7. You may also notice some `.json` and `.txt` files sitting alongside
   the `.py` files. These aren't code — they're data files some exercises
   read from or write to (for example, saving a list of names or loading
   sample data). You don't need to open or edit these yourself; the
   corresponding `.py` file handles them automatically when run.
8. Run whichever exercise you'd like by typing `python` followed by the
   exact file name:
   ```
   python 1_program.py
   ```
9. You should see the program's output printed directly in the Command
   Prompt window.

---

## Troubleshooting

- **`'python' is not recognized as an internal or external command`**
  Python isn't set up on your system's PATH yet. Revisit Step 2.

- **`python: can't open file '...': [Errno 2] No such file or directory`**
  Make sure you're in the correct folder (Step 4.3) and that you typed
  the file name exactly as it appears, including the number and
  underscores.

---

Thanks for taking a look at my practice work!
