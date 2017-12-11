numberOfFaces = 5;
theLeftSide = document.getElementById('leftside');
theRightSide = document.getElementById('rightside');
theBody = document.getElementsByTagName('body')[0];

function generateFaces() {
  count = 0;

  while (theLeftSide.lastChild)
    theLeftSide.removeChild(theLeftSide.lastChild)

  while (theRightSide.lastChild)
    theRightSide.removeChild(theRightSide.lastChild)

  while (count < numberOfFaces) {
    anImg = document.createElement("img");
    anImg.src = "smile.png";
    topy = Math.floor(Math.random()*400);
    leftx = Math.floor(Math.random()*400);
    console.log(leftx);
    console.log(topy);
    anImg.style.top = topy + "px";
    anImg.style.left = leftx + "px";
    theLeftSide.appendChild(anImg);
    count++;
  }
  leftSideImages = theLeftSide.cloneNode(true);
  leftSideImages.removeChild(leftSideImages.lastChild);
  theRightSide.appendChild(leftSideImages);

  theLeftSide.lastChild.onclick = function nextLevel(event){
    event.stopPropagation();
    numberOfFaces += 5;
    generateFaces();
  };

  theBody.onclick = function gameOver(event) {
    alert("Game Over");
    theBody.onclick = null;
    theLeftSide.lastChild.onclick = null;
  };
}
