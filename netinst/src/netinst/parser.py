import json
from pathlib import Path

fixtures_folder = Path(__file__).resolve().parents[2] / "tests" / "fixtures"

file_paths = {f.stem: f for f in fixtures_folder.glob("*.json") if f.is_file()}

def iter_nodes(node):
  yield node
  for child in node.get("children", []):
    yield from iter_nodes(child)


def find_by_class(root, cls):
  return [node for node in iter_nodes(root) if node.get("class") == cls]


def map_nodes(nodes, fn):
  return [fn(node) for node in nodes]


if __name__ == "__main__":
  user_choose = input(f"Choose a file from the following options (type the number f.e. 1): {list(file_paths.keys())}:")
  file_choose = list(file_paths.keys())[int(user_choose or 1) - 1]

  data = json.loads(file_paths[file_choose].read_text())

  networks = find_by_class(data, "network")
  storage = find_by_class(data, "storage")
  system = find_by_class(data, "system")

  macs = map_nodes(networks, lambda n: (n.get("logicalname"), n.get("serial")))

  print(f"{system}")