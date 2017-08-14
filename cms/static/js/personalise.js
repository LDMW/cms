var personaliseDiv = document.getElementById('elm-personalise');

var issue_tags = getTags('issue')
var content_tags = getTags('content')
var reason_tags = getTags('reason')
var issue_label = document.getElementById('issue_label').innerText;
var reason_label = document.getElementById('reason_label').innerText;
var content_label = document.getElementById('content_label').innerText;

var selected_tags = selectedTags(getQuery('issue', 'content', 'reason'));

Elm.Main.embed(personaliseDiv, {
  issue_tags: issue_tags,
  content_tags: content_tags,
  reason_tags: reason_tags,
  issue_label: issue_label,
  reason_label: reason_label,
  content_label: content_label,
  selected_tags: selected_tags
});

function getTags(name) {
  return Array.prototype.map.call(personaliseDiv.querySelectorAll("input[name='" + name + "']"), function(el){
    return el.value;
  });
}

function getQuery() {
  var qs = window.location.href.split("?")[1];
  var query = {};

  Array.prototype.forEach.call(arguments, function(a) {
    query[a] = [];
    var reg = new RegExp("(?:^" + a + "|&" + a + ")=([^&]+)", "g")
    var arr;

    while ((myArray = reg.exec(qs)) !== null) {
      query[a].push(myArray[1].split('%20').join(' '));
    }
  });
  return query;
}

function selectedTags(queryObj) {
  var selected = [];
  for (var type in queryObj) {
    selected = selected.concat(queryObj[type]);
  }
  return selected;
}