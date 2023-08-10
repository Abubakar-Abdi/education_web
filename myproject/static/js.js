
document.getElementById("home").style.display = "block";
document.getElementById("allinstitute-page").style.display = "none";
document.getElementById("login").style.display = "none";


function homePage() {
    document.getElementById("home").style.display = "block";
    document.getElementById("login").style.display = "none";
    document.getElementById("allinstitute-page").style.display = "none";
    
}

function postPage() {
    document.getElementById("allinstitute-page").style.display = "block";
    document.getElementById("home").style.display = "none";
    document.getElementById("login").style.display = "none";
   
}
function logIn() {
    document.getElementById("login").style.display = "block";
    document.getElementById("home").style.display = "none";
    document.getElementById("allinstitute-page").style.display = "none";
   
}

