var link = document.getElementById("color-mode");
var button = document.getElementById("theme-button");
var searchButton = document.getElementById("search-button");
var userSettings = document.getElementById("user-settings");
var siteLogo = document.getElementById("site-logo");
var isDefault = true;

button.onclick = function() {
    if(isDefault == false) {
        DefaultTheme();
    }
    else {
        DarkTheme();
    }
}

function DefaultTheme() {
    isDefault = true;
    link.href = "../static/CSS/default.css";
    searchButton.src = "../static/Media/SearchIconDefault.png";
    userSettings.src = "../static/Media/UserIconDefault.png";
    siteLogo.src = "../static/Media/LogoDefault.png";
}

function DarkTheme() {
    isDefault = false
    link.href = "../static/CSS/dark.css";
    searchButton.src = "../static/Media/SearchIconDark.png";
    userSettings.src = "../static/Media/UserIconDark.png";
    siteLogo.src = "../static/Media/LogoDark.png";
}
