import wavedrom
signals = """
{
	"assign":
		[
			["X",["&","A3","A2",["~","A1"],"A0"]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17a.svg")
signals = """
{
	"assign":
		[
			["X",["&","A3",["~","A2"],["~","A1"],["~","A0"]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17b.svg")
signals = """
{
	"assign":
		[
			["X",["&","A4","A3",["~","A2"],"A1","A0"]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17c.svg")
signals = """
{
	"assign":
		[
			["X",["&","A4","A3","A2",["~","A1"],["~","A0"]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17d.svg")
signals = """
{
	"assign":
		[
			["X", ["&","A5",["~","A4"],"A3",["~","A2"],"A1",["~","A0"]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17e.svg")
signals = """
{
	"assign":
		[
			["X", ["&","A5","A4","A3","A2","A1",["~","A0"]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17f.svg")
signals = """
{
	"assign":
		[
			["X", ["&",["~","A5"],["~","A4"],["~","A3"],"A2",["~","A1"],"A0"]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17g.svg")
signals = """
{
	"assign":
		[
			["X", ["&","A6","A5","A4",["~","A3"],"A2","A1",["~","A0"] ] ]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-17h.svg")
signals = """
{
	"assign":
		[
			["X",
				["|",
					["&",["~","A3"],["~","A2"],["~","A1"],"A0"],
					["&","A3","A2",["~","A1"],["~","A0"]],
					["&","A3",["~","A2"],"A1"]
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk5_6-5-19.svg")
