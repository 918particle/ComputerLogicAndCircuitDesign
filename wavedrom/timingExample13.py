import wavedrom
signals = """
{
	"signal":
		[
			{"name": "CLK", "wave": "p...l..."},
			{"name": "EN", "wave": "h...l..."},
			{"name": "D_{in}", "wave": "hlhl...."},
			{"name": "Q_0", "wave": "lhlhl..."},
			{"name": "Q_1", "wave": "l.hlh..."},
			{"name": "Q_2", "wave": "l..hl..."},
			{"name": "Q_3", "wave": "l...h..."}
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample13.svg")