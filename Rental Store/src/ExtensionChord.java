
// Decerator for the rental class, adds an extension chord to the order
public class ExtensionChord extends RentalDecerator{

	RentalAbstract rental;
	
	// Constructor sets the days due and tools rented to its predecessor
	public ExtensionChord(RentalAbstract r) {
		rental = r;
		this.setDaysDue(rental.getDaysDue());
		this.setToolsRented(rental.returnTools());
	}
	
	// Add to the description indicating that it includes and extension chord
	public String getDescription() {
		return rental.getDescription() +"\t\tWith an Extension Chord \n";
	}

	// update the cost to add a $2.5 flat fee
	@Override
	public double cost() {
		return rental.cost() + 2.5;
	}
	
	// returns the customers type
	public String getCustomerType() {
		return rental.getCustomerType();
	}

}
