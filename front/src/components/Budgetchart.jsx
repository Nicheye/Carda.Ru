
import React, { useEffect } from 'react';
import anychart from 'anychart';

const Budgetchart = (props) => {
console.log(props.chart_data)
  useEffect(() => {
	const piece =  props.chart_data
    // add the data

    var data = anychart.data.set(piece.map(chunk => [chunk.name, chunk.sum]));

    var palette = anychart.palettes.distinctColors();

    palette.items([
      { color: "#BF2761" },
      { color: "#EA3077" },
      { color: "#0F9900" },
      { color: "#AE8507" },
      { color: "#C79800" },
      { color: "#0749DB" },
      { color: "#072D82" },
      { color: "#868686" },
      { color: "#D91629" },

    ]);

    // create a pie chart instance with the passed data
    var chart = anychart
      .pie(data)
      // set the inner radius to make a donut chart
      .innerRadius("50%")
      // set the color palette
      .palette(palette);

    // set the chart title
   

    // draw the resulting chart
    chart.container("container");
    chart.draw();

    // clean up
    return () => {
      chart.dispose();
    };
  }, []);

  return (
    <div id="container" style={{ width: '100%', height: '100%' , background: 'transparent' }}></div>
  );
};

export default Budgetchart;
