    let count = 0;

    document.getElementById("decreaseBtn").onclick = function () {
        "use strict";
        if (count > 0){
            count -= 1;
        }
        else{
            count = 0;
        }
        document.getElementById("countLabel").innerHTML = count;
    };

    document.getElementById("resetBtn").onclick = function (){
        "use strict";
        count = 0;
        document.getElementById("countLabel").innerHTML = count;
    };
    document.getElementById("increaseBtn").onclick = function (){
        "use strict";
        count += 1;
        document.getElementById("countLabel").innerHTML = count;
    };