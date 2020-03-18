import wavedrom
signals = """
{
	"assign":
		[
			["S",["^",["^","A","B"],"Cin"]],
			["Cout",["|",["&","A","B"],["&","Cin",["^","A","B"]]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample3.svg")