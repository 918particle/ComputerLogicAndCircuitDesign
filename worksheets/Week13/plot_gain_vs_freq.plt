unset key
unset grid
set lmargin 12
set tmargin 2
set xrange [0:60]
set yrange [-100:20]
set xtics font "Helvetica,22" offset 0,-1
set ytics font "Helvetica,22" offset -1,0
set xlabel "Frequency [MHz]" font "Helvetica,22" offset 0,-2
set ylabel "Gain (dB)" font "Helvetica,22" offset -2,0
set terminal png
set output "FIR_gain_vs_freq.png"
plot "FIR_gain_vs_freq.dat" using ($1/1e6):2 w l lc -1 lw 2
