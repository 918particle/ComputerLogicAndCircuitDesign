import wavedrom
signals = """
{
	"signal":
		[
			{"name": "A0", "wave": "lhlhlhlh"},
			{"name": "A1", "wave": "l.h.l.h."},
			{"name": "Out", "wave": "l.hl..hl"}
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample11.svg")