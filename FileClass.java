import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;

public class FileClass
{
    private ArrayList<Rentable> vehicles;

    public FileClass()
    {
        vehicles = new ArrayList<>();
    }

    public void createSampleFile() throws IOException
    {
        File file = new File("vehicles.txt");

        if (!file.exists())
        {
            BufferedWriter bw = new BufferedWriter(new FileWriter(file));

            bw.write("P#Anna Mols#CA123456#3#S#5#4");
            bw.newLine();
            bw.write("P#Peter Khumalo#GP654321#5#U#7#4");
            bw.newLine();
            bw.write("P#Sara Lee#WC111222#7#B#2#2");
            bw.newLine();
            bw.write("C#Bob Smith#NP789012#5#3.5");
            bw.newLine();
            bw.write("C#Lisa Ray#EC444555#10#5.0");
            bw.newLine();
            bw.write("P#Priya Nair#KZN987654#4#U#7#4");
            bw.newLine();

            bw.close();
            System.out.println("Created vehicles.txt with sample data.");
        }
    }

    public void readFromFile() throws IOException
    {
        createSampleFile();

        File file = new File("vehicles.txt");

        Scanner input = new Scanner(file);

        while(input.hasNextLine())
        {
            String line = input.nextLine().trim();

            if(line.isEmpty()) continue;

            String[] parts = line.split("#");

            if(parts[0].equals("P"))
            {
                PrivateVehicle pv = new PrivateVehicle(
                        'P',
                        parts[1],
                        parts[2],
                        Integer.parseInt(parts[3]),
                        parts[4].charAt(0),
                        Integer.parseInt(parts[5]),
                        Integer.parseInt(parts[6])
                );

                vehicles.add(pv);
            }
            else if(parts[0].equals("C"))
            {
                CommercialVehicle cv = new CommercialVehicle(
                        'C',
                        parts[1],
                        parts[2],
                        Integer.parseInt(parts[3]),
                        Double.parseDouble(parts[4])
                );

                vehicles.add(cv);
            }
        }

        input.close();
    }

    public ArrayList<Rentable> getVehicles()
    {
        return vehicles;
    }

    public void writeSUVsToFile() throws IOException
    {
        FileWriter fw = new FileWriter("suvs.txt");
        BufferedWriter bw = new BufferedWriter(fw);

        for(Rentable r : vehicles)
        {
            if(r instanceof PrivateVehicle)
            {
                PrivateVehicle pv = (PrivateVehicle) r;

                if(pv.getCategory() == 'U' || pv.getCategory() == 'u')
                {
                    bw.write(
                        String.format(
                            "%-15s %-10s R%.2f",
                            pv.getClientName(),
                            pv.getLicencePlateNumber(),
                            pv.calcDailyRent()
                        )
                    );

                    bw.newLine();
                }
            }
        }

        bw.close();
        System.out.println("SUVs written to suvs.txt");
    }
}