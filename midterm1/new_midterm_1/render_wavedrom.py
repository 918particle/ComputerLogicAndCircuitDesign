"""
render_wavedrom.py

Render all fig_*.json files in the current directory.

* WaveDROM ``assign`` descriptions are rendered with the Python
  ``wavedrom`` package.
* Timing-diagram ``signal`` descriptions are rendered locally as ideal
  digital waveforms: zero rise/fall time and strictly vertical transitions.

Run with:
    python3 render_wavedrom.py
"""

import html
import json
from pathlib import Path


def _expand_bits(wave: str):
    """Expand simple WaveJSON 0/1/x/. states into one state per interval."""
    states = []
    previous = "0"
    for ch in wave:
        if ch == ".":
            states.append(previous)
        elif ch in "01xXzZ":
            previous = ch.lower()
            states.append(previous)
        elif ch in "pP":
            # Clock rows are handled separately.
            states.append("p")
            previous = "p"
        else:
            # Preserve interval count but show unsupported states as unknown.
            previous = "x"
            states.append("x")
    return states


def render_ideal_timing(data: dict, svg_file: Path) -> None:
    signals = data.get("signal", [])

    n_intervals = 1
    for sig in signals:
        if isinstance(sig, dict) and sig.get("wave"):
            n_intervals = max(n_intervals, len(sig["wave"]))

    label_w = 105
    bit_w = 78
    right_margin = 25
    top_margin = 58
    row_h = 46
    gap_h = 18

    rows = []
    y = top_margin
    for sig in signals:
        if not sig:
            y += gap_h
            continue
        rows.append((sig, y))
        y += row_h

    width = label_w + n_intervals * bit_w + right_margin
    height = max(y + 22, 120)
    x0 = label_w
    x1 = x0 + n_intervals * bit_w

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    out.append('<rect x="0" y="0" width="100%" height="100%" fill="white"/>')
    out.append('<g font-family="DejaVu Sans, Arial, sans-serif" fill="black">')

    head = data.get("head", {}) or {}
    title = head.get("text")
    if title:
        out.append(f'<text x="{(x0+x1)/2:.1f}" y="20" text-anchor="middle" font-size="15">{html.escape(str(title))}</text>')

    # Time grid: boundaries line up exactly with digital transitions.
    tick_y = 40
    for i in range(n_intervals + 1):
        x = x0 + i * bit_w
        out.append(f'<line x1="{x}" y1="{top_margin-15}" x2="{x}" y2="{height-18}" stroke="#c8c8c8" stroke-width="1" stroke-dasharray="2,3"/>')
        if i < n_intervals:
            out.append(f'<text x="{x + bit_w/2:.1f}" y="{tick_y}" text-anchor="middle" font-size="12" fill="#555">{i}</text>')

    for sig, cy in rows:
        name = html.escape(str(sig.get("name", "")))
        wave = sig.get("wave", "")
        out.append(f'<text x="{x0-16}" y="{cy+5}" text-anchor="end" font-size="15">{name}</text>')

        # Clock: exact rectangular waveform, one complete cycle per interval.
        if wave and wave[0] in "pP":
            high = cy - 11
            low = cy + 11
            d = [f'M {x0} {high}']
            for i in range(n_intervals):
                xa = x0 + i * bit_w
                xm = xa + bit_w/2
                xb = xa + bit_w
                if i == 0:
                    d = [f'M {xa} {high}']
                else:
                    # Vertical low-to-high edge exactly on the interval boundary.
                    d.append(f'L {xa} {high}')
                d.append(f'L {xm} {high}')
                d.append(f'L {xm} {low}')
                d.append(f'L {xb} {low}')
                if i != n_intervals - 1:
                    d.append(f'L {xb} {high}')
            out.append(f'<path d="{" ".join(d)}" fill="none" stroke="black" stroke-width="2" stroke-linejoin="miter" stroke-linecap="butt"/>')
            continue

        states = _expand_bits(wave)
        if len(states) < n_intervals:
            states.extend([states[-1] if states else "x"] * (n_intervals - len(states)))

        high = cy - 11
        low = cy + 11
        mid = cy

        # Unknown/output-to-be-drawn row: clean dotted guide, no artificial transitions.
        if all(s in ("x", "z") for s in states[:n_intervals]):
            out.append(f'<line x1="{x0}" y1="{mid}" x2="{x1}" y2="{mid}" stroke="#777" stroke-width="1.5" stroke-dasharray="5,5"/>')
            continue

        def yy(state):
            return high if state == "1" else low if state == "0" else mid

        current = states[0]
        d = [f'M {x0} {yy(current)}']
        for i in range(n_intervals):
            xa = x0 + i * bit_w
            xb = xa + bit_w
            state = states[i]
            if i > 0 and state != current:
                # Vertical transition at the bit boundary: zero rise/fall time.
                d.append(f'L {xa} {yy(state)}')
                current = state
            d.append(f'L {xb} {yy(state)}')
        out.append(f'<path d="{" ".join(d)}" fill="none" stroke="black" stroke-width="2" stroke-linejoin="miter" stroke-linecap="butt"/>')

    out.append('</g></svg>')
    svg_file.write_text("\n".join(out), encoding="utf-8")


def render_json(json_file: Path) -> None:
    svg_file = json_file.with_suffix(".svg")
    print(f"Rendering {json_file.name} -> {svg_file.name}")

    data = json.loads(json_file.read_text(encoding="utf-8"))

    if "signal" in data and "assign" not in data:
        render_ideal_timing(data, svg_file)
        return

    # Lazy import: timing diagrams can still be rendered even if wavedrom
    # is not installed in the current Python environment.
    import wavedrom

    with json_file.open("r", encoding="utf-8") as f:
        svg = wavedrom.render(f)
    svg.saveas(str(svg_file))


def main() -> None:
    files = sorted(Path(".").glob("fig_*.json"))
    if not files:
        print("No fig_*.json files found.")
        return

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
