import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			[ "Data/And",
			{ "name": "D0", "wave": "lhlhlhlhlhlhlhlhlhl"},
			{ "name": "D1", "wave": "lh.l.h.l.h.l.h.l.h."},
			{ "name": "D2", "wave": "lh...l...h...l...h."},
			{ "name": "D3", "wave": "lh.......l.......h."},
			{ "name": "D4", "wave": "lhl..hl..hl..hl..hl"},
			{ "name": "Output", "wave": "lhl..............hl"}]
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("Homework1.2a.svg")