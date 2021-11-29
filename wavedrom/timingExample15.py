import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			{ "name": "Q7", "wave": "hl.............h"},
			{ "name": "Q6", "wave": "lhl...........hl"},
			{ "name": "Q5", "wave": "l.hl.........h.."},
			{ "name": "Q4", "wave": "l..hl.......h..."},
			{ "name": "Q3", "wave": "l...hl.....h...."},
			{ "name": "Q2", "wave": "l....hl...h....."},
			{ "name": "Q1", "wave": "l.....hl.h......"},
			{ "name": "Q0", "wave": "l......h.l......"}
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
svg.saveas("timingExample15.svg")
