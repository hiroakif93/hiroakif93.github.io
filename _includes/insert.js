function navbar(FILE){
    var html = "";
    html += '<nav>'
    html += '<ul id="nav">'
    html += '<li class="current"><a href="index.html">Home</a></li>'
    html += '<li><a href="about/about.html">About</a></li>'
    html += '<li><a href="Publications/index.html">Publications</a></li>'
    html += '<li>'
    html += '<a class="dropdown">Documents</a>'
    html += '<ul class="menu">'
    html += '<li><a href="Documents/R/index.html">R</a></li>'
    html += '<li><a href="Documents/bioinfo/index.html">Bioinfo</a></li>'                    
    html += '</ul>'
    html += '</li>'
    html += '</ul>'
    html += '</nav>'

    document.write(html);
}

function navbar_jp(FILE){
    var html = "";
    html += '<nav>'
    html += '<ul id="nav">'
    html += '<li class="current"><a href="index_jp.html">Home</a></li>'
    html += '<li><a href="about/about_jp.html">About</a></li>'
    html += '<li><a href="Publications/index_jp.html">Publications</a></li>'
    html += '<li>'
    html += '<div class="dropdown">'
    html += '<button class="dropbtn" onclick="drop()">Documents'
    html += '<i class="fa fa-caret-down"></i>'
    html += '</button>'
    html += '<a href="Documents/R/index_jp.html">R</a>'
    html += '<a href="Documents/bioinfo/index_jp.html">Bioinfo</a>'
    html += '</div>'
    html += '</ul>'
    html += '</li>'
    html += '</ul>'
    html += '</nav>'

    document.write(html);
}
  
function footer(FILE){
    var html = ''
    html += '<footer>'
    html += '<small>Copyright 2024, Hiroaki Fujita</small>'
    html += '</footer>'

    document.write(html);
}            
        
function drop() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
    }
  }