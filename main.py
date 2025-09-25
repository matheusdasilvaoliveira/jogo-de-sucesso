import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "games.json"

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "fronkongames/steam-games-dataset",
  file_path
)

print("First 5 records:", df.head())