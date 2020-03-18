import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "A", "wave": "p.......", "period": 2},
			{ "name": "B", "wave": "h.l.h.l.h.l.h.l."},
			{ "name": "C", "wave": "h.l.....h.l...h."},
			{},
			{ "name": "X", "wave": "hlhl..hlhlhl..hl"}
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample3.svg")