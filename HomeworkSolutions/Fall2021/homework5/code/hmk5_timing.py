import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p......."},
			[ "Data",
				{ "name": "A1", "wave": "h.l..h.."},
				{ "name": "A2", "wave": "lh.lh..l"},
				{ "name": "B1", "wave": "h.l...h."},
				{ "name": "B2", "wave": "lhlhlhlh"},
				{ "name": "Cin", "wave": "l...h..."}
			],
			[ "Output",
				{ "name": "Sum1", "wave": "l...hlh."},
				{ "name": "Sum2", "wave": "h.....l."},
				{ "name": "Cout", "wave": "lhl..h.."}
			]
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
svg.saveas("hmk5_6-4-13.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p...."},
			[ "Data",
				{ "name": "A0", "wave": "hlhlh"},
				{ "name": "A1", "wave": "hlhl."},
				{ "name": "B0", "wave": "l.h.."},
				{ "name": "B1", "wave": "hl..h"}
			],
			[ "Output",
				{ "name": "A=B", "wave": "lhl.."}
			]
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
svg.saveas("hmk5_6-4-14.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p...."},
			[ "Data",
				{ "name": "A0", "wave": "h.l.h"},
				{ "name": "A1", "wave": "lh.l."},
				{ "name": "A2", "wave": "lh..."},
				{ "name": "A3", "wave": "h...l"},
				{ "name": "B0", "wave": "lhlhl"},
				{ "name": "B1", "wave": "lh..l"},
				{ "name": "B2", "wave": "h.l.h"},
				{ "name": "B3", "wave": "lhl.h"}
			],
			[ "Output",
				{ "name": "A>B", "wave": "hlh.l"},
				{ "name": "A=B", "wave": "lhl.."},
				{ "name": "A<B", "wave": "l...h"}
			]
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
svg.saveas("hmk5_6-4-14.svg")
