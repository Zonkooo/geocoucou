$(document).ready(function ()
{ 
	//alert('menu');
					
	// MENU 
	// Cacher sous menus
	$(".navigation ul.subMenu").hide(); 
	$(".navigation ul.subSubMenu").hide(); 
	
	// Remplacer le span par un lien
	$(".navigation li.toggleSubMenu span").each( function () { 
		var TexteSpan = $(this).text(); 
		$(this).replaceWith('<a href="" title="Afficher le sous-menu">' + TexteSpan + '<\/a>') ; 
	} ) ; 
	$(".navigation li.toggleSubSubMenu span").each( function () { 
		var TexteSpan2 = $(this).text(); 
		$(this).replaceWith('<a href="" title="Afficher le sous-sous-menu">' + TexteSpan2 + '<\/a>') ; 
	} ) ; 			
 
	// Gestion du click 
	$(".navigation li.toggleSubMenu > a").click( function () { 
		// Si le sous-menu était déjà ouvert, on le referme : 
		if ($(this).next("ul.subMenu:visible").length != 0) { 
			$(this).next("ul.subMenu").slideUp("normal"); 
		} 
		// Si le sous-menu est caché, on ferme les autres et on l'affiche : 
		else { 
			$(".navigation ul.subMenu").slideUp("normal"); 
			$(this).next("ul.subMenu").slideDown("normal"); 
		} 
		// On empêche le navigateur de suivre le lien : 
		return false; 
	});     
	
	// Gestion du click 
	$(".navigation li.toggleSubSubMenu > a").click( function () { 
		// Si le sous-sous-menu était déjà ouvert, on le referme : 
		if ($(this).next("ul.subSubMenu:visible").length != 0) { 
			$(this).next("ul.subSubMenu").slideUp("normal"); 
		} 
		// Si le sous-menu est caché, on ferme les autres et on l'affiche : 
		else { 
			$(".navigation ul.subSubMenu").slideUp("normal"); 
			$(this).next("ul.subSubMenu").slideDown("normal"); 
		} 
		// On empêche le navigateur de suivre le lien : 
		return false; 
	});
			
			
				 
		 
}); 