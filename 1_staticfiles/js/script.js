/** Dictionary of learning objectives */
let lo = {
    LO1: "LO1 blah",
    LO2: "LO2 blahblah",
    LO3: "LO3 blahblah",
    LO4: "LO4 blahblah",
    LO5: "LO5 blahblah",
    LO6: "LO6 blahblah",
    LO7: "LO7 blahblah",
    LO8: "LO8 blahblah",
    LO9: "LO9 blahblah",
    LO10: "LO10 blahblah"
};

/** Dictionary of warnings */
let warning = {
    w0: "None",
    w1: "Warning",
    w2: "Flag"
};


/**
 * Changes the textContent of the LO from the table integer to a human-readable "verbose" string.
 * @return {String} "LOx [the learning objective]."
 */
function loVerbose () {
    let loN = document.getElementsByClassName("q-lo");

    for (i = 0; i < loN.length; i++) {
        if (loN[i].textContent == "1") {
            loN[i].innerHTML = lo.LO1;
        }
        else if (loN[i].textContent == "2") {
            loN[i].innerHTML = lo.LO2;
        }
        else if (loN[i].textContent == "3") {
            loN[i].innerHTML = lo.LO3;
        }
        else if (loN[i].textContent == "4") {
            loN[i].innerHTML = lo.LO4;
        }
        else if (loN[i].textContent == "5") {
            loN[i].innerHTML = lo.LO5;
        }
        else if (loN[i].textContent == "6") {
            loN[i].innerHTML = lo.LO6;
        }
        else if (loN[i].textContent == "7") {
            loN[i].innerHTML = lo.LO7;
        }
        else if (loN[i].textContent == "8") {
            loN[i].innerHTML = lo.LO8;
        }
        else if (loN[i].textContent == "9") {
            loN[i].innerHTML = lo.LO9;
        }
        else if (loN[i].textContent == "10") {
            loN[i].innerHTML = lo.LO10;
        }
    }
}

/**
 * Changes the textContent of the WARNING from the table integer to a human-readable "verbose" string.
 * @return {String} "None / Warning / Flag"
 */
function warningVerbose () {
    let warningN = document.getElementsByClassName("q-warning");

    for (i = 0; i < warningN.length; i++) {
        if (warningN[i].textContent == "0") {
            warningN[i].innerHTML = warning.w0;
        }
        else if (warningN[i].textContent == "1") {
            warningN[i].innerHTML = warning.w1;
        }
        else if (warningN[i].textContent == "2") {
            warningN[i].innerHTML = warning.w2;
        }
    }
}


/**
 * On DOM load:
 * - Run loVerbose()
 */
document.addEventListener("DOMContentLoaded", function () {
    loVerbose();
    warningVerbose();
});