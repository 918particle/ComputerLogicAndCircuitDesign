import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "out", "wave": "hl.h.l.h.l.h.l.h"}
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample8.svg")