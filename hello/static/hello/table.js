// document.addEventListener('DOMContentLoaded', function (e) {
//     // Set Dimensions
//     const xSize = 500;
//     const ySize = 500;
//     const margin = 40;
//     const xMax = xSize - margin * 2;
//     const yMax = ySize - margin * 2;

//     // Create Random Points
//     const numPoints = 100;
//     const data = [];
//     for (let i = 0; i < numPoints; i++) {
//         data.push([Math.random() * xMax, Math.random() * yMax]);
//     }

//     // Append SVG Object to the Page
//     const svg = d3.select("#myPlot")
//         .append("svg")
//         .append("g")
//         .attr("transform", "translate(" + margin + "," + margin + ")");

//     // X Axis
//     const x = d3.scaleLinear()
//         .domain([0, 500])
//         .range([0, xMax]);

//     svg.append("g")
//         .attr("transform", "translate(0," + yMax + ")")
//         .call(d3.axisBottom(x));

//     // Y Axis
//     const y = d3.scaleLinear()
//         .domain([0, 500])
//         .range([yMax, 0]);

//     svg.append("g")
//         .call(d3.axisLeft(y));

//     // Dots
//     svg.append('g')
//         .selectAll("dot")
//         .data(data).enter()
//         .append("circle")
//         .attr("cx", function (d) { return d[0] })
//         .attr("cy", function (d) { return d[1] })
//         .attr("r", 3)
//         .style("fill", "Red");
// })

function get_sublist(list, specIndex) {
    specList = []
    for (let i = 0; i < list.length; i++) {
        specList.push(list[i][specIndex])
    }
    return specList
}

function get_avg(specList) {

    avgList = []
    total = 0
    for (let i = 0; i < specList.length; i++) {
        total += Number(specList[i])
    }
    console.log(total)
    // Find per day
    dayAvg = total / specList.length
    avgList.push(dayAvg)

    // Find per month
    monthAvg = total / (specList.length / 30)
    avgList.push(monthAvg)

    // Find per year
    yearAvg = total / (specList.length / 365)
    avgList.push(yearAvg)

    return avgList
}


function header_color() {
    let cat
    for (let i = 1; i < 6; i++) {
        cat = document.getElementById("header" + i)
        cat.style.color = 'white'
        cat.style.backgroundColor = 'grey'
        cat.addEventListener('mouseover', function (event) {
            event.target.style.backgroundColor = 'black'
        })
        cat.addEventListener('mouseout', function (event) {
            event.target.style.backgroundColor = 'grey'
        })
    }

}


function get_insight(header, list) {
    // console.log(header)
    // console.log(list)
    let cat
    for (let i = 2; i < 6; i++) {
        cat = document.getElementById("header" + i)
        cat.addEventListener('click', function (event) {
            // Gets the index of the header that is selected
            clickedIndex = Number(event.target.id.slice(6)) - 1

            table = document.getElementById("data")
            table.style.display = 'none';

            const tableDiv = document.createElement("div")
            const newTable = document.createElement("table")
            const newTableBody = document.createElement("tbody")
            newTable.id = "newTable"
            const row = document.createElement("tr")
            const cell = document.createElement("td")
            const text = document.createTextNode(header[clickedIndex])

            cell.appendChild(text)
            row.appendChild(cell)

            newTableBody.appendChild(row)

            for (let i = 0; i < list.length; i++) {
                const row = document.createElement("tr")
                const cell = document.createElement("td")
                const text = document.createTextNode(list[i][clickedIndex])
                cell.appendChild(text)
                row.appendChild(cell)

                newTableBody.appendChild(row)
            }

            newTable.appendChild(newTableBody)

            // document.body.appendChild(newTable)

            newTable.setAttribute("border", "2")

            tableDiv.appendChild(newTable)
            document.body.appendChild(tableDiv)


            const backButton = document.createElement("button");

            backButton.textContent = 'Back'
            backButton.id = 'backButton'


            specList = get_sublist(list, clickedIndex)
            avgList = get_avg(specList)

            console.log(avgList)

            const insightDiv = document.createElement("div")
            const testText = document.createTextNode("Test Text")



            // testText.setAttribute("border", "2")
            const insightOffset = newTable.offsetWidth
            // console.log(insightOffset)


            insightDiv.classList.add("topLeft")
            insightDiv.style.left = insightOffset + 15
            insightDiv.appendChild(testText)

            backButton.addEventListener('click', function () {
                table.style.display = ''
                backButton.remove()
                tableDiv.remove()
                insightDiv.remove()
            })


            document.body.appendChild(insightDiv)

            document.body.appendChild(backButton)



        });
    }

}

