import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			[ "Data", { "name": "D0", "wave": "l...h.......l..."},
			{ "name": "D1", "wave": "l.....h...l....."},
			{ "name": "D2", "wave": "l......h.l......"},
			{ "name": "D3", "wave": "h...lhl...hlh..."}],
			{},
			{ "name": "EN", "wave": "l...h..l........"},
			{ "name": "~EN", "wave": "h...l..h........"}
		],
	"head":
		{
			"tock":0
		},
	"foot":
		{
			"tock":0
		}
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample1.svg")