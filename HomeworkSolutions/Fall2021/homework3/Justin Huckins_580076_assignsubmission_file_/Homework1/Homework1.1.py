import wavedrom
signals = """
{
	"assign":
		[
			["x",

				["&", "a","b","c","d"]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("Homework1.1.svg")