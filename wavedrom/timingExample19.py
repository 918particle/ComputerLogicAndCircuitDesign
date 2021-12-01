import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "P..............." },
			{ "name": "S_in_R", "wave": "hl.............." },
			{ "name": "S_in_L", "wave": "l.......hl......" },
			{ "name": "L_LR", "wave": "l.......h......." },
			{ "name": "R_LR", "wave": "h.......l......." }
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
svg.saveas("timingExample19.svg")
