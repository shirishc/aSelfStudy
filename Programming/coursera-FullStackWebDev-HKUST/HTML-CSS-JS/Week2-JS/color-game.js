var colors = ["blue", "cyan", "gold", "gray", "green", "magenta", "orange", "red", "white", "yellow"];
var choices = colors.join();

function play_game() {
  var correct_guess = colors[Math.floor((Math.random()*10)+1)-1];
  var found = false;
  var iter = 1;

  while (!found) {
    var guess = prompt("I am thinking of one of these colors:\n\n"
                  + choices + "\n\nWhat color am I thinking of?").toLowerCase();

    found = check_guess(guess, correct_guess);
    iter++;
  }
  alert("Well Done. The number of guesses you took - " + iter)
  document.body.style.backgroundColor = correct_guess;
}

function check_guess(guess, correct_guess) {
  if (colors.indexOf(guess) == -1)
    alert("Sorry, " + guess + " is not a color in the list - " + choices +
          + ".\n\nPlease try again");
  else if (guess == correct_guess)
    return true;
  else if (guess > correct_guess)
    alert("Your guess is alphabetically higer than mine.\n\nPlease try again.");
  else
    alert("Your guess is alphabetically lower than mine.\n\nPlease try again.");

  return false;
}
