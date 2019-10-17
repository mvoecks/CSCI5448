import java.util.Random;

public class RegularCustomer extends Customer{

	Random r = new Random();
	
	
	public RegularCustomer(String n) {
		this.setName(n);
	}
	
	
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
