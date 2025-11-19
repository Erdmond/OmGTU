import os

def run_scripts_from_folder(folder_path):
    scripts = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    for script in scripts:
        script_path = os.path.join(folder_path, script)
        print(f"Запуск {script}...")
        with open(script_path, 'r', encoding='utf-8') as file:
            code = file.read()
        exec(code, {})
    print("Все скрипты выполнены.")


run_scripts_from_folder(r"Practicum/LAB_1/LAB_1/plots")
