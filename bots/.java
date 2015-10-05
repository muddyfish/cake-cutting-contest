public class Hungry {
    public static void main(String[] args) {
        double[] arguments = new double[4];
        for (int i = 0; i < 4; i++) {
            arguments[i] = Double.parseDouble(args[i]);
        }
        int myCake = (int) Math.ceil(arguments[1]/arguments[3]);
        System.out.println(myCake);
    }
}
