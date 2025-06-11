import os

def generate_directory_structure(root_dir, ignore_list=None):
    """
    Menghasilkan dan mencetak struktur direktori secara rekursif.

    Args:
        root_dir (str): Path ke direktori utama yang akan dipindai.
        ignore_list (set, optional): Set berisi nama file/folder yang ingin diabaikan. 
                                     Jika None, akan menggunakan daftar default.
    """
    if ignore_list is None:
        # Daftar default untuk file/folder yang diabaikan
        ignore_list = {'.git', '__pycache__', 'venv', '.idea', '.vscode', 'node_modules'}

    print(f"{os.path.basename(root_dir)}/")  # Cetak nama folder utama
    _walk_directory(root_dir, "", ignore_list)

def _walk_directory(current_path, prefix, ignore_list):
    """Fungsi helper rekursif untuk menjelajahi direktori."""
    try:
        # Ambil semua item, filter yang diabaikan, dan urutkan
        items = sorted([item for item in os.listdir(current_path) if item not in ignore_list])
    except FileNotFoundError:
        print(f"Error: Direktori tidak ditemukan di {current_path}")
        return

    for index, item_name in enumerate(items):
        # Tentukan konektor: '└──' untuk item terakhir, '├──' untuk yang lain
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "
        
        print(f"{prefix}{connector}{item_name}")
        
        item_path = os.path.join(current_path, item_name)
        
        # Jika item adalah direktori, panggil fungsi ini lagi (rekursif)
        if os.path.isdir(item_path):
            # Siapkan prefix baru untuk level yang lebih dalam
            new_prefix = prefix + ("    " if is_last else "│   ")
            _walk_directory(item_path, new_prefix, ignore_list)


if __name__ == "__main__":
    # Direktori target adalah direktori tempat skrip ini dijalankan
    # Ganti dengan path lain jika perlu, contoh: "/path/to/your/project"
    target_directory = os.getcwd()
    
    print("Menganalisis struktur direktori untuk:")
    print(f"-> {target_directory}\n")
    print("```") # Pembuka untuk blok kode di Markdown
    generate_directory_structure(target_directory)
    print("```") # Penutup untuk blok kode di Markdown