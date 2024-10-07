let stacks = parseInt(prompt("How tall should the pyramid be?"))
let x = 1;
let y = 9;
let a = `#`;
let b = ` `;
if (stacks >= 1 && stacks <= 8) {
    for (let i = 0; i < stacks; i++) {
        console.log(a.repeat(x) + b.repeat(y));
        x++;
        y--; }}
else {console.log(`Number needs to be between 1-8.`); }