import wavedrom
signals = """
{signal: [
  {name: "clk", wave: "p..............."},
  {name: "D_0", wave: "lhlhlhlhlhlhlhlh"},
  {name: "D_1", wave: "l.h.l.h.l.h.l.h."},
  {name: "X",   wave: "lh.l.h.l.h.l.h.l"}
]}"""
svg = wavedrom.render(signals)
svg.saveas("timing_1.svg")