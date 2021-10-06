import wavedrom
signalsProb8 = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p........"},
  				["Data",
                    { "name": "A", "wave": "nh.plh..l" },
                    { "name": "B", "wave": "lnl.plnl."},
                    { "name": "C", "wave": "nhl.h.pl."},
                    { "name": "D", "wave": "nh..pl..."}],
                  {},
                ["Output",
      				{ "name": "AND", "wave": "lnl......"}]
                
		]
}"""
svg = wavedrom.render(signalsProb8)
svg.saveas("circuitsHW3prob8.svg")
signalsProb14="""
{ 
     "signal" : 
         [
            	{ "name": "CLK", "wave": "p........"},
            ["Data",
                 	{ "name": "A", "wave": "p........"},
                 	{ "name": "B", "wave": "hlhlhlhlh"},
  					{ "name": "C", "wave": "h.l.h.l.h"},
  					{ "name": "D", "wave": "h...l...h"},
  					{ "name": "E", "wave": "plplplplp"}
                ],
  				{},
                ["Output",
      				{"name": "AND", "wave": "pl......p"},
                    {"name": "OR", "wave": "h......ph"}
                ]
        ]

}"""
svg2=wavedrom.render(signalsProb14)
svg2.saveas("circuitsHWprob14.svg")
signalsProb18="""
{
	"signal":
		[
			{ "name": "CLK", "wave": "p........"},
  				["Data",
                 	{ "name": "A", "wave": "hph.ph.ph" },
              		{ "name": "B", "wave": "lh.l..h.l"},
  					{ "name": "C", "wave": "p...lp..."}
                ],
          		{},
          		["Output",
  					{ "name": "NAND", "wave": "nl..nl..n"}
                ]
		]
}"""
svg3=wavedrom.render(signalsProb18)
svg3.saveas("circuitsHWprob18.svg")
