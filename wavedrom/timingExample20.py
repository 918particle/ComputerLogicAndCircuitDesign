import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CE_out", "wave": "l...h.......l..." },
			{ "name": "CLK", "wave": "l...p.......l..." },
			{ "name": "JC_out", "wave": "l...h.......l..." },
			{ "name": "A", "wave": "l...hl.........." },
			{ "name": "B", "wave": "l........hl....." },
			{ "name": "C", "wave": "l..............." },
			{ "name": "D", "wave": "l..............." },
			{},
			{ "name": "OUT", "wave": "l........hl....." }
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
svg.saveas("timingExample20.svg")
