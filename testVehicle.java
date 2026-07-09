import java.util.ArrayList;

public class testVehicle
{
    public static void displayPrivateVehicles(ArrayList<Rentable> list)
    {
        System.out.println("Private Vehicles Report\n");

        System.out.println("Name             Licence       Days   Type  Seats  Doors  Rate(pd)");
        System.out.println(
        "-----------------------------------------------------------------------");
        
        for(Rentable r : list)
        {
            if(r instanceof PrivateVehicle)
            {
                System.out.println(r);
            }
        }
    }

    public static void displayCommercialVehicles(ArrayList<Rentable> list)
    {
        System.out.println("\nCommercial Vehicles Report\n");

        System.out.println("Name             Licence       Days   Tons   Insurance(pd)  Rate(pd)");

        System.out.println("-----------------------------------------------------------------------");

        for(Rentable r : list)
        {
            if(r instanceof CommercialVehicle)
            {
                System.out.println(r);
            }
        }
    }

    public static void main(String[] args)
    {
        try
        {
            FileClass fileObj = new FileClass();

            fileObj.readFromFile();

            ArrayList<Rentable> vehicles =
                    fileObj.getVehicles();

            displayPrivateVehicles(vehicles);

            displayCommercialVehicles(vehicles);

            fileObj.writeSUVsToFile();

            System.out.println(
                    "\nSUVs written to suvs.txt");
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}