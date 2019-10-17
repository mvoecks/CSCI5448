
public class BusinessCustomer extends Customer {
	
	public BusinessCustomer(String n) {
		this.setName(n);
		this.setType("Business");
		
	}
	
	@Override
	void rentTools(RentalStore store) {
		if (store.getInventorySize() > 2) {
			store.createRental(this, 3, 7);
		}
		
	}

}
