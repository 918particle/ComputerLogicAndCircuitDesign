import wavedrom
signals = """
{ assign:[
  ["out",
    ["~&",
      ["~&", "a", "b"],
      ["~&", "b", "a"]
    ]
  ]
]}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample6.svg")