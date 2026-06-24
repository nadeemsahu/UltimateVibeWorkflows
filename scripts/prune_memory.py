import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(script_dir, "..", "..")
memory_path = os.path.join(project_root, "workflows", "MEMORY.md")

if os.path.exists(memory_path):
    with open(memory_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Prune if file is getting large (over 2000 chars for example)
    if len(content) > 2000 and "## 📜 Completed Phases" in content:
        print("MEMORY.md token bloat detected. Pruning older completed items...")
        pruned_content = content.split("## 📜 Completed Phases")[0] + "## 📜 Completed Phases\n*(Older phases compressed by prune_memory.py)*\n"
        with open(memory_path, "w", encoding="utf-8") as f:
            f.write(pruned_content)
        print("Memory successfully pruned.")
    else:
        print("MEMORY.md is within token limits.")
else:
    print("MEMORY.md not found.")
