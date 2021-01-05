// create a function to build both the bubble and bar chart
function buildCharts(sample) {

  // Use `d3.json` to fetch the sample data for the plots
  d3.json("samples.json").then((data) => {
    var samples= data.samples;
    var resultsarray= samples.filter(sampleobject => sampleobject.id == sample);
    var result= resultsarray[0]

    var ids = result.otu_ids;
    var labels = result.otu_labels;
    var values = result.sample_values;


    // Build a Bubble Chart using the sample data
    var BubbleLayout = {
      title: "Bubble Chart of each sample",
      xaxis: { title: "OTU ID" },
      hovermode: "closest",
      };

      var DataBubble = [
      {
        x: ids,
        y: values,
        text: labels,
        mode: "markers",
        marker: {
          color: ids,
          size: values,
          }
      }
    ];

    Plotly.newPlot("bubble", DataBubble, BubbleLayout);


    //  Build a bar Chart
    
    // doing it in this format allows us to not have to use trace...
    // ...slightly more efficient

    var bar_data =[
      {
        y:ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
        x:values.slice(0,10).reverse(),
        text:labels.slice(0,10).reverse(),
        type:"bar",
        orientation:"h"

      }
    ];

    var barLayout = {
      title: "Top 10 OTUs Found",
      margin: { t: 30, l: 200 }
    };

    Plotly.newPlot("bar", bar_data, barLayout);
  });
}
   
// Demographic info
function buildMetadata(sample) {
  d3.json("samples.json").then((data) => {
    var metadata= data.metadata;
    var resultsarray= metadata.filter(sampleobject => sampleobject.id == sample);
    var result= resultsarray[0]
    var PANEL = d3.select("#sample-metadata");
    PANEL.html("");
    Object.entries(result).forEach(([key, value]) => {
      PANEL.append("h6").text(`${key}: ${value}`);
    });
  
  });
}

 
function init() {
// Grab the dropdown select id/element
  var selector = d3.select("#selDataset");

// Use the list of sample names(ID's) to populate the select options
  d3.json("samples.json").then((data) => {
    var sampleNames = data.names;
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

// Use the first sample from the list to build the initial charts
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
// Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();