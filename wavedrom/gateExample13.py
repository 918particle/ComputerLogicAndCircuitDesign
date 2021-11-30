import wavedrom
signals = """
{
	"assign":
		[
			["b3","g3"],
			["b2",["^","b3","g2"]],
			["b1",["^","b2","g1"]],
			["b0",["^","b1","g0"]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample13.svg")
