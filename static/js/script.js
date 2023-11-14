
  /** This function will pop a JS prompt to ensure deleting or not 
 * https://stackoverflow.com/questions/46625535/delete-confirmation-in-django */
 function deletePost() {
	var isValid = confirm('Are you sure you want to delete this post?');
	if (!isValid) { event.preventDefault();}
   }


function toggleMenu() {
	const navMenu = document.querySelector('.mainNavbar ul');
	navMenu.classList.toggle('show');
  }

