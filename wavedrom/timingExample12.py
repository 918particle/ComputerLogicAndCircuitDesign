import wavedrom
signals = """
{
	"signal":
		[
			{"name": "CLK", "wave": "p......."},
			{"name": "D_{in}", "wave": "hl......"},
			{"name": "Q_0", "wave": "lhl....."},
			{"name": "Q_1", "wave": "l.hl...."},
			{"name": "Q_2", "wave": "l..hl..."},
			{"name": "Q_3", "wave": "l...hl.."}
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample12.svg")