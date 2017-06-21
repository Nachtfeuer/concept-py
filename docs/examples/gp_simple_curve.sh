#!/bin/bash
cat << EOF_MAIN > simple_curve.gp
set title "Simple curve"
set grid
set xlabel "steps"
set ylabel "duration (seconds)"
set xtics "1"
set ytics "0.5"
set style line 1 lc rgb "#00ff00" lw 2
plot "-" with filledcurves x1 ls 1 fs transparent solid 0.4 border notitle

1.0 2.5
2.0 5.5
3.0 1.5
4.0 9.5
EOF
EOF_MAIN

gnuplot -p -e "load 'simple_curve.gp'"
rm simple_curve.gp