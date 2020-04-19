import wavedrom
signals = """
{
	"assign":
		[
			["out",
				["|",
					["&",["~","a"],["~","b"],["~","c"],"d"],
					["&",["~","a"],["~","b"],"c","d"],
					["&","a",["~","b"],["~","c"],"d"],
					["&","a",["~","b"],"c","d"]
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample6.svg")