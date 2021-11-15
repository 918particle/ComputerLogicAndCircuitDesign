import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p........"},
			["Q-Data",
				{ "name": "Q0", "wave": "lh.lhlhl."},
				{ "name": "Q1", "wave": "hlh.lhlhl"},
				{ "name": "Q2", "wave": "h.lh.lhlh"},
				{ "name": "Q3", "wave": "h..lh.lhl"}
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
svg.saveas("hmk6_8-2-6.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p..................."},
			{ "name": "Serial Out", "wave": "l.........hlhl.h..l."}
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
svg.saveas("hmk6_8-2-8.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p....."},
			["Q-Data",
				["Internal",
					{ "name": "Q0", "wave": "hl.hl."},
					{ "name": "Q1", "wave": "lhl.hl"},
					{ "name": "Q2", "wave": "hlh.lh"}
				],
				["Out",
					{ "name": "Q3", "wave": "lhl.hl"}
				]
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
svg.saveas("hmk6_8-2-14.svg")
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p....."},
			["Q-Data",
				["Internal",
					{ "name": "Q0", "wave": "hl.hl."},
					{ "name": "Q1", "wave": "lhl.hl"},
					{ "name": "Q2", "wave": "hlh.lh"}
				],
				["Out",
					{ "name": "Q3", "wave": "lhl.hl"}
				]
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
svg.saveas("hmk6_8-2-21.svg")
