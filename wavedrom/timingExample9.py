import wavedrom
signals = """
{
	"signal":
		[
			{"name": "A0", "wave": "lhlhlhlh"},
			{"name": "A1", "wave": "l.h.l.h."},
			{"name": "A2", "wave": "l...h..."},
			{"name": "A3", "wave": "l......."},
			{"name": "Error", "wave": "d......."},
			{"name": "Even parity bit", "wave": "lhlhlhl."}
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample9.svg")