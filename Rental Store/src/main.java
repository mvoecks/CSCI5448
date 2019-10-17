import java.util.ArrayList;
import java.util.Random;

public class main {

	
	public static void main(String[] args) {

		Random r = new Random();
		
		ArrayList<Customer> customers = new ArrayList<Customer>();
		
		//Add 6 casual customers
		for (int i = 0; i<6; i++) {
			customers.add(new CasualCustomer("CasualCustomer"+Integer.toString(i)));
		}

		//Add 2 business customers
		for (int i = 0; i<2; i++) {
			customers.add(new BusinessCustomer("BusinessCustomer"+Integer.toString(i)));
		}
		
		//Add 4 regular customers
		for (int i = 0; i<6; i++) {
			customers.add(new RegularCustomer("RegularCustomer"+Integer.toString(i)));
		}
		
		RentalStore store = new RentalStore(customers);
		
		for(int i=1; i<=35; i++) {
			System.out.println("\n\n----- Day: "+Integer.toString(i)+" -----");
			store.nextDay();
		}
		
	}

}
