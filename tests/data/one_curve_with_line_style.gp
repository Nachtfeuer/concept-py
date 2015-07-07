
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
set style line 1 lc rgb "#00ff00" lw 2
# plotting values
plot\
    "-" with lines ls 1 title "some data"
1 1
2 0
3 1
EOF
