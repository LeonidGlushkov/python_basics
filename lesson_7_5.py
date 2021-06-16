import pathlib

dict_of_files = {}
path_to_dir = pathlib.Path(input(r'Введите путь к папке: ')).resolve()
for root, dirs, files in os.walk(path_to_dir):
    for file in files:
        number = len(str(pathlib.Path(root, file).stat().st_size))
        dict_of_files.setdefault(10 ** number, [])
        dict_of_files[10 ** number].append(pathlib.Path(root, file).suffix)
for k, v in dict_of_files.items():
    dict_of_files[k] = (len(v), list(set(v)))
for k, v in sorted(dict_of_files.items()):
    print(f'{k}: {dict_of_files[k]}')
with open(f'{pathlib.Path.cwd().parts[-1]}_summary.json', 'w', encoding='UTF-8') as f:
    for k, v in sorted(dict_of_files.items()):
        print(f'{k}: {dict_of_files[k]}', file=f)