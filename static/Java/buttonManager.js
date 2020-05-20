var userSettingsButton = document.getElementById("user-settings");
var userSettingsDisplay = document.getElementById("user-settings-container");
var loginButton = document.getElementById("log-in");

var logInContainer = document.getElementById("log-in-container-id");
var userDetailsContaner = document.getElementById("user-details-container-id");

var userSettingsIsVisible = false;

var isLoggedIn = false;

userSettingsButton.onclick = function() {
    if(userSettingsIsVisible == true) {
        userSettingsDisplay.style.visibility = "hidden";
        userSettingsDisplay.style.display = "none";
        userSettingsIsVisible = false;
    }
    else if(userSettingsIsVisible == false) {
        userSettingsDisplay.style.visibility = "visible";
        userSettingsDisplay.style.display = "block";
        userSettingsIsVisible = true;
    }
};

loginButton.onclick = function() {
    if(isLoggedIn == false) {
        logInContainer.style.opacity = 0;
        userDetailsContaner.style.opacity = 1;
        loginButton.style.cursor = "default";
        isLoggedIn = true;
    }
    // else if(isLoggedIn == true) {
    //     logInContainer.style.opacity = 1;
    //     userDetailsContaner.style.opacity = 0;
    //     loginButton.style.cursor = "pointer";
    //     isLoggedIn = false;
    // }
}
