var selectedFilters = {
  issue: [],
  reason: [],
  content: []
}

if (isNotIE8()) {
  (function(){
    // Overlay when sidebar is open
    select(".sidebar-overlay").addEventListener('click', function() {
      select("#filter_filter").checked = false;
      select("body").classList.remove("stop-scrolling");
    });
    select(".sidebar-overlay").classList.add("sidebar-overlay-js");

    // Stops main page scrolling when sidebar open
    select("#filter_filter").addEventListener('click', function() {
      if (select("#filter_filter").checked) {
        select("body").classList.add("stop-scrolling");
      } else {
        select("body").classList.remove("stop-scrolling");
      }
    });

    // Moves buttons to bottom of sidebar
    select(".sidebar-buttons").classList.add("mt5");

    // Displays orange arrows on select box
    selectAll(".fa-down").forEach(function(el) {
      el.classList.remove("filter-arrow-hide");
    });

    // Event listeners and CSS for scrollable filter boxes
    ["issue", "reason", "content"].forEach(function(el) {
      var filterType = select("." + el + "-filters");
      var filterSelect = select(".select-" + el + "-filters");
      var sidebar = select(".sidebar");
      var addYourOwn = select(".add-own", filterType);

      addClasses(filterType, ["hide-filters", "br1", "w-100", "absolute", "bg-white", "z-1", "overflow-y-scroll", "overflow-x-hidden"]);
      addClasses(filterSelect, ["select-filters", "pointer"]);

      filterSelect.addEventListener("click", function() {
        toggleClasses(filterType, ["hide-filters", "shadow-2", "h45"])
        toggleArrows(el);

        sidebar.addEventListener("click", function hideFilters(e) {
          var path = getPath(e);

          updateSelected(select("#filter-form"));
          displaySelected(el);

          if (path.indexOf(filterSelect) == -1 && path.indexOf(filterType) == -1){
            toggleArrows(el);
            filterType.classList.add("hide-filters");
            filterType.classList.remove("shadow-2", "h45");
            sidebar.removeEventListener("click", hideFilters);
          }
        });
      });

      addYourOwn.addEventListener("click", function(e) {
        e.preventDefault();

        var opts = {body: {}};
        opts.body[el] = {add_your_own: select("#tags_" + el + "_add_your_own").value};

        var pending = select(".alert.pending", filterType);
        pending.innerText = "Submitting...";

        makePhoenixFormRequest("POST", select("#filter-form"), function(err, res) {
          if (res) {
            var alert = select(".alert.complete", filterType);
            pending.innerText = "";
            alert.innerText = "Thank you for your suggestion";
          }
        }, opts);
      })

      // Clicking 'Show Everything' deselects all other filters
      select(".show-everything-" + el).addEventListener("click", function() {
        selectAll(".filters-" + el).forEach(function(elem) {
          elem.checked = false;
        })
        if (select(".show-everything-" + el).checked) {
          selectedFilters[el] = ["Show-Me-Everything"];
        }
      });

      // Clicking any other filter deselects 'Show Everything'
      selectAll(".filters-" + el).forEach(function(elem){
        elem.addEventListener("click", function() {
          select(".show-everything-" + el).checked = false;
          selectedFilters[el]["Show-Me-Everything"] = false;
        });
      });

      updateSelected(select("#filter-form"));
      displaySelected(el);
    });
  })();
}

function toggleArrows(type) {
  toggleClasses(select(".select-" + type + "-filters > h5 > .fa-up"), ["filter-arrow-hide"]);
  toggleClasses(select(".select-" + type + "-filters > h5 > .fa-down"), ["filter-arrow-hide"]);
 }

function updateSelected(form) {
  selectedFilters = Object.assign(selectedFilters, getFormData(form))
}

function displaySelected(el) {
  var selected = [];
  var exclude = ["all-issue", "all-reason", "all-content"];
  var title = select("." + el + "-filters-header");

  selected = selected.concat(selectedFilters[el]);

  if (selected.length === 1) {
    title.innerText = selected[0].split("-").join(" ");
    addClasses(title, ["segoe-bold", "lm-dark-blue"]);
  } else if (selected.length > 1) {
    title.innerText = selected.length + " filters selected";
    addClasses(title, ["segoe-bold", "lm-dark-blue"]);
  } else {
    title.innerText = "Select as many as are relevant";
    removeClasses(title, ["segoe-bold", "lm-dark-blue"]);
  }
}

function getPath(event) {
  if (event.path) {
    return event.path;
  } else {
    var current = event.target;
    var path = [current];

    while (current.parentNode) {
      current = current.parentNode
      path.push(current);
    }
    return path;
  }
}
