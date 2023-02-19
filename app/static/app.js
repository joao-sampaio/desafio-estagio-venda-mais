function redirect() {
    let button = document.getElementById("redirect_button");
    let dist = button.getAttribute('name')
    window.location.href=`/${dist}`;
}