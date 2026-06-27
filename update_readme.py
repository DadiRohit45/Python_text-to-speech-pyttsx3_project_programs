import os
import re

# folders to always ignore
IGNORE = {'.git', '.github', '__pycache__', '.vscode', 'node_modules'}

# emoji map based on folder name keywords
EMOJI_MAP = {
    'calculator': '🧮',
    'game':       '🧒',
    'quiz':       '🧠',
    'voice':      '🔊',
    'chat':       '💬',
    'paint':      '🎨',
    'clock':      '🕐',
    'weather':    '🌤️',
    'todo':       '📝',
    'music':      '🎵',
}

def get_emoji(folder_name):
    name = folder_name.lower()
    for keyword, emoji in EMOJI_MAP.items():
        if keyword in name:
            return emoji
    return '📁'  # default emoji

def get_description(folder_name):
    """Reads description from child README if it exists"""
    readme_path = os.path.join(folder_name, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # description is usually the first non-empty line after the title
        for line in lines[1:]:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                return line
    return 'A Tkinter mini project'

def get_libraries(folder_name):
    """Detects libraries used by scanning the Python files"""
    libs = set()
    for file in os.listdir(folder_name):
        if file.endswith('.py'):
            with open(os.path.join(folder_name, file), 'r', encoding='utf-8') as f:
                content = f.read()
            if 'tkinter' in content:
                libs.add('`tkinter`')
            if 'simpleeval' in content:
                libs.add('`simpleeval`')
            if 'random' in content:
                libs.add('`random`')
            if 'pyttsx3' in content:
                libs.add('`pyttsx3`')
            if 'PIL' in content or 'pillow' in content.lower():
                libs.add('`Pillow`')
    return ', '.join(sorted(libs)) if libs else '`tkinter`'

def update_readme():
    # get all project folders
    folders = sorted([
        f for f in os.listdir('.')
        if os.path.isdir(f) and f not in IGNORE
    ])

    if not folders:
        print("No project folders found.")
        return

    # build the projects table
    table  = "## 🗂️ Projects\n\n"
    table += "| Project | Description | Key Libraries |\n"
    table += "|---|---|---|\n"

    for folder in folders:
        emoji       = get_emoji(folder)
        description = get_description(folder)
        libraries   = get_libraries(folder)
        display     = folder.replace('_', ' ').replace('-', ' ').title()
        table += f"| [{emoji} {display}](./{folder}/README.md) | {description} | {libraries} |\n"

    # read current README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # replace content between markers
    start   = '<!-- PROJECTS_START -->'
    end     = '<!-- PROJECTS_END -->'
    new_section = f"{start}\n{table}\n{end}"
    updated = re.sub(
        f"{start}.*?{end}",
        new_section,
        content,
        flags=re.DOTALL
    )

    # write updated README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated)

    print(f"✅ README updated with {len(folders)} projects:")
    for folder in folders:
        print(f"   - {folder}")

if __name__ == '__main__':
    update_readme()
