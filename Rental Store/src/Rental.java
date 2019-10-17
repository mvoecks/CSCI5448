
import java.util.ArrayList;
import Tools.Tool;

public class Rental extends RentalAbstract {
	
	private Customer customer;
	
	
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
	

	@Override
	public double cost() {
		int costCount = 0;
		for (Tool t : this.returnTools()) {
			costCount += (t.getCost()*this.getDaysDue());
		}
		return costCount;
	}
	
}
