import wavedrom
signals = """
{
	"signal":
		[
          // Assiegnment 3.2#8
          // gate And
			{ "name": "CLK", "wave": "p.........."},
			[ "Input", { 
              "name": "A", "wave": "h...l..h..."},
			{ "name": "B", "wave": "lh.l.hl.h.l"},
			{ "name": "C", "wave": "h.l..h...l."},
             { "name": "D", "wave": "h.....l...."}],
          ["   output",
            { "name": "X", "wave": "lhl........"}
            ]
		]
}"""
svg = wavedrom.render(signals)
svg.saveas("timingExample1.svg")


