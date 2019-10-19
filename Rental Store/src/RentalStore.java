
import java.util.ArrayList;
import java.util.Random;


import Tools.Tool;
import Tools.ToolFactory;

// The RentalStore class is the rental store itself. The store adds customers that it serves,
// creates inventory for the store, sends customers to itself, and prints useful information about its daily operations.
public class RentalStore {
	
	Random r = new Random();
	
	private ArrayList<Tool> inventory;
	private ArrayList<RentalAbstract> activeRentals;
	private ArrayList<RentalAbstract> completedRentals;
	private ArrayList<RentalAbstract> completedToday;
	private ArrayList<Customer> customers;
	private ArrayList<Customer> custToStore;
	private ToolFactory toolCreator;
	private double dailyRevenue = 0;
	private double totalRevenue;
	
	// Constrcutor initializes private variables.
	public RentalStore() {
		inventory = new ArrayList<Tool>();
		activeRentals = new ArrayList<RentalAbstract>();
		completedRentals = new ArrayList<RentalAbstract>();
		completedToday = new ArrayList<RentalAbstract>();
		toolCreator = new ToolFactory();
		customers = new ArrayList<Customer>();
		custToStore = new ArrayList<Customer>();
		this.generateInventory();
	}
	
	
	// Adds customers from a list of customers to the current customer base.
	public void addCustomers(ArrayList<Customer> custs) {
		customers.addAll(custs);
	}
	
	// Creates the inventory for the store, and names the items in the inventory. Here we create:
	// -- 3 of each of the following: Saw, Sander, Brush, Roller
	// -- 2 of each of the following: Mixer, Jackhammer, Wrench, Plunger, Rake, Shovel
	private void generateInventory() {
		try {
			for(int i=1; i<=3; i++) {
				inventory.add(toolCreator.getTool("saw", "Saw"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("sander", "Sander"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("brush", "Brush"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("roller", "Roller"+Integer.toString(i)));
			}
			for(int i=1; i<=2; i++) {
				inventory.add(toolCreator.getTool("mixer", "Mixer"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("jackhammer", "Jackhammer"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("wrench", "Wrench"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("plunger", "Plunger"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("rake", "Rake"+Integer.toString(i)));
				inventory.add(toolCreator.getTool("shovel", "Shovel"+Integer.toString(i)));
			}
			
			
		} catch(Exception e) {
			System.out.println(e);
			System.exit(1);
		}
	}
	
	// The createRental function is called by Customers, they pass parameters:
		// -- cust : Customers will pass "this" to pass themselves
		// -- numTools : The customer requests a number of tools, and the store randomly picks which ones they want
		// -- daysDue : The customer specifies how long he is renting the tools for
		// The store then "persuades" the customer into getting 0-6 additional packages, either extension chords, accessory kits, and/or protective gear.
		public void createRental(Customer cust, int numTools, int daysDue) {
			ArrayList<Tool> rentedTools = new ArrayList<Tool>();
			for(int i=0; i<numTools; i++) {
				rentedTools.add(inventory.remove(r.nextInt(inventory.size())));
			}
			RentalAbstract rental = new Rental(cust, rentedTools, daysDue);
			
			int numPackages = r.nextInt(7);
			int randNumb;
			for (int i=0; i<numPackages; i++) {
				randNumb = r.nextInt(3);
				if (randNumb == 0) {
					rental = new ExtensionChord(rental);				
				}
				else if (randNumb == 1) {
					rental = new AccessoryKit(rental);				
				}
				else {
					rental = new ProtectiveGear(rental);
					
				}
			}
			activeRentals.add(rental);
			dailyRevenue += rental.cost();
		}
		
		
		// Simulate one day of activity for the rental store:
		// Print useful information about the daily actvities.
		public void nextDay() {
			this.sendCustsToStore();
			for(int i=0; i<activeRentals.size(); i++) {
				activeRentals.get(i).addDay();
				if (activeRentals.get(i).getActiveStatus() == false){
					inventory.addAll(activeRentals.get(i).returnTools());
					completedToday.add(activeRentals.remove(i));
				}
			}
			this.printCompletedTodayRentals();
			this.printActiveRentals();
			this.printInventory();
			this.printDailyRevenue();
			completedRentals.addAll(completedToday);
			totalRevenue += dailyRevenue;
			dailyRevenue = 0;
			completedToday = new ArrayList<RentalAbstract>();
		}
		
		// Sends a random number of customers from the customers list to the store (itself).
		private void sendCustsToStore() {
			int numCustToStore = r.nextInt(12);
			for (int j=0; j<numCustToStore; j++) {
				custToStore.add(customers.remove(r.nextInt(customers.size())));
			}
			for (Customer c : custToStore) {
				c.rentTools(this);
			}
			customers.addAll(custToStore);
			custToStore = new ArrayList<Customer>();
		}
	
	// Some getters for useful info from the private variables
	public int getInventorySize() {
		return inventory.size();
	}
	public double getTotalRevenue() {
		return totalRevenue;
	}
	
	// Prints the total revenue in a concise format
	public void printTotalRentals() {
		System.out.println("Total Completed Rentals: " + Integer.toString(completedRentals.size()));
		int countCasual = 0;
		int countBusiness = 0;
		int countRegular = 0;
		for (RentalAbstract r : completedRentals) {
			if (r.getCustomerType() == "Business") {
				countBusiness++;
			}
			else if (r.getCustomerType() == "Regular") {
				countRegular++;
			}
			else if (r.getCustomerType() == "Casual") {
				countCasual++;
			}
		}
		System.out.println("\tRentals by Casual Customers: "+Integer.toString(countCasual));
		System.out.println("\tRentals by Regular Customers: "+Integer.toString(countRegular));
		System.out.println("\tRentals by Business Customers: "+Integer.toString(countBusiness));
	}
	
	
	// Prints the stores current inventory in a concise format
	private void printInventory() {
		System.out.println("---Currernt Inventory Has "+Integer.toString(inventory.size())+" Tools:---");
		if (inventory.size() == 0) {
			System.out.println("There is nothing currently in inventory.\n");
		}
		else {
			for (Tool t: this.inventory) {
				System.out.println("\t"+t.getDescription());
			}
		}
		
	}

	// Printes the stores active rentals in a concises format
	private void printActiveRentals() {
		System.out.println("---Current Active Rentals:---");
		if (activeRentals.size() == 0) {
			System.out.println("\tThere are no active rentals.\n");
		}
		else {
			for (RentalAbstract r : activeRentals) {
				System.out.println(r.getDescription()+"\n");
			}
		}
	}
	
	
	// Prints the daily rentals in a concise format
	private void printCompletedTodayRentals() {
		System.out.println("---Rentals Completed Today:---");
		if (completedToday.size() == 0) {
			System.out.println("No rentals were completed today.\n");
		}
		else {
			for (RentalAbstract r : completedToday) {
				System.out.println(r.getDescription() + "Rented for "+r.getDaysDue()+" days\nCost: $"+Double.toString(r.cost())+"\n");
			}
		}
		
	}
	
	// Prints the daily revenue in a concise format
	private void printDailyRevenue() {
		System.out.println("\n---Daily Revenue:---\n \t$"+Double.toString(dailyRevenue));
	}
	
	
	// Prints the total revenue in a concise format
	public void printTotalRevenue() {
		System.out.println("---Total Revenue Made:--- $"+Double.toString(totalRevenue));
	}
	
	
}
