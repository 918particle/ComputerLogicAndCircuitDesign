import wavedrom
signals = """
{
	"assign":
		[
			["out",
				["~&",
					["~&","a","a"],
					["~&","b","b"]
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample2.svg")