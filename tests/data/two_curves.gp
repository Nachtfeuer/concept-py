
# displaying a plot title
set title "test plot"
# enables displaying a grid
set grid
# plotting values
plot\
    "-" with lines ls 1 title "some data",\
    "-" with lines ls 2 title "some other data"
1 1
2 0
3 1
EOF
1 0
2 1
3 0
EOF
