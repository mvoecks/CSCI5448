
// BusinessCustomer object extends the abstract Customer class
public class BusinessCustomer extends Customer {
	
	// Constructor sets name, sets type to Business
	public BusinessCustomer(String n) {
		this.setName(n);
		this.setType("Business");
		
	}
	
	// Checks to see if there are 3 items in the store, rents 3 items if it can
	@Override
	void rentTools(RentalStore store) {
		if (store.getInventorySize() > 2) {
			store.createRental(this, 3, 7);
		}
		
	}

}
