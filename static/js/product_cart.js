function quantityUpdate(operation,productId)
{
	const inputBox=	document.getElementById("quantity"+productId)
	let quantity=parseInt(inputBox.value);
	inputBox.value=quantity+operation
}