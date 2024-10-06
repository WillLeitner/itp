let season = parseInt(prompt("What number month is it?"));
if (season < 1 || season > 12) {
    console.log("There are only 12 months in a year!");
 } else if (season <= 6 && season >= 4) {
    console.log("Boston is in Spring!");
  } else if (season <= 9 && season >= 7) {
    console.log("Boston is in Summer!");
  } else if (season <= 11 && season >= 10) {
    console.log("Boston is in Fall!");
  } else console.log("Boston is in Winter!");