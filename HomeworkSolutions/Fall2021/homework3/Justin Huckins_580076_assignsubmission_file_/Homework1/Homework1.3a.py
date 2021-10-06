import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			[ "Data/Nand",
			{ "name": "D0", "wave": "h.....l.h......l.h......l.h....."},
			{ "name": "D1", "wave": "l...h.......l........h.......l.."},
			{ "name": "D2", "wave": "lhl.lhl.lhl.lhl....lhl..lhl..lhl"},
			{ "name": "Output", "wave": "h..lh.lh..........lh..lh..lh...."}]
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("Homework1.3a.svg")