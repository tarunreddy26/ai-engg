# Dev Workflow Cheat Sheet — venv, pip, Git & GitHub

A reference for the tools you use every time you start or save a project. Read once, then keep this open in a tab whenever you forget a command — that's normal, everyone looks these up constantly, including experienced developers.

---

## Part 1: Python Virtual Environments (`venv`)

### What it is
A `venv` is an isolated, self-contained copy of Python just for one project. Without it, every project on your computer shares the same global Python and the same installed packages — which causes conflicts when Project A needs version 1 of a library and Project B needs version 2.

### The commands

```
python -m venv venv
```
- **Syntax, fixed:** `python -m venv` — this exact phrase tells Python "run the built-in `venv` module."
- **Your choice:** the second `venv` is just a folder name — you're naming the folder that will hold the isolated environment. Calling it `venv` is a very strong convention (almost everyone does), not a requirement. You could name it `env` or `myproject-env` and it would work identically.

```
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```
- **Syntax, fixed** (given you named the folder `venv`). This runs a script *inside* that folder which reconfigures your current terminal session.
- **What it actually does:** temporarily makes `python` and `pip` in this terminal window point to the copies inside `venv/`, instead of your computer's system-wide Python. You'll see `(venv)` appear at the start of your terminal prompt — that's your confirmation it worked.
- **Common-sense part:** this only affects the *current terminal tab*. If you open a new terminal tab/window, you must activate it again there too. This is the #1 reason people get "module not found" errors — they installed something in one activated terminal, then ran their code in a different, unactivated one.

### How to tell if it's active
Look at your prompt. Inactive:
```
tarunreddyalla@Taruns-MacBook-Pro Week-1 %
```
Active:
```
(venv) tarunreddyalla@Taruns-MacBook-Pro Week-1 %
```
That `(venv)` prefix is the whole signal. No prefix = you're using system Python, and any `pip install` will go to the wrong place.

### Deactivating
```
deactivate
```
Run this when you're done working on a project and want your terminal back to normal. You won't need this often as a beginner, but good to know it exists.

---

## Part 2: `pip` (Python's package installer)

### What it is
`pip` downloads and installs Python libraries (other people's pre-written code) so you can `import` them in your scripts.

### The commands

```
pip install <package-name>
```
- **Syntax, fixed:** `pip install`.
- **Your choice:** the package name(s) — whatever library you actually need, e.g. `requests`, `openai`, `python-dotenv`.
- You can install several at once, space-separated: `pip install requests openai python-dotenv`.

```
pip list
```
- Shows everything currently installed **in the active environment**. Use this to double check something actually installed, especially when debugging a "module not found" error.

```
pip freeze > requirements.txt
```
- **Common sense, not just syntax:** this is a *habit*, not a required command. It writes a list of everything installed (with exact versions) into a file called `requirements.txt`. You commit this file to GitHub so that anyone (including future-you on a new machine) can recreate your exact environment with one command:
```
pip install -r requirements.txt
```
- Do this near the end of a project or whenever your dependencies stabilize — it's good practice to add to your routine, not something Python forces on you.

### The mistake you hit (and how to spot it again)
If you activate your venv but still get `ModuleNotFoundError` after installing something, check whether `python` and `pip` are actually pointing to the same place:
```
which python
which pip
```
Both should show a path containing your project's `venv/` folder. If `python` shows something like `/usr/bin/python3` instead, something (often a shell alias in a config file like `.zshrc`) is overriding the normal venv behavior. The fix in that situation is to just be explicit:
```
venv/bin/python your_script.py
venv/bin/pip install package-name
```
This bypasses whatever is confusing `python`/`pip` and points directly at the venv's own copies.

---

## Part 3: `.env` and `.gitignore` — secrets and exclusions

### `.env`
A plain text file storing secret values (like API keys) as `KEY=value` pairs, one per line:
```
OPENAI_API_KEY=sk-abc123...
```
- **Syntax:** no spaces around the `=`, no quotes needed around the value.
- **Common sense:** this file is never meant to be shared or uploaded — it's the one place your secrets live, kept separate from your actual code.
- Your Python code reads it via the `python-dotenv` library:
```python
from dotenv import load_dotenv
import os

load_dotenv()                          # reads .env into the environment
key = os.getenv("OPENAI_API_KEY")      # retrieves that specific value
```

### `.gitignore`
A plain text list of files/folders you want Git to **never** track, even when you run broad commands like `git add .`
```
.env
venv/
```
- **Common sense, not syntax:** there's no fixed format beyond "one pattern per line" — you're just listing what shouldn't be tracked. Every project's `.gitignore` differs slightly based on what it generates locally (build folders, cache files, secrets, etc.).
- **Why it matters:** if `.env` isn't listed here *before* your first commit, your API key could end up permanently in your Git history — simply deleting the file later doesn't remove it from past commits.

---

## Part 4: Git — saving versions of your code

Git tracks changes to your code over time on your own machine. GitHub (Part 5) is the separate, online place you *send* those tracked changes to.

### One-time setup per project
```
git init
```
- **Syntax, fixed.** Turns your current folder into a Git repository by creating a hidden `.git` folder. Run this once per project, right at the start.

### The core three-step loop (you'll do this constantly)
```
git add .
git commit -m "short description of what changed"
git push
```

1. **`git add .`**
   - **Syntax:** `git add` is fixed; `.` is shorthand meaning "everything in this folder and subfolders that isn't ignored."
   - **What it does:** moves changed files into a "staging area" — a holding zone of what will go into your next saved snapshot. You can also add specific files: `git add main.py`.

2. **`git commit -m "..."`**
   - **Syntax:** `git commit -m` is fixed; the quoted text is a message *you* write.
   - **Common sense:** the message should describe *what changed*, in your own words, e.g. `"Add conversation history to chatbot"` — not `"update"` or `"fix"` (too vague to be useful later when you're scanning history).
   - **What it does:** permanently saves a snapshot of everything currently staged, tagged with your message and a timestamp.

3. **`git push`**
   - **Syntax, fixed** (once a remote is set up — see Part 5).
   - **What it does:** uploads your local commits to GitHub, so they exist online too, not just on your machine.

### Checking status (use this often, especially before adding)
```
git status
```
Shows what's changed, what's staged, and — importantly — confirms `.env`/`venv/` are being correctly ignored (they simply won't appear in the list at all).

### The order that matters
`add` → `commit` → `push`, always in that sequence. You can `add` and `commit` many times locally before ever pushing — pushing just syncs whatever commits you've built up.

---

## Part 5: GitHub — where your code lives online

GitHub is a website that hosts Git repositories. Git itself works entirely offline on your machine; GitHub is where you optionally back it up and make it visible/shareable.

### Connecting a local project to a GitHub repo (one-time, per project)

1. Create an empty repository on github.com (no README/gitignore/license, since your project already has files).
2. GitHub then shows you commands like:
```
git remote add origin git@github.com:yourname/your-repo.git
git branch -M main
git push -u origin main
```
- **`git remote add origin <url>`** — **syntax fixed**, except the URL, which is your choice — this tells your local Git "this specific GitHub repo is where 'origin' refers to." You only run this once per project.
- **`git branch -M main`** — renames your current branch to `main` (the modern standard name; older tutorials sometimes say `master`, which is what you saw as your default — both work, `main` is just today's convention).
- **`git push -u origin main`** — pushes your code AND remembers ("sets upstream," the `-u`) that this local branch should always sync with `origin/main` in the future. Because of this, after the first push, plain `git push` alone is enough — the `-u origin main` part was only needed once.

### After that first setup
Every future save-and-upload is just the three-step loop from Part 4:
```
git add .
git commit -m "..."
git push
```
No need to repeat the `remote add` or `-u` steps — those were one-time wiring.

---

## Quick reference — the whole flow for a normal working session

```
cd your-project-folder
source venv/bin/activate          # start of session

# ...write/edit code...

pip install something-new         # only if you added a new library

git status                        # sanity check
git add .
git commit -m "what you changed"
git push                          # send it to GitHub
```

If you forget everything else, remember this shape: **activate → work → add → commit → push.** Everything above exists to explain *why* those steps work the way they do, so the errors make sense when they happen — and they will keep happening, to every developer, forever. That's normal, not a sign you're behind.
