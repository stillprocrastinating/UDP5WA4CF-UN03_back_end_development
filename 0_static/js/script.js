/** Dictionary of learning objectives */
let lo = {
    LO1: "LO1 To understand the historical framework of ASPA and the ethics behind it.",
    LO2: "LO2 To state what the ethical framework which underpins ASPA is and how programs of work are justified, by weighing likely adverse effects on the animals against the likely benefits.",
    LO3: "LO3 To define the 3Rs. Indicate what they are for and how these relate to ethical principles.",
    LO4: "LO4 To identify relevant sources of information relating to ethics and the 3Rs.",
    LO5: "LO5 To identify ethical and animal welfare issues in their own work.",
    LO6: "LO6 To explain the limits of what is considered permissible to do within a research establishment and how cultural, national, temporal, and institutional factors can differ.",
    LO7: "LO7 To discuss to what extent welfare issues, pain, suffering, distress, and lasting harm should be interpreted.",
    LO8: "LO8 To explain what a culture of care is, its importance, and how they may contribute.",
    LO9: "LO9 To recognise the importance of ethical responsibility and identify the consequences of their actions—connected to culture of care.",
    LO10: "LO10 To explain the purpose of the local AWERB.",
    LO11: "LO11",
    LO12: "LO12",
    LO13: "LO13",
    LO14: "LO14",
};

/** Dictionary of warnings */
let warning = {
    w1: "None",
    w2: "Warning",
    w3: "Flag"
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
        else if (loN[i].textContent == "11") {
            loN[i].innerHTML = lo.LO11;
        }
        else if (loN[i].textContent == "12") {
            loN[i].innerHTML = lo.LO12;
        }
        else if (loN[i].textContent == "13") {
            loN[i].innerHTML = lo.LO13;
        }
        else if (loN[i].textContent == "14") {
            loN[i].innerHTML = lo.LO14;
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
 * Calculates the Q_DIFFICULTY of the Question from the correct_option_frequency of the Answers.
 * @return {Integer} "1 / 2 / 3"
 */
function calculateQuestionDifficulty () {}


/**
 * Calculates the T_DIFFICULTY of the Test from the Q_DIFFUCULTY of the Question.
 * @return {Integer} "1 / 2 / 3"
 */
function calculateTestDifficulty () {}


/**
 * Calculates the WARNING of the Question from the incorrect_option_frequency of the Answers.
 * @return {Integer} "1 / 2 / 3"
 */
function calculateQuestionWarning () {}


/**
 * On DOM load:
 * - Run loVerbose()
 * - Run warningVerbose()
 * - Run calculateQuestionDifficulty()
 * - Run calculateTestDifficulty()
 * - Run calculateQuestionWarning()
 */
document.addEventListener("DOMContentLoaded", function () {
    loVerbose();
    warningVerbose();
    calculateQuestionDifficulty();
    calculateTestDifficulty();
    calculateQuestionWarning();
});
