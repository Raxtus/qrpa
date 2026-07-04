algorithms = [
    "randomcircuit",
    "qft",
    "vqe_real_amp",
    "qaoa",
    "grover",
    "hhl"
]

types = [
    "independent",
    "mapped_ibm_all",
    "mapped_ibm_line",
    "mapped_quantinuum_all",
    "mapped_quantinuum_line",
    "targeted_ibm",
    "targeted_quantinuum"
]


import re

def format_for_caption(name):
    """Replace underscores with spaces for display"""
    return name.replace('_', ' ')

def generate_latex(algorithms, types):
    blocks = []

    for algo in algorithms:
        # Format for caption only
        algo_display = format_for_caption(algo)
        
        blocks.append(f"\\section{{{algo}}}\n")  # Keep section title with underscores
        
        for t in types:
            # Format for caption only
            t_display = format_for_caption(t)
            
            # Keep original for file operations
            filename = f"figure/{algo}_{t}.png"
            label = f"fig:{algo}_{t}"  # Note: labels shouldn't have slashes
            
            block = f"""
\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=0.5\\textwidth]{{{filename}}}
    \\caption{{Results showing time gate count and equivalency of each run for {algo_display} ({t_display})}}
    \\label{{{label}}}
\\end{{figure}}
"""
            blocks.append(block)

    return "\n".join(blocks)


print(generate_latex(algorithms, types))
