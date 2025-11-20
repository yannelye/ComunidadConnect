import json
import os

class ResourceStore:
    def __init__(self, json_path):
        self.json_path = json_path
        if not os.path.exists(self.json_path):
            raise FileNotFoundError(f"Resource file not found: {self.json_path}")
        with open(self.json_path, "r", encoding="utf-8") as f:
            self.resources = json.load(f)

    def find_by_zip(self, zip_code):
        zip_str = str(zip_code).strip()
        results = [r for r in self.resources if str(r.get("zip", "")).strip() == zip_str]
        return {"count": len(results), "resources": results}

    def query(self, zipcode=None, category=None):
        results = self.resources
        if zipcode:
            zip_str = str(zipcode).strip()
            results = [r for r in results if str(r.get("zip", "")).strip() == zip_str]
        if category:
            results = [r for r in results if r.get("category") == category]
        return results