var showPasswordButton = document.getElementById("show-password");
var isShowingPassword = false;

var signInButton = document.getElementById("sign-in");
var errorMessage = document.getElementById("wrong-username-password");

showPasswordButton.onclick = function () {
    if(isShowingPassword == false) {
        isShowingPassword = true;
        PIP.type = "text";
        showPasswordButton.textContent = "Hide Password"
    }
    else {
        isShowingPassword = false;
        PIP.type = "password";
        showPasswordButton.textContent = "Unhide Password"
    }
};