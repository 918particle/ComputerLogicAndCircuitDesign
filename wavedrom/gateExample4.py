import wavedrom
signals = """
{
	"assign":
		[
			["Record",["~",["&",["~","Ready"],["~","Cam2"],["~|",["~","VCR"],["~","Cam1"],["~","Cam2"]]]]]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample4.svg")