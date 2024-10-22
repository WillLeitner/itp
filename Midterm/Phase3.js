function setup() {
  createCanvas(400, 400);
  noStroke();
}

function drawObject(x, y, s) {
  push();
  translate(x, y);
  scale(s);
  fill(90);
  rect(110, 200, 180, 200);
  fill(80);
  ellipse(200, 220, 240, 200);
  fill(0);
  rect(170, 320, 60, 80);
  fill(255)
  ellipse(180, 360, 7, 7);
  ellipse(155, 170, 45, 45);
  ellipse(135, 240, 45, 45);
  ellipse(250, 220, 75, 78)
  pop();
}