import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..."},
			{ "name": "A0", "wave": "lhl."},
			{ "name": "A1", "wave": "lhl."},
			{ "name": "A2", "wave": "lhl."},
			{ "name": "A3", "wave": "lhl."},
			{ "name": "B0", "wave": "l..."},
			{ "name": "B1", "wave": "l..."},
			{ "name": "B2", "wave": "l..."},
			{ "name": "B3", "wave": "lhl."},
			{},
			{ "name": "S0", "wave": "lhl.", "phase" : -0.1 },
			{ "name": "S1", "wave": "lhl.", "phase" : -0.2 },
			{ "name": "S2", "wave": "lhl.", "phase" : -0.3 },
			{ "name": "S3", "wave": "l...", "phase" : -0.4 },
			{ "name": "C_out", "wave": "lhl.", "phase" : -0.5 }
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
svg.saveas("timingExample16.svg")
