import wavedrom
signals = """
{
	"assign":
		[
			["b0",
				["|",
					"1","3","5","7","9","B","D","F"
				]
			],
			["b1",
				["|",
					"2","3","6","7","A","B","E","F"
				]
			],
			["b2",
				["|",
					"4","5","6","7","C","D","E","F"
				]
			],
			["b3",
				["|",
					"8","9","A","B","C","D","E","F"
				]
			]
		]
}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample14.svg")
