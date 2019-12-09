
import java.util.ArrayList;
import Tools.Tool;


// Rental extends Rental abstract and is the base object for creating rentals
// A customer rents a specified number of tools we get for them and cost is calculated
// A decorator will add extra options to this class later.
public class Rental extends RentalAbstract {
	
	private Customer customer;
	
	// Create a rental for a specifed customer and toolList. Then keep track of the due date for
	// These rentals
	public Rental(Customer cust, ArrayList<Tool> toolList, int due) {
		customer = cust;
		this.setToolsRented(toolList);
		this.setDaysDue(due);
		
		String retStr = "Rentee: \n\t"+customer.getName()+"\nTools Rented: \n";
		for (Tool t : this.returnTools()) {
			retStr += "\t"+t.getDescription()+"\n";
		}
		this.setDescription(retStr);
	}
	

	// Calculate the cost of the rental as the product of the items daily cost and the number of days rented.
	@Override
	public double cost() {
		int costCount = 0;
		for (Tool t : this.returnTools()) {
			costCount += (t.getCost()*this.getDaysDue());
		}
		return costCount;
	}
	
	
	// Return the type of the customer (Business, casual, etc.)
	public String getCustomerType() {
		return customer.getType();
	}
	
}
