﻿$(document).ready(function ()
{
	//Visionneuse
	//alert('Visionneuse');
			
	$("#viewer").wslide({
		width: 698,
		height: 212,
		pos: 1,
		horiz: true,
		duration: 500,
		autolink: 'viewer_navig',
		//effect: 'easeOutElastic'
	});	
			
						
	$(document).ready(function()
	{
		var position = 1;
		function move() {
			position++;
			var start = '#viewer-'+position;
			$('a[href*="'+start+'"]').click();
			if(position == 6) position = 0;
			setTimeout(function() {
					move();
					},3600);
		}
		setTimeout(function() {
			move();
		},3600);
	});
				 
				
});
