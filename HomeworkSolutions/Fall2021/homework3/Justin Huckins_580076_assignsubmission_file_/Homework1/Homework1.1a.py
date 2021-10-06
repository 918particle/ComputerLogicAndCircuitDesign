import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			[ "Data/And",
			{ "name": "D0", "wave": "l.h.....l....h.....l"},
			{ "name": "D1", "wave": "l..h.l...h.l..h..l.."},
			{ "name": "D2", "wave": "l.h...l...h.....l..."},
			{ "name": "D3", "wave": "l.h........l........"},
			{ "name": "Output", "wave": "lhl................"}]
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("Homework1.1a.svg")