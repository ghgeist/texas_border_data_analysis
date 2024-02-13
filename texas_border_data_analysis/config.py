from pathlib import Path

#Project Directory
project_base_dir = Path(__file__).resolve().parent.parent

#Config File Directory
config_base_dir = Path(__file__).resolve().parent

#Raw Data Directory
raw_data_dir = project_base_dir / 'data' / '1_raw'