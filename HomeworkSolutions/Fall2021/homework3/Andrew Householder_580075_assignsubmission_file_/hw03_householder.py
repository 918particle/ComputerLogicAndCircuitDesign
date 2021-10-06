import wavedrom
problem8 = """
{
	"signal":
		[
			{ "name": "CLK", "wave": "p.............."},
			[ "Data", { "name": "D0", "wave": "lh....l..h....l"},
			{ "name": "D1", "wave": "l.h..l.hl.h.l.."},
			{ "name": "D2", "wave": "lh..l..h...l..."},
			{ "name": "D3", "wave": "lh......l......"}],
                        { "name": "AND", "wave": "l.h.l......"}
		]
}"""
svg = wavedrom.render(problem8)
svg.saveas("problem8.svg")

problem14 = """
{
	"signal":
		[
			[ "Data", 
			{ "name": "D0", "wave": "p........"},
                        { "name": "D1", "wave": "hlhlhlhlh"},
			{ "name": "D2", "wave": "h.l.h.l.h"},
			{ "name": "D3", "wave": "h...l...h"},
			{ "name": "D4", "wave": "plplplplp"}],
                        { "name": "AND", "wave": "pl......p"},
                        { "name": "OR", "wave": "h......lh"}
		]
}"""
svg = wavedrom.render(problem14)
svg.saveas("problem14.svg")

problem18 = """
{
	"signal":
		[
			[ "Data", 
			{ "name": "A", "wave": "h..lh..lh..lh.."},
			{ "name": "B", "wave": "lh...l...h...l."},
			{ "name": "C", "wave": "plplplplplplplp"}],
                        { "name": "NAND", "wave": "h.nhnh....nhnh."}
		]
}"""
svg = wavedrom.render(problem18)
svg.saveas("problem18.svg")
