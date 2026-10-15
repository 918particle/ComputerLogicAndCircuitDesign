Homework 4 -- COSC330/PHYS306
Chapters 5 and 6

Contents
--------
homework4.tex
    Two-column LaTeX homework handout.

fig_5_56a.json ... fig_5_56f.json
    WaveDROM logic-diagram sources for Floyd Figure 5-56.

fig_6_75a.json ... fig_6_75d.json
    WaveDROM logic-diagram sources for Floyd Figure 6-75.

generate_static_figures.py
    Regenerates the clean SVG versions of Figures 6-69, 6-72, 6-74,
    and 6-79. These are block/waveform figures rather than gate diagrams.

render_homework4.py
    Runs generate_static_figures.py and renders every WaveDROM JSON file
    to SVG using the Python wavedrom package.

Important source note
---------------------
Chapter 5, Exercise 20 refers to Figure 5-54. Figure 5-54 was not visible
in the supplied textbook photographs, so the handout tells students to
refer to Figure 5-54 in the course text rather than inventing/reconstructing
an unsupported diagram.

Rendering
---------
The Python package used in the prior homework workflow is `wavedrom`.
On Debian/Ubuntu systems using an externally-managed Python install, the
installation command may be:

    python3 -m pip install wavedrom --break-system-packages

Then render all figures:

    python3 render_homework4.py

Compile LaTeX:

    pdflatex -shell-escape homework4.tex

The svg LaTeX package normally uses Inkscape during compilation.
