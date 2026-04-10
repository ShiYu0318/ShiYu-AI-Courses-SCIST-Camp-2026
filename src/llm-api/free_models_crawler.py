import requests
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "free_models.txt")

url = "https://openrouter.ai/api/v1/models"
response = requests.get(url)
data = response.json()

free_models = []

for model in data.get("data", []):
    pricing = model.get("pricing", {})
    if float(pricing.get("prompt", "0")) == 0 and float(pricing.get("completion", "0")) == 0 and float(pricing.get("request", "0")) == 0:
        free_models.append(f'{model["id"]}:free')

with open(file_path, "w", encoding="utf-8") as f:
    for m in free_models:
        f.write(f'"{m}",\n')