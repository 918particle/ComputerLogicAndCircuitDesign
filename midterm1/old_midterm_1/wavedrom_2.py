import wavedrom
signals = """
{signal: [
  {name: "clk", wave: "p..............."},
  {name: "D_2", wave: "l...h...l...h..."},
  {name: "D_3", wave: "l.......h......."},
  {name: "X",   wave: "l...h.......l..."}
]}"""
svg = wavedrom.render(signals)
svg.saveas("timing_2.svg")