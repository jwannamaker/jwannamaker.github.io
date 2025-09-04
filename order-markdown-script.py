import os

# Define the exact desired order
ORDERED_PATHS = [
    "_pages/hello-triangle/notes/1.md",
    "_pages/hello-triangle/notes/2.md",
    "_pages/hello-triangle/notes/3.md",
    "_pages/hello-triangle/exercises/1.md",
    "_pages/hello-triangle/exercises/2.md",
    "_pages/hello-triangle/exercises/3.md",
    "_pages/shaders/notes/1.md",
    "_pages/shaders/notes/2.md",
    "_pages/shaders/notes/3.md",
    "_pages/shaders/exercises/1.md",
    "_pages/shaders/exercises/2.md",
    "_pages/shaders/exercises/3.md",
    "_pages/textures/notes/1.md",
    "_pages/textures/notes/2.md",
    "_pages/textures/notes/3.md",
    "_pages/textures/notes/4.md",
    "_pages/textures/notes/5.md",
    "_pages/textures/notes/6.md",
    "_pages/textures/exercises/1.md",
    "_pages/textures/exercises/2.md",
    "_pages/textures/exercises/3.md",
    "_pages/textures/exercises/4.md",
    "_pages/transformations/notes/1.md",
    "_pages/transformations/notes/2.md",
    "_pages/transformations/notes/3.md",
    "_pages/transformations/exercises/1.md",
    "_pages/transformations/exercises/2.md",
    "_pages/coordinates/notes/1.md",
    "_pages/coordinates/notes/2.md",
    "_pages/coordinates/notes/3.md",
    "_pages/coordinates/notes/4.md",
    "_pages/coordinates/notes/5.md",
    "_pages/coordinates/notes/6.md",
    "_pages/coordinates/notes/7.md",
    "_pages/coordinates/notes/8.md",
    "_pages/coordinates/notes/9.md",
    "_pages/coordinates/exercises/1.md",
    "_pages/coordinates/exercises/2.md",
    "_pages/coordinates/exercises/3.md",
]

def insert_order_field(filepath, order):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines[0].strip() == "---":
        print(f"[WARN] Skipping {filepath}: missing front matter start")
        return

    try:
        # Find where front matter ends
        end_index = lines.index("---\n", 1)
    except ValueError:
        print(f"[WARN] Skipping {filepath}: missing closing front matter")
        return

    # Check if order already exists
    if any(line.strip().startswith("order:") for line in lines[1:end_index]):
        print(f"[INFO] Skipping {filepath}: already has 'order'")
        return

    # Insert order line after permalink or at the end of front matter
    for i in range(1, end_index):
        if lines[i].strip().startswith("permalink:"):
            lines.insert(i + 1, f"order: {order}\n")
            break
    else:
        lines.insert(end_index, f"order: {order}\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"[OK] Updated {filepath} with order: {order}")

if __name__ == "__main__":
    for i, rel_path in enumerate(ORDERED_PATHS, start=1):
        if os.path.isfile(rel_path):
            insert_order_field(rel_path, i)
        else:
            print(f"[ERROR] File not found: {rel_path}")
