var showPasswordButton = document.getElementById("show-password");
var isShowingPassword = false;

var signInButton = document.getElementById("sign-in");
var errorMessage = document.getElementById("not-allowed-data");
var UIP = document.getElementById("UIP");
var PIP = document.getElementById("PIP");
var RePIP = document.getElementById("RePIP");
var email = document.getElementById("email");

showPasswordButton.onclick = function () {
    if(isShowingPassword == false) {
        isShowingPassword = true;
        PIP.type = "text";
        RePIP.type = "text";
    }
    else {
        isShowingPassword = false;
        PIP.type = "password";
        RePIP.type = "password";
    }
};

PIP.onkeyup = function() {
    validatePassword();
};

RePIP.onkeyup = function() {
    validatePassword();
};

email.onkeyup = function() {
    validatePassword();
};

UIP.onkeyup = function() {
    validatePassword(); 
};

PIP.onclick = function() {
    validatePassword();
};

RePIP.onclick = function() {
    validatePassword();
};

email.onclick = function() {
    validatePassword();
};

UIP.onclick = function() {
    validatePassword();
};

PIP.onchange = function() {
    validatePassword();
};

RePIP.onchange = function() {
    validatePassword();
};

email.onchange = function() {
    validatePassword();
};

UIP.onchange = function() {
    validatePassword();
};

function validatePassword() {
    var isEmail = email.value.includes("@");
    
    if (isEmail == true) {
        if(/\S/.test(UIP.value)) {
            if (/\S/.test(PIP.value) && /\S/.test(RePIP.value)) {
                if (PIP.value == RePIP.value) {
                    signInButton.disabled = false;
                    signInButton.style.backgroundColor = "#0723C0";
                    signInButton.style.cursor = "pointer";
//                    errorMessage.innerHTML = "";
                }
                else {
                    errorMessage.innerHTML = "Your password does not match";
                    signInButton.disabled = true;
                    signInButton.style.backgroundColor = "#FF0000";
                    signInButton.style.cursor = "default";
                }
            }
            else {
                errorMessage.innerHTML = "Your password does not match";
                signInButton.disabled = true;
                signInButton.style.backgroundColor = "#FF0000";
                signInButton.style.cursor = "default";
                errorMessage.innerHTML = "You can not have that password";
            }
            errorMessage.innerHTML = "";
        }
        else {
            errorMessage.innerHTML = "Please enter a valid username";
        }
        
    }
    else {
        errorMessage.innerHTML = "Please enter a valid email address";
    }
    
}
