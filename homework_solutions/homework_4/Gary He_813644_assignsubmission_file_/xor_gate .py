import wavedrom
signals = """
{ assign:[
  ["out",
    ["~&",
        ["~&",
          ["~&", "a", "a"],
          "b"],
        ["~&",
          ["~&", "b", "b"],
          "a"]
    ]
  ]
]}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample6.svg")
