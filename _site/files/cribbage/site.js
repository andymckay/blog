let game = getOrSetupData();
setupNames();
updateScore();
changeViews();

function setupData() {
  let game = {};
  game.one = {
    name: '',
    points: []
  }
  game.two = {
    name: '',
    points: []
  }
  game.inProgress = false;
  game.resumable = false;
  return game;
}

function saveData() {
  console.log('Saved data');
  window.localStorage.setItem('game', JSON.stringify(game));
}

function getOrSetupData() {
  let data = window.localStorage.game;
  if (data) {
    console.log('Retrieved saved data.');
    return JSON.parse(data);
  } else {
    console.log('Created new data.');
    return setupData();
  }
}

function setupNames() {
  document.getElementById("name-one").value = game.one.name;
  document.getElementById("name-two").value = game.two.name;
}

function clearData() {
  console.log('Cleared local data.')
  window.localStorage.clear();
}

function changeViews() {
  if (game.inProgress) {
    document.getElementById("game-setup").style.display = 'none';
    document.getElementById("in-progress").style.display = 'block';
    document.getElementById("game-resume").style.display = 'none';
    updateScore();
  } else {
    document.getElementById("game-setup").style.display = 'block';
    document.getElementById("in-progress").style.display = 'none';
    if (game.resumable) {
      document.getElementById("game-resume").style.display = 'block';
    }
  }
}

function processSetup(event) {
  event.preventDefault();
  let data = new FormData(event.target);
  game = setupData();
  game.one.name = data.get('one', 'player-1');
  game.two.name = data.get('two', 'player-2');
  game.inProgress = true;
  let winner = document.getElementById("winner");
  winner.style.display = 'none';
  changeViews();
  saveData();
}

function sumArray(data) {
  if (data.length) {
    return data.reduce((a, e) => a + e);
  }
}

function processScore(event) {
  if (game.inProgress) {
    event.preventDefault();
    let data = new FormData(event.target);
    if (data.get('one')) {
      game.one.points.push(parseInt(data.get('one')));
    }
    if (data.get('two')) {
      game.two.points.push(parseInt(data.get('two')));
    }
    let list = event.target.getElementsByTagName('input');
    for (let item of list) {
      item.value = '';
    }
    saveData();
    updateScore();
  }
}

function updateScore() {
  if (game.inProgress) {
    let one_score = sumArray(game.one.points);
    let two_score = sumArray(game.two.points);
    document.getElementById("score-name-one").innerText = game.one.name;
    document.getElementById("score-name-two").innerText = game.two.name;
    document.getElementById("score-one").innerText = one_score ? one_score : 0;
    document.getElementById("score-two").innerText = two_score ? two_score : 0;
    document.getElementById("score-one-last").innerText = game.one.points.slice(Math.max(game.one.points.length - 5, 0))
    document.getElementById("score-two-last").innerText = game.two.points.slice(Math.max(game.two.points.length - 5, 0))
    if (one_score >= 121) {
      declareWinner(game.one);
    }

    if (two_score >= 121) {
      declareWinner(game.two);
    }
  }
}

function declareWinner(player) {
    game.inProgress = false;
    game.resumable = false;
    let winner = document.getElementById("winner");
    winner.innerText = `${player.name} has won.`
    winner.style.display = 'block';
    saveData();
    updateScore();
}

function processEnd() {
  if (game.inProgress) {
    game.resumable = true;
  }
  game.inProgress = false;
  saveData();
  changeViews();
}

function processResume() {
  game.inProgress = true;
  saveData();
  changeViews();
}

function processQuickAdd(event) {
  let result = event.target.value.split('-');
  game[result[0]].points.push(parseInt(result[1]));
  updateScore();
}

document.getElementById("game-setup").addEventListener("submit", processSetup);
document.getElementById("game-end").addEventListener("submit", processEnd);
document.getElementById("game-resume").addEventListener("submit", processResume);

let list = document.getElementsByClassName("enter-points");
for (let item of list) {
  item.addEventListener("submit", processScore);
}

list = document.getElementsByClassName("quick-add");
for (let item of list) {
  item.addEventListener("click", processQuickAdd);
}
