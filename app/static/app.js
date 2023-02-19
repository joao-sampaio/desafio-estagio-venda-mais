function redirect() {
    let button = document.getElementById("redirect-button");
    console.log(button);
    let dist = button.getAttribute('name');
    window.location.href=`/${dist}`;
}