
// Decerator object for a rental. Adds an accessory kit to the order.
public class AccessoryKit extends RentalDecerator{

	RentalAbstract rental;
	
	// Create the accessory kit object using a RentalAbstract object
	// and set the days due and tools rented to their original
	
	public AccessoryKit(RentalAbstract r) {
		rental = r;
		this.setDaysDue(rental.getDaysDue());
		this.setToolsRented(rental.returnTools());
	}
	
	// Add the text specifying this rental has an accessory kit
	@Override
	public String getDescription() {
		return rental.getDescription() +"\t\tWith an Accessory Kit \n";
	}

	// Add the flat fee of $7.25 to the cost of the rental
	@Override
	public double cost() {
		return rental.cost() + 7.25;
	}

	// Get the customer type
	public String getCustomerType() {
		return rental.getCustomerType();
	}
	
}
