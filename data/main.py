import os

root_dir = 'Arkavidiaa_Processed'
output_file = 'data_paths.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Tulis path folder
        rel_dir = os.path.relpath(dirpath, root_dir)
        dir_display = os.path.join(root_dir, rel_dir) if rel_dir != '.' else root_dir
        print(dir_display)
        f.write(dir_display + '\n')

        # Tulis path file di dalam folder tersebut
        for filename in filenames:
            file_path = os.path.join(dir_display, filename)
            print(file_path)
            f.write(file_path + '\n')

print(f'\n✅ Semua nama file dan folder dalam "{root_dir}/" telah disimpan ke "{output_file}"')
