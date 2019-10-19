import java.io.FileNotFoundException;
import java.io.PrintStream;

public class main {

	
	public static void main(String[] args) {
		
		// Set the output stream to output to the file dayatthezoo.out
		PrintStream streamOut;
		try {
			streamOut = new PrintStream("./Simulate_Rental_Store.out");
			System.setOut(streamOut);
		} catch (FileNotFoundException e) {
			System.out.println("Unable to print to file, printing to console.");
		}

		// Create a rental store facade object
		RentalStoreFacade store = new RentalStoreFacade();
		
		// Add 2 business, 6 casual, and 4 regular customers to the store
		store.addCustomers(2, 6, 4);
		
		// Open the store for business for 35 days.
		store.openStore(35);
		
	}

}
