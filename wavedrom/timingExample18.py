import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "P..............." },
			{ "name": "S0", "wave": "l..............." },
			{ "name": "S1", "wave": "l.......h......." },
			{},
			{ "name": "B0", "wave": "lhlhlhlhl...h...", "phase" : -0.1 }
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
svg.saveas("timingExample18.svg")
