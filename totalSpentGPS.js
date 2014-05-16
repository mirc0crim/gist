var totalAmount = 0.0
$('.list-table').find('tbody').find('tr').each(function() {
	var isCancelled = $(this).find('.purchase-status').find('div').hasClass('history-canceled')
	if (!isCancelled) {
		var text = $(this).find('.purchase-price').text()
		appPrice = parseFloat(Number(text.replace(/[^0-9\.]+/g,"")))
		if (text.substr(1,1)=="$"){
			//reference price
			appPrice = appPrice
		} else if (text.substr(1,3)=="CHF"){
			//CHF
			appPrice = appPrice * 1.12
		} else if (text.substr(1,1)=="€"){
			//Euro
			appPrice = appPrice * 1.37
		} else if (text.substr(1,1)=="£"){
			//Pound
			appPrice = appPrice * 1.68
		} else {
			//Currency not covered
			alert(text)
		}
		if (!isNaN(appPrice))
			totalAmount = totalAmount + appPrice
	}
})
alert('Total amount spent on Google Play: $' + totalAmount.toFixed(2))