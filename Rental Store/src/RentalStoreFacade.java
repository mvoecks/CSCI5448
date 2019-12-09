import java.util.ArrayList;

// The purpose of this class is to create a store, add customers that will shop at the store, 
// and simulate the activity for the store for a specific ammount of time (days)

// This makes use of the facade design pattern to hide unnecessary details from the main program
// to make it easier to run simulations
public class RentalStoreFacade {
	
	private RentalStore store;
	private int businessCount;
	private int casualCount;
	private int regularCount;
	
	// Constructor, initializes private variables
	public RentalStoreFacade() {
		store = new RentalStore();
		businessCount = 1;
		casualCount = 1;
		regularCount = 1;
	}
	
	
	// Add a specfied number of each type of customer to the store
	public void addCustomers(int numBusiness, int numCasual, int numRegular){
		ArrayList<Customer> tempCustList = new ArrayList<Customer>();

		for (int i = casualCount; i<=(numCasual+casualCount); i++) {
			tempCustList.add(new CasualCustomer("CasualCustomer"+Integer.toString(i)));
		}

		for (int i = businessCount; i<=(numBusiness+businessCount); i++) {
			tempCustList.add(new BusinessCustomer("BusinessCustomer"+Integer.toString(i)));
		}
		
		for (int i = regularCount; i<=(numRegular+regularCount); i++) {
			tempCustList.add(new RegularCustomer("RegularCustomer"+Integer.toString(i)));
		}
		
		store.addCustomers(tempCustList);
		
		businessCount += numBusiness;
		casualCount += numCasual;
		regularCount += numRegular;
	}
	
	
	// Open the store for business for a specified number of days. Then print any relevent information about the simulation
	public void openStore(int numDays) {
		for(int i=1; i<=numDays; i++) {
			System.out.println("\n\n----- Day: "+Integer.toString(i)+" -----");
			store.nextDay();
		}
		System.out.println("\n----------SIMULATION COMPLETE----------\n");
		store.printTotalRentals();
		store.printTotalRevenue();
	}
	
}
