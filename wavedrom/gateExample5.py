import wavedrom
signals = """
{
	"assign":
		[
			["out",
				["~&",["~&",["~&","a",["~&","a","b"]],["~&",["~&","a","b"],"b"]],["~&",["~&","a",["~&","a","b"]],["~&",["~&","a","b"],"b"]]]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample5.svg")