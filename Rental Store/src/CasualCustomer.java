import java.util.Random;

public class CasualCustomer extends Customer{

	Random r = new Random();
	
	
	public CasualCustomer(String n) {
		this.setName(n);
	}
	
	
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
