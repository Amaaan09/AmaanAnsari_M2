let stringCont = document.getElementById("var1");
let intCont = document.getElementById("var2");
let sumFuncAns = document.getElementById("funca");
let if_elseAns = document.getElementById("if-else-header-answer");

let stringVar = "Amaan";
stringCont.innerHTML = stringVar;
let integerVar = 13;
intCont.innerHTML = integerVar;

let sumFunc = (num1, num2) => {
  return num1 + num2;
};

sumFuncAns.innerHTML = sumFunc(1, 2);

let age = 21;
if (age >= 21) {
  if_elseAns.innerHTML = "Yes!";
} else {
  if_elseAns.innerHTML = "No!";
}

for (let k = 1; k < 21; k++) {
  document.write(k * 3 + "<br>");
}