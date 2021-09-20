import wavedrom
signals = """
{
	"assign":
		[
			["x",
			 	["|",
					["&", "a","b","c","d"],
					["&", "a","b","c","d"]
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample1.svg")
