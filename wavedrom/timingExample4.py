import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "Xa", "wave": "l..............."},
			{ "name": "Xb", "wave": "l......h.l......"}
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
svg.saveas("timingExample4.svg")