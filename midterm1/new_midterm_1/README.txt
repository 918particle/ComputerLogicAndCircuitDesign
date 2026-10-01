MIDTERM 1 -- WaveDROM / IDEAL TIMING PACKAGE

1. Install the Python WaveDROM package if needed:

   python3 -m pip install wavedrom --break-system-packages

2. Render the figures:

   python3 render_wavedrom.py

   Gate diagrams (JSON files using "assign") are rendered by WaveDROM.
   Timing diagrams (JSON files using "signal") are rendered by the same
   script as ideal digital signals with zero rise/fall time and vertical
   transitions exactly on bit boundaries.

3. Compile the exam:

   pdflatex -shell-escape midterm1.tex
   pdflatex -shell-escape midterm1.tex

The LaTeX source is two-column and will display placeholders if an SVG has
not yet been rendered.
