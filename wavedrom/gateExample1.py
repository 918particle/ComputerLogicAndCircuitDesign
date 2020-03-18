import wavedrom
signals = """
{
	"assign":
		[
			["out",
				["~&",
					["~&","a","b"],
					["~&","a","b"]
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample1.svg")