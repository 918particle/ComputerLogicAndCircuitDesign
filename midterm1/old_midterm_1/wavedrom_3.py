import wavedrom
signals = """
{signal: [
  {name: "clk", wave: "p..............."},
  {name: "X_1", wave: "lh.l.h.l.h.l.h.l"},
  {name: "X_2", wave: "l...h.......l..."},
  {name: "EN",  wave: l.....h...l......"},
  {name: "X_3", wave: l.....hl.hl......"},
]}"""
svg = wavedrom.render(signals)
svg.saveas("timing_3.svg")