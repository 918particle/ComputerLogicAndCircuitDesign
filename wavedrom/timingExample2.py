import wavedrom
signals = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p......."},
			{ "name": "A", "wave": "10xx0.xx"},
			{ "name": "B", "wave": "0.xx10xx"},
			{ "name": "Cin", "wave": "0.xx10xx"},
			{},
			{ "name": "S", "wave": "d......."},
			{ "name": "Cout", "wave": "d......."}
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
svg.saveas("timingExample2.svg")