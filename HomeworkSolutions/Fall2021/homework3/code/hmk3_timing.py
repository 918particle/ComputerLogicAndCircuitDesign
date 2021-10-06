import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..............."},
			[ "Data",
				{ "name": "A", "wave": "h.....l...h....."},
				{ "name": "B", "wave": "l.h..l.h.l.h..l."},
				{ "name": "C", "wave": "h..l...h.....l.."},
				{ "name": "D", "wave": "h.......l......."}
			],
			[ "Output",
				{ "name": "X", "wave": "l.hl............"},
				{ "name": "~X", "wave": "h.lh............"}
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
svg.saveas("hmk3_3-2-8.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p................"},
			[ "Data",
				{ "name": "A", "wave": "hlhlhlhlhlhlhlhlh"},
				{ "name": "B", "wave": "h.l.h.l.h.l.h.l.h"},
				{ "name": "C", "wave": "h...l...h...l...h"},
				{ "name": "D", "wave": "h.......l.......h"},
				{ "name": "E", "wave": "hl..hl..hl..hl..h"}
			],
			[ "Output",
				{ "name": "F", "wave": "hl..hl..hl..hl..h"},
				{ "name": "G", "wave": "hl..hl..........h"},
				{ "name": "H", "wave": "h...l...h...l...h"}
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
svg.saveas("hmk3_3-3-14.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p............................."},
			[ "Data",
				{ "name": "A", "wave": "h....lh.......lh.............."},
				{ "name": "B", "wave": "l.h.....l............h.....l.."},
				{ "name": "C", "wave": "hl.hl.hl.hl.hl..hl.hl.hl.hl.hl"}
			],
			[ "Output",
				{ "name": "X", "wave": "h..lh.lh..............lh.lh..."}
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
svg.saveas("hmk3_3-4-18.svg")