import os
from pathlib import Path

project_name = "DVP"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # Create the directory if needed
    if filepath.parent != Path('.'):
        filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Check if the path seems to be a file (e.g. has a suffix)
    if filepath.suffix:
        if (not filepath.exists()) or (filepath.stat().st_size == 0):
            filepath.write_text("")  # creates or empties the file
        else:
            print(f"File is already present at: {filepath}")
    else:
        # If it's a directory path, nothing further is needed.
        pass
