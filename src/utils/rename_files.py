import re
from pathlib import Path

current_dir = Path(".")
script_name = Path(__file__).name

for file_path in current_dir.glob("*.py"):
    if file_path.name == script_name:
        continue

    stem = file_path.stem  # Filename without '.py'

    # Match leading digits, optional dot/spaces, and the rest of the title
    match = re.match(r"^(\d+)\.?\s*(.+)$", stem)

    if match:
        number, title = match.groups()
        # Pad number to 5 digits (e.g., '2942' -> '02942')
        padded_number = number.zfill(5)
        # Lowercase and replace spaces or hyphens with underscores
        clean_title = re.sub(r"[\s-]+", "_", title.strip().lower())
        new_stem = f"{padded_number}_{clean_title}"
    else:
        # Fallback if a file doesn't start with a number
        new_stem = re.sub(r"[\s-]+", "_", stem.strip().lower())

    new_name = f"{new_stem}{file_path.suffix}"

    if new_name == file_path.name:
        continue

    new_path = file_path.with_name(new_name)

    if new_path.exists():
        print(f"Skipped: {file_path.name} -> {new_name} (target already exists)")
    else:
        file_path.rename(new_path)
        print(f"Renamed: {file_path.name} -> {new_name}")