import wavedrom
signals = """
{
	"assign":
		[
			["X",
				["|",
					["&","A",["~","B"],["~","C"]],
					["&","A","B",["~","C"],["~","D"]],
					["&",["~","A"],["~","B"],["~","C"],"D"],
					["&",["~","A"],["~","B"],["~","C"],["~","D"]]
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample10.svg")