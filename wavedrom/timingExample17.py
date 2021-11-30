import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..." },
			{ "name": "G0", "wave": "lhl." },
			{ "name": "G1", "wave": "l..." },
			{ "name": "G2", "wave": "l..." },
			{ "name": "G3", "wave": "l..." },
			{},
			{ "name": "B0", "wave": "lhl.", "phase" : -0.1 },
			{ "name": "B1", "wave": "lhl.", "phase" : -0.2 },
			{ "name": "B2", "wave": "lhl.", "phase" : -0.3 },
			{ "name": "B3", "wave": "lhl.", "phase" : -0.4 }
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
svg.saveas("timingExample17.svg")
