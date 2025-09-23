import json
from pathlib import Path
from typing import Mapping, Any

RESULTS_PATH = Path("data/survey.ndjson")

def append_json_line(record: Mapping[str, Any]) -> None:
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RESULTS_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
