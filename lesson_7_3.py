from pathlib import Path

new_path = Path('my_project').resolve()
path_to_new_dir = Path(new_path, 'templates')
if not path_to_new_dir.exists():
    path_to_new_dir.mkdir()
list_of_dirs = [i for i in new_path.rglob('*.html')]
for path in list_of_dirs:
    path_to_dir = Path(path_to_new_dir, path.parts[-2])
    if not path_to_dir.exists():
        path_to_dir.mkdir()
    shutil.copy2(path, path_to_dir)