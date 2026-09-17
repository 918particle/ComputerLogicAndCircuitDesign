"""Render all fig_*.json WaveDROM files in the current directory to SVG."""

from pathlib import Path
import wavedrom

def render_json(json_file: Path) -> None:
    svg_file = json_file.with_suffix(".svg")
    print(f"Rendering {json_file.name} -> {svg_file.name}")
    with json_file.open("r", encoding="utf-8") as f:
        svg = wavedrom.render(f)
    svg.saveas(str(svg_file))

def main() -> None:
    files = sorted(Path(".").glob("fig_*.json"))
    if not files:
        print("No fig_*.json files found.")
        return
    print(f"Found {len(files)} WaveDROM JSON files.\n")
    failures = []
    for json_file in files:
        try:
            render_json(json_file)
        except Exception as exc:
            print(f"ERROR rendering {json_file.name}: {exc}")
            failures.append(json_file.name)
    print()
    if failures:
        print(f"{len(failures)} figure(s) failed:")
        for name in failures:
            print(f"  {name}")
    else:
        print(f"Successfully rendered {len(files)} figures.")

if __name__ == "__main__":
    main()
