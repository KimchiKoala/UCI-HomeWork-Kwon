// from data.js
var tableData = data;

// select tbody 
tbody = d3.select("tbody")


// loop through table
function displayData(ufo){ 
    tbody.text("")
    ufo.forEach(function(ufo_sighting){
    new_tr = tbody.append("tr")
    Object.entries(ufo_sighting).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)	
    })
})}

// display using displayData function
displayData(tableData)


// Select the submit button
var submit = d3.select("#submit");

// print the filter button test to check if it works...
submit.on("click", function() {
    console.log("filter button test")

    
  // Prevent the page from refreshing...
  d3.event.preventDefault();

  // Select the input id 
  var dateInput = d3.select("#datetime");
  var cityInput = d3.select("#city");
  var stateInput = d3.select("#state");
  var countryInput = d3.select("#country");
  var shapeInput = d3.select("#shape");

  // Get the value of the input id
  console.log(dateInput.property("value"));
  console.log(cityInput.property("value"));
  console.log(stateInput.property("value"));
  console.log(countryInput.property("value"));
  console.log(shapeInput.property("value"));

  //this part was difficult.. but esssentially you had to create a variable that would include...
//   more than just the initial value, so that even if some stuff was written it would still work..

 var filtered = tableData.filter(ufo_sighting =>{
  return (ufo_sighting.datetime===dateInput.property("value") || !dateInput.property("value") ) && 
            (ufo_sighting.city===cityInput.property("value") || !cityInput.property("value")) &&
            (ufo_sighting.state===stateInput.property("value") || !stateInput.property("value")) &&
            (ufo_sighting.country===countryInput.property("value") || !countryInput.property("value")) &&
            (ufo_sighting.shape===shapeInput.property("value") || !shapeInput.property("value"))
 })

 //run the filtered entries through the displayData function to update the table
 displayData(filtered);


});

// create a variable that selects all of the form-control classes, aka the table entries
var filterInputs = d3.selectAll('.form-control');




// Clears input fields and input object, using a clearEntries function
function clearEntries() {
    filters = {};

    // Sets every input field to empty
    filterInputs._groups[0].forEach(entry => {
        if (entry.value != 0) {
            d3.select('#' + entry.id).node().value = "";
        }
    });
};

var clearButton = d3.select("#clear");

// Clear button on click clears fields
// include clear button test
clearButton.on('click', function () {
    console.log("testing clear button")

    // Keeps page from refreshing completely, only want the table to refresh...
    d3.event.preventDefault();

    // Clears input fields..
    clearEntries()
});


