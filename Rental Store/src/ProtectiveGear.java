
// Rental decerator for a rental, adds protective gear to the order
public class ProtectiveGear extends RentalDecerator{

	RentalAbstract rental;
	
	// Constructor sets daysDue and toolsRented to its predecessor
	public ProtectiveGear(RentalAbstract r) {
		rental = r;
		this.setDaysDue(rental.getDaysDue());
		this.setToolsRented(rental.returnTools());
	}
	
	// Add to the description indicating that protective gear was added to the order.
	@Override
	public String getDescription() {
		return rental.getDescription() +"\t\tWith a Protective Gear Pack\n";
	}

	// Update the cost to include the $10 flat fee
	@Override
	public double cost() {
		return rental.cost() + 10;
	}
	
	// Returns the customers type
	public String getCustomerType() {
		return rental.getCustomerType();
	}

}
