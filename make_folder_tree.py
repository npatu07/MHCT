import os
from graphviz import Digraph

def draw_directory_tree(root_dir):
    dot = Digraph()
    dot.node('0', root_dir, shape='folder')

    def add_nodes(parent_path, parent_id):
        files = []
        folders = []
        for idx, name in enumerate(sorted(os.listdir(parent_path))):
            child_id = f'{parent_id}-{idx + 1}'
            full_path = os.path.join(parent_path, name)
            if os.path.isdir(full_path):
                folders.append((name, child_id))
            else:
                files.append((name, child_id))
        
        # Sort files based on their extensions
        files.sort(key=lambda x: os.path.splitext(x[0])[1])
        # Add files first
        for file_name, file_child_id in files:
            dot.node(file_child_id, file_name)
            dot.edge(parent_id, file_child_id)
        # Then add folders
        for folder_name, folder_child_id in folders:
            dot.node(folder_child_id, folder_name, shape='folder')
            dot.edge(parent_id, folder_child_id)
            add_nodes(os.path.join(parent_path, folder_name), folder_child_id)

    add_nodes(root_dir, '0')
    os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'
    dot.render('directory_tree', format='png', cleanup=True)


def print_directory_structure(root_dir, indent=''):
    print(indent + os.path.basename(root_dir) + "/")
    files = []
    folders = []
    for item in sorted(os.listdir(root_dir)):
        if os.path.isdir(os.path.join(root_dir, item)):
            folders.append(item + "/")  # Add "/" to indicate it's a folder
        else:
            files.append(item)
    # Sort files based on their extensions
    files.sort(key=lambda x: os.path.splitext(x)[1])
    # Print files first
    for file_name in files:
        print(indent + "├── " + file_name)
    # Then print folders
    for folder_name in folders:
        print(indent + "├── " + folder_name)
        print_directory_structure(os.path.join(root_dir, folder_name[:-1]), indent + "│   ")

if __name__ == "__main__":
    current_directory = os.getcwd()
    draw_directory_tree(current_directory)
    print("Directory tree has been drawn.")
    print("Directory structure:")
    print_directory_structure(current_directory)
