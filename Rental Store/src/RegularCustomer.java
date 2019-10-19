import java.util.Random;

// Regular customer object extends customer abstract class
// Rents 1-3 tools for 3-5 days
public class RegularCustomer extends Customer{

	Random r = new Random();
	
	// Constructor sets name, sets type to Regular
	public RegularCustomer(String n) {
		this.setName(n);
		this.setType("Regular");
	}
	
	
	// If there is no inventory, nothing is rented, otherwise it rents a random number up to 3
	// Rents tools for a random amount of time from 3-5 days.
	@Override
	void rentTools(RentalStore store) {
		int numTools = 0;
		int numDays = r.nextInt(3)+3;
		if (store.getInventorySize() < 3 && store.getInventorySize() > 0) {
			numTools = r.nextInt(store.getInventorySize()) + 1;
			store.createRental(this, numTools, numDays);
		}
		else if (store.getInventorySize() >= 3) {
			numTools = r.nextInt(3) + 1;
			store.createRental(this, numTools, numDays);
		}
	}	
}
