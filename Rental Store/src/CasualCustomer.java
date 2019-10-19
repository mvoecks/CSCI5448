import java.util.Random;

// Casual customer object extends Customer abstract class
public class CasualCustomer extends Customer{

	Random r = new Random();
	
	// Constructor sets name, sets type to Casual
	public CasualCustomer(String n) {
		this.setName(n);
		this.setType("Casual");
	}
	
	// Checks to see the if there is only 1 item and rents it if thats the case,
	// if there are no items it doesnt rent any, and otherwise it rents a random 
	// number of tools between 1-2
	@Override
	void rentTools(RentalStore store) {
		int numTools = 0;
		int numDays = r.nextInt(2)+1;
		if (store.getInventorySize() == 1) {
			store.createRental(this, 1, numDays);
		}
		else if (store.getInventorySize() > 1) {
			numTools = r.nextInt(2) + 1;
			store.createRental(this, numTools, numDays);
		}
	}

}
