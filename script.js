const operation = document.getElementById("operation");
const num2 = document.getElementById("num2");

function toggleSecondInput(){

    const singleInputOperations = [
        "sqrt",
        "square",
        "cube",
        "factorial",
        "log",
        "sine"
    ];

    if(singleInputOperations.includes(operation.value)){

        num2.style.display = "none";
        num2.required = false;

    }
    else{

        num2.style.display = "block";
        num2.required = true;

    }

}

operation.addEventListener("change",toggleSecondInput);

toggleSecondInput();
