# Welcome to some examples on gnuplot

## Generating a simple curve
The main adjustments for this curve:

 * Using gnuplot 5.x
 * main title above graph
 * tixs on x-axis and y-axis (steps)
 * title on x-axis and y-axis
 * displaying a grid
 * Filled area under the curve
 * Line color (also influences fill color)
 * Plotting from a list of data (reusable: here document)
 * Fonts for titles, labels and tics
 * The **all in one** script: [here](examples/gp_simple_curve.sh)

![simple curve](images/simple-curve.png)

## Smooth csplines curve

Just putting a `smooth csplines` in front of the **with filledcurves** the
simple curve examples looks like following:

![simple csplines curve](images/smooth-csplines-curve.png)
