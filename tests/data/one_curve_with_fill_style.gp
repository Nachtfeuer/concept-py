
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
# plotting values
plot\
    "-" with filledcurves x1 ls 1 fs transparent solid 0.5 border title "some data"
1 1
2 0
3 1
EOF
