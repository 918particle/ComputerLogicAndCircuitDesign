import wavedrom
signals = """
{

	"assign":
		[
			//Assignment 3.2#8
          ["X",
			 	
					["&", "a","b","c","d"]
				
			],
          
		// Assignment 3.3#14
   	       
            ["X",
          			["&", "a","b","c","d","f"]
             		
            ],
          ["Y",
          			["|", "a","b","c","d","f"]
           ],
          
          // Assignment 3.4#18
            ["X",
             ["~&", "a","b","c","d","f"]         		
  			],

  ]
  

}
"""
svg = wavedrom.render(signals)
svg.saveas("gateExample1.svg")
