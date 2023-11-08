
/** This function make the tab animation on profile page.
 * Source: https://www.w3schools.com/howto/howto_js_tabs.asp */
function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }


/** This function will pop a JS prompt to ensure deleting or not 
 * https://stackoverflow.com/questions/46625535/delete-confirmation-in-django */
  function deletePost() {
     var isValid = confirm('Are you sure you want to delete this post?');
     if (!isValid) { event.preventDefault();}
    }