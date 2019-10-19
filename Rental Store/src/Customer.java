
// Abstract Customer class. Defines behavior for all types of customer
public abstract class Customer {
	private String name;
	private String type;
	
	// Getters and Setters for name and type
	public void setName(String n) {
		name = n;
	}
	public String getName() {
		return name;
	}
	public String getType() {
		return type;
	}
	public void setType(String t) {
		type = t;
	}

	// Abstract rentTools will define how a customer rents tools, such as always rents 7 tools for 3 days 
	// or however the customer does it.
	abstract void rentTools(RentalStore store);
	
}
