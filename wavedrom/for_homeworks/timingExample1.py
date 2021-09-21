import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			[ "Data", { "name": "D0", "wave": "l...h.......l...."},
			{ "name": "D1", "wave": "l...h...lh...l..."},
			{ "name": "D2", "wave": "l...h.lh......l.."},
			{ "name": "D3", "wave": "l...h.....lh..l.."}]
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample1.svg")
