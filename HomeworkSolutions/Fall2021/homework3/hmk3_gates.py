import wavedrom
signals = """
{
	"assign":
		[
			["~X",["~",["&","A","B","C","D"]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk3_3-2-8_gates.svg")
signals = """
{
	"assign":
		[
			["F",["&","A","B"]],
			["G",["&","D","E"]],
			["H",["|","C","F","G"]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("hmk3_3-3-14_gates.svg")