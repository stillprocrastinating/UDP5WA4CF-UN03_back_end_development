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
    LO11: "LO11 To explain the Five Freedoms and how these apply to laboratory species.",
    LO12: "LO12 To describe the concept of harms to animals including avoidable and unavoidable suffering, direct, contingent, and cumulative suffering.",
    LO13: "LO13 To describe the importance of good animal welfare including its' effect on scientific outcomes as well as for societal and moral reasons.",
    LO14: "LO14 To describe the responsibility of humans when working with research animals and recognise the importance of having a respectful and humane attitude towards working with animals in research."
};


/** Dictionary of question types */
let q_type = {
    qt1: "Diagram",
    qt2: "Drag & drop",
    qt3: "Multiple choice",
    qt4: "Matching",
    qt5: "Missing word",
    qt6: "True/false"
};


/** Dictionary of test difficulties */
let q_difficulty = {
    qd0: "Error in calculation",
    qd1: "Easy",
    qd2: "Optimal",
    qd3: "Difficult"
};


/** Dictionary of test difficulties */
let t_difficulty = {
    td0: "Error in calculation",
    td1: "Easy",
    td2: "Optimal",
    td3: "Difficult"
};


/** Dictionary of test types */
let t_type = {
    tt1: "E1/L PiLAB Test",
    tt2: "PiLAB Test",
    tt3: "Resit"
};


/** Dictionary of warnings */
let warning = {
    w0: "Error in calculation",
    w1: "None.",
    w2: "Yes."
};


/**
 * Calculates the Q_DIFFICULTY of the Question from the correct_option_frequency of the Answers.
 * @return {Integer} "1 / 2 / 3"
 */
function calculateDifficultyQuestion () {}


/**
 * Calculates the T_DIFFICULTY of the Test from the Q_DIFFUCULTY of the Question.
 * @return {Integer} "1 / 2 / 3"
 */
function calculateDifficultyTest () {}


/**
 * Calculates the WARNING of the Question from the calculateWarningTestQuestions().
 * @return {Integer} "1 / 2 / 3"
 */
function calculateWarningQuestion () {}


/**
 * Calculates the WARNING of the Tests' Question from the .answers-list-warning of the Answers.
 * @return {Integer} "1 / 2"
 */
function calculateWarningTestQuestions () {
    let tw = document.getElementsByClassName("q-warnings").textContent;
    let qw = document.getElementsByClassName("answers-list-warning");

    for (i = 0; i < qw.length; i++) {
        if (qw[i].textContent[18] == "C") {     // Consider a learning objective teaching method audit.
            tw == 2;
        }
        else if (qw[i].textContent[18] == "N") {     // None.
            tw == 1;
        }
        else {
            tw == 0;
        }
    }

    verboseWarning();
}


/**
 * Edit the TestForm() form attributes.
 */
function formModifications () {
    let inputIdId = document.getElementById("id_id");
    let inputIdDate = document.getElementById("id_date");
    let inputIdQuestion = document.getElementById("id_question");

    if (inputIdId != null) {
        inputIdId.placeholder = "E1/L PiLAB Jan 26 resit";
        inputIdId.autofocus = true;
        inputIdId.previousElementSibling.innerHTML = inputIdId.previousElementSibling.innerHTML + "<span class='form-hint'>( [E1/L] PiLAB Month Year [resit] )</span>";
    }

    if (inputIdDate != null) {
        inputIdDate.type = "date";
    }

    if (inputIdQuestion != null) {
        inputIdQuestion.style.width = "90%";
    }
}


/**
 * Changes the textContent of the p.answers-list-answer from the table integer to a human-readable "verbose" string.
 * @return {String} "[The text answer for that participant for that question]."
 */
// function verboseAnswer () {
//     let q = document.getElementsByClassName("answers-list-question");
//     let q_id = 

//     let loN = document.getElementsByClassName("q-lo");

//     for (i = 0; i < loN.length; i++) {
//         if (loN[i].textContent == "1") {
//             loN[i].innerHTML = lo.LO1;
//         }
//     }
// }


/**
 * Changes the textContent of the LO from the table integer to a human-readable "verbose" string.
 * @return {String} "LOx [the learning objective]."
 */
function verboseLO () {
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
 * Changes the textContent of the T_DIFFICULTY from the table integer to a human-readable "verbose" string.
 * @return {String} "Error in calculation / Easy / Optimal / Difficult"
 */
function verboseDifficultyQuestion () {
    let N = document.getElementsByClassName("q-difficulty");

    for (i = 0; i < N.length; i++) {
        if (N[i].textContent == "0") {
            N[i].innerHTML = q_difficulty.qd0;
        }
        else if (N[i].textContent == "1") {
            N[i].innerHTML = q_difficulty.qd1;
        }
        else if (N[i].textContent == "2") {
            N[i].innerHTML = q_difficulty.qd2;
        }
        else if (N[i].textContent == "3") {
            N[i].innerHTML = q_difficulty.qd3;
        }
    }
}


/**
 * Changes the textContent of the T_DIFFICULTY from the table integer to a human-readable "verbose" string.
 * @return {String} "Error in calculation / Easy / Optimal / Difficult"
 */
function verboseDifficultyTest () {
    let N = document.getElementsByClassName("t-difficulty");

    for (i = 0; i < N.length; i++) {
        if (N[i].textContent == "0") {
            N[i].innerHTML = t_difficulty.td0;
        }
        else if (N[i].textContent == "1") {
            N[i].innerHTML = t_difficulty.td1;
        }
        else if (N[i].textContent == "2") {
            N[i].innerHTML = t_difficulty.td2;
        }
        else if (N[i].textContent == "3") {
            N[i].innerHTML = t_difficulty.td3;
        }
    }
}


/**
 * Changes the textContent of the Q_TYPE from the table integer to a human-readable "verbose" string.
 * @return {String} "[the question type]."
 */
function verboseTypeQuestion () {
    let testN = document.getElementsByClassName("q-type");

    for (i = 0; i < testN.length; i++) {
        if (testN[i].textContent == "1") {
            testN[i].innerHTML = q_type.qt1;
        }
        else if (testN[i].textContent == "2") {
            testN[i].innerHTML = q_type.qt2;
        }
        else if (testN[i].textContent == "3") {
            testN[i].innerHTML = q_type.qt3;
        }
        else if (testN[i].textContent == "4") {
            testN[i].innerHTML = q_type.qt4;
        }
        else if (testN[i].textContent == "5") {
            testN[i].innerHTML = q_type.qt5;
        }
        else if (testN[i].textContent == "6") {
            testN[i].innerHTML = q_type.qt6;
        }
    }
}


/**
 * Changes the textContent of the T_TYPE from the table integer to a human-readable "verbose" string.
 * @return {String} "[the test type]."
 */
function verboseTypeTest () {
    let testN = document.getElementsByClassName("t-type");

    for (i = 0; i < testN.length; i++) {
        if (testN[i].textContent == "0") {
            testN[i].innerHTML = t_type.tt1;
        }
        else if (testN[i].textContent == "1") {
            testN[i].innerHTML = t_type.tt2;
        }
        else if (testN[i].textContent == "2") {
            testN[i].innerHTML = t_type.tt3;
        }
    }
}


/**
 * Changes the textContent of the WARNING from the table integer to a human-readable "verbose" string.
 * @return {String} "None / Yes"
 */
function verboseWarning () {
    let warningN = document.getElementsByClassName("q-warnings");

    for (i = 0; i < warningN.length; i++) {
        if (warningN[i].textContent == "2") {
            warningN[i].innerHTML = warning.w2;
        }
        else if (warningN[i].textContent == "1") {
            warningN[i].innerHTML = warning.w1;
        }
        else {
            warningN[i].innerHTML = warning.w0;
        }
    }
}


/**
 * On DOM load:
 * - Run calculateDifficultyQuestion()
 * - Run calculateDifficultyTest()
 * - Run calculateWarningQuestion()
 * - Run calculateWarningTestQuestions()
 * - Run formModifications()
 * - Run verboseLO()
 * - Run verboseDifficultyQuestion()
 * - Run verboseDifficultyTest()
 * - Run verboseTypeQuestion()
 * - Run verboseTypeTest()
 * - Run verboseWarning()
 */
document.addEventListener("DOMContentLoaded", function () {
    // calculateDifficultyQuestion();
    // calculateDifficultyTest();
    // calculateWarningQuestion();
    calculateWarningTestQuestions();
    // verboseAnswer();
    verboseLO();
    verboseDifficultyQuestion();
    verboseDifficultyTest();
    verboseTypeQuestion();
    verboseTypeTest();
    // verboseWarning();

    if (document = "/test/new") {
        formModifications();
    }     // etc for each page to avoid console errors
});
