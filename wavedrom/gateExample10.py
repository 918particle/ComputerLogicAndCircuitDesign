import wavedrom
signals = """
{
	"assign":
		[
			["d_1",["&","A","B",["~","C"],["~","D"]]],
			["d_0",["&","A",["~","B"],"C",["~","D"]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample10.svg")