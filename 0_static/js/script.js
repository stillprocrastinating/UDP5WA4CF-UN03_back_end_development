function loVerbose () {
    let loN = document.getElementsByClassName("q-lo");

    for (i = 0; i < loN.length; i++) {
        if (loN[i].textContent == "1") {
            loLabel == "LO1";
        }
        
        loN[i].textContent = loLabel;
    }
}