import wavedrom
signals = """
{
	"assign":
		[
			["out",
				["&",["~","b"],"d"]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample7.svg")