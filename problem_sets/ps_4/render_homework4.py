"""
render_homework4.py

1. Regenerates the custom SVG figures used for the Chapter 6 block/waveform
   diagrams.
2. Renders all WaveDROM JSON logic-gate diagrams to SVG using the Python
   `wavedrom` package.

Run from this directory with:
    python3 render_homework4.py
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def render_wavedrom_files() -> None:
    try:
        import wavedrom
    except ImportError:
        print("ERROR: Python package 'wavedrom' is not installed.")
        print("Install it with:")
        print("  python3 -m pip install wavedrom --break-system-packages")
        raise

    files = sorted(ROOT.glob("fig_*.json"))
    print(f"Found {len(files)} WaveDROM JSON files.\n")

    failures = []
    for json_file in files:
        svg_file = json_file.with_suffix(".svg")
        try:
            print(f"Rendering {json_file.name} -> {svg_file.name}")
            with json_file.open("r", encoding="utf-8") as f:
                drawing = wavedrom.render(f)
            drawing.saveas(str(svg_file))
        except Exception as exc:
            print(f"ERROR rendering {json_file.name}: {exc}")
            failures.append(json_file.name)

    if failures:
        print("\nWaveDROM failures:")
        for name in failures:
            print(f"  {name}")
        raise RuntimeError(f"{len(failures)} WaveDROM figure(s) failed")


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "generate_static_figures.py")], check=True)
    render_wavedrom_files()
    print("\nAll Homework 4 figures generated successfully.")


if __name__ == "__main__":
    main()
