#!/bin/bash
cat << 'EOF_MAIN' > simple_curve.gp
set title "Simple curve" font "Courier, 18"
set grid
set xlabel "steps" font "Courier, 12"
set ylabel "duration (seconds)" font "Courier, 12"
set xtics "1" font "Courier, 10"
set ytics "0.5" font "Courier, 10"
set style line 1 lc rgb "#00ff00" lw 2

$DATA << EOD
1.0 2.5
2.0 5.5
3.0 1.5
4.0 9.5
5.0 7.5
EOD

plot $DATA with filledcurves x1 ls 1 fs transparent solid 0.4 border notitle
EOF_MAIN

gnuplot5 -p -e "load 'simple_curve.gp'"
rm simple_curve.gp
