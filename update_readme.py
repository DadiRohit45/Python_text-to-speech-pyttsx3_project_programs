import os
import re

# folders to always ignore
IGNORE = {'.git', '.github', '__pycache__', '.vscode', 'node_modules', 'venv', 'env'}

# emoji map based on folder name keywords (tailored for pyttsx3/audio projects)
EMOJI_MAP = {
    'calculator': '🧮',
    'voice':      '🔊',
    'speech':     '🗣️',
    'reader':     '📖',
    'audio':      '🎧',
    'tts':        '🎙️',
    'assistant':  '🤖',
    'pdf':        '📄',
    'music':      '🎵',
    'chat':       '💬',
}

# all known modules with install info
# format: 'import_name': ('pip_name', 'description', is_builtin)
MODULE_MAP = {
    'pyttsx3':            ('pyttsx3',            'offline text-to-speech engine',        False),
    'simpleeval':         ('simpleeval',         'safe math expression evaluator',       False),
    'speech_recognition': ('SpeechRecognition',  'speech recognition library',           False),
    'playsound':          ('playsound',          'play audio files',                     False),
    'gtts':               ('gTTS',               'Google Text-to-Speech API',            False),
    'PyPDF2':             ('PyPDF2',             'PDF toolkit for reading files',        False),
    'docx':               ('python-docx',        'Word document reader/writer',          False),
    'tkinter':            ('tkinter',            'GUI library',                          True),
    'random':             ('random',             'random number generator',              True),
    'os':                 ('os',                 'operating system interface',           True),
    'datetime':           ('datetime',           'date and time library',                True),
    'math':               ('math',               'mathematical functions',               True),
    'time':               ('time',               'time access and conversions',          True),
    'json':               ('json',               'JSON parsing library',                 True),
    'threading':          ('threading',          'thread-based parallelism',             True),
    'requests':           ('requests',           'HTTP requests library',                False),
}

def get_emoji(folder_name):
    name = folder_name.lower()
    for keyword, emoji in EMOJI_MAP.items():
        if keyword in name:
            return emoji
    return '📁'

def get_description(folder_name):
    """Reads description from child README if it exists"""
    readme_path = os.path.join(folder_name, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                return line
    return 'A mini project'

def scan_imports(folder_name):
    """Scans all Python files in a folder and returns detected modules"""
    detected = set()
    for file in os.listdir(folder_name):
        if file.endswith('.py'):
            with open(os.path.join(folder_name, file), 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                # handle: import X, from X import Y
                match_import = re.match(r'^import\s+([\w]+)', line)
                match_from   = re.match(r'^from\s+([\w]+)\s+import', line)
                if match_import:
                    detected.add(match_import.group(1))
                if match_from:
                    detected.add(match_from.group(1))
    return detected

def get_libraries(folder_name):
    """Returns formatted library string for projects table"""
    detected = scan_imports(folder_name)
    libs = []
    for mod in sorted(detected):
        if mod in MODULE_MAP:
            libs.append(f'`{mod}`')
    return ', '.join(libs) if libs else '`python`'

def get_all_modules(folders):
    """Scans all project folders and returns all detected modules"""
    all_modules = set()
    for folder in folders:
        all_modules.update(scan_imports(folder))
    return all_modules

def build_projects_section(folders):
    """Builds the projects table"""
    table  = "## 🗂️ Projects\n\n"
    table += "| Project | Description | Key Libraries |\n"
    table += "|---|---|---|\n"
    for folder in folders:
        emoji       = get_emoji(folder)
        description = get_description(folder)
        libraries   = get_libraries(folder)
        display     = folder.replace('_', ' ').replace('-', ' ').title()
        table += f"| [{emoji} {display}](./{folder}/README.md) | {description} | {libraries} |\n"
    return table

def build_requirements_section(folders):
    """Builds the requirements section based on detected modules"""
    all_modules = get_all_modules(folders)

    builtin_lines  = []
    install_lines  = []
    unknown_lines  = []

    for mod in sorted(all_modules):
        if mod in MODULE_MAP:
            pip_name, description, is_builtin = MODULE_MAP[mod]
            if is_builtin:
                builtin_lines.append(f"- `{mod}` — {description} *(built into Python)*")
            else:
                install_lines.append((pip_name, mod, description))
        else:
            unknown_lines.append(mod)

    section  = "## 🛠️ Requirements\n\n"
    section += "- Python 3.6+\n"

    if builtin_lines:
        section += "\n**Built-in (no install needed):**\n"
        for line in builtin_lines:
            section += f"{line}\n"

    if install_lines:
        section += "\n**Install via pip:**\n"
        for pip_name, mod, description in install_lines:
            section += f"- [`{mod}`](https://pypi.org/project/{pip_name}/) — {description}\n"

        section += "\nInstall all at once:\n"
        section += "```bash\n"
        section += "pip install " + " ".join(p[0] for p in install_lines) + "\n"
        section += "```\n"

    if unknown_lines:
        section += "\n**Other modules detected:**\n"
        for mod in unknown_lines:
            section += f"- `{mod}`\n"

    return section

def build_structure_section(repo_name, folders):
    """Builds the repository structure tree"""
    structure  = "## 📁 Repository Structure\n\n"
    structure += "```text\n"
    structure += f"{repo_name}/\n"
    structure += "│\n"
    structure += "├── README.md                          ← You are here (parent README)\n"

    for i, folder in enumerate(folders):
        is_last   = (i == len(folders) - 1)
        connector = "└──" if is_last else "├──"
        spacer    = "    " if is_last else "│   "

        structure += f"│\n"
        structure += f"{connector} {folder}/\n"

        try:
            files = sorted(os.listdir(folder))
            files = [f for f in files if not f.startswith('.') and f != '__pycache__']
            for j, file in enumerate(files):
                is_last_file   = (j == len(files) - 1)
                file_connector = "└──" if is_last_file else "├──"
                comment = ""
                if file == 'README.md':
                    comment = f"  ← {folder.replace('_',' ').replace('-',' ').title()} documentation"
                elif file.endswith('.py'):
                    comment = f"  ← {folder.replace('_',' ').replace('-',' ').title()} source code"
                structure += f"{spacer}{file_connector} {file}{comment}\n"
        except Exception:
            pass

    structure += "```\n"
    return structure

def replace_section(content, start_marker, end_marker, new_content):
    """Replaces content between markers"""
    new_section = f"{start_marker}\n{new_content}\n{end_marker}"
    return re.sub(
        f"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        new_section,
        content,
        flags=re.DOTALL
    )

def update_readme():
    repo_name = os.path.basename(os.path.abspath('.'))

    folders = sorted([
        f for f in os.listdir('.')
        if os.path.isdir(f) and f not in IGNORE
    ])

    if not folders:
        print("No project folders found.")
        return

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # update all 3 sections
    content = replace_section(
        content,
        '<!-- PROJECTS_START -->',
        '<!-- PROJECTS_END -->',
        build_projects_section(folders)
    )

    content = replace_section(
        content,
        '<!-- REQUIREMENTS_START -->',
        '<!-- REQUIREMENTS_END -->',
        build_requirements_section(folders)
    )

    content = replace_section(
        content,
        '<!-- STRUCTURE_START -->',
        '<!-- STRUCTURE_END -->',
        build_structure_section(repo_name, folders)
    )

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

    # print summary
    all_modules = get_all_modules(folders)
    pip_installs = [MODULE_MAP[m][0] for m in all_modules if m in MODULE_MAP and not MODULE_MAP[m][2]]

    print(f"✅ Projects updated     → {len(folders)} projects")
    print(f"✅ Requirements updated → {len(pip_installs)} pip installs detected: {', '.join(pip_installs)}")
    print(f"✅ Structure updated    → {len(folders)} folders")

if __name__ == '__main__':
    update_readme()
