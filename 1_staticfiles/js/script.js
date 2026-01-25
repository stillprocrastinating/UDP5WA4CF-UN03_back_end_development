/** Dictionary of learning objectives */
let lo = {
    LO1: "LO1 blah",
    LO2: "LO2 blahblah"
}


/**
 * Changes the textContent of the LO from the table integer to a human-readable "verbose" string.
 * @return {String} "LOx [the learning objective]."
 */
function loVerbose () {
    let loN = document.getElementsByClassName("q-lo");

    for (i = 0; i < loN.length; i++) {
        if (loN[i].textContent == "1") {
            loN[i].textContent == lo.LO1;
        }
    }
}