let size = parseInt(prompt("What will the size of the chessboard be?"))
let x = ``;
for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        if ((i + j) % 2 === 0) {
            x += ` `; 
            }
            else {
                x += `#`; 
            }
        } x += `\n`; }
console.log(x);